# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Zia integration decorators """
import logging
import time
from functools import wraps
from .exceptions import ZiaException, ZiaRateLimitException

NUM_TRIES = 3 # No of request tries to attempt request.
RETRY_DELAY = 3 # Delay before retrying request.
RETRY_BACKOFF = 2 # Multiplication value for retry exponential backoff.
LOG = logging.getLogger(__name__)


def retry(num_tries=NUM_TRIES, retry_delay=RETRY_DELAY, retry_backoff=RETRY_BACKOFF,
          raise_on_max=False):
    """"Retry decorator for ZIA api requests with exponential backoff.

    :param num_tries: Number of tries for the request.
    :param retry_delay: Delay in seconds, to wait between retries.
    :param retry_backoff: Backoff multiplier.
    :param raise_on_max: Raise an error if max reached.
    :return: Parsed url.
    """
    def retry_decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            tries = 1
            delay = retry_delay
            while tries < num_tries + 1:
                try:
                    return func(*args, **kwargs)

                except ZiaRateLimitException as zia_rl_ex:
                    if tries == num_tries:
                        if raise_on_max:
                            raise zia_rl_ex
                        return zia_rl_ex.args[0]
                    # Example zia_rl_ex.args tuple value:
                    # ({'error_code': 429, 'status': 'Exceeded the rate limit or quota.',
                    # 'text': {'message': 'Rate Limit (1000/HOUR) exceeded', 'Retry-After': '868 seconds'}},)
                    retry_after = int(zia_rl_ex.args[0]["text"]["Retry-After"].split()[0]) + 1
                    LOG.info("Ratelimit exception %s: retrying in %s seconds...", zia_rl_ex, retry_after)
                    time.sleep(retry_after)
                    tries += 1

                except ZiaException as zia_ex:
                    if tries == num_tries:
                        if raise_on_max:
                            raise zia_ex
                        return zia_ex.args[0]
                    LOG.info("Exception %s, retrying in %s seconds...", zia_ex, delay)
                    time.sleep(delay)
                    tries += 1
                    delay *= retry_backoff

        return func_wrapper

    return retry_decorator
