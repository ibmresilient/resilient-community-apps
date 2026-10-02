import contextvars
import logging
import logging.config

import random
import string

request_id_var = contextvars.ContextVar("request_id", default=None)

class RequestIdLoggingFilter(logging.Filter):
    def filter(self, record: logging.LogRecord):
        """Add the request ID from the context variable to the log record"""
        record.request_id = request_id_var.get() or "N/A"
        return True

class SuppressWatsonxLogs(logging.Filter):
    def filter(self, record: logging.LogRecord):
        return not record.name.startswith("ibm_watsonx_ai")



def create_logger(name: str) -> logging.Logger:
    # 1) Set up a global LogRecordFactory that adds request_id to *every* record
    old_factory = logging.getLogRecordFactory()

    def record_factory(*args, **kwargs):
        record = old_factory(*args, **kwargs)
        # Inject request_id; formatter can safely print %(request_id)s
        record.request_id = request_id_var.get() or "N/A"
        return record

    logging.setLogRecordFactory(record_factory)

    # 2) Configure logging once; keep root at DEBUG (or your level)
    logging.config.dictConfig({
        "version": 1,
        "disable_existing_loggers": False,  # don't clobber 3rd-party loggers
        "formatters": {
            "std": {
                # Now safe to use %(request_id)s for all records:
                "format": "%(asctime)s %(levelname)s [%(name)s:%(lineno)d] "
                          "- [Request ID: %(request_id)s] - %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "std",
            }
        },
        "root": {
            "handlers": ["console"],
        },
    })

    # Optional: bring specific noisy libs back under your control
    # If a library installs its own handlers and suppresses propagation,
    # clearing handlers + enabling propagation makes logs flow to your root.
    lib = logging.getLogger("ibm_watsonx_ai")
    lib.handlers.clear()   # remove handlers the lib may have added
    lib.propagate = True
    # Keep warnings/errors but drop debug/info, if you want:
    lib.setLevel(logging.WARNING)
    return logging.getLogger(name)

def get_request_id() -> str:
    return request_id_var.get()

def set_request_id(req_id: str):
    request_id_var.set(req_id)

def generate_request_id() -> str:
    """Generate a random 12-character alphanumeric string"""
    req_id = "".join(random.choices(string.ascii_letters + string.digits, k=6))
    request_id_var.set(req_id)

    return req_id
