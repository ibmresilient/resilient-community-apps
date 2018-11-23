# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Class for Resilient circuits Functions supporting Rate Limiting for Cisco AMP for endpoints  """
import logging
import time
import threading

LOG = logging.getLogger(__name__)
AMP_RL_RATE = 3600
AMP_RL_LIMIT = 3000
# Use module variables to share rate limit dynamic data shared between functions.
REQ_TIMESTAMPS = []
LIMIT_INFO = {}

rl_lock = threading.Lock()

class AmpRateLimit():
    """
    Class to store Rate limit information and introduce delays to throttle requests for
    Cisco AMP API calls.
    Class shares Rate limit data across Cisco AMP functions.
    """

    def __init__(self):
        """
        Class constructor
        """
        # Initialize global dict to defaults.
        with rl_lock:
            if not LIMIT_INFO:
                self._set_defaults()

    def _set_defaults(self):
        """ Set default values.

        """
        LIMIT_INFO.update({
            "X-RateLimit-Limit": 0.0,
            "X-RateLimit-Remaining": 0.0,
            "X-RateLimit-Reset": 0.0,
            "X-RateLimit-ResetDate": 0.0,
            "limit_update_ts": 0.0,
            "lastest_request_ts": 0.0
        })

    def _set_limit_update_ts(self, ts):
        """ Set time when get_delay executed.

        :param ts: Timestamp Unix format.

        """
        LIMIT_INFO["limit_update_ts"] = ts

    def _pop_request_ts(self):
        """"
        Remove from start of current in-progress request backlog.

        """
        if len(REQ_TIMESTAMPS):
            return REQ_TIMESTAMPS.pop(0)

    def _get_oldest_req_ts_info(self):
        """"
        Get oldest request timestamp and in-progress request count.

        :return : Return tuple with in-progress request count and oldest timestamp in secs.

        """
        if len(REQ_TIMESTAMPS):
            return (len(REQ_TIMESTAMPS), REQ_TIMESTAMPS[0])
        else:
            return (0,0)

    def _get_lastest_req_ts(self):
        """" Get oldest in-progress request timestamp.

        :return : Return timestamp in secs.

        """
        return LIMIT_INFO["lastest_request_ts"]

    def add_ts(self, ts):
        """ Add time to list and update latest executed timestamp.

        :param ts: Timestamp Unix format.

        """
        with rl_lock:
            REQ_TIMESTAMPS.append(ts)
            LIMIT_INFO["lastest_request_ts"] = ts

    def get_limit_update_ts(self):
        """"
        Return timestamp for when limits last updated.

        :return : Return timestamp.

        """
        return LIMIT_INFO["limit_update_ts"]

    def save_limits(self, limit_headers):
        """Save rate limit headers from request response and execution timestamp.

        :param limit_headers: Rate limit headers from response.

        """
        with rl_lock:
            now = time.time()
            self._set_limit_update_ts(now) # Save timestamp when limits updated.
            # Ensure we have all 4 rate limit headers returned before updating limits.
            if len(limit_headers) == 4:
                for k, v in limit_headers.items():
                    LIMIT_INFO[k] = v
            else:
                LOG.error("Not all required rate limit headers returned from request response.")
                raise ValueError("Not all required rate limit headers returned from request response.")
            # Pop oldest timestamp so window moves forward.
            self._pop_request_ts()

    def get_delay(self):
        """Calculate delay to  wait (seconds) before making another api call.

        :return delay_period: Delay period in secs.

        """
        delay_period = 0
        reset_period = 0
        min_time = 0
        calls_remaining = AMP_RL_LIMIT

        with rl_lock:
            now = time.time()
            (request_count, oldest_ts) = self._get_oldest_req_ts_info()
            lastest_ts = self._get_lastest_req_ts()
            limit_update_ts = self.get_limit_update_ts()

            if not limit_update_ts:
                delay_period = 0
            else:
                elapsed_time = now - limit_update_ts
                try:
                    for k, v in LIMIT_INFO.items():
                        if k.endswith("Limit"):
                            # Set default minimum interval between calls.
                            min_time = AMP_RL_RATE / float(v)
                        if k.endswith("Remaining"):
                            # We had this many remaining calls after last request.
                            calls_remaining = min(int(v), calls_remaining)
                        if k.endswith("Reset"):
                            # Timestamp (seconds) when this limit will reset from last request.
                            reset_period = float(v)
                except ZeroDivisionError:
                    # Got here if limit is zero, something went along saving limit information in previous run.
                    LOG.error("Zero value detected for rate limit parameter 'X-RateLimit-Limit'.")
                    raise ValueError("Zero value detected for rate limit parameter 'X-RateLimit-Limit'.")

                if calls_remaining <= 0:
                    if reset_period - elapsed_time > 1:
                        # Calls remaining are used up, wait until end of current period otherwise
                        # a 429 error will be thrown.
                        delay_period = reset_period - elapsed_time
                    else:
                        # Assume reset_period has in fact reset.
                        delay_period = 0
                else:
                    # Increase min_time from default if rate limiting interval has increased.
                    new_reset = reset_period - elapsed_time
                    if request_count:
                        # Decrease calls_remaining if new requests since limit information updated.
                        calls_remaining -= request_count
                    try:
                        new_min = new_reset/calls_remaining
                    except ZeroDivisionError:
                        LOG.error("Unexpected zero value detected for calls remaining '%s'.", calls_remaining)
                        raise ValueError("Unexpected zero value detected for calls remaining '{}'."
                                         .format(calls_remaining))

                    if new_min > min_time:
                        min_time = new_min

                    if request_count:
                        # If other requests out-standing which have not yet updated limit information.
                        left_to_wait = (oldest_ts + (request_count * min_time)) - now
                    else:
                        # If no other requests out-standing.
                        left_to_wait =  (lastest_ts + min_time) - now
                    if left_to_wait > 0:
                        delay_period = left_to_wait

            return delay_period