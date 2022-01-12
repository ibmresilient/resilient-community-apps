# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""Function implementation"""

import datetime
import functools
import logging
import pytz
from threading import Thread, Event
import traceback
from resilient_circuits import ResilientComponent
from resilient_lib import validate_fields, RequestsCommon
from resilient import get_client
from fn_siemplify.lib.jinja_common import JinjaEnvironment
from fn_siemplify.lib.resilient_common import ResilientCommon
from fn_siemplify.lib.siemplify_common import SiemplifyCommon, PACKAGE_NAME

TICKET_ID_FIELDNAME = "simplify_case_id"

DEFAULT_SOAR_CLOSE_CASE = "templates/soar_close_case.jinja"
DEFAULT_SOAR_UPDATE_CASE = "templates/soar_update_case.jinja"

GMT = "Etc/GMT"

DEFAULT_POLLER_SECONDS = 600
LOG = logging.getLogger(__name__)

def poller(named_poller_interval, named_last_poller_time):
    """[summary]

    Args:
        named_poller_interval ([str]): [name of instance variable containing the poller interval in seconds]
        named_last_poller_time ([datetime]): [name of instance variable containing the lookback value in mseconds]
    """
    def poller(func):
        # decorator for running a function forever, passing the ms timestamp of
        #  when the last poller run to the function it's calling
        @functools.wraps(func)
        def wrapped(self):
            last_poller_time = getattr(self, named_last_poller_time)
            exit_event = Event()

            while not exit_event.is_set():
                try:
                    LOG.info(u"%s polling start.", PACKAGE_NAME)
                    poller_start = datetime.datetime.now()
                    # function execution with the last poller time in ms
                    func(self, last_poller_time=int(last_poller_time.timestamp()*1000))

                except Exception as err:
                    LOG.error(str(err))
                    LOG.error(traceback.format_exc())
                finally:
                    LOG.info(u"%s polling complete.", PACKAGE_NAME)
                    # set the last poller time for next cycle
                    last_poller_time = poller_start

                    # sleep before the next poller execution
                    exit_event.wait(getattr(self, named_poller_interval))
            exit_event.set() # loop complete

        return wrapped
    return poller

class SiemplifyPollerComponent(ResilientComponent):
    """
    poller for Siemplify Incidents
    """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(SiemplifyPollerComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

        # Validate required fields in app.config are set
        validate_fields(["api_key", "base_url"], self.options)

        if not self._init_env(opts, self.options):
            LOG.info(u"Siemplify poller interval is not configured.  Automated escalation is disabled.")
            return

        poller_thread = Thread(target=self.run)
        poller_thread.daemon = True
        poller_thread.start()

    def _init_env(self, opts, options):
        """[initialize the environment based on app.config settings]

        Args:
            opts ([dict]): [all settings include SOAR settings]
            options ([dict]): [settings specific to Siemplify]

        Returns:
            [bool]: [True if poller is configured]
        """
        self.polling_interval = int(options.get("polling_interval", 0))
        if not self.polling_interval:
            return False

        LOG.info(u"Siemplify poller initiated, polling interval %s", self.polling_interval)
        self.timezone = pytz.timezone(options.get("polling_timezone", GMT))
        self.last_poller_time = self._get_last_poller_date(int(options.get('polling_lookback', 0)))

        rest_client = get_client(opts)
        self.res_common = ResilientCommon(rest_client)

        # Create api client
        rc = RequestsCommon(opts, options)
        self.siemplify_env = SiemplifyCommon(rc, options)

        self.jinja_env = JinjaEnvironment()

        return True

    @poller('polling_interval', 'last_poller_time')
    def run(self, last_poller_time=None):
        """[Process to query for changes in Siemplify incidents and the cooresponding update SOAR incident]
           The steps taken are to
           1) query SOAR for all open incidents associated with Siemplify
           2) query Siemplify incidents for changes based on these incidents
           3) determine SOAR actions to take: update incident or close

        Args:
            last_poller_time ([int]): [time in milliseconds when the last poller ran]
        """
        # get all open siemplify linked incidents
        soar_incident_list = self.res_common.get_open_siemplify_incidents()
        if not soar_incident_list:
            LOG.info("IBM SOAR open incidents: 0")
            return

        # get the list of siemplify cases linked to SOAR to check for closed statuses
        seimplify_case_list, error_msg = self.siemplify_env.get_cases([ str(key) for key in soar_incident_list.keys() ])
        LOG.debug(seimplify_case_list)
        cases_closed = cases_updated = 0
        for case in seimplify_case_list['results']:
            case_id = case['id']

            soar_inc_id = soar_incident_list[case_id]
            if case.get("isCaseClosed"):
                # close the SOAR incident
                incident_close_payload = self.jinja_env.make_payload_from_template(
                                                    self.options.get("soar_close_case_template"),
                                                    DEFAULT_SOAR_CLOSE_CASE,
                                                    case)
                _close_resilient_incident = self.res_common.update_incident(
                                                    soar_inc_id,
                                                    incident_close_payload
                                                )
                cases_closed += 1
                LOG.info("Closed SOAR incident %s from Siemplify case %s",
                        soar_inc_id, case_id)
            else:
                # check if the case has been modified
                if self.siemplify_env.is_case_modified(case_id, last_poller_time):
                    case, error_msg = self.siemplify_env.get_case(case_id)

                    incident_update_payload = self.jinja_env.make_payload_from_template(
                                                    self.options.get("soar_update_case_template"),
                                                    DEFAULT_SOAR_UPDATE_CASE,
                                                    case)

                    LOG.debug("Case changed: %s. Updating SOAR incident: %s", case_id, soar_incident_list[case_id])
                    cases_updated += 1
                    # Update description, tags, priority, assignee, stage, important
                    _update_resilient_incident = self.res_common.update_incident(
                                                    soar_incident_list[case_id],
                                                    incident_update_payload
                                                )

                    # SYNC Comments
                    new_comments = self.res_common.filter_resilient_comments(soar_inc_id, case.get('insights', []))
                    LOG.info(new_comments)
                    for comment in new_comments:
                        self.res_common.create_incident_comment(soar_inc_id, comment['title'], comment['content'])

        LOG.info("IBM SOAR open cases: %s, Cases closed: %s, Cases Updated: %s",
                 len(soar_incident_list), cases_closed, cases_updated)

    def _get_last_poller_date(self, polling_lookback):
        """get the last poller datetime based on a lookback value
        Args:
            polling_lookback ([number]): # of minutes to lookback
        Returns:
            [datetime]: [datetime to use for last poller run time]
        """
        return self._get_timestamp() - datetime.timedelta(minutes=polling_lookback)


    def _get_timestamp(self):
        return datetime.datetime.now().astimezone(self.timezone)
