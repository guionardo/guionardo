import asyncio

from src.sectors import get_context
from src.template import process_template


async def main(template_file:str,output_file:str) -> None:
    with open(template_file,"r") as f:
        template = f.read()
    
    context = await get_context()
    processed_template = await process_template(template,context)
    with open(output_file, "w") as f:
        f.write(processed_template)

if __name__ == "__main__":
    asyncio.run(main('TEMPLATE.md','README.md'))