import base64


def get_img_svg_tag(src: bytes, height: int = 180) -> str:
    b64 = base64.b64encode(src)
    return f'<img height="{height}em" src="data:image/svg+xml;base64,{b64.decode()}" />'
