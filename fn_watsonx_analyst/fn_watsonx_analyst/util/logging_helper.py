import contextvars
import logging
import random
import string

request_id_var = contextvars.ContextVar("request_id", default=None)

class RequestIdLoggingFilter(logging.Filter):
    def filter(self, record: logging.LogRecord):
        """Add the request ID from the context variable to the log record"""
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

def get_request_id() -> str:
    return request_id_var.get()

def set_request_id(req_id: str):
    request_id_var.set(req_id)

def generate_request_id() -> str:
    """Generate a random 12-character alphanumeric string"""
    req_id = "".join(random.choices(string.ascii_letters + string.digits, k=6))
    request_id_var.set(req_id)

    return req_id
