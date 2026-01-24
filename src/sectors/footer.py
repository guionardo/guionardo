from datetime import datetime,timezone


async def get_footer() -> tuple[str, str]:
    return (
        "FOOTER",
        f"*Generated with [Guionardo's README Generator] @ {datetime.now(timezone.utc).isoformat()} UTC*",
    )
