import asyncio
import os

from src.sectors import get_context
from src.template import process_template


async def main(template_file: str, output_file: str) -> None:
    with open(template_file, "r") as f:
        template = f.read()

    context = await get_context()
    processed_template = await process_template(template, context)
    with open(output_file, "w") as f:
        f.write(processed_template)


if __name__ == "__main__":
    if os.path.exists("OUTPUT.md"):
        os.remove("OUTPUT.md")
    asyncio.run(main("TEMPLATE.md", "OUTPUT.md"))
