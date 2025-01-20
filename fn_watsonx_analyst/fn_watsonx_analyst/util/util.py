import contextvars
import json
import logging
import os
import random
import re
import string
from typing import List

from fn_watsonx_analyst.types.model_config import ModelConfigOption

request_id_var = contextvars.ContextVar("request_id", default=None)

class RequestIdLoggingFilter(logging.Filter):
    def filter(self, record):
        # Add the request ID from the context variable to the log record
        record.request_id = request_id_var.get() or "N/A"
        return True

def create_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.addFilter(RequestIdLoggingFilter())

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s:%(lineno)d] - [Request ID: %(request_id)s] - %(message)s"
    )
    handler.setFormatter(formatter)

    logger.handlers.clear() # remove existing default
    logger.addHandler(handler)
    logger.propagate = False # don't propagate to root logger, just use custom.

    return logger

def generate_request_id() -> str:
    # Generate a random 12-character alphanumeric string
    req_id = "".join(random.choices(string.ascii_letters + string.digits, k=6))
    request_id_var.set(req_id)

    return req_id

def get_model_config() -> List[ModelConfigOption]:
    model_config_path = os.path.abspath(
        os.path.join(os.path.dirname("fn_watsonx_analyst/util/"), "model_config.json")
    )
    with open(model_config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def defang_text(input_str: str) -> str:
    return re.sub(r"<a\s+[^>]*>(.*?)</a>", r"\1", input_str, flags=re.DOTALL)
