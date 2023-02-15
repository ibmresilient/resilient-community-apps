# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Poller implementation"""

import logging
import os
from threading import Thread

from resilient_circuits import AppFunctionComponent, is_this_a_selftest
from resilient_lib import (SOARCommon, get_last_poller_date,
                           make_payload_from_template, poller, validate_fields)

from fn_jira.lib.app_common import AppCommon
from fn_jira.poller.configure_tab import init_incident_groups_tab
from fn_jira.util import helper


PACKAGE_NAME = "fn_jira"
ENTITY_ID = "<- ::CHANGE_ME:: ->"  # name of field in the endpoint entity (alert, case, etc) with the ID value
ENTITY_CLOSE_FIELD = "<- ::CHANGE_ME:: ->" # name of field in endpoint entity to reference the close state
SOAR_ENTITY_ID_FIELD = "<- ::CHANGE_ME:: ->" # name of custom IBM SOAR case field to retain the endpoint entity_id
ENTITY_LABEL = "<- ::CHANGE_ME:: ->" # label the name the case, alert, event, etc. native to your endpoint solution
ENTITY_COMMENT_HEADER = "Created by <- ::CHANGE_ME:: ->" # header used to identify comments create by the endpoint entity

LOG = logging.getLogger(__name__)

# Directory of default templates
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "data")

# Default Templates used to create/update/close SOAR cases.
#   Mostly they will be modified to include custom SOAR fields
CREATE_CASE_TEMPLATE = os.path.join(TEMPLATE_DIR, "soar_create_case.jinja")
UPDATE_CASE_TEMPLATE = os.path.join(TEMPLATE_DIR, "soar_update_case.jinja")
CLOSE_CASE_TEMPLATE = os.path.join(TEMPLATE_DIR, "soar_close_case.jinja")

def init_app(rc, options):
    """
    Intialize settings used for your app

    :param rc:  RequestsCommon class for making API calls
    :type rc: ``resilient_lib.RequestsCommon``
    :param options: app.config settings for the app
    :type options: dict
    :return: class to app class for ongoing API calls
    :rtype: ``AppCommon``
    """
    # initialize the class for making API calls to your endpoint
    app_common = AppCommon(rc, PACKAGE_NAME, options)

    # <add additional initialization steps for your endpoint as necessary>

    return app_common

def query_entities(app_common, last_poller_time):
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
    # <::CHANGE_ME:: change this field to reflect the field and logic to determine if the entity is now closed >
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

        super(PollerComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
        init_incident_groups_tab()

        # Collect settings necessary and initialize libraries used by the poller
        if not self._init_env():
            LOG.info("Poller interval is not configured. Automated escalation is disabled.")
            return

        # Create poller thread
        poller_thread = Thread(target=self.run)
        poller_thread.daemon = True
        poller_thread.start()

    def _init_env(self):
        """
        Initialize the environment based on app.config settings

        :return: True if poller is configured
        :rtype: bool
        """
        global_settings = self.opts.get(helper.GLOBAL_SETTINGS, {})
        self.polling_interval = int(global_settings.get("polling_interval", 0))
        if not self.polling_interval or is_this_a_selftest(self):
            LOG.debug("Exiting poller because polling interval set to 0 or this run is a selftest.")
            return False

        LOG.info("Poller initiated, polling interval %s", self.polling_interval)
        self.last_poller_time = get_last_poller_date(int(global_settings.get("polling_lookback", 0)))
        LOG.info("Poller lookback: %s", self.last_poller_time)

        # Collect the override templates to use when creating, updating and closing cases
        self.soar_create_case_template = global_settings.get("soar_create_case_template")
        self.soar_update_case_template = global_settings.get("soar_update_case_template")
        self.soar_close_case_template = global_settings.get("soar_close_case_template")

        # rest_client is used to make IBM SOAR API calls
        self.rest_client = self.rest_client()
        self.soar_common = SOARCommon(self.rest_client)

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

        # List of the Jira datatable names found in the app.config
        jira_dt_names = []

        # Dictionary of dicts that say what info to get from each SOAR case
        data_to_get_from_case = {"tasks": []}

        # Get list of Jira servers configured in the app.config
        servers_list = helper.JiraServers(self.opts).get_server_name_list()
        # If no servers labeled then add fn_jira to list
        if not servers_list:
            servers_list.append(helper.PACKAGE_NAME)

        # Get global_setting if definied in the app.config
        global_settings = self.opts.get(helper.GLOBAL_SETTINGS, {})

        # Validation dictionary for the "poller_filters" app.config setting
        poller_filters_validator = {"name": "poller_filters",
                                   "placeholder": "priority in (high, medium, low) and "\
                                   "status in ('to do', 'in progress', done) and project in "\
                                   "(project_name1, project_name2)"}

        # Dictionary for Jira Issues
        jira_issues_dict = {}

        # Loop through all the Jira servers in the app.config
        for server in servers_list:

            # If multiple servers are define get just the servers label
            if server.startswith(f"{helper.PACKAGE_NAME}:"):
                server = server[len(helper.PACKAGE_NAME)+1:]

            # Get settings for server from the app.config
            options = helper.get_server_settings(self.opts, server)

            # Add the datatable name specified in the current app.config
            dt_name = options.get("jira_dt_name")
            if dt_name not in jira_dt_names:
                jira_dt_names.append(dt_name)

            # Get the max_results settings from the global_settings
            max_results = global_settings.get("max_issues_returned")
            if not max_results:
                # Get the max_results settings from the servers settings
                max_results = options.get("max_issues_returned")

            # If poller_filters and or max_results are defnined in the global_settings
            poller_filters = global_settings.get("poller_filters")
            if poller_filters:
                # Validate poller_filter
                validate_fields([poller_filters_validator], global_settings)
            else: # If poller_filters is defnined in individual Jira server settings
                # Validate poller_filter
                validate_fields([poller_filters_validator], options)
                # Get the poller_filters settings from the servers settings
                poller_filters = options.get("poller_filters")

            # Get a list of Jira issues bases on the given search filters
            jira_issue_list, data_to_get_from_case = AppCommon(self.opts, options).search_jira_issues(
                poller_filters,
                self.last_poller_time,
                max_results,
                data_to_get_from_case
            )

            # Add list of Jira issues to jira_issues_dict under the server the issues where found in
            jira_issues_dict[server] = jira_issue_list

        # Get a list of open SOAR cases that contain the field jira_issue_id.
        soar_cases_list, err_msg = SOARCommon(self.rest_client()).get_soar_cases({"jira_issue_id": True})

        soar_cases_list = self.process_soar_cases(soar_cases_list, data_to_get_from_case)

        # Process Jira issues returned from search
        self.process_jira_issue_dict(jira_issues_dict, soar_cases_list)

    def process_query_list(self, query_results):
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
            for entity in query_results:
                entity_id = get_entity_id(entity)

                # create linkback url
                entity["entity_url"] = self.app_common.make_linkback_url(entity_id)

                # determine if this is an existing SOAR case
                soar_case, _error_msg = self.soar_common.get_soar_case({ SOAR_ENTITY_ID_FIELD: entity_id }, open_cases=False)

                # if case does not exist, create a new one
                if not soar_case:
                    # create the SOAR case
                    soar_create_payload = make_payload_from_template(
                        self.soar_create_case_template,
                        CREATE_CASE_TEMPLATE,
                        entity)
                    create_soar_case = self.soar_common.create_soar_case(
                        soar_create_payload)

                    soar_case_id = create_soar_case.get("id") # get newly created case_id

                    cases_insert += 1
                    LOG.info("Created SOAR case %s from %s %s", soar_case_id, ENTITY_LABEL, entity_id)
                else:
                    soar_case_id = soar_case.get("id")

                    if is_entity_closed(entity):
                        if soar_case.get("plan_status", "C") == "A":
                            # close the SOAR case
                            soar_close_payload = make_payload_from_template(
                                self.soar_close_case_template,
                                CLOSE_CASE_TEMPLATE,
                                entity)
                            _close_soar_case = self.soar_common.update_soar_case(
                                soar_case_id,
                                soar_close_payload)

                            cases_closed += 1
                            LOG.info("Closed SOAR case %s from %s %s", soar_case_id, ENTITY_LABEL, entity_id)
                    else:
                        # perform an update operation on the existing SOAR case
                        soar_update_payload = make_payload_from_template(
                            self.soar_update_case_template,
                            UPDATE_CASE_TEMPLATE,
                            entity)
                        _update_soar_case = self.soar_common.update_soar_case(
                            soar_case_id,
                            soar_update_payload)

                        cases_updated += 1
                        LOG.info("Updated SOAR case %s from %s %s", soar_case_id, ENTITY_LABEL, entity_id)

            LOG.info("IBM SOAR cases created: %s, cases closed: %s, cases updated: %s",
                     cases_insert, cases_closed, cases_updated)
        except Exception as err:
            LOG.error("%s poller run failed: %s", PACKAGE_NAME, str(err))
