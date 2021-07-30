# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Zia integration decorators """
import logging
import time
import threading
from functools import wraps
from .exceptions import ZiaException, ZiaRateLimitException

LOG = logging.getLogger(__name__)
NUM_TRIES = 4 # No of request tries to attempt request.
RETRY_DELAY = 3 # Delay before retrying request.
RETRY_BACKOFF = 2 # Multiplication value for retry exponential backoff.
# Ratelimit settings.
# RESET_MAX: The amount of time (secs) before the rate limit resets after making initial call within 1 hour period.
RESET_MAX = 3600
# limit_max: Maximum function default invocations for a request method allowed within a time period.
RL_DEFS = {
    "get": {
        "limit_max": 1000,
    },
    "put": {
        "limit_max": 400,
    },
    "post": {
        "limit_max": 400,
    },
}
# Map of endpoint types by method supported by ratelimiter
EP_MAP = {
    "get": ["blocklist", "allowlist", "categories", "sandbox_report"],
    "post": ["authenticate", "blocklist_action", "categories", "activate"],
    "put": ["allowlist", "categories"]
}
# Create RLock object for each request method type.
LOCKS = {}
for k in ["get", "post", "put"]:
    LOCKS.setdefault(k, threading.RLock())


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

class RateLimit():
    """"
    RateLimiter class decorator for ZIA api requests.
    """
    #Class attribute Dict to hold ratelimit state for each request method/endpoint type.
    # The state will be shared by ratelimit threads
    #Example state dict content:
    #    {'get': {'blocklist': {'last_reset': 1627481586.467038, 'num_calls': 1},
    #             'allowlist': {'last_reset': 1627481493.014187, 'num_calls': 1},
    #             'categories': {'last_reset': 1627481654.963858, 'num_calls': 1},
    #             'sandbox_report': {'last_reset': None, 'num_calls': 0}},
    #     'put': {'allowlist': {'last_reset': None}, 'categories': {'last_reset': None, 'num_calls': 0}},
    #     'post': {'authenticate': {'last_reset': 1627481487.153119, 'num_calls': 3},
    #              'blocklist_action': {'last_reset': None}, 'categories': {'last_reset': None},
    #              'activate': {'last_reset': None, 'num_calls': 0}}}
    states = {
        "get": {},
        "put": {},
        "post": {},
    }
    def __init__(self, init=False, method="get", ep="allowlist", limit_max=None):
        """
        The ratelimiter will be share by multiple threads. The class will be imported
        by each function to ensure it is shared across the threads.

        :param init: Initialize the settings on startup of a function.
        :param ep: A string with endpoint type e.g. "allowlist", "blocklist" etc
        :param method: A string with request method should be one of "get","post" or "put".
        """
        self.init = init
        self.method = method
        self.ep = ep
        self.limit_max = limit_max

        if init:
            with LOCKS[method]:
                # Set the initial state for the method for the decorator in a
                # thread safe way.
                self._set_init_state(method, ep, init=True)

    def __call__(self, func):
        """
        Return a wrapped function that prevents further function invocations if
        previously called within a specified period of time.

        :param func: The function to decorate.
        :return: Decorated function.
        """
        @wraps(func)
        def func_wrapper(*args, **kargs):
            """
            Wrapper for the function to be decorated by the ratelimiter.
            :param args: Decorated function arguments list.
            :param kargs: Decorated function arguments dict.
            :raises: ZiaRateLimitException
            """
            method = self.method
            ep = self.ep

            if not self.limit_max:
                self.limit_max = RL_DEFS[method]["limit_max"]

            # Get default interval between calls.
            def_interval = self._calculate_interval(RESET_MAX, self.limit_max)

            if not self.init:
                with LOCKS[method]:
                    if RateLimit.states[method][ep]["last_reset"] is None:
                        # Set initial state if 1st run.
                        self._set_init_state(method, ep)
                        RateLimit.states[method][ep]["num_calls"] += 1
                    else:
                        time_left = self._window_time_remaining(method, ep)

                        # If the time window has elapsed then reset state.
                        if time_left <= 0:
                            self._set_init_state(method, ep)

                        # Get the number of calls already processed for the request method and endpoint.
                        num_calls = RateLimit.states[method][ep]["num_calls"]

                        # Increase the count of number of attempts to call the function.
                        RateLimit.states[method][ep]["num_calls"] += 1

                        # If the number of attempts to call the function exceeds the
                        # maximum then raise a ZiaRateLimitException exception.
                        if RateLimit.states[method][ep]["num_calls"] > self.limit_max:
                            err_msg = {"error_code": 429,
                                        "status": "Exceeded the rate limit or quota.",
                                        "text": {"message": "Rate Limit (1000/HOUR) exceeded",
                                                "Retry-After": "{} seconds".format(time_left)
                                                }
                                        }
                            raise ZiaRateLimitException(err_msg)

                        # Get expected time left in window.
                        expected_time_left = RESET_MAX - (num_calls * def_interval)

                        # Calculate the delay to use to throttle.
                        delay = time_left - expected_time_left

                        # Throttle the request.
                        if delay > 0:
                            time.sleep(delay)

            return func(*args, **kargs)
        return func_wrapper

    def _window_time_remaining(self, method, ep):
        """
        Get the time left in the current rate limit window.
        :param method: A string with request method can be one of "get","post" or "put"
        :param ep: A string with endpoint type e.g. "allowlist", "blocklist" etc
        :return: The remaing time.
        """
        elapsed = time.time() - RateLimit.states[method][ep]["last_reset"]
        return RESET_MAX - elapsed

    def _set_init_state(self, method, ep=None, init=False):
        """
        Set the initial state of the RateLimit class for a request method.
        :param method: A string with request method can be one of "get","post" or "put"
        :param ep: A string with endpoint type e.g. "allowlist", "blocklist" etc
        :param init: A boolean to determine if the decorator is in the setup mode.
        """
        if init:
            # Setup state dict in ratelimit class attribute for a request method.
            if method not in RateLimit.states:
                RateLimit.states[method] = {}
            for end_pt in EP_MAP[method]:
                if end_pt not in RateLimit.states[method]:
                    RateLimit.states[method][end_pt] = {}
                if "last_reset" not in RateLimit.states[method][end_pt]:
                    RateLimit.states[method][end_pt]["last_reset"] = None
                if "num_calls" not in RateLimit.states[method][end_pt]:
                    RateLimit.states[method][end_pt]["num_calls"] = 0
        else:
            RateLimit.states[method][ep]["last_reset"] = time.time()
            RateLimit.states[method][ep]["num_calls"] = 0

    def _calculate_interval(self, period, calls):
        """
        Calculate an interval value.
        :param period: Time over which to calculate interval
        :param calls: Number of calls withing time period.
        :return: Interval value (float).
        """
        try:
            # Calculate the latest interval between calls.
            interval = float(period/calls)
        except ZeroDivisionError:
            # Got here if denominator is zero, something went wrong..
            raise ValueError("Zero value detected setting 'interval'.")
        return interval
