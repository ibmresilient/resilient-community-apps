# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Function implementation"""

import logging
import re
import sys
from resilient_lib import IntegrationError, str_to_bool

# <field> <operator> <value>. ex: org_id = 201
REGEX_OPERATORS = re.compile(r"([a-zA-Z0-9_]+)\s*(!=|=<|>=|=>|>=|<|>|==|=|is not|is|not in|in)\s*(.+)")
REGEX_FIND_ST = re.compile(r"['\"]+(.*)['\"]+")

class Filters:
    """
    this class handles the criteria for determining if an incident (and it's child objects) are synchronized
    """
    def __init__(self, filters, filter_operator):
        """
        build the filter criteria, if present
        :param filters:
        :param filter_operator: any|all
        """
        self.filter_and_operator = (filter_operator.strip().lower() == 'all') if filter_operator else None
        self.log = logging.getLogger(__name__)
        # retain all fields we test
        self.filter_results = []

        # parse the filters and produce a tuble of (field, operator, value)
        self.filter_list = {}
        if filters:
            for filter in filters.split(';'):
                m = REGEX_OPERATORS.match(filter.strip())
                if not m:
                    raise IntegrationError("Unable to parse filter '{}'".format(filter))
                else:
                    filter_value = m.group(3)

                    # determine if working with a string, boolean, or int
                    if filter_value in ["true", "True", "false", "False"]:
                        filter_value = str_to_bool(filter_value)
                    elif filter_value == 'None':
                        filter_value = None
                    else:
                        try:
                            filter_value = int(filter_value) # this will fail for numbers, which will be trapped
                        except:
                            pass

                    compare_tuple = (m.group(1), m.group(2), filter_value)
                    self.log.debug(compare_tuple)
                    self.filter_list[m.group(1)] = compare_tuple

    def filter_payload_value(self, field, value):
        """
        for a given payload value, determine if it matches the filter criteria.
        :param field:
        :param value:
        :return: true or false based on filter_and_operator: any or all
        """

        # TODO shortcircuit once 'any' returns true?

        eval_result = self._test_field_value(field, value)
        # maintain the running result for this incident
        self.filter_results.append(eval_result)

        if self.filter_and_operator:
            return all(self.filter_results)
        else:
            return any(self.filter_results)

    def _test_field_value(self, field, value):
        """
        Confirm if a field matches the filter criteria.
        :param field:
        :param value:
        :return: true/false if matches. No criteria will return true
        """
        if not self.filter_list:
            return True

        if field not in self.filter_list:
            return True

        filter_field, filter_opr, filter_value = self.filter_list[field]
        try:
            eval_result = self._eval_field(value, filter_opr, filter_value)
        except (SyntaxError, TypeError) as err:
            self.log.error(err)
            eval_result = False

        return eval_result

    def _eval_field(self, payload_value, filter_opr, filter_value):
        """
        Return if a filter value matches the criteria specified
        :param payload_value:
        :param filter_opr:
        :param filter_value:
        :return: true/false
        """
        # correct mistyped comparison
        if filter_opr.strip() == '=':
            filter_opr = '=='

        # test each value of the list. Only one needs to match
        if isinstance(payload_value, list):
            result_list = []
            for item in payload_value:
                result_list.append(self.do_eval(item, filter_opr, filter_value))

            return any(result_list)
        else:
            return self.do_eval(payload_value, filter_opr, filter_value)

    def do_eval(self, payload_value, filter_opr, filter_value):
        if is_string(payload_value):
            eval_str = u"'{}' {} {}".format(payload_value, filter_opr, filter_value)
        else:
            eval_str = u"{} {} {}".format(payload_value, filter_opr, filter_value)
        self.log.debug(eval_str)

        return eval(eval_str)

def is_string(value):
    """
    return if a value is a string
    :param value:
    :return: true/false
    """
    if sys.version_info.major < 3:
        return isinstance(value, basestring)
    else:
        return isinstance(value, str)
