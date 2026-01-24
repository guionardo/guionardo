import asyncio

from src.gh_api import get_organization_async, get_repos_async, get_user_async
from src.models import Org, Repository, User
from src.reports import (
    create_language_pie,
    get_language_stats,
    create_commits_chart,
    create_language_bar,
    get_significant,
)

GH_ORGANIZATIONS = ["escoteirando"]
GH_USERS = ["guionardo"]


async def get_last_updated_repositories() -> tuple[str, str]:
    organizations: dict[str, Org] = {
        org: await get_organization_async(org) for org in GH_ORGANIZATIONS
    }
    users: dict[str, User] = {user: await get_user_async(user) for user in GH_USERS}

    all_repos: list[Repository] = []
    organizations_repos = await asyncio.gather(
        *(get_repos_async(org_name, "orgs") for org_name in GH_ORGANIZATIONS)
    )
    users_repos = await asyncio.gather(
        *(get_repos_async(user_name) for user_name in GH_USERS)
    )
    for repos in users_repos + organizations_repos:
        all_repos.extend(repos)

    all_repos = [repo for repo in all_repos if "nostats" not in repo.topics]

    last_updated = sorted(
        all_repos, key=lambda r: r.last_commit_date(True) or r.updated_at, reverse=True
    )[:10]

    body = """## Monitored Organizations and Users

| Name | Type | Location | Description |
|----|-----|----|---|
"""

    for org in organizations.values():
        body += f"|{org.name} | Organization | {org.location or 'N/A'} | {org.description or 'No description'} |\n"
    for user in users.values():
        body += f"|{user.name} | User | {user.location or 'N/A'} |  |\n"

    body += """

## Last Updated Repositories

| Repository | Description | Last Commit | Status |Languages|
|----|-----|----|---|---|
"""
    for repo in last_updated:
        last_commit = (
            f"<span>{'<br>'.join(str(repo.last_commit()).splitlines())}</span>"
        )
        languages = ", ".join(repo.languages.keys()) if repo.languages else "N/A"
        status = f'<span title="{repo.estado_atualizacao}">{repo.estado_atualizacao[0]}</span>'
        body += f"| [{repo.name}]({repo.html_url}) | {repo.description or 'No description'} | {last_commit} | {status}|{languages}\n"

    language_stats, total_length, total_repos = get_language_stats(all_repos)
    create_language_bar(language_stats, total_length, total_repos, "languages_bar.svg")

    body += '\n<img src="languages_bar.svg"/>\n'

    ls = get_significant(language_stats)
    body += "\n### Significant Languages\n\n"
    body += "| Language | Repositories | Total Bytes | Greater Repo |\n"
    body += "|---|---|---|---|\n"
    for l in ls:
        body += f"| {l.name} | {len(l.repos)} | {l.length} | {l.greater_repo_name} ({l.greater_repo_length}) |\n"

    return "LAST_UPDATED_REPOSITORIES", body
