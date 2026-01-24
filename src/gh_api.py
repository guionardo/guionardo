import asyncio
import concurrent.futures
import os

import httpx

from .models import Commit, Org, Repository, User

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

    raise httpx.HTTPError(f"{response.reason_phrase} for URL: {url}")


async def async_get(url) -> dict | None:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url,
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "Authorization": f"Bearer {TOKEN}",
            },
        )
        if response.status_code < 400:
            return response.json()

    raise httpx.HTTPError(f"{response.reason_phrase} for URL: {url}")


def get_organization(org):
    """https://api.github.com/orgs/escoteirando"""
    data = get(f"https://api.github.com/orgs/{org}")
    return Org.from_dict(data)


async def get_organization_async(org):
    """https://api.github.com/orgs/escoteirando"""
    data = await async_get(f"https://api.github.com/orgs/{org}")
    return Org.from_dict(data)


def get_user(user) -> User | None:
    """curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/user"""

    data = get(f"https://api.github.com/users/{user}")

    return User.from_dict(data)


async def get_user_async(user) -> User | None:
    data = await async_get(f"https://api.github.com/users/{user}")
    return User.from_dict(data)


def update_repo(repo: Repository) -> Repository:
    """Update languages"""
    languages = get(f"https://api.github.com/repos/{repo.full_name}/languages")
    repo.languages = languages
    repo.commits = get_commits(repo)
    return repo


async def update_repo_async(repo: Repository) -> Repository:
    """Update languages"""
    try:
        languages = await async_get(
            f"https://api.github.com/repos/{repo.full_name}/languages"
        )
        repo.languages = languages
        repo.commits = await get_commits_async(repo)
    except Exception as e:
        print(f"Error updating repo {repo.full_name}: {e}")

    return repo


async def get_repos_async(owner: str, owner_type: str = "users"):
    data = await async_get(
        f"https://api.github.com/{owner_type}/{owner}/repos?per_page=250"
    )
    result = await asyncio.gather(
        *(update_repo_async(Repository.from_dict(repo)) for repo in data)
    )
    return result


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


async def get_commits_async(repo: Repository):
    data = await async_get(f"https://api.github.com/repos/{repo.full_name}/commits")
    commits = [Commit.from_dict(commit) for commit in data]
    commits.sort(key=lambda c: c.date, reverse=True)
    return commits


def get_repo(user, repo):
    """https://api.github.com/repos/guionardo/gs-dev"""


async def get_traffic_views():
    try:
        data = await async_get(
            "https://api.github.com/repos/guionardo/guionardo/traffic/views"
        )
        return data
    except httpx.HTTPStatusError as e:
        print("Error fetching traffic views:", e)
        return {}
