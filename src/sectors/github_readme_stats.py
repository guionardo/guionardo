import asyncio

import httpx

from src.tools.html import get_img_svg_tag


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
        # async with httpx.AsyncClient() as client:
            return f'<img src="{url}" alt="GitHub Readme Stats" height="180em"/>'
            # response = await client.get(url)
            # response.raise_for_status()

            # body = await response.aread()

            # return get_img_svg_tag(body, height=180)

    except Exception as e:
        return f"<p>Error fetching image: {e}</p>"
