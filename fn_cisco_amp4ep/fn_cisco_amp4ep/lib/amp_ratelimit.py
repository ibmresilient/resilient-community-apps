# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Class for Resilient circuits Functions supporting Rate Limiting for Cisco AMP for endpoints  """
import logging
import time
import threading

LOG = logging.getLogger(__name__)
AMP_RL_RESET_MAX = 3600
AMP_RL_LIMIT_MAX = 3000
# Use module variables to share rate limit dynamic between functions.
REQ_TIMESTAMPS = []
LIMIT_INFO = {}

rl_lock = threading.Lock()


class LimitValues():
    """
    Class to store updated Rate limit information.
    """
    def __init__(self):
        self.limit = 0
        self.calls_remaining = 0
        self.min_time = 0.0
        self.reset_period = 0.0

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

    @staticmethod
    def _get_lastest_req_ts():
        """" Get oldest in-progress request timestamp.

        :return : Return timestamp in secs.

        """
        return LIMIT_INFO["lastest_request_ts"]

    def _set_limits_from_last_saved(self, lv, r_cnt):
        """ Method to set limit values based on last saved update.

        :param lv: Instance of LimitValues to store values.
        :param r_cnt: Count of oustanding requests which have not received responses.
        """
        try:
            # Dict LIMIT_INFO should have the following 4 keys: "X-RateLimit-Limit", "X-RateLimit-Remaining",
            # "X-RateLimit-Reset", "X-RateLimit-ResetDate" with numeric values saved from request responses.
            # Only the 1st 3 headers are used in the calculations.
            for k, v in LIMIT_INFO.items():
                if k.endswith("Limit"):
                    # Set default minimum interval between calls.
                    lv.limit = min(int(v), AMP_RL_LIMIT_MAX)
                    lv.min_time = AMP_RL_RESET_MAX / float(v)
                if k.endswith("Remaining"):
                    # We had this many remaining calls after last request.
                    lv.calls_remaining = min(int(v), AMP_RL_LIMIT_MAX)
                    if r_cnt:
                        # Decrease calls_remaining if new requests since limit information updated.
                        lv.calls_remaining -= r_cnt
                if k.endswith("Reset"):
                    # Timestamp (seconds) when this limit will reset from last request.
                    lv.reset_period = float(v)
        except ZeroDivisionError:
            # Got here if limit is zero, something went along saving limit information in previous run.
            LOG.error("Zero value detected for rate limit parameter 'X-RateLimit-Limit'.")
            raise ValueError("Zero value detected for rate limit parameter 'X-RateLimit-Limit'.")

    def _calculate_latest_delay(self, lv, now, e_time, r_cnt, o_ts):
        """ Method to calculate delay based on last update.


        :param lv: Instance of 'LimitValues' to store values.
        :param now: Time when calling function started.
        :param e_time: Time elapsed since limit values last updated or since period was reset.
        :param r_cnt: Count of outstanding reqests which have not received responses.
        :param o_ts: Oldest timestamp of requests awaiting responses.
        :return : Return delay period value.
        """
        delay_period = 0
        lastest_ts = self._get_lastest_req_ts()

        # Alter self.min_time to take account of changes in limiting interval.
        lv.reset_period = lv.reset_period - e_time
        try:
            lv.min_time = lv.reset_period / lv.calls_remaining
        except ZeroDivisionError:
            LOG.error("Unexpected zero value detected for calls remaining '%s'.", self.calls_remaining)
            raise ValueError("Unexpected zero value detected for calls remaining '{}'."
                             .format(lv.calls_remaining))

        if r_cnt:
            # If other requests out-standing which have not yet updated limit information.
            left_to_wait = (o_ts + (r_cnt * lv.min_time)) - now
        else:
            # If no other requests out-standing.
            left_to_wait = (lastest_ts + lv.min_time) - now
        if left_to_wait > 0:
            delay_period = left_to_wait

        return delay_period

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
            # Save timestamp when limits updated.
            self._set_limit_update_ts(now)
            # Ensure we have all 4 rate limit headers returned before updating limits.
            # The header keys are "X-RateLimit-Limit", "X-RateLimit-Remaining",
            # "X-RateLimit-Reset", "X-RateLimit-ResetDate" which should have numeric values.
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
        now = time.time()
        lv = LimitValues()
        delay_period = 0

        with rl_lock:
            limit_update_ts = self.get_limit_update_ts()
            (request_count, oldest_ts) = self._get_oldest_req_ts_info()
            if not limit_update_ts:
                delay_period = 0
            else:
                # Set time elapsed since limit values last updated from a response.
                elapsed_time = now - limit_update_ts
                self._set_limits_from_last_saved(lv, request_count)

                if lv.calls_remaining <= 0:
                    if lv.reset_period - elapsed_time > 1:
                        # Calls remaining are used up, wait until end of current period otherwise
                        # a 429 error will be thrown.
                        delay_period = lv.reset_period - elapsed_time
                        return delay_period
                    else:
                        # Assume 'reset_period' has reset.
                        # Adjust/Reset values for new period.
                        elapsed_time = elapsed_time - lv.reset_period
                        lv.calls_remaining = AMP_RL_LIMIT_MAX + lv.calls_remaining
                        lv.reset_period = AMP_RL_RESET_MAX

                delay_period = self._calculate_latest_delay(lv, now, elapsed_time, request_count, oldest_ts)
            return delay_period