# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

import re
import calendar

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = SECONDS_IN_MINUTE*60
SECONDS_IN_DAY = SECONDS_IN_HOUR*24
SECONDS_IN_WEEK = SECONDS_IN_DAY*7

def get_interval(time_string):
    """
    Parse the input time string into "time value" and "time unit" and compute the time in seconds.
    The input string will be in format time_value with the time unit character concatenated on the end.
    Time unit will be: 's' for seconds, 'm' for minutes, 'h' for hours or 'd' for days.
    For example '30s' = 30 seconds; '20m' = 20 minutes; '2h' = 2 hours; '5d' = 5 days.
    """
    # Parse time string time value which should be integer.
    try:
        time_value = int(time_string[:-1])
    except:
        raise ValueError("Invalid interval format: time value should be integer. For example: 5s, 10m, 1d, 2w, 1M")

    if time_value <= 0:
        raise ValueError("time value needs to be > 0: {}".format(time_value))

    # Get the time units from input string.
    time_unit = time_string.rstrip()[-1]
    in_seconds = 0

    # Compute the total time to sleep in seconds
    if time_unit == 's':
        in_seconds = time_value
    elif time_unit == 'm':
        in_seconds = time_value*SECONDS_IN_MINUTE
    elif time_unit == 'h':
        in_seconds = time_value*SECONDS_IN_HOUR
    elif time_unit == 'd':
        in_seconds = time_value*SECONDS_IN_DAY
    elif time_unit == 'w':
        in_seconds = time_value*SECONDS_IN_WEEK
    else:
        raise ValueError("Invalid interval format: should end in 's' = seconds, 'm = minutes, 'h' = hours, 'd' = days, 'w' = weeks, 'M' = Months")

    return in_seconds

def clean_phone_number(phone_number):
    """
    remove all characters other can numbers and dashes
    :param phone_number:
    :return: cleaned number
    """
    return '+' + re.sub("[^0-9]", "", phone_number)

def get_ts_from_datetime(dt):
    """
    return an epoch value of a datefield, in milliseconds
    :param dt:
    :return: epoch in milliseconds
    """
    return calendar.timegm(dt.timetuple())*1000
