# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
import functools
from datetime import datetime
from logging import getLogger
from threading import Event
from traceback import format_exc
from resilient import SimpleHTTPException

LOG = getLogger(__name__)

# P O L L E R   L O G I C
def poller(named_poller_interval, named_last_poller_time, package_name):
    """
    Decorator for poller, manage poller time, calling the customized method for getting the next entities
    :param named_poller_interval: (str) Name of instance variable containing the poller interval in seconds
    :param named_last_poller_time: (datetime) Name of instance variable containing the lookback value in mseconds
    :param package_name: (str) Name of package for loggging
    """
    def poller_wrapper(func):
        # Decorator for running a function forever, passing the ms timestamp of
        # when the last poller run to the function it's calling
        @functools.wraps(func)
        def wrapped(self):
            last_poller_time = getattr(self, named_last_poller_time)
            exit_event = Event()

            while not exit_event.is_set():
                try:
                    LOG.info(f"{package_name} polling start.")
                    poller_start = datetime.now()
                    # Function execution with the last poller time in ms
                    func(self, last_poller_time = int(last_poller_time.timestamp()*1000))

                except Exception as err:
                    LOG.error(str(err))
                    LOG.error(format_exc())
                finally:
                    LOG.info(f"{package_name} polling complete.")
                    # Set the last poller time for next cycle
                    last_poller_time = poller_start

                    # Sleep before the next poller execution
                    exit_event.wait(getattr(self, named_poller_interval))
            exit_event.set() # Loop complete

        return wrapped
    return poller_wrapper