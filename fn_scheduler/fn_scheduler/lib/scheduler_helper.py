# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

import re
import threading
from datetime import datetime, timedelta

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
        return _scheduler_

    """
    def the_job(oid):
        print('Run job: object.id={}, datetime={}'.format(oid, datetime.now()))
    
    
    def main():
        sqlite_file = 'apscheduler-jobs.sqlite'
        os.system('rm -f {}'.format(sqlite_file))
        jobstores = {
            'default': SQLAlchemyJobStore(url='sqlite:///{}'.format(sqlite_file)),
        }
        executors = {
            'default': ThreadPoolExecutor(20),
        }
        job_defaults = {
            'coalesce': False,
            'max_instances': 1
        }
        scheduler = BackgroundScheduler(
            jobstores=jobstores, executors=executors,
            job_defaults=job_defaults, timezone=utc
        )
        scheduler.start()
    
        def add_job(oid):
            trigger = DateTrigger(
                run_date=datetime.now() + timedelta(seconds=oid),
                timezone=timezone('Asia/Shanghai')
            )
            # scheduler.add_job(myfunc, 'interval', minutes=2, id='my_job_id')
            scheduler.add_job(the_job, args=[oid],
                              trigger=trigger,
                              id='task-{}'.format(oid),
                              name='Task({})'.format(oid),
                              coalesce=True, max_instances=1)
        add_job(3)
        add_job(6)
        add_job(9)
        try:
            print('Press <Ctrl + C> to stop! datetime={}'.format(datetime.now()))
            time.sleep(1000000000)
        except KeyboardInterrupt:
            print('Stopping...')
            scheduler.shutdown()
    """

    def build_trigger(self, type, value):
        """

        :param type:
        :param value:
        :return:
        """

        validate_crontab_time_format_regex = re.compile( \
            "{0}\s+{1}\s+{2}\s+{3}\s+{4}".format( \
                "(?P<minute>\*|[0-5]?\d)", \
                "(?P<hour>\*|[01]?\d|2[0-3])", \
                "(?P<day>\*|0?[1-9]|[12]\d|3[01])", \
                "(?P<month>\*|0?[1-9]|1[012])", \
                "(?P<day_of_week>\*|[0-6](\-[0-6])?)" \
                ) # end of str.format()
        )

        trigger = None
        if type == "cron":
            if not validate_crontab_time_format_regex.match(value):
                raise ValueError("Invalid cron entry: %s", value)

            split_cron = value.split(" ")
            trigger = CronTrigger(minute=split_cron[0],
                                  hour=split_cron[1],
                                  day=split_cron[2],
                                  month=split_cron[3],
                                  day_of_week=split_cron[4])

        elif type == "interval":
            seconds = self.get_sleep_time_in_seconds(value)
            trigger = IntervalTrigger(seconds=seconds)

        elif type == "date":
            trigger = DateTrigger(run_date=value, timezone=self.timezone)

        elif type == "delta":
            seconds = self.get_sleep_time_in_seconds(value)
            delta_dt = datetime.now() + timedelta(seconds=seconds)

            trigger = DateTrigger(run_date=delta_dt, timezone=self.timezone)

        else:
            ValueError("Unrecognized type %s", type)

        return trigger

    def get_sleep_time_in_seconds(self, time_string):
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
            raise ValueError("Invalid interval format: time value should be integer. For example: 5s, 10m, 1d, 2w")

        # Get the time units from input string.
        time_unit = time_string.rstrip()[-1].lower()

        # Compute the total time to sleep in seconds
        if time_unit == 's':
            time_in_seconds = time_value
        elif time_unit == 'm':
            time_in_seconds = time_value * SECONDS_IN_MINUTE
        elif time_unit == 'h':
            time_in_seconds = time_value * SECONDS_IN_HOUR
        elif time_unit == 'd':
            time_in_seconds = time_value * SECONDS_IN_DAY
        elif time_unit == 'w':
            time_in_seconds = time_value * SECONDS_IN_WEEK
        else:
            raise ValueError("Invalid interval format: should end in 's' = seconds, 'm = minutes, 'h' = hours, 'd' = days, 'w' = weeks")

        return time_in_seconds

    def job_to_json(self, job):
        result = {
            "id": job.id,
            "args": job.args
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
            result['value'] = self.get_str_date(job_state['run_date'])

        else:
            result['type'] = 'unknown'
            result['value'] = None

        return result

    def get_str_date(self, dt):
        """
        convert a python date into a string
        :param dt: datetime
        :return: str version as
        """
        format = '%b %d %Y %I:%M%p' # The format

        return dt.strftime(format) if dt else None