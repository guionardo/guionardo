import os

import httpx
from models import Commit, Org, Repository, User
import concurrent.futures

TOKEN = os.getenv("GITHUB_TOKEN")
if not TOKEN:
    raise Exception("MISSING GITHUB_TOKEN ENVIRONMENT")


def get(url) -> dict | None:
    response = httpx.get(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Authorization": f"Bearer {TOKEN}",
        },
    )
    if response.status_code < 400:
        return response.json()

    raise httpx.HTTPStatusError(response.reason_phrase)


def get_organization(org):
    """https://api.github.com/orgs/escoteirando"""
    data = get(f"https://api.github.com/orgs/{org}")
    return Org.from_dict(data)


def get_user(user) -> User | None:
    """curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/user"""

    data = get(f"https://api.github.com/users/{user}")

    return User.from_dict(data)


def update_repo(repo: Repository) -> Repository:
    """Update languages"""
    languages = get(f"https://api.github.com/repos/{repo.full_name}/languages")
    repo.languages = languages
    repo.commits = get_commits(repo)
    return repo


def get_repos(owner: str, owner_type: str = "users"):
    """curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/orgs/ORG/repos
  
    owner_type -> users | orgs
  """
    data = get(f"https://api.github.com/{owner_type}/{owner}/repos")
    with concurrent.futures.ThreadPoolExecutor(3, "repos_updater") as executor:
        repos = [Repository.from_dict(repo) for repo in data]
        updates = {executor.submit(update_repo, repo) for repo in repos}
        for future in concurrent.futures.as_completed(updates):
            try:
                data = future.result()
            except Exception as exc:
                print("ERROR ON CONCURRENT FUTURE", exc)
            else:
                print("Updated repository", data)
    # repos = [update_repo(Repository.from_dict(repo)) for repo in data]

    return repos


def get_commits(repo: Repository):
    """curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/commits"""
    data = get(f"https://api.github.com/repos/{repo.full_name}/commits")
    commits = [Commit.from_dict(commit) for commit in data]
    commits.sort(key=lambda c: c.date, reverse=True)

    return commits


def get_repo(user, repo):
    """https://api.github.com/repos/guionardo/gs-dev"""
