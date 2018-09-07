# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation"""

import logging
import requests
import time
from datetime import datetime
from threading import current_thread
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_mcafee_esm.util.helper import check_config, get_authenticated_headers, check_status_code


log = logging.getLogger(__name__)


def alarm_get_triggered_alarms(options, params):
    url = options["esm_url"] + "/rs/esm/v2/alarmGetTriggeredAlarms"

    headers = get_authenticated_headers(options["esm_url"], options["esm_username"],
                                        options["esm_password"], options["trust_cert"])

    r = requests.post(url, headers=headers, params=params, verify=options["trust_cert"])
    check_status_code(r.status_code)

    return r.json()


def create_parameters(**kwargs):
    params_dict = dict()
    if "start" in kwargs and "end" in kwargs:
        params_dict["customStart"] = kwargs.get("start")
        params_dict["customEnd"] = kwargs.get("end")
        params_dict["triggeredTimeRange"] = "CUSTOM"
    else:
        params_dict["triggeredTimeRange"] = kwargs.get("time_range")

    return params_dict


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_esm_get_list_of_cases"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_mcafee_esm", {})

        # Check config file and change trust_cert to Boolean
        self.options = check_config(self.options)
#        alarm_get_triggered_alarms(self.options, {"triggeredTimeRange": "CURRENT_DAY"})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_mcafee_esm", {})

    @function("mcafee_esm_get_triggered_alarms")
    def _mcafee_esm_get_triggered_alarms_function(self, event, *args, **kwargs):
        """Function: """
        try:
            start_time = time.time()

            yield StatusMessage("starting...")
            options = self.options

            # Get inputs
            mcafee_esm_alarm_triggered_time_range = self.get_select_param(
                kwargs.get("mcafee_esm_alarm_triggered_time_range", "CURRENT_DAY"))  # select
            mcafee_esm_alarm_triggered_start_time = kwargs.get("mcafee_esm_alarm_triggered_start_time")  # text
            mcafee_esm_alarm_triggered_end_time = kwargs.get("mcafee_esm_alarm_triggered_end_time")  # text

            # Log inputs
            if mcafee_esm_alarm_triggered_time_range:
                log.info("mcafee_esm_alarm_triggered_time_range: %s", mcafee_esm_alarm_triggered_time_range)
            if mcafee_esm_alarm_triggered_start_time:
                log.info("mcafee_esm_alarm_triggered_start_time: %s", mcafee_esm_alarm_triggered_start_time)
            if mcafee_esm_alarm_triggered_end_time:
                log.info("mcafee_esm_alarm_triggered_end_time: %s", mcafee_esm_alarm_triggered_end_time)

            # Call alarmGetTriggeredAlarms
            params = create_parameters(time_range=mcafee_esm_alarm_triggered_time_range,
                                       start=mcafee_esm_alarm_triggered_start_time,
                                       end=mcafee_esm_alarm_triggered_end_time)
            alarm_list = alarm_get_triggered_alarms(options, params)
            if len(alarm_list) == 0:
                yield StatusMessage("No alarms returned")
            else:
                yield StatusMessage("Triggered alarm list returned")

            end_time = time.time()
            results = {
                "inputs": {
                    "mcafee_esm_alarm_triggered_time_range": mcafee_esm_alarm_triggered_time_range,
                    "mcafee_esm_alarm_triggered_start_time": mcafee_esm_alarm_triggered_start_time,
                    "macfee_esm_alarm_triggered_end_time": mcafee_esm_alarm_triggered_end_time
                },
                "metrics": {
                    "execution_time": str(end_time - start_time),
                    "function": "mcafee_esm_get_triggered_alarms",
                    "thread": current_thread().name,
                    "timestamp": datetime.fromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")
                },
                "alarm_list": alarm_list
            }
            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
