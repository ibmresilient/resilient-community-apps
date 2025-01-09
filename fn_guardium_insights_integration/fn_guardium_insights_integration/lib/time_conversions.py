# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
import time
from datetime import datetime, timedelta

import pytz
import six


def convert_utc_date_time_milli_seconds(date_time_str, format_str="%Y-%m-%dT%H:%M:%SZ"):
    """
    Convert UTC format dates to epoch milli seconds
    """
    if date_time_str is None:
        return None
    if isinstance(date_time_str, int):
        return date_time_str * 1000
    time_stamp_object = datetime.strptime(date_time_str, format_str)
    time_stamp_object_2 = pytz.timezone("UTC").localize(time_stamp_object)
    if six.PY2:
        epoch = pytz.timezone("UTC").localize(datetime(1970, 1, 1, 0, 0, 0))
        milli_sec = int((time_stamp_object_2 - epoch).total_seconds()) * 1000
    else:
        milli_sec = int(time_stamp_object_2.timestamp() * 1000)
    return milli_sec


def _convert_time_as_timezone(epoch_sec, timezone="UTC", format_str="%Y-%m-%dT%H:%M:%SZ"):
    """
    Convert given epoch sec to date time format as per timezone, default UTC
    """
    # 2021-03-01 10:00
    utc_dt = datetime.utcfromtimestamp(epoch_sec)
    utc_dt = pytz.UTC.localize(utc_dt)
    t_zone = pytz.timezone(timezone)
    cet_dt = utc_dt.astimezone(t_zone)
    return datetime.strftime(cet_dt, format_str)


def convert_epoch_utc_date_time(epoch_sec, format_str="%Y-%m-%dT%H:%M:%SZ"):
    utc_dt = datetime.utcfromtimestamp(epoch_sec)
    utc_dt = pytz.UTC.localize(utc_dt)
    return datetime.strftime(utc_dt, format_str)


def compute_query_times(poll_sec=0, delta_range=0):
    """
    By default this function given 1hrs difference between stop time and start time.
    stop time would be the current time, start time would be 4hrs past date.
    If poll seconds given then this would stretch default start time to given seconds in past.

    """
    _epoch_sec = int(time.time())
    _offset_sec = int(timedelta(hours=int(delta_range)).total_seconds()) + int(poll_sec)
    _start_epoch = _epoch_sec - _offset_sec
    stop_time = convert_epoch_utc_date_time(_epoch_sec)
    start_time = convert_epoch_utc_date_time(_start_epoch)
    return start_time, stop_time


def compute_start_stop_times(report_period):
    """
    By default this function generate the stop time and start time based on report_period.
    valid report_period values can be `Now minus 3 hours`,`Now minus 24 hours`, `Now minus 7 days`, `Now minus 14 days`
    """
    _epoch_sec = int(time.time())
    _offset_sec = 0
    if report_period == "Now minus 3 hours":
        _offset_sec = int(timedelta(hours=3).total_seconds())
    elif report_period == "Now minus 24 hours":
        _offset_sec = int(timedelta(hours=24).total_seconds())
    elif report_period == "Now minus 7 days":
        _offset_sec = int(timedelta(days=7).total_seconds())
    elif report_period == "Now minus 14 days":
        _offset_sec = int(timedelta(days=14).total_seconds())
    _start_epoch = _epoch_sec - _offset_sec
    stop_time = convert_epoch_utc_date_time(_epoch_sec)
    start_time = convert_epoch_utc_date_time(_start_epoch)
    return start_time, stop_time
