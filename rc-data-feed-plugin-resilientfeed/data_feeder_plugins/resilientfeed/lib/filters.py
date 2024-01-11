# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Function implementation"""

import copy
import logging
import json
import re
import sys
from resilient_lib import str_to_bool

# <field> <operator> <value>. ex: org_id = 201
REGEX_OPERATORS = re.compile(r"([a-zA-Z0-9_]+)\s*(~|!=|=<|>=|=>|>=|<|>|==|=|is not| is |not in| in )\s*(.+)")

LOG = logging.getLogger(__name__)

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

    def match_payload_value(self, field, payload_value):
        """
        for a given payload value, determine if it matches the filter criteria.
        for all tests in a payload, maintain an array to know if the entire payload passes all criteria
        :param field:
        :param payload_value:
        :return: true or false based on filter_and_operator: any or all
        """

        if not self.match_list:
            return True

        if field not in self.match_list:
            return True

        eval_result = self._test_field_value(field, payload_value)

        self.log.debug(u"%s: %s->%s %s", field, payload_value, eval_result, self.match_results)
        # maintain the running result for this incident
        self.match_results.append(eval_result)

        if self.match_operator_and:
            return all(self.match_results)

        return any(self.match_results)

    def _test_field_value(self, field, payload_value):
        """
        Confirm if a field matches the filter criteria
        :param field:
        :param payload_value:
        :return: true/false if matches. No criteria will return true
        """

        _, match_opr, match_value = self.match_list[field]
        _match_opr = copy.copy(match_opr)
        if _match_opr == "~":
            _match_opr = "in"
            # flip the match_value and payload_value
            _match_value = match_value
            match_value = payload_value
            payload_value = _match_value

        try:
            if isinstance(payload_value, list):
                # test each payload_value as OR logic
                eval_result = False
                for item in payload_value:
                    item_result = self._eval_field(match_value, _match_opr, item)
                    eval_result = eval_result | item_result
            else:
                eval_result = self._eval_field(match_value, _match_opr, payload_value)
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

        _payload_value = copy.copy(payload_value)
        if is_string(_payload_value):
            _payload_value = "'''{}'''".format(_payload_value)

        _match_value = copy.copy(match_value)
        if is_string(_match_value):
            _match_value = "'''{}'''".format(_match_value)

        eval_str = u"{} {} {}".format(_match_value, match_opr, _payload_value)
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

def parse_matching_criteria(filters, filter_operator):
    """
    build the filter criteria, if present
    :param filters:field opr value[;]...
    :param filter_operator: any|all
    :return dictionary of parsed filter settings, True/False for "all"/"any" setting
    """
    LOG.debug("%s %s", filters, filter_operator)

    if filter_operator and filter_operator.strip().lower() not in ('all', 'any'):
        raise ValueError("operator must be 'all' or 'any': {}".format(filter_operator))

    match_operator_and = (filter_operator.strip().lower() == 'all') if filter_operator else True

    # parse the filters and produce a tuple of (field, operator, value)
    match_list = {}
    if filters:
        for filter_str in filters.split(';'):
            m = REGEX_OPERATORS.match(filter_str.strip())
            if not m or len(m.groups()) != 3:
                raise ValueError("Unable to parse filter '{}'".format(filter_str))

            match_field = m.group(1)
            match_opr = m.group(2)
            # correct mistyped comparison
            if match_opr.strip() == '=':
                match_opr = '=='

            match_value = m.group(3)

            # restore lists to actual lists
            if match_value.startswith("["):
                try:
                    match_value = json.loads(match_value.replace("'", '"'))  # make sure correct json format
                except Exception as err:
                    LOG.error(str(err))
                    pass
            # determine if working with a string, boolean, or int
            elif match_value in ["true", "True", "false", "False"]:
                match_value = str_to_bool(match_value)
            elif match_value == 'None':
                match_value = None
            else:
                try:
                    match_value = int(match_value) # this will fail for numbers, which will be trapped
                except:
                    pass

            compare_tuple = (match_field, match_opr, match_value)
            LOG.debug(compare_tuple)
            match_list[match_field] = compare_tuple

    return match_list, match_operator_and

class MatchError(Exception):
    """
    Class used to signal Filter Error. It doesn't add any specific information other than
    identifying the type of error
    """
    def __init__(self, message):
        super(MatchError, self).__init__(message)
        self.message = message

    def __str__(self):
        return repr(self.message)
