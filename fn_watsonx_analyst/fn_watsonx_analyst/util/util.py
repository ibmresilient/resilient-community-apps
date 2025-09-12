import re


def defang_text(input_str: str) -> str:
    return re.sub(r"<a\s+[^>]*>(.*?)</a>", r"\1", input_str, flags=re.DOTALL)

