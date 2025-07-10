import random
from functools import wraps
import time

from fn_watsonx_analyst.util.errors import WatsonxTooManyRequestsException
from fn_watsonx_analyst.util.util import create_logger

log = create_logger(__name__)


def retry_with_backoff(retries=3, delay=3, backoff=2):
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
                    delay = random.uniform(delay, delay * 1.5)
                    log.warning("Retrying request in %d seconds...", delay)
                    time.sleep(delay)
                    delay *= backoff

                except Exception as e:
                    raise e
            raise exc

        return wrapper

    return retry_decorator
