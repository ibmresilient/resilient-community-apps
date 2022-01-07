# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""Function implementation"""

import datetime
import logging
import pytz
import traceback
from circuits import Event, Timer
from resilient_circuits import ResilientComponent, handler
from resilient_lib import validate_fields, RequestsCommon
from resilient import get_client
from fn_siemplify.lib.jinja_common import JinjaEnvironment
from fn_siemplify.lib.resilient_common import ResilientCommon
from fn_siemplify.lib.siemplify_common import SiemplifyCommon, PACKAGE_NAME

POLLER_CHANNEL = "siemplify_poller"
TICKET_ID_FIELDNAME = "simplify_case_id"

DEFAULT_POLLER_LOOBACK_MINUTES = 120
DEFAULT_SOAR_CLOSE_CASE = "templates/soar_close_case.jinja"
DEFAULT_SOAR_UPDATE_CASE = "templates/soar_update_case.jinja"

GMT = "Etc/GMT"

DEFAULT_POLLER_SECONDS = 600
LOG = logging.getLogger(__name__)

class Poll(Event):
    """A Circuits event to trigger polling"""
    channels = (POLLER_CHANNEL,)

class PollCompleted(Event):
    """A Circuits event to notify that this poll event is completed"""
    channels = (POLLER_CHANNEL,)


class SiemplifyPollerComponent(ResilientComponent):
    """
    Event-driven polling for Siemplify Incidents
    """

    # This doesn't listen to Action Module, only its internal channel for timer events
    # But we still inherit from ResilientComponent so we get a REST client etc
    channel = POLLER_CHANNEL

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(SiemplifyPollerComponent, self).__init__(opts)
        self.jinja_env = JinjaEnvironment()
        self.options = opts.get(PACKAGE_NAME, {})

        self._load_options(opts)
        if self.polling_interval == 0:
            LOG.info(u"Siemplify poller interval is not configured.  Automated escalation is disabled.")
            return

        LOG.info(u"Siemplify poller initiated, polling interval %s", self.polling_interval)
        Timer(self.polling_interval, Poll(), persist=False).register(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self._load_options(opts)

    @handler("Poll")
    def _poll(self, event):
        """Handle the timer"""
        LOG.info(u"Siemplify start polling.")
        self._escalate()

    @handler("PollCompleted")
    def _poll_completed(self, event):
        """Set up the next timer"""
        LOG.info(u"Siemplify poller complete.")
        Timer(self.polling_interval, Poll(), persist=False).register(self)

    def _load_options(self, opts):
        """Read options from config"""
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

        # Validate required fields in app.config are set
        required_fields = ["api_key", "base_url"]
        validate_fields(required_fields, self.options)

        self.polling_interval = int(self.options.get("polling_interval", 0))
        if not self.polling_interval:
            return

        self.timezone = pytz.timezone(self.options.get("polling_timezone", GMT))
        self.last_poller_time = self._get_last_poller_date(int(self.options.get('polling_lookback', DEFAULT_POLLER_LOOBACK_MINUTES)))

        rest_client = get_client(self.opts)
        self.res_common = ResilientCommon(rest_client)

        # Create api client
        rc = RequestsCommon(self.opts, self.options)
        self.siemplify_env = SiemplifyCommon(rc, self.options)


    def _escalate(self):
        """ This is the main logic of the poller
            Search for Siemplify incidents and create associated cases in Resilient SOAR
        """
        poller_start = self._get_timestamp()
        try:
            # call Siemplify for closed incidents
            self.process_cases(int(self.last_poller_time.timestamp()*1000))
        except Exception as err:
            LOG.error(str(err))
            LOG.error(traceback.format_exc())
        finally:
            # set the last poller time for next cycle
            self.last_poller_time = poller_start
            # We always want to reset the timer to wake up, no matter failure or success
            self.fire(PollCompleted())

    def process_cases(self, last_poller_time):
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
        """get the last poller datetime based on a lookback time
        Args:
            polling_lookback ([number]): # of minutes to lookback
        Returns:
            [datetime]: [datetime to use for last poller run time]
        """
        return self._get_timestamp() - datetime.timedelta(minutes=polling_lookback)


    def _get_timestamp(self):
        return datetime.datetime.now().astimezone(self.timezone)
