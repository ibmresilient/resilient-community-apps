import json
import os
import re
from typing import List

from fn_watsonx_analyst.types.model_config import ModelConfigOption


def get_model_config() -> List[ModelConfigOption]:
    model_config_path = os.path.abspath(
        os.path.join(os.path.dirname("fn_watsonx_analyst/util/"), "model_config.json")
    )
    with open(model_config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def defang_text(input_str: str) -> str:
    return re.sub(r"<a\s+[^>]*>(.*?)</a>", r"\1", input_str, flags=re.DOTALL)
