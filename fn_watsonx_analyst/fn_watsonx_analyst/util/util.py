import re

from pydantic import BaseModel
from resilient import SimpleClient

from ibm_watsonx_ai.foundation_models.schema import (
    TextChatResponseFormat, TextChatResponseFormatType, TextChatResponseJsonSchema)

def defang_text(input_str: str) -> str:
    return re.sub(r"<a\s+[^>]*>(.*?)</a>", r"\1", input_str, flags=re.DOTALL)

def get_soar_version(res_client: SimpleClient) -> str:
    const = res_client.get_const(timeout=5)
    return const.get("server_version", {}).get("version", "")

def base_model_to_structured_output(model: BaseModel) -> TextChatResponseFormat:
    """Construct a watsonx structured output payload from a pydantic model"""
    if model is None:
        return model

    return TextChatResponseFormat(
        TextChatResponseFormatType.JSON_SCHEMA, TextChatResponseJsonSchema(
            name=model.__name__, schema=model.model_json_schema()
        )
    )

def format_duration(seconds):
    """Provide a a plaintext english duration"""
    negative = seconds < 0
    abs_seconds = abs(seconds)

    SECS_PER_YEAR   = 365.25 * 24 * 60 * 60          # ~31 557 600
    SECS_PER_MONTH  = 30 * 24 * 60 * 60              # 2 592 000
    SECS_PER_DAY    = 24 * 60 * 60                   #   86 400
    SECS_PER_HOUR   = 60 * 60                        #    3 600
    SECS_PER_MINUTE = 60                              #      60

    units = [
        ("year",   SECS_PER_YEAR),
        ("month",  SECS_PER_MONTH),
        ("day",    SECS_PER_DAY),
        ("hr",     SECS_PER_HOUR),
        ("min",    SECS_PER_MINUTE),
        ("sec",    1)
    ]

    parts = []
    cnt = 0 # only show 3 significant values
    for name, size in units:
        if cnt >= 3:
            break

        qty, abs_seconds = divmod(abs_seconds, size)
        if qty:
            # plural / singular
            part_name = name + ("s" if qty != 1 else "")
            parts.append(f"{int(qty)} {part_name}")
            cnt += 1

    # If the duration was zero seconds, make sure we return "0 sec"
    if not parts:
        parts.append("0 sec")

    result = ", ".join(parts)
    return f"-{result}" if negative else result
