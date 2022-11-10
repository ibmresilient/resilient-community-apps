# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Poller implementation"""

import logging
import os
from threading import Thread

from fn_darktrace.lib.app_common import (DEVICE_DT_NAME, EVENT_DT_NAME,
                                         MODEL_BREACHES_DT, PACKAGE_NAME,
                                         AppCommon)
from fn_darktrace.poller.configure_tab import init_incident_groups_tab
from resilient import SimpleClient
from resilient_circuits import AppFunctionComponent, is_this_a_selftest
from resilient_lib import (IntegrationError, SOARCommon, get_last_poller_date,
                           make_payload_from_template, poller)

ENTITY_ID = "id"
ENTITY_CLOSE_FIELD = "acknowledged"
SOAR_ENTITY_ID_FIELD = "darktrace_aianalyst_incident_group_id" # name of custom IBM SOAR case field to retain the endpoint entity_id
ENTITY_LABEL = "AI Analyst Incident" # label the name the case, alert, event, etc. native to your endpoint solution
ENTITY_COMMENT_HEADER = "Created by Darktrace" # header used to identify comments create by the endpoint entity

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
URL_FORMATTER = "<a target='_blank' href='{0}'>{1}</a>"
SPAN_FORMATTER = "<span class='label' rel='tooltip' title='{0}'>{0}</span>"

# Directory of default templates
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "data")

def get_template_dir():
    # quick property to get template directory
    return TEMPLATE_DIR

LOG = logging.getLogger(__name__)

# Default Templates used to create/update/close SOAR cases.
#   Mostly they will be modified to include custom SOAR fields
CREATE_INCIDENT_TEMPLATE = os.path.join(TEMPLATE_DIR, "soar_create_incident.jinja")
UPDATE_INCIDENT_TEMPLATE = os.path.join(TEMPLATE_DIR, "soar_update_incident.jinja")
CLOSE_INCIDENT_TEMPLATE = os.path.join(TEMPLATE_DIR, "soar_close_incident.jinja")

def init_app(rc, app_configs, integrations_configs):
    """
    Intialize settings used for Darktrace

    :param rc:  RequestsCommon class for making API calls
    :type rc: ``resilient_lib.RequestsCommon``
    :param options: app.config settings for the app
    :type options: dict
    :return: class to app class for ongoing API calls
    :rtype: ``AppCommon``
    """
    endpoint_class = AppCommon(rc, app_configs, integrations_configs)

    init_incident_groups_tab()

    return endpoint_class

def query_entities(app_common: AppCommon, last_poller_time):
    """
    Method call to query the endpoint solution for newly created or 
    modified entities for synchronization with IBM SOAR

    :param app_common: class for app API calls
    :type app_common: obj
    :param last_poller_time: timestamp in milliseconds to collect the changed entities (alerts, cases, etc.)
    :type last_poller_time: int
    :return: list of entities to synchronize with SOAR
    :rtype: list
    """
    query_results = []

    # enter the code needed to perform a query to the endpoint platform, using the last_poller_time to
    # identify entities changed since that timestamp.
    # use *args and **kwargs to collect urls, api_keys, etc. needed for API call(s).
    #   query_entities_since_ts(last_poller_time, *args, **kwargs)
    query_results = app_common.query_entities_since_ts(last_poller_time)

    return query_results


def get_entity_id(entity):
    """
    Get the id for the entity returned in your query

    :param entity: data structure of an entity
    :type entity: dict
    :return: entity_id to use
    :rtype: str
    """
    return entity.get(ENTITY_ID)

def is_entity_closed(entity):
    """
    Determine if your entity is in a closed state

    :param entity: data structure of an entity
    :type entity: dict
    :return: true/false if entity is closed
    :rtype: bool
    """
    return bool(entity.get(ENTITY_CLOSE_FIELD, False))

class PollerComponent(AppFunctionComponent):
    """
    poller for escalating SOAR incidents and synchronizing changes
    """

    def __init__(self, opts):
        """
        Constructor provides access to the configuration options

        :param opts: all settings including SOAR settings
        :type opts: dict
        """
        # Validate required fields in app.config are set
        required_fields = ["polling_interval", "polling_lookback"]

        super(PollerComponent, self).__init__(opts, PACKAGE_NAME, required_app_configs=required_fields)

        # collect settings necessary and initialize libraries used by the poller
        if not self._init_env(opts, self.options):
            LOG.info("Poller interval is not configured.  Automated escalation is disabled.")
            return

        poller_thread = Thread(target=self.run)
        poller_thread.daemon = True
        poller_thread.start()

    def _init_env(self, opts, options):
        """
        Initialize the environment based on app.config settings

        :param opts: all settings including SOAR settings
        :type opts: dict
        :param options: settings specific to this app
        :type options: dict
        :return: True if poller is configured
        :rtype: bool
        """
        self.polling_interval = float(options.get("polling_interval", 0))
        if not self.polling_interval or is_this_a_selftest(self):
            LOG.debug("Exiting poller because polling interval set to 0 or this run is a selftest.")
            return False

        LOG.info("Poller initiated, polling interval %s", self.polling_interval)
        self.last_poller_time = get_last_poller_date(int(options.get("polling_lookback", 0)))
        LOG.info("Poller lookback: %s", self.last_poller_time)

        # collect the override templates to use when creating, updating and closing cases
        self.soar_create_case_template = options.get("soar_create_case_template")
        self.soar_update_case_template = options.get("soar_update_case_template")
        self.soar_close_case_template = options.get("soar_close_case_template")

        # rest_client is used to make IBM SOAR API calls
        self.rest_client = self.rest_client()
        self.soar_common = SOARCommon(self.rest_client)
        self.app_common = init_app(self.rc, options, opts.get("integrations", {}))

        return True

    @poller("polling_interval", "last_poller_time")
    def run(self, *args, **kwargs):
        """
        Process to query for changes in datasource entities and the cooresponding update SOAR case.
        The steps taken are:
           1) query SOAR for all open entities associated with the datasource
           2) query datasource entities for changes based on these incidents
           3) determine SOAR actions to take: create, update, or close a case

        :param last_poller_time: time in milliseconds when the last poller ran
        :type last_poller_time: int
        """

        # get the list of entities (alerts, cases, etc.) to insert, update or close as cases in IBM SOAR
        query_results = query_entities(self.app_common, kwargs["last_poller_time"])

        if query_results:
            # iterate over all the entities.
            self.process_query_list(query_results)

        # get list of open cases in SOAR that were created by Darktrace
        # in order to update them with new comments or close them if they've
        # been acknowledged in Darktrace
        all_open_cases_from_darktrace, _ = self.soar_common.get_soar_cases({SOAR_ENTITY_ID_FIELD: True}, open_cases=True)
        if all_open_cases_from_darktrace:
            if self.app_common.auto_sync_comments:
                self.update_comments(all_open_cases_from_darktrace)
            self.close_case_if_acknowledged_in_darktrace(all_open_cases_from_darktrace)

    def process_query_list(self, query_results, allow_updates=True):
        """
        Perform all the processing on the entity list, creating, updating and closing SOAR
        cases based on the states of the endpoint entities.

        The logic is to determine if a SOAR case needs to be created, updated or closed, and
        apply the correct template file to apply the field changes.

        :param query_results: list of endpoint entities to check against SOAR cases
        :type query_results: list
        """

        try:
            cases_insert = cases_closed = cases_updated = 0
            for incident_group in query_results:

                entity_id = get_entity_id(incident_group)

                # determine if this is an existing SOAR case
                soar_case, _error_msg = self.soar_common.get_soar_case({ SOAR_ENTITY_ID_FIELD: entity_id }, open_cases=False)

                # if case does not exist, create a new one
                if not soar_case:
                    # create the SOAR case
                    soar_create_payload = make_payload_from_template(
                        self.soar_create_case_template,
                        CREATE_INCIDENT_TEMPLATE,
                        incident_group)
                    create_soar_case = self.soar_common.create_soar_case(soar_create_payload)

                    soar_case_id = create_soar_case.get("id") # get newly created case_id

                    # comments are associated with events, thus, we'll post the comment to the first event
                    # TODO: reimplement this once Darktrace has exposed this endpoint fully for our use
                    # comment_content = f"Synced to SOAR Case {soar_case_id}"
                    # first_incident_event_id = incident_group.get("incidentEvents")[0].get("uuid")
                    # self.app_common.add_incident_group_comment(first_incident_event_id, comment_content, capture_error=True)

                    cases_insert += 1
                    LOG.info("Created SOAR case %s from %s %s", soar_case_id, ENTITY_LABEL, entity_id)
                else:
                    soar_case_id = soar_case.get("id")

                    if is_entity_closed(incident_group):
                        if soar_case.get("plan_status", "C") == "A":
                            # close the SOAR case only if active
                            soar_close_payload = make_payload_from_template(
                                self.soar_close_case_template,
                                CLOSE_INCIDENT_TEMPLATE,
                                incident_group)
                            _close_soar_case = self.soar_common.update_soar_case(soar_case_id, soar_close_payload)

                            cases_closed += 1
                            LOG.info("Closed SOAR case %s from %s %s", soar_case_id, ENTITY_LABEL, entity_id)
                    elif allow_updates:
                        # perform an update operation on the existing SOAR case
                        soar_update_payload = make_payload_from_template(
                            self.soar_update_case_template,
                            UPDATE_INCIDENT_TEMPLATE,
                            incident_group)
                        self.soar_common.update_soar_case(soar_case_id, soar_update_payload)

                        cases_updated += 1
                        LOG.info("Updated SOAR case %s from %s %s", soar_case_id, ENTITY_LABEL, entity_id)

            if cases_insert or cases_closed or cases_updated:
                LOG.info("IBM SOAR cases created: %s, cases closed: %s, cases updated: %s",
                        cases_insert, cases_closed, cases_updated)
        except Exception as err:
            LOG.error("%s poller run failed: %s", PACKAGE_NAME, str(err))

    def update_comments(self, cases):
        """
        Runs through every open Darktrace case in SOAR and
        sees if there are any new comments to sync across.
        If there are, they are posted individually as a comment in SOAR

        NOTE: This method can be heavy time-wise if there are a lot of open
        cases from Darktrace in SOAR. That is why there is the option to disable
        comment syncing. See the config.py file for more info.

        :param cases: list of SOAR case objects
        :type cases: list[dict]
        """
        for case in cases:
            case_id = case.get("id")
            case_darktrace_group_id = case.get("properties", {}).get(SOAR_ENTITY_ID_FIELD)

            comments = self.app_common.query_group_comments(case_darktrace_group_id)

            if comments:
                comments = self.soar_common.filter_soar_comments(case_id, comments)

                for comment in comments:
                    LOG.info("Added comment from Darktrace to IBM SOAR case %s", case_id)
                    LOG.debug("Comment details: %s", comment)
                    self.soar_common.create_case_comment(case_id, comment)

    def close_case_if_acknowledged_in_darktrace(self, cases):
        """
        Generate a list of group objects based on the current
        open cases from Darktrace in SOAR and see if they need
        to be closed in SOAR (i.e. they've been "acknowledged")
        in Darktrace.

        :param cases: list of SOAR case objects
        :type cases: list[dict]
        """
        # for efficiency (only one API call), get a list of all the group_ids and join
        # them together in a comma-separated string to use in the get_incident_groups API call
        group_ids = ",".join([case.get("properties", {}).get(SOAR_ENTITY_ID_FIELD) for case in cases])
        incident_groups = self.app_common.get_incident_groups({"groupid": group_ids})

        # if no incident groups were found, exit gracefully
        if not incident_groups:
            return

        # process each case and close if needed (i.e. if the case is currently open and
        # should be moved to closed because the incident group is "acknowledged")
        # but don't make any updates to the case as that is handled elsewhere
        # and would be too frequent (thus the `allow_updates=False`)
        self.process_query_list(incident_groups, allow_updates=False)
