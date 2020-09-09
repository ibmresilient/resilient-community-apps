# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Function implementation"""

import logging
import re
import sys

class Filters():
    """
    this class handles the criteria for determining if an incident (and it's child objects) are synchronized
    """
    def __init__(self, match_list, match_operator_and):
        """
        save the filter criteria, if present
        :param match_list: list of tuples of (field, operator, value)
        :param filter_operator: any|all
        """
        # parsed settings to use
        self.match_list = match_list if match_list else {}
        self.match_operator_and = match_operator_and

        self.log = logging.getLogger(__name__)

        self.match_results = []

    def match_payload_value(self, field, value):
        """
        for a given payload value, determine if it matches the filter criteria.
        for all tests in a payload, maintain an array to know if the entire payload passes all criteria
        :param field:
        :param value:
        :return: true or false based on filter_and_operator: any or all
        """

        if not self.match_list:
            return True

        if field not in self.match_list:
            return True

        eval_result = self._test_field_value(field, value)

        self.log.debug("%s: %s->%s %s", field, value, eval_result, self.match_results)
        # maintain the running result for this incident
        self.match_results.append(eval_result)

        if self.match_operator_and:
            return all(self.match_results)

        return any(self.match_results)

    def _test_field_value(self, field, value):
        """
        Confirm if a field matches the filter criteria
        :param field:
        :param value:
        :return: true/false if matches. No criteria will return true
        """

        _, match_opr, match_value = self.match_list[field]
        try:
            eval_result = self._eval_field(value, match_opr, match_value)
        except (SyntaxError, TypeError) as err:
            self.log.error(err)
            eval_result = False

        return eval_result

    def _eval_field(self, payload_value, match_opr, match_value):
        """
        Return if a filter value matches the criteria specified
        :param payload_value:
        :param match_opr:
        :param match_value:
        :return: true/false
        """
        # test each value in the list. Only one needs to match
        if isinstance(payload_value, list):
            result_list = []
            for item in payload_value:
                result_list.append(self.do_eval(item, match_opr, match_value))

            return any(result_list)

        return self.do_eval(payload_value, match_opr, match_value)

    def do_eval(self, payload_value, match_opr, match_value):
        """
        perform the comparison using eval, such as 'plan_status == "C"'
        this function uses eval
        :param payload_value:
        :param match_opr:
        :param match_value:
        :return: true/false based on comparison
        """
        if is_string(payload_value):
            eval_str = u"'{}' {} {}".format(payload_value, match_opr, match_value)
        else:
            eval_str = u"{} {} {}".format(payload_value, match_opr, match_value)
        self.log.debug(eval_str)

        return eval(eval_str)

def is_string(value):
    """
    return true/false if a value is a string
    :param value:
    :return: true/false
    """
    if sys.version_info.major < 3:
        return isinstance(value, basestring)

    return isinstance(value, str)
