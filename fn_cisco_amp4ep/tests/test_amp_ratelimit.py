# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Test Bigfix client  class"""
from __future__ import print_function
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
import pytest
from fn_cisco_amp4ep.lib.amp_ratelimit import *
from  mock_artifacts import mocked_session

"""
Suite of tests to test Cisco AmpRateLimit class
"""


class TestAMPRatelimit:
    """ Test rate_limiter.  """

    """ Setup """
    def setup(self):
        # Initalize test env
        self.rate_limiter = AmpRateLimit() # Set defaults
        self.rate_limiter._set_defaults()
        while self.rate_limiter._pop_request_ts(): # Zero out requests
            pass

    """ Test AmpRateLimit defaults """
    def test_defaults(self):
        default_info = {
            "X-RateLimit-Limit": 0.0,
            "X-RateLimit-Remaining": 0.0,
            "X-RateLimit-Reset": 0.0,
            "X-RateLimit-ResetDate": 0.0,
        }
        response = self.rate_limiter.get_limit_update_ts()
        assert response == 0.0
        assert self.rate_limiter.get_limit_update_ts() == LIMIT_INFO["limit_update_ts"]
        for k, v in default_info.items():
            assert default_info[k] == LIMIT_INFO[k]

    """ Test AmpRateLimit._save_limits """

    def test_save_limits(self):
        limit_info = {
            "X-RateLimit-Limit": 3000,
            "X-RateLimit-Remaining": 2500,
            "X-RateLimit-Reset": 2000,
            "X-RateLimit-ResetDate": 0.0,
        }
        now = time.time()
        self.rate_limiter.save_limits(limit_info)
        response = self.rate_limiter.get_limit_update_ts()
        assert now < response
        assert self.rate_limiter.get_limit_update_ts() == LIMIT_INFO["limit_update_ts"]
        for k, v in limit_info.items():
            assert v == LIMIT_INFO[k]

    """ Test AmpRateLimit.get_delay default """

    def test_get_delay_default(self):
        response = self.rate_limiter.get_delay()
        assert 0 == response

    """ Test AmpRateLimit.get_delay with save_limits values """
    def test_get_delay(self):
        limit_info = {
            "X-RateLimit-Limit": 3000,
            "X-RateLimit-Remaining": 2500,
            "X-RateLimit-Reset": 2000,
            "X-RateLimit-ResetDate": 0.0,
        }
        self.rate_limiter.save_limits(limit_info)
        response = self.rate_limiter.get_delay()
        assert 0 == response

    """ Test AmpRateLimit.get_delay with save_limits and timestamp """

    def test_get_delay_with_new_ts(self):
        limit_info_1 = {
            "X-RateLimit-Limit": 3000,
            "X-RateLimit-Remaining": 2500,
            "X-RateLimit-Reset": 2000,
            "X-RateLimit-ResetDate": 0.0,
        }
        self.rate_limiter.add_ts(time.time())
        self.rate_limiter.save_limits(limit_info_1)
        response = self.rate_limiter.get_delay()
        assert 1.19 < response
        assert 1.2 > response

    """ Test AmpRateLimit.get_delay now in future with save_limits, delay and add timestamp """
    def test_get_delay_with_delay_and_new_ts(self):
        limit_info_1 = {
            "X-RateLimit-Limit": 3000,
            "X-RateLimit-Remaining": 2500,
            "X-RateLimit-Reset": 2000,
            "X-RateLimit-ResetDate": 0.0,
        }
        now = time.time() + 1.2
        self.rate_limiter.add_ts(now)
        self.rate_limiter.save_limits(limit_info_1)
        self.rate_limiter._set_limit_update_ts(now)
        response = self.rate_limiter.get_delay()
        test=1
        assert 2.39 < response
        assert 2.4 > response

    """ Test AmpRateLimit.get_delay with save_limits and 4 X timestamp """
    def test_get_delay_new_ts_X4(self):
        limit_info_1 = {
            "X-RateLimit-Limit": 3000,
            "X-RateLimit-Remaining": 2500,
            "X-RateLimit-Reset": 2000,
            "X-RateLimit-ResetDate": 0.0,
        }
        now = time.time()
        self.rate_limiter.add_ts(now)
        self.rate_limiter.save_limits(limit_info_1)
        self.rate_limiter.add_ts(now)
        self.rate_limiter.add_ts(now)
        self.rate_limiter.add_ts(now)
        response = self.rate_limiter.get_delay()
        assert 3.59 < response
        assert 3.6 > response

    """ Test AmpRateLimit.get_delay with now in future, save_limits and 4 X timestamp """
    def test_get_delay_with_delay_and_new_ts_X4(self):

        limit_info_1 = {
            "X-RateLimit-Limit": 3000,
            "X-RateLimit-Remaining": 2500,
            "X-RateLimit-Reset": 2000,
            "X-RateLimit-ResetDate": 0.0,
        }
        now = time.time() + 1.2
        self.rate_limiter.add_ts(now)
        self.rate_limiter.save_limits(limit_info_1)
        self.rate_limiter.add_ts(now)
        self.rate_limiter.add_ts(now)
        self.rate_limiter.add_ts(now)
        response = self.rate_limiter.get_delay()
        assert 4.79 < response
        assert 4.8 > response

    """ Test AmpRateLimit.get_delay with zero remaining requests in time remaining"""
    def test_get_delay_zero_remaining(self):
        REQ_TIMESTAMPS = []
        limit_info_1 = {
            "X-RateLimit-Limit": 3000,
            "X-RateLimit-Remaining": 0,
            "X-RateLimit-Reset": 180,
            "X-RateLimit-ResetDate": 0.0,
        }
        now = time.time()
        self.rate_limiter.add_ts(now)
        self.rate_limiter.save_limits(limit_info_1)
        self.rate_limiter._set_limit_update_ts(now)
        response = self.rate_limiter.get_delay()
        assert 179.99 < response
        assert 180 > response

    """ Test AmpRateLimit.save_limits test missing response header"""

    @pytest.mark.parametrize("expected_results", [
                                 ("Not all required rate limit headers returned from request response.")
                             ])
    def test_missing_header(self,expected_results):
        REQ_TIMESTAMPS = []
        limit_info_1 = {
            "X-RateLimit-Limit": 3000,
            "X-RateLimit-Remaining": 2500,
            "X-RateLimit-Reset": 2000,
        }
        with pytest.raises(ValueError) as e:
            self.rate_limiter.save_limits(limit_info_1)
        assert str(e.value) == expected_results

    """ Test AmpRateLimit.save_limits test missing response header"""

    @pytest.mark.parametrize("expected_results", [
                                 ("Zero value detected for rate limit parameter 'X-RateLimit-Limit'.")
                             ])
    def test_limit_zero(self,expected_results):
        REQ_TIMESTAMPS = []
        limit_info_1 = {
            "X-RateLimit-Limit": 0.0,
            "X-RateLimit-Remaining": 2500,
            "X-RateLimit-Reset": 2000,
            "X-RateLimit-ResetDate": 0.
        }
        self.rate_limiter.save_limits(limit_info_1)
        with pytest.raises(ValueError) as e:
            response = self.rate_limiter.get_delay()
        assert str(e.value) == expected_results

