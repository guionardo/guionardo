async def process_template(template:str,context:dict[str,str]) -> str:
    for key, value in context.items():
        placeholder = f"%{key}%"
        template = template.replace(placeholder, value)
    return template