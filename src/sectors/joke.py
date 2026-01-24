import httpx


async def get_joke() -> tuple[str, str]:
    url = "https://official-joke-api.appspot.com/jokes/random"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code >= 400:
            return "JOKE", "Could not fetch a joke at this time."

        joke_data = response.json()
        return (
            "JOKE",
            f"""## Daily joke from <a href="https://official-joke-api.appspot.com/">official-joke-api</a>

>{joke_data["setup"]}

>{joke_data["punchline"]}
""",
        )
