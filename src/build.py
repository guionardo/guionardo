""" Guionardo GitHub Page Builder """

from datetime import datetime, timedelta

from gh_api import get_organization, get_repos, get_user
from reports import create_language_pie, get_language_stats, create_commits_chart

GH_ORGANIZATIONS = ["escoteirando"]
GH_USERS = ["guionardo"]

organizations = {org: get_organization(org) for org in GH_ORGANIZATIONS}
users = {user: get_user(user) for user in GH_USERS}

all_repos = []

for user_name, user in users.items():
    repos = get_repos(user_name)
    all_repos.extend(repos)
    # pprint(repos)

for org_name, org in organizations.items():
    repos = get_repos(org_name, "orgs")
    all_repos.extend(repos)
    # pprint(repos)

all_repos.sort(key=lambda r: r.last_change, reverse=True)

# pprint(users)
# pprint(organizations)

language_stats, total_length, total_repos = get_language_stats(all_repos)
# pprint(language_stats)

with open("README_2.md", "w", encoding="utf-8") as tmp:
    tmp.write("# Guionardo's github profile report\n\n")
    tmp.write("## Repositories (by activity)\n")

    state = ""
    for repo in all_repos:
        if repo.estado_atualizacao != state:
            state = repo.estado_atualizacao
            tmp.write(f"\n### {state}\n")
        tmp.write(repo.detail())

    tmp.write("\n## Languages (by usage)\n")
    for language in language_stats:
        tmp.write(language.detail(total_repos))

    # <img src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjwhLS0gR2VuZXJhdG9yOiBBZG9iZSBJbGx1c3RyYXRvciAxNi4wLjAsIFNWRyBFeHBvcnQgUGx1Zy1JbiAuIFNWRyBWZXJzaW9uOiA2LjAwIEJ1aWxkIDApICAtLT4NCjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+DQo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4Ig0KCSB3aWR0aD0iMTI2cHgiIGhlaWdodD0iMTI2cHgiIHZpZXdCb3g9IjAgMCAxMjYgMTI2IiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCAxMjYgMTI2IiB4bWw6c3BhY2U9InByZXNlcnZlIj4NCjxnPg0KCTxyZWN0IHg9IjEuMDk1IiB5PSI5OC4yMjQiIHdpZHRoPSIxMjMuODEiIGhlaWdodD0iMTkuMjc1Ii8+DQoJPHJlY3QgeD0iMS4wOTUiIHk9Ijg1Ljc0IiB3aWR0aD0iMTIzLjgxIiBoZWlnaHQ9IjUuMjA1Ii8+DQoJPHBhdGggZD0iTTE4LjQwNCw5NS43MjFjMC43NjcsMCwxLjM4OS0wLjYyMywxLjM4OS0xLjM5cy0wLjYyMi0xLjM4OC0xLjM4OS0xLjM4OEgzLjQ4MWMtMC43NjcsMC0xLjM4OCwwLjYyMS0xLjM4OCwxLjM4OA0KCQlzMC42MjIsMS4zOSwxLjM4OCwxLjM5SDE4LjQwNHoiLz4NCgk8cGF0aCBkPSJNNDQuNDMzLDk1LjcyMWMwLjc2NywwLDEuMzg4LTAuNjIzLDEuMzg4LTEuMzlzLTAuNjIyLTEuMzg4LTEuMzg4LTEuMzg4SDI5LjUxYy0wLjc2NywwLTEuMzg5LDAuNjIxLTEuMzg5LDEuMzg4DQoJCXMwLjYyMiwxLjM5LDEuMzg5LDEuMzlINDQuNDMzeiIvPg0KCTxwYXRoIGQ9Ik03MC40NjEsOTUuNzIxYzAuNzY3LDAsMS4zODgtMC42MjMsMS4zODgtMS4zOXMtMC42MjItMS4zODgtMS4zODgtMS4zODhINTUuNTM5Yy0wLjc2NywwLTEuMzg4LDAuNjIxLTEuMzg4LDEuMzg4DQoJCXMwLjYyMiwxLjM5LDEuMzg4LDEuMzlINzAuNDYxeiIvPg0KCTxwYXRoIGQ9Ik05Ni40OSw5NS43MjFjMC43NjcsMCwxLjM4OS0wLjYyMywxLjM4OS0xLjM5cy0wLjYyMi0xLjM4OC0xLjM4OS0xLjM4OEg4MS41NjdjLTAuNzY3LDAtMS4zODgsMC42MjEtMS4zODgsMS4zODgNCgkJczAuNjIyLDEuMzksMS4zODgsMS4zOUg5Ni40OXoiLz4NCgk8cGF0aCBkPSJNMTIyLjUxOSw5NS43MjFjMC43NjcsMCwxLjM4OS0wLjYyMywxLjM4OS0xLjM5cy0wLjYyMi0xLjM4OC0xLjM4OS0xLjM4OGgtMTQuOTIzYy0wLjc2NywwLTEuMzg4LDAuNjIxLTEuMzg4LDEuMzg4DQoJCXMwLjYyMiwxLjM5LDEuMzg4LDEuMzlIMTIyLjUxOXoiLz4NCgk8cGF0aCBkPSJNNy40MSw4MC45aDUzLjQ0MmMwLjg2MywwLDEuNTYyLTAuNjk5LDEuNTYyLTEuNTYyVjM5LjU0M2MwLTAuODYyLTAuNjk5LTEuNTYzLTEuNTYyLTEuNTYzSDQ1LjMxNHYtNi41MzkNCgkJYzAtMC44NjEtMC42OTgtMS41NjItMS41NjEtMS41NjJIMjMuNDI4Yy0wLjg2MywwLTEuNTYyLDAuNy0xLjU2MiwxLjU2MnY2LjU0SDcuNDFjLTAuODYyLDAtMS41NjIsMC43LTEuNTYyLDEuNTYzdjM5Ljc5NQ0KCQlDNS44NDgsODAuMjAxLDYuNTQ3LDgwLjksNy40MSw4MC45eiBNMzQuNDkyLDU3Ljg3NGgtMS43OTZ2LTYuNzY4aDEuNzk2VjU3Ljg3NHogTTI2LjU2MywzNC41NzRoMTQuMDU1djMuNDA2SDI2LjU2M1YzNC41NzR6DQoJCSBNMTAuNTQ0LDQyLjY3OGg0Ny4xNzN2MTEuOThIMzYuOTQydi00LjAwNmMwLTAuODYzLTAuNjk5LTEuNTYzLTEuNTYyLTEuNTYzaC0zLjU4MmMtMC44NjMsMC0xLjU2MiwwLjY5OS0xLjU2MiwxLjU2M3Y0LjAwNg0KCQlIMTAuNTQ0VjQyLjY3OHoiLz4NCgk8cGF0aCBkPSJNNjguNzM0LDgwLjloNDkuOTU4YzAuODA3LDAsMS40Ni0wLjY1MywxLjQ2LTEuNDZWMTcuNTM0YzAtMC44MDYtMC42NTMtMS40NTktMS40Ni0xLjQ1OWgtMTQuNTI0VjkuOTYxDQoJCWMwLTAuODA3LTAuNjUzLTEuNDYtMS40Ni0xLjQ2aC0xOWMtMC44MDcsMC0xLjQ2LDAuNjUzLTEuNDYsMS40NnY2LjExNUg2OC43MzRjLTAuODA3LDAtMS40NiwwLjY1My0xLjQ2LDEuNDU5Vjc5LjQ0DQoJCUM2Ny4yNzQsODAuMjQ3LDY3LjkyNyw4MC45LDY4LjczNCw4MC45eiBNODYuNjM4LDEyLjg5aDEzLjEzOXYzLjE4Nkg4Ni42MzhWMTIuODl6Ii8+DQo8L2c+DQo8L3N2Zz4NCg=="/>
    create_language_pie(language_stats, total_length, total_repos, "languages.svg")
    tmp.write('<img src="languages.svg"/>')

    # Commit activity
    create_commits_chart(all_repos, datetime.now() - timedelta(days=365), "commits.svg")
    tmp.write('<img src="commits.svg"/>')

    tmp.write("---\n")
    tmp.write(f"Built with python @ {datetime.utcnow()}")
    tmp.flush()
