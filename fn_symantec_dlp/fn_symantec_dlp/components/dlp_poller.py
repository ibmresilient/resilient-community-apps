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
from resilient_lib import validate_fields, RequestsCommon, build_incident_url, build_resilient_url
from resilient import get_client
from fn_symantec_dlp.lib.jinja_common import JinjaEnvironment
from fn_symantec_dlp.lib.resilient_common import ResilientCommon
from fn_symantec_dlp.lib.dlp_common import SymantecDLPCommon, PACKAGE_NAME

TICKET_ID_FIELDNAME = "sdlp_incident_id"

DEFAULT_CREATE_DLP_CASE = "templates/dlp_create_incident_template.jinja"

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

class SymantecDLPPollerComponent(ResilientComponent):
    """
    poller for Symantec DLP Incidents
    """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(SymantecDLPPollerComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

        # Validate required fields in app.config are set
        validate_fields(["sdlp_host", "sdlp_username", "sdlp_password"], self.options)

        if not self._init_env(opts, self.options):
            LOG.info(u"Symantec DLP poller interval is not configured.  Automated escalation is disabled.")
            return

        poller_thread = Thread(target=self.run)
        poller_thread.daemon = True
        poller_thread.start()

    def _init_env(self, opts, options):
        """[initialize the environment based on app.config settings]
        Args:
            opts ([dict]): [all settings include SOAR settings]
            options ([dict]): [settings specific to Symantec DLP]
        Returns:
            [bool]: [True if poller is configured]
        """
        self.polling_interval = int(options.get("polling_interval", 0))
        if not self.polling_interval:
            return False

        LOG.info(u"Symantec DLP poller initiated, polling interval %s", self.polling_interval)
        self.timezone = pytz.timezone(options.get("polling_timezone", GMT))
        self.last_poller_time = self._get_last_poller_date(int(options.get('polling_lookback', 0)))

        rest_client = get_client(opts)
        self.res_common = ResilientCommon(rest_client)

        # Create api client
        rc = RequestsCommon(opts, options)
        self.sdlp_env = SymantecDLPCommon(rc, options)

        self.jinja_env = JinjaEnvironment()

        return True

    @poller('polling_interval', 'last_poller_time')
    def run(self, last_poller_time=None):
        """[Process to query for changes in Symantec DLP incidents and the corresponding update SOAR incident]
           The steps taken are to
           1) query SOAR for all open incidents associated with Symantec DLP
           2) query Symantec DLP incidents for changes based on these incidents
           3) determine SOAR actions to take: update incident or close
        Args:
            last_poller_time ([int]): [time in milliseconds when the last poller ran]
        """
        # get all open Symantec DLP linked incidents
        sdlp_incident_list = self.sdlp_env.get_sdlp_incidents_in_save_report(self.sdlp_env.saved_report_id, last_poller_time)
 
        sdlp_custom_attributes = self.sdlp_env.get_sdlp_incident_custom_attributes()

        if 'ibm_soar_case_id' not in sdlp_custom_attributes:
            LOG.warning("The DLP Custom Attribute 'ibm_soar_case_id' was not found on your DLP Instance. This may result in duplicate Incidents found in IBM SOAR as no filtering will be done on the DLP Side")

        for sdlp_incident_id in sdlp_incident_list:
            soar_case = self.res_common.find_incident(sdlp_incident_id)
            if soar_case is None:
                sdlp_incident_payload = self.sdlp_env.get_sdlp_incident_payload(sdlp_incident_id)
                # create a new incident
                incident_payload = self.jinja_env.make_payload_from_template(
                                                    self.options.get("create_incident_template"),
                                                    DEFAULT_CREATE_DLP_CASE,
                                                    sdlp_incident_payload)
                soar_case = self.res_common.create_incident(incident_payload)
                
                # Send ibm_soar_case_id and ibm_soar_case_url custom fields in DLP to then DLP incident
                # so that it has links back to the SOAR case.
                host = self.opts.get('host')
                port = self.opts.get('port')
                soar_case_id = soar_case.get("id")
                soar_case_url = build_incident_url(build_resilient_url(host, port), soar_case_id)
                status = self.sdlp_env.set_sdlp_update_incident_custom_attribute(sdlp_incident_id, 
                                                                                 soar_case_id, 
                                                                                 soar_case_url)

                
                LOG.info("IBM SOAR case created %s for DLP incident %s", soar_case_id, sdlp_incident_id)
        # get the list of Symantec DLP cases linked to SOAR to check for closed statuses
        """
        sdlp_case_list, error_msg = self.sdlp_env.get_cases([ str(key) for key in soar_incident_list.keys() ])
        LOG.debug(sdlp_case_list)
        cases_closed = cases_updated = 0
        for case in sdlp_case_list['results']:
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
                msg = "Closed SOAR incident {} from Symantec DLP case {}".format(soar_inc_id, case_id)
                LOG.info(msg)
                self.res_common.create_incident_comment(soar_inc_id, None, msg)
            else:
                # check if the case has been modified
                if self.sdlp_env.is_case_modified(case_id, last_poller_time):
                    case, error_msg = self.sdlp_env.get_case(case_id)

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
"""

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

