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
    Simple class to store updated Rate limit information.
    """
    def __init__(self):
        self.limit = 0
        self.calls_remaining = 0
        self.min_time = 0.0
        self.reset_period = 0.0
        self.limit_update_ts = 0.0,
        self.lastest_ts = 0.0,
        self.oldest_ts = 0.0,
        self.request_count = 0

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

    @staticmethod
    def _set_defaults():
        """ Set default values.

        """
        LIMIT_INFO.update({
            "X-RateLimit-Limit": 0,
            "X-RateLimit-Remaining": 0,
            "X-RateLimit-Reset": 0,
            "X-RateLimit-ResetDate": 0,
            "limit_update_ts": 0.0,
            "lastest_request_ts": 0.0,
        })

    @staticmethod
    def _set_limit_update_ts(ts):
        """ Set time when get_delay executed.

        :param ts: Timestamp Unix format.

        """
        LIMIT_INFO["limit_update_ts"] = ts

    @staticmethod
    def _pop_request_ts():
        """"
        Remove from start of current in-progress request backlog.

        """
        if len(REQ_TIMESTAMPS):
            return REQ_TIMESTAMPS.pop(0)

    @staticmethod
    def _get_oldest_req_ts_info():
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

    def _set_limit_data_from_saved(self, lv):
        """ Method to set limit data based on saved updates.

        :param lv: Instance of LimitValues to store values.
        """
        lv.limit_update_ts = self.get_limit_update_ts()
        lv.lastest_ts = self._get_lastest_req_ts()
        (lv.request_count, lv.oldest_ts) = self._get_oldest_req_ts_info()
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
                    if lv.request_count:
                        # Decrease calls_remaining if new requests since limit information updated.
                        lv.calls_remaining -= lv.request_count
                if k.endswith("Reset"):
                    # Timestamp (seconds) when this limit will reset from last request.
                    lv.reset_period = float(v)
        except ZeroDivisionError:
            # Got here if limit is zero, something went along saving limit information in previous run.
            LOG.error("Zero value detected for rate limit parameter 'X-RateLimit-Limit'.")
            raise ValueError("Zero value detected for rate limit parameter 'X-RateLimit-Limit'.")

    def _calculate_latest_delay(self, lv, now, e_time):
        """ Method to calculate delay based on last update.


        :param lv: Instance of 'LimitValues' to store values.
        :param now: Time when calling function started.
        :param e_time: Time elapsed since limit values last updated or since period was reset.
        :return : Return delay period value.
        """
        delay_period = 0

        # Alter self.min_time to take account of changes in limiting interval.
        lv.reset_period = lv.reset_period - e_time
        try:
            lv.min_time = lv.reset_period / lv.calls_remaining
        except ZeroDivisionError:
            LOG.error("Unexpected zero value detected for calls remaining '%s'.", lv.calls_remaining)
            raise ValueError("Unexpected zero value detected for calls remaining '{}'."
                             .format(lv.calls_remaining))

        if lv.request_count:
            # If other requests out-standing which have not yet updated limit information.
            left_to_wait = (lv.oldest_ts + (lv.request_count * lv.min_time)) - now
        else:
            # If no other requests out-standing.
            left_to_wait = (lv.lastest_ts + lv.min_time) - now
        if left_to_wait > 0:
            delay_period = left_to_wait

        return delay_period

    @staticmethod
    def add_ts(ts):
        """ Add time to list and update latest executed timestamp.

        :param ts: Timestamp Unix format.

        """
        with rl_lock:
            REQ_TIMESTAMPS.append(ts)
            LIMIT_INFO["lastest_request_ts"] = ts

    @staticmethod
    def get_limit_update_ts():
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
            if not self.get_limit_update_ts():
                delay_period = 0
            else:
                # Setup saved data for current execution.
                self._set_limit_data_from_saved(lv)
                # Set time elapsed since limit values last updated from a response.
                elapsed_time = now - lv.limit_update_ts
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

                delay_period = self._calculate_latest_delay(lv, now, elapsed_time)
            return delay_period