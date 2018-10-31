# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
from fn_machine_learning.lib.incident_filter import IncidentFilter

# 2018-10-14 17:07:45
CREATE_DATE = 1539536865000

def test_none_time_limit():
    """
    if not time_start and time_end given, it shall return True to keep
    :return:
    """
    filter = IncidentFilter()

    filter.time_start = None
    filter.time_end = None

    inc = {"create_date": 1539536865000}

    result = filter.shall_include_incident(inc)
    assert result


def test_time_start():
    """

    :return:
    """
    TIME_START1 = "2018-10-10"
    TIME_START2 = "2018-10-15"

    filter = IncidentFilter()
    filter.time_start = TIME_START1

    inc = {"create_date": 1539536865000}

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

    filter = IncidentFilter()
    filter.time_end = TIME_END_TOO_EARLY

    inc = {"create_date": 1539536865000}

    result = filter.shall_include_incident(inc)
    assert not result

    filter.time_end = TIME_END_INCLUDE

    result = filter.shall_include_incident(inc)
    assert result

