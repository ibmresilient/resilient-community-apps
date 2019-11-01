# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import datetime
import logging
import os
import platform
import re
import time
import sys
from collections import deque
from io import BytesIO
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from resilient_lib.components.integration_errors import IntegrationError
from resilient_lib.components.resilient_common import write_file_attachment, validate_fields

PACKAGE_NAME = "fn_log_capture"
LOG_FILE = "app.log"
DATE_PATTERN = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
DEFAULT_ATTACHMENT_NAME = "{}_resilient-circuits_{}.log"

LOG_LEVELS = {
    "debug": ['debug', 'info', 'warning', 'error'],
    "info": ['info', 'warning', 'error'],
    "warning": ['warning', 'error'],
    "error": ['error']
}

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_log_capture"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self._init_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self._init_function(opts)

    def _init_function(self, opts):
        """
        setup information on the log directory to setup
        :param opts:
        :return:
        """
        log_dir = opts.get("resilient", {}).get("logdir")
        if not log_dir:
            raise IntegrationError("Log directory not found")

        self.log_file = os.path.join(log_dir, LOG_FILE)
        if not os.path.isfile(self.log_file):
            raise IntegrationError("Log file incorrect: {}".format(self.log_file))

    @function("fn_log_capture")
    def _fn_log_capture_function(self, event, *args, **kwargs):
        """Function: Get the resilient-circuits log, optionally specifying the last n lines"""
        try:
            # Get the function parameters:
            log_capture_maxlen = kwargs.get("log_capture_maxlen")  # number
            log_capture_date = kwargs.get("log_capture_date")  # datetimepicker (epoch)
            log_capture_date_option = self.get_select_param(kwargs.get("log_capture_date_option"))  # select
            log_min_level = self.get_select_param(kwargs.get("log_min_level")) # select
            incident_id = kwargs.get("incident_id") # number
            task_id = kwargs.get("task_id") # number
            log_attachment_name = kwargs.get("log_attachment_name")

            validate_fields(['incident_id'], kwargs)

            if not log_attachment_name:
                dt = datetime.datetime.now()
                fqdn = platform.node().split('.')

                log_attachment_name = DEFAULT_ATTACHMENT_NAME.format(fqdn[0], dt.strftime("%Y%m%d_%H%M%S"))

            log = logging.getLogger(__name__)
            log.info("log_capture_maxlen: %s", log_capture_maxlen)
            log.info("log_capture_date: %s", log_capture_date)
            log.info("log_capture_date_option: %s", log_capture_date_option)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info(u"log_attachment_name: %s", log_attachment_name)
            log.info("log_min_level: %s", log_min_level)

            result_payload = ResultPayload(PACKAGE_NAME, **kwargs)
            yield StatusMessage("starting...")

            if not log_capture_date and not log_capture_date_option:
                num_of_lines, captured_lines = get_log_by_filter(self.log_file, log_min_level, log_capture_maxlen)

            elif log_capture_date and log_capture_date_option:
                num_of_lines, captured_lines = get_log_by_date(self.log_file, log_capture_date, log_capture_date_option,
                                                               log_capture_maxlen, log_min_level)
            else:
                raise ValueError("Specify date with date option")

            # add as an attachment
            rest_client = self.rest_client()
            if sys.version_info.major < 3:
                datastream = BytesIO(captured_lines)
            else:
                datastream = BytesIO(captured_lines.encode("utf-8"))

            # failures will raise an exception
            write_file_attachment(rest_client, log_attachment_name, datastream,
                                                      incident_id, task_id)

            # Produce a FunctionResult with the results
            yield StatusMessage(u"attachment created '{}' with {} lines".format(log_attachment_name, num_of_lines))
            yield StatusMessage("done...")

            result_data = { "attachment_name": log_attachment_name, "num_of_lines": num_of_lines }
            results = result_payload.done(True, result_data)

            yield FunctionResult(results)
        except Exception:
            yield FunctionError()

def get_log_file_data(log_file):
    """
    get the resilient circuits log file
    :param log_file:
    :return: all lines for the log file
    """
    with open(log_file, "r") as f:
        return f.readlines()

def filter_log_level(filter_log_lvl, line, multi_line=False):
    """
    filter data by log level. If a multi-line log statement, it will be returned based on multi_ine argument
    :param filter_log_lvl: Debug, Info, Warning, Error
    :param line: log line
    :param multi_line: True = return line of data detail part of a previous log level
    :return: original line if match log level or None. pass_detail will override None
    """
    split_line = line.split(' ')
    if len(split_line) >= 3:
        line_level = split_line[2].lower()   # log level
        if line_level in LOG_LEVELS:
            if line_level in LOG_LEVELS[filter_log_lvl.lower()]:
                return line
        elif multi_line:
            return line
    elif multi_line:
        return line

    return None

def get_log_by_filter(log_file, log_min_level, log_capture_maxlen):
    """
    capture log lines only by filter level
    :param log_min_level: Debug, Info, Warning, Error
    :param log_capture_maxlen:
    :return: # of lines returned, concatenated log lines
    """
    captured_list = []
    result_line = None
    for line in get_log_file_data(log_file):
        result_line = filter_log_level(log_min_level, line, multi_line=result_line)
        if result_line:
            captured_list.append(result_line)

    d = deque(captured_list, maxlen=log_capture_maxlen)
    d_list = list(d)

    return len(d_list), "".join(d_list)

def get_log_by_date(log_file, log_capture_date, log_capture_date_option, log_capture_maxlen, log_min_level):
    """
    capture log files based on capture_date before or after fields
    :param log_file:
    :param log_capture_date epoch formatted field in milliseconds
    :param log_capture_date_option: 'before' or 'after'
    :param log_capture_maxlen: # of lines to capture at end of list
    :param log_min_level: DEBUG, INFO, WARNING, ERROR levels to filter DEBUG is all, INFO imcludes
       WARNING and ERROR, etc.
    :return: list of log fields to capture
    """
    log = logging.getLogger(__name__)

    # read from the beginning looking for lines to capture based on timestamp
    compare_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(log_capture_date/1000))
    log.debug("Looking for date: {}".format(compare_date))

    captured_list = []
    result_line = None
    triggered = False

    for line in get_log_file_data(log_file):
        startswith = line[0: len(compare_date)]
        if not triggered:

            if re.match(DATE_PATTERN, line):
                if log_capture_date_option == 'before' and \
                        startswith <= compare_date:
                    triggered = True
                elif startswith >= compare_date:
                    triggered = True

        if triggered:
            # don't capture after the compare_date
            if log_capture_date_option == 'before' and re.match(DATE_PATTERN, line):
                if startswith <= compare_date:
                    result_line = filter_log_level(log_min_level, line, multi_line=result_line)
                    if result_line:
                        captured_list.append(line)
                else:
                    break
            else:
                result_line = filter_log_level(log_min_level, line, multi_line=result_line)
                if result_line:
                    captured_list.append(line)

    # add maxlen
    if log_capture_maxlen:
        d = deque(captured_list, maxlen=log_capture_maxlen)
        d_list = list(d)
        captured_lines = "".join(d_list)

        num_of_lines = len(d_list)
    else:
        captured_lines = "".join(captured_list)
        num_of_lines = len(captured_list)

    return num_of_lines, captured_lines
