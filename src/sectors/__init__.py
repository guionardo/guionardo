import asyncio
from typing import Any, Awaitable, Callable

from .badges import get_badges
from .bio import session_bio
from .github_readme_stats import get_readme_stats
from .joke import get_joke
from .footer import get_footer
from .repositories import get_last_updated_repositories

FuncType = Callable[[], Awaitable[Any]]

SESSIONS: list[FuncType] = [
    session_bio,
    get_joke,
    get_badges,
    get_readme_stats,
    get_footer,
    get_last_updated_repositories,
]


async def get_context() -> dict[str, str]:
    context = {}
    results = await asyncio.gather(*(session() for session in SESSIONS))
    context = {key: value for key, value in results}
    return context
