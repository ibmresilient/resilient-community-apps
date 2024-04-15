# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""Function implementation"""

import datetime
import functools
import logging
from threading import Thread, Event
import traceback
from resilient_circuits import ResilientComponent
from resilient_lib import validate_fields, RequestsCommon, build_incident_url, build_resilient_url
from resilient import get_client
from fn_symantec_dlp.lib.jinja_common import JinjaEnvironment
from fn_symantec_dlp.lib.resilient_common import ResilientCommon
from fn_symantec_dlp.lib.dlp_common import SymantecDLPCommon, PACKAGE_NAME

DEFAULT_CREATE_DLP_CASE = "templates/dlp_create_case_template.jinja"
DEFAULT_SOAR_CLOSE_CASE = "templates/dlp_close_case_template.jinja"
DEFAULT_SOAR_UPDATE_CASE = "templates/dlp_update_case_template.jinja"

LOG = logging.getLogger(__name__)

def poller(named_poller_interval, named_last_poller_time):
    """[ Main polling function for triggering a search for Symantec DLP incidents to escalate to SOAR. ]
    Args:
        named_poller_interval ([str]): [name of instance variable containing the poller interval in seconds]
        named_last_poller_time ([datetime]): [name of instance variable containing the lookback value in mseconds]
    """
    def poller(func):
        # decorator for running a function forever, passing the ms timestamp of
        #  when the last poller run to the function it's calling
        @functools.wraps(func)
        def wrapped(self, *args):
            last_poller_time = getattr(self, named_last_poller_time)
            exit_event = Event()

            while not exit_event.is_set():
                try:
                    LOG.info(u"%s polling start.", PACKAGE_NAME)
                    poller_start = datetime.datetime.now()
                    # function execution with the last poller time in ms
                    func(self, *args, last_poller_time=int(last_poller_time.timestamp()*1000))

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
        validate_fields(["sdlp_host", "sdlp_username", "sdlp_password", "sdlp_saved_report_id"], self.options)

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
        self.last_poller_time = self._get_last_poller_date(int(options.get('polling_lookback', 0)))

        # collect the override templates to use when creating, updating and closing cases
        self.create_case_template = options.get("create_case_template")
        self.update_case_template = options.get("update_case_template")
        self.close_case_template = options.get("close_case_template")

        rest_client = get_client(opts)
        self.res_common = ResilientCommon(rest_client)

        # Create api client
        rc = RequestsCommon(opts, options)
        self.sdlp_env = SymantecDLPCommon(rc, options)

        self.jinja_env = JinjaEnvironment()

        return True

    @poller('polling_interval', 'last_poller_time')
    def run(self, *args, **kwargs):
        """[Process to query for changes in Symantec DLP incidents and the corresponding update SOAR incident]
           The steps taken are to
           1) query SOAR for all open cases associated with Symantec DLP
           2) query Symantec DLP incidents for changes based on these incidents
           3) determine SOAR actions to take: update or close case
        Args:
            last_poller_time ([int]): [time in milliseconds when the last poller ran]
        """
        # Get all open Symantec DLP incidents matching filter from saved report in DLP.
        sdlp_incident_list = self.sdlp_env.get_sdlp_incidents_in_save_report(self.sdlp_env.saved_report_id, kwargs['last_poller_time'])
 
        # Get the list of custom attributes in DLP (similar to custom fields in SOAR)
        sdlp_custom_attributes = self.sdlp_env.get_sdlp_incident_custom_attributes()

        # Give a warning if the ibm_soar_case_id custom attribute is not created in DLP by the user.
        if 'ibm_soar_case_id' not in sdlp_custom_attributes:
            LOG.warning("The DLP Custom Attribute 'ibm_soar_case_id' was not found on your DLP Instance. This may result in duplicate Incidents found in IBM SOAR as no filtering will be done on the DLP Side")

        for sdlp_incident_id in sdlp_incident_list:
            soar_case = self.res_common.find_incident(sdlp_incident_id)

            if soar_case is None:
                # Create a new case
                sdlp_incident_payload = self.sdlp_env.get_sdlp_incident_payload(sdlp_incident_id)
                incident_payload = self.jinja_env.make_payload_from_template(
                                                    self.options.get("create_case_template"),
                                                    DEFAULT_CREATE_DLP_CASE,
                                                    sdlp_incident_payload)
                soar_case = self.res_common.create_incident(incident_payload)
                soar_case_id = soar_case.get("id")

                # Send ibm_soar_case_id and ibm_soar_case_url custom attributes in DLP to the DLP incident
                # so that it has links back to the SOAR case.
                soar_case_url = build_incident_url(build_resilient_url(self.opts.get('host'), self.opts.get('port')),
                                                   soar_case_id)
                status = self.sdlp_env.patch_sdlp_incident_custom_attribute(sdlp_incident_id,
                                                                            soar_case_id,
                                                                            soar_case_url)
                # Send a note to DLP incident to have creation in the history
                sdlp_note_text = u"""IBM SOAR case created: {0}""".format(soar_case_url)                
                response = self.sdlp_env.send_note_to_sdlp(sdlp_incident_id, sdlp_note_text)

                if sdlp_incident_id not in response.get("updatedIncidentIds"):
                    LOG.error("Unable to send note to Symantec DLP incident %s", sdlp_incident_id)

                LOG.info("IBM SOAR case created %s for DLP incident %s", soar_case_id, sdlp_incident_id)
            else: 
                soar_case_id = soar_case.get("id")
                sdlp_incident_id = soar_case.get("sdlp_incident_id")
                sdlp_incident_payload = self.sdlp_env.get_sdlp_incident_editable_detail_payload(sdlp_incident_id)
                sdlp_incident_status_name = self.sdlp_env.get_incident_status_name(sdlp_incident_payload)

                if sdlp_incident_status_name is'Resolved':
                    # Close the case in SOAR
                    incident_close_payload = self.jinja_env.make_payload_from_template(
                                                    self.options.get("close_case_template"),
                                                    DEFAULT_SOAR_CLOSE_CASE,
                                                    sdlp_incident_payload)

                    _close_resilient_incident = self.res_common.update_incident(
                                                    soar_case_id,
                                                    incident_close_payload)
                    msg = "Closed SOAR incident {0} from Symantec DLP incident {1}".format(soar_case_id, sdlp_incident_id)
                    LOG.info(msg)
                    self.res_common.create_incident_comment(soar_case_id, msg)                
                
                else:
                    # Update the case in SOAR
                    incident_update_payload = self.jinja_env.make_payload_from_template(
                                                    self.options.get("update_case_template"),
                                                    DEFAULT_SOAR_UPDATE_CASE,
                                                    sdlp_incident_payload)

                    _update_resilient_incident = self.res_common.update_incident(
                                                    soar_case_id,
                                                    incident_update_payload)
                
                    # SYNC Comments
                    sdlp_notes  = self.sdlp_env.get_sdlp_incident_notes(sdlp_incident_id)
                    new_comments = self.res_common.filter_resilient_comments(soar_case_id, sdlp_notes)
                    LOG.info(new_comments)

                    for comment in new_comments:
                        self.res_common.create_incident_comment(soar_case_id, comment)

                    LOG.info("IBM SOAR case updated %s for DLP incident %s", soar_case_id, sdlp_incident_id)

    def _get_last_poller_date(self, polling_lookback):
        """get the last poller datetime based on a lookback value
        Args:
            polling_lookback ([number]): # of minutes to lookback
        Returns:
            [datetime]: [datetime to use for last poller run time]
        """
        return self._get_timestamp() - datetime.timedelta(days=polling_lookback)


    def _get_timestamp(self):
        return datetime.datetime.now()

