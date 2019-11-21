# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import calendar
import logging
import time
from datetime import datetime
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import RequestsCommon, ResultPayload, str_to_bool, validate_fields
from fn_ansible_tower.lib.common import SECTION_HDR, TOWER_API_BASE, get_common_request_items

JOBS_URL = "jobs/"
EVENTS_URL = "jobs/{id}/job_events/"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ansible_tower_list_jobs"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(SECTION_HDR, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(SECTION_HDR, {})

    @function("ansible_tower_list_jobs")
    def _ansible_tower_list_jobs_function(self, event, *args, **kwargs):
        """Function: None"""
        try:
            validate_fields(("url"), self.options) # validate key app.config settings

            # Get the function parameters:
            tower_job_status_list = self.get_select_param(kwargs.get("tower_job_status"))  # multi-select
            tower_last_updated = self.get_select_param(kwargs.get("tower_last_updated"))  # select

            log = logging.getLogger(__name__)
            log.info("tower_job_status: %s", tower_job_status_list)
            log.info("tower_last_updated: %s", tower_last_updated)

            last_update_epoch = None
            if tower_last_updated:
                last_update_epoch = convert_job_search_time(tower_last_updated)
                log.debug(last_update_epoch)

            result = ResultPayload(SECTION_HDR, **kwargs)
            rc = RequestsCommon(self.opts, self.options)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")
            job_results = []
            url = "/".join((self.options.get('url'), TOWER_API_BASE, JOBS_URL))
            # common
            basic_auth, cafile = get_common_request_items(self.options)

            while url:
                paged_results, next_url = get_paged_jobs(rc, url, basic_auth, cafile, tower_job_status_list,
                                                         last_update_epoch)
                if paged_results:
                    job_results.extend(paged_results)

                if next_url:
                    url = "/".join((self.options.get('url'), next_url)).replace("//api", "/api")
                else:
                    url = None

            result_payload = result.done(True, job_results)
            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(result_payload)
        except Exception:
            yield FunctionError()

def get_paged_jobs(rc, url, basic_auth, cafile, tower_job_status_list, last_update_epoch):
    """
    get jobs results, returning paged results as
    :param rc: RequestsCommon
    :param url:
    :param basic_auth:
    :param cafile:
    :param tower_job_status_list: list of pending, failed, successful
    :param last_update_epoch: optional date for review jobs to return
    :return: results, next url
    """
    tower_result = rc.execute_call_v2("get", url, proxies=rc.get_proxies(), auth=basic_auth,
                                      verify=cafile)

    json_results = tower_result.json()

    # for each job, get the job events
    job_list = []
    for job in json_results['results']:
        candidate = job
        if tower_job_status_list and job['status'] not in tower_job_status_list:
            candidate = None

        last_modified = convert_time_to_epoch(job['modified'])
        if last_update_epoch and last_modified < last_update_epoch:
            candidate = None

        if candidate:
            job_list.append(candidate)

    return job_list, json_results['next']


def convert_time_to_epoch(time_value):
    """
    convert string time reference to epoch
    :param time_value: 2019-11-11T21:51:07.426058Z
    :return: epoch value
    """
    return calendar.timegm(time.strptime(time_value, '%Y-%m-%dT%H:%M:%S.%fZ'))


def convert_job_search_time(search_time):
    """
    return value to search when jobs have been modified since
    :param search_time: '1 hours', '3 days', '1 week', etc.
    :return: epoch time to search for jobs which have been modified since
    """
    now = int(calendar.timegm(time.gmtime()))
    # read from the beginning looking for lines to capture based on timestamp
    delta = 0

    search_time_split = search_time.split(" ")
    if len(search_time_split) == 1:
        if search_time_split[0].strip().lower() == "today":
            # get midnight of this day
            dt = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            now = calendar.timegm(dt.timetuple())
        else:
            raise ValueError("Unrecognized time frame: %s", search_time_split[0])

    else:
        delta = int(search_time_split[0])
        if search_time_split[1].strip().lower() in ("minute", "minutes"):
            delta = delta*60 # convert minutes to seconds
        elif search_time_split[1].strip().lower() in ("hour", "hours"):
            delta = delta*60*60 # convert hours to seconds
        elif search_time_split[1].strip().lower() in ("day", "days"):
            delta = delta*60*60*24 # convert days to seconds
        elif search_time_split[1].strip().lower() in ("week", "weeks"):
            delta = delta*60*60*24*7 # convert weeks to seconds
        else:
            raise ValueError("Unrecognized time frame: %s", search_time_split[1])

    return now - delta
