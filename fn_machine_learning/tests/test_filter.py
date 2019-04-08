# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
from fn_machine_learning.lib.incident_time_filter import IncidentTimeFilter

# 2018-10-14 17:07:45
CREATE_DATE = 1539536865000


def test_none_time_limit():
    """
    if not time_start and time_end given, it shall return True to keep
    :return:
    """
    filter = IncidentTimeFilter(time_start=None,
                                time_end=None)

    inc = {"create_date": CREATE_DATE}

    result = filter.shall_include_incident(inc)
    assert result


def test_time_start():
    """

    :return:
    """
    TIME_START1 = "2018-10-10"
    TIME_START2 = "2018-10-15"

    filter = IncidentTimeFilter(time_start=TIME_START1)

    inc = {"create_date": CREATE_DATE}

    result = filter.shall_include_incident(inc)
    assert result

    filter.time_start = TIME_START2
    result = filter.shall_include_incident(inc)

    assert not result


def test_time_end():
    """

    :return:
    """
    TIME_END_TOO_EARLY = "2018-10-12"
    TIME_END_INCLUDE = "2018-10-15"

    filter = IncidentTimeFilter()
    filter.time_end = TIME_END_TOO_EARLY

    inc = {"create_date": CREATE_DATE}

    result = filter.shall_include_incident(inc)
    assert not result

    filter.time_end = TIME_END_INCLUDE

    result = filter.shall_include_incident(inc)
    assert result


def test_wrong_time_field():

    TIME_START2 = "2018-10-15"
    WRONG_TIME_FIELD = "no_field"
    filter = IncidentTimeFilter(time_start=TIME_START2,
                                time_field=WRONG_TIME_FIELD)

    inc = {"create_date": CREATE_DATE}

    result = filter.shall_include_incident(inc)
    #
    #   Because the time field is wrong, we will always include.
    #
    assert result


def test_wrong_time_format():
    WRONG_TIME_FORMAT="10-15-2018"
    filter = IncidentTimeFilter(time_start=WRONG_TIME_FORMAT)
    inc = {"create_date": CREATE_DATE}

    result = filter.shall_include_incident(inc)
    #
    #   Because the time field is wrong, we will always include.
    #
    assert result

    filter.time_start = None
    filter.time_end = WRONG_TIME_FORMAT

    result = filter.shall_include_incident(inc)
    #
    #   Because the time field is wrong, we will always include.
    #
    assert result
