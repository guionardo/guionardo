import inspect
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone


def _create_class_from_dict(cls, data: dict):
    return cls(
        **{k: v for k, v in data.items() if k in inspect.signature(cls).parameters}
    )


@dataclass
class User:
    name: str
    location: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls, data):
        return _create_class_from_dict(cls, data)

    def __post_init__(self):
        self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S%z")
        self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S%z")


@dataclass
class Org:
    name: str
    location: str
    description: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls, data):
        return _create_class_from_dict(cls, data)

    def __post_init__(self):
        self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S%z")
        self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S%z")


@dataclass
class Repository:
    name: str
    full_name: str
    created_at: datetime
    updated_at: datetime
    pushed_at: datetime
    language: str
    html_url: str
    description: str
    size: int
    visibility: str
    languages: dict = field(default_factory=dict)
    commits: list["Commit"] = field(default_factory=list)
    topics: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data):
        return _create_class_from_dict(cls, data)

    def __post_init__(self):
        self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S%z")
        self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S%z")
        self.pushed_at = datetime.strptime(self.pushed_at, "%Y-%m-%dT%H:%M:%S%z")

    @property
    def last_change(self) -> datetime:
        return (
            self.commits[0].date
            if self.commits
            else max(self.pushed_at, self.created_at)
        )

    @property
    def activity_age(self) -> timedelta:
        return self.last_change - self.created_at

    @property
    def age(self) -> timedelta:
        return datetime.now(timezone.utc) - self.created_at

    @property
    def estado_atualizacao(self) -> str:
        last_change_age = (
            datetime.now(tz=self.last_change.tzinfo) - self.last_change
        ).days
        if last_change_age > 365:
            return "💀 Inactive (more than a year)"

        if last_change_age > 183:
            return "💤 Sleeping (more than 6 months)"

        if last_change_age > 30:
            return "🦥 Active (more than a month)"

        return "🚀 Recently Active"

    def last_commit(self) -> str:
        if self.commits:
            return f"{len(self.commits)} commits<br>{self.commits[0]}"
        return "No commits"

    def last_commit_date(self) -> datetime | None:
        if self.commits:
            return self.commits[0].date
        return None

    def detail(self) -> str:
        return f"""<details>
        <summary><a href="https://github.com/{self.full_name}" _target="new">{self.full_name}</a> : {self.last_change:%Y-%m-%d}</summary>
        <p>{self.activity_age}</p>
        <p>{self.description}</p>        
        <p>{self.last_commit()}</p>
</details>
"""


@dataclass
class Commit:
    commit: dict
    sha: str
    author: str = ""
    message: str = ""
    url: str = ""
    date: datetime = None

    def __post_init__(self):
        author = self.commit.get("author", {})
        self.author = author.get("name", "UNIDENTIFIED")
        self.date = datetime.strptime(author.get("date"), "%Y-%m-%dT%H:%M:%S%z")
        self.message = self.commit.get("message")
        self.url = self.commit.get("url")

    @classmethod
    def from_dict(cls, data):
        return _create_class_from_dict(cls, data)

    def __str__(self) -> str:
        return f'<a href="{self.url}" title="{self.author} @ {self.date}">Commit {self.sha[0:8]}</a><pre>{self.message}</pre>'


# tv = {
#     "count": 13,
#     "uniques": 1,
#     "views": [
#         {"timestamp": "2026-01-09T00:00:00Z", "count": 0, "uniques": 0},
#         {"timestamp": "2026-01-10T00:00:00Z", "count": 0, "uniques": 0},
#         {"timestamp": "2026-01-11T00:00:00Z", "count": 0, "uniques": 0},
#         {"timestamp": "2026-01-12T00:00:00Z", "count": 0, "uniques": 0},
#         {"timestamp": "2026-01-13T00:00:00Z", "count": 0, "uniques": 0},
#         {"timestamp": "2026-01-14T00:00:00Z", "count": 11, "uniques": 1},
#         {"timestamp": "2026-01-15T00:00:00Z", "count": 0, "uniques": 0},
#         {"timestamp": "2026-01-16T00:00:00Z", "count": 0, "uniques": 0},
#         {"timestamp": "2026-01-17T00:00:00Z", "count": 0, "uniques": 0},
#         {"timestamp": "2026-01-18T00:00:00Z", "count": 1, "uniques": 1},
#         {"timestamp": "2026-01-19T00:00:00Z", "count": 1, "uniques": 1},
#         {"timestamp": "2026-01-20T00:00:00Z", "count": 0, "uniques": 0},
#         {"timestamp": "2026-01-21T00:00:00Z", "count": 0, "uniques": 0},
#         {"timestamp": "2026-01-22T00:00:00Z", "count": 0, "uniques": 0},
#     ],
# }


# @dataclass
# class TrafficViews: ...
