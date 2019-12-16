# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

import re
import threading
from datetime import datetime
from dateutil.relativedelta import *

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = SECONDS_IN_MINUTE*60
SECONDS_IN_DAY = SECONDS_IN_HOUR*24
SECONDS_IN_WEEK = SECONDS_IN_DAY*7

_scheduler_ = None

class ResilientScheduler:
    """
    This class builds a singleton instance of the scheduler.
    It also contains helper functions for building and managing scheduler jobs
    """

    def __init__(self, datastore_dir, threat_max, timezone):
        global _scheduler_

        self.timezone = timezone

        lock = threading.Lock()
        with lock:
            if not _scheduler_:
                jobstores = {
                    'default': SQLAlchemyJobStore(url='sqlite:///{}/scheduler.sqlite'.format(datastore_dir)),
                }
                executors = {
                    'default': ThreadPoolExecutor(threat_max),
                }
                job_defaults = {
                    'coalesce': False,
                    'max_instances': 1
                }
                _scheduler_ = BackgroundScheduler(
                    jobstores=jobstores, executors=executors,
                    job_defaults=job_defaults, timezone=timezone
                )
                _scheduler_.start()

    @staticmethod
    def get_scheduler():
        """
        return the instance of the scheduler
        :return:
        """
        return _scheduler_

    def build_trigger(self, type, value):
        """
        build a trigger for a schuduled job
        :param type: cron, interval, delta, date
        :param value: value to convert for a scheduled job
        :return: appropriate trigger
        """

        trigger = None
        if type == "cron":

            split_cron = value.split(" ")
            trigger = CronTrigger(minute=split_cron[0],
                                  hour=split_cron[1],
                                  day=split_cron[2],
                                  month=split_cron[3],
                                  day_of_week=split_cron[4])

        elif type == "interval":
            seconds = self.get_interval(value)
            trigger = IntervalTrigger(seconds=seconds)

        elif type == "date":
            trigger = DateTrigger(run_date=value, timezone=self.timezone)

        elif type == "delta":
            dt = self.get_interval(value, date=True)
            trigger = DateTrigger(run_date=dt, timezone=self.timezone)

        else:
            raise ValueError("Unrecognized type %s", type)

        return trigger

    @staticmethod
    def get_interval(time_string, date=False):
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

        now_dt = datetime.now()

        # Compute the total time to sleep in seconds
        if time_unit == 's':
            m_dt = now_dt + relativedelta(seconds=+time_value)
        elif time_unit == 'm':
            m_dt = now_dt + relativedelta(minutes=+time_value)
        elif time_unit == 'h':
            m_dt = now_dt + relativedelta(hours=+time_value)
        elif time_unit == 'd':
            m_dt = now_dt + relativedelta(days=+time_value)
        elif time_unit == 'w':
            m_dt = now_dt + relativedelta(weeks=+time_value)
        elif time_unit == 'M':
            m_dt = now_dt + relativedelta(months=+time_value)
        else:
            raise ValueError("Invalid interval format: should end in 's' = seconds, 'm = minutes, 'h' = hours, 'd' = days, 'w' = weeks, 'M' = Months")

        if date:
            return m_dt

        return int((m_dt - now_dt).total_seconds())

    @staticmethod
    def job_to_json(job):
        """
        rebuild type of scheduled job
        :param job:
        :return: json string with argument similar to use when job originally scheduled
        """
        result = {
            "id": job.id,
            "args": job.args,
            "next_run_time": ResilientScheduler.get_str_date(job.next_run_time)
        }

        if isinstance(job.trigger, IntervalTrigger):
            result['type'] = 'interval'
            value = None

            if int(job.trigger.interval_length % SECONDS_IN_WEEK) == 0:
                value = str(int(job.trigger.interval_length / SECONDS_IN_WEEK)) + "w"
            elif int(job.trigger.interval_length % SECONDS_IN_DAY) == 0:
                value = str(int(job.trigger.interval_length / SECONDS_IN_DAY)) + "d"
            elif int(job.trigger.interval_length % SECONDS_IN_HOUR) == 0:
                value = str(int(job.trigger.interval_length / SECONDS_IN_HOUR)) + "h"
            elif int(job.trigger.interval_length % SECONDS_IN_MINUTE) == 0:
                value = str(int(job.trigger.interval_length / SECONDS_IN_MINUTE)) + "m"
            else:
                value = str(job.trigger.interval_length) + "s"

            result['value'] = value

        elif isinstance(job.trigger, CronTrigger):
            result['type'] = 'cron'
            job_state = job.trigger.__getstate__()
            cron = ['*', '*', '*', '*', '*']
            for field in job_state['fields']:
                if field.name == "minute":
                    cron[0] = str(field)
                elif field.name == "hour":
                    cron[1] = str(field)
                elif field.name == "day":
                    cron[2] = str(field)
                elif field.name == "month":
                    cron[3] = str(field)
                elif field.name == "day_of_week":
                    cron[4] = str(field)
                #elif field.name == "year":
                #    cron[5] = str(field)

            result['value'] = ' '.join(cron)

        elif isinstance(job.trigger, DateTrigger):
            result['type'] = 'date'
            job_state = job.trigger.__getstate__()
            result['value'] = ResilientScheduler.get_str_date(job_state['run_date'])

        else:
            result['type'] = 'unknown'
            result['value'] = None

        return result

    @staticmethod
    def get_str_date(dt):
        """
        convert a python date into a string
        :param dt: datetime
        :return: str version as
        """
        format = '%b %d %Y %I:%M%p' # The format

        return dt.strftime(format) if dt else None

    @staticmethod
    def sanitize_job(job):
        """
        convert job to json for presentation, removing sensitive data
        :return: json formatted job
        """
        job_json = ResilientScheduler.job_to_json(job)

        return ResilientScheduler.clean_password(job_json)

    @staticmethod
    def clean_password(job_json):
        """
        remove arguments which contain passwords
        :param job_json:
        :return: cleaned up job_json
        """

        params = list(job_json['args'])

        # hide settings which contain passwords
        params[8] = None
        job_json['args'] = tuple(params)

        return job_json