import asyncio


async def get_readme_stats() -> tuple[str, str]:
    urls = [
        "https://github-readme-stats.vercel.app/api?username=guionardo&show_icons=true&hide_title=true&count_private=true&include_all_commits=true&theme=dark",
        "https://github-readme-stats.vercel.app/api/top-langs/?username=guionardo&theme=dark",
        "https://github-readme-stats.vercel.app/api/wakatime?username=guionardo&custom_title=Last%20week&layout=compact&theme=dark",
    ]
    result = asyncio.gather(*(async_get(url) for url in urls))
    return "README_STATS", "\n".join(await result)


async def async_get(url) -> str:
    try:
        return f'<img src="{url}" alt="GitHub Readme Stats" height="180em"/>'

    except Exception as e:
        return f"<p>Error fetching image: {e}</p>"
