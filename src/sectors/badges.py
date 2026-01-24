# from src.gh_api import get_traffic_views


async def get_badges() -> tuple[str, str]:
    # traffic_views = await get_traffic_views()

    badges = [
        # f"{traffic_views}",
        "![Profile View Counter](https://komarev.com/ghpvc/?username=guionardo&style=for-the-badge)",
        "[![Keybase PGP](https://img.shields.io/keybase/pgp/guionardo?style=for-the-badge)](https://keybase.io/guionardo)",
        '<a href="https://guiosoft.prose.sh"><img src="https://img.shields.io/badge/Experimental%20Blog-guiosoft.prose.sh-blueviolet?style=for-the-badge" target="_blank"></a>',
        "[![KB](https://img.shields.io/badge/KB-Guionardo's%20Knowledge%20Bank-brightgreen?style=for-the-badge)](https://guionardo.github.io/kb)",
        "[![Email](https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white)](mailto:guionardo@gmail.com)",
        "[![Linkedin](https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/guionardo)",
    ]
    return "BADGES", "\n".join(badges)
