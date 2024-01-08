from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from itertools import chain
from typing import List, Tuple

import pygal
from models import Commit, Repository


def format_percent(value: float) -> str:
    if value > 0.2:
        return f"{100*value:.0f}%"
    if value > 0.01:
        return f"{100*value:.1f}%"
    return f"{100*value:.2f}%"


@dataclass
class LanguageStat:
    name: str = ""
    length: int = 0
    repos: list[str] = field(default_factory=list)

    def percent_by_repositories(self, total_repos: int) -> float:
        return len(self.repos) / total_repos

    def percent_by_length(self, total_length: int) -> float:
        return self.length / total_length

    def detail(self, total_length) -> str:
        uls = "\n".join(f"<li>{repo}</li>" for repo in self.repos)
        return f"""<details>
<summary>{self.name} ({format_percent(self.percent_by_repositories(total_length))})</summary>
<ul>{uls}</ul>
</details>
"""


def get_language_stats(repos: List[Repository]) -> Tuple[List[LanguageStat], int, int]:
    languages = defaultdict(LanguageStat)
    total_length = 0
    total_repos = 0
    for repo in repos:
        for language, length in repo.languages.items():
            total_length += length
            total_repos += 1
            languages[language].name = language
            languages[language].length += length
            languages[language].repos.append(repo.full_name)

    langs = list(languages.values())
    langs.sort(key=lambda x: len(x.repos), reverse=True)
    return langs, total_length, total_repos


def create_language_pie(
    langs: List[LanguageStat], total_length: int, total_repos: int, filename: str
):
    pie_chart = pygal.Pie()
    pie_chart.title = "Languages distribution"
    for lang in langs:
        pie_chart.add(lang.name, len(lang.repos))

    pie_chart.render_to_file(filename)


def get_all_commits(repos: List[Repository]) -> List[Commit]:
    all_commits = list(chain.from_iterable([repo.commits for repo in repos]))
    all_commits.sort(key=lambda c: c.date)
    return all_commits


def create_commits_chart(repos: List[Repository], since: datetime, filename: str):
    commits = [
        commit
        for commit in get_all_commits(repos)
        if commit.date >= since.replace(tzinfo=timezone.utc)
    ]
    weeks = defaultdict(int)

    for commit in commits:
        week = (commit.date.year, int(commit.date.strftime("%U")))
        weeks[week] += 1

    config = pygal.Config()
    config.show_legend = False
    config.human_readable = True
    chart = pygal.Bar(config)
    chart.title = f"Commits since {since:%Y-%m-%d}"
    chart.x_labels = [
        (datetime(y, 1, 1) + timedelta(days=(w - 1) * 7)).strftime("%Y-%m %U")
        for y, w in weeks.keys()
    ]

    bar = chart.add("Commits", weeks.values())

    chart.render_to_file(filename)
