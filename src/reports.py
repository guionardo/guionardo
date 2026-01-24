from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from itertools import chain
from typing import List, Tuple

import pygal

from src.models import Commit, Repository


def format_percent(value: float) -> str:
    if value > 0.2:
        return f"{100 * value:.0f}%"
    if value > 0.01:
        return f"{100 * value:.1f}%"
    return f"{100 * value:.2f}%"


@dataclass
class LanguageStat:
    name: str = ""
    length: int = 0
    repos: list[str] = field(default_factory=list)
    repos_length: dict[str, int] = field(default_factory=lambda: defaultdict(int))
    greater_repo_name: str | None = None
    greater_repo_length: int =0

    def add_repo(self, repo: Repository):
        self.repos.append(repo.full_name)
        self.repos_length[repo.full_name] = repo.languages.get(self.name, 0)
        length = repo.languages.get(self.name, 0)
        self.length += length
        if self.greater_repo_length < length:
            self.greater_repo_length = length
            self.greater_repo_name = repo.full_name

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

    def greater_repo(self) -> str | None:
        mr = None
        ml = 0
        for repo, length in self.repos_length.items():
            if length > ml:
                mr = repo
        return mr


def get_significant(ls: List[LanguageStat]) -> List[LanguageStat]:
    total_length = sum(l.length for l in ls)
    threshold = total_length * 0.95
    out = []
    accum = 0
    others = LanguageStat(name="Others", length=0)
    others_langs = set()
    for l in ls:
        accum += l.length
        if accum <= threshold:
            out.append(l)
            continue
        others_langs.add(l.name)
        others.length += l.length
        others.repos.extend(l.repos)

    if others.length > 0:
        others.repos = list(set(others.repos))
        others.name = ", ".join(sorted(others_langs))
        out.append(others)

    return out


def get_language_stats(repos: List[Repository]) -> Tuple[List[LanguageStat], int, int]:
    languages = defaultdict(LanguageStat)
    total_length = 0
    total_repos = 0
    for repo in repos:
        for language, length in repo.languages.items():
            total_length += length
            total_repos += 1
            languages[language].name = language
            languages[language].add_repo(repo)
            # languages[language].length += length
            # languages[language].repos.append(repo.full_name)
            # languages[language].repos_length[repo.full_name] = length

    langs = list(languages.values())
    langs.sort(key=lambda x: x.length, reverse=True)
    return langs, total_length, total_repos


def create_language_pie(
    langs: List[LanguageStat], total_length: int, total_repos: int, filename: str
):
    pie_chart = pygal.Pie()
    pie_chart.title = "Languages distribution"
    pie_chart.setup()
    percentil = 0
    others = 0
    others_names = []
    langs = get_significant(langs)
    for lang in langs:
        percentil += lang.length
        if (percentil / total_length) < 0.9:
            pie_chart.add(lang.name, lang.length)
            continue
        others += lang.length
        others_names.append(lang.name)
    if others:
        pie_chart.add(", ".join(others_names), others)

    pie_chart.render_to_file(filename)


def fmtMult(x):
    suf = ""
    if x >= 1_000_000_000:
        x /= 1_000_000_000
        suf = "B"
    elif x >= 1_000_000:
        x /= 1_000_000
        suf = "M"
    elif x >= 1_000:
        x /= 1_000
        suf = "K"
    return f"{x:.1f}{suf}"


def create_language_bar(
    langs: List[LanguageStat], total_length: int, total_repos: int, filename: str
):
    config = pygal.Config(
        show_legend=True,
        print_values=True,
        # print_values_position="bottom",
        print_labels=True,
        legend_at_bottom_columns=True,
        value_formatter=fmtMult,
    )
    bar_chart = pygal.Bar(config)
    bar_chart.title = "Languages distribution (by length)"
    langs = get_significant(langs)
    for lang in langs:
        bar_chart.add(
            lang.name,
            lang.length,
        )

    bar_chart.render_to_file(filename)


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

    config = pygal.Config(print_values=True)
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
