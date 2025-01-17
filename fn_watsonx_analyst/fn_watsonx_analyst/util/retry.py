from functools import wraps
import logging
import time

from fn_watsonx_analyst.util.errors import WatsonxTooManyRequestsException

log = logging.getLogger(__name__)


def retry_with_backoff(retries=3, delay=1.5, backoff=2):
    def retry_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal retries, delay
            exc: Exception = None
            while retries > 0:
                try:
                    return func(*args, **kwargs)
                except WatsonxTooManyRequestsException as e:
                    exc = e
                    retries -= 1
                    log.warning(f"Retrying request in {delay} seconds...")
                    time.sleep(delay)
                    delay *= backoff

                except Exception as e:
                    raise e
            raise exc

        return wrapper

    return retry_decorator
