# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
# Generated with resilient-sdk v51.0.2.2.1096
"""Poller implementation"""

import logging
import os
from threading import Thread

from resilient_circuits import (AppFunctionComponent, is_this_a_selftest)
from resilient_lib import (SOARCommon, build_incident_url, build_resilient_url, get_last_poller_date,
                           make_payload_from_template, poller, str_to_bool)

from fn_sumo_logic.lib.app_common import (AppCommon, SOAR_HEADER)
from fn_sumo_logic.poller.configure_tab import (init_sumo_logic_tab)

PACKAGE_NAME = "fn_sumo_logic"
ENTITY_ID = "id"  # name of field in the endpoint entity (alert, case, etc) with the ID value
READABLE_ENTITY_ID = "readableId"  # name of field in the endpoint entity (alert, case, etc) with the ID value
ENTITY_CLOSE_FIELD = "status" # name of field in endpoint entity to reference the close state
SOAR_ENTITY_ID_FIELD = "sumo_logic_insight_id" # name of custom IBM SOAR case field to retain the endpoint entity_id
ENTITY_LABEL = "Sumo Logic Insight" # label the name the case, alert, event, etc. native to your endpoint solution
ENTITY_COMMENT_HEADER = "Created by Sumo Logic" # header used to identify comments create by the endpoint entity

LOG = logging.getLogger(__name__)

# Directory of default templates
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "data")

# Default Templates used to create/update/close SOAR cases.
#   Mostly they will be modified to include custom SOAR fields
CREATE_CASE_TEMPLATE = os.path.join(TEMPLATE_DIR, "soar_create_case.jinja")
UPDATE_CASE_TEMPLATE = os.path.join(TEMPLATE_DIR, "soar_update_case.jinja")
CLOSE_CASE_TEMPLATE = os.path.join(TEMPLATE_DIR, "soar_close_case.jinja")

def init_app(options):
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
    app_common = AppCommon(PACKAGE_NAME, options)

    init_sumo_logic_tab()

    return app_common

def query_entities(app_common, soar_common, last_poller_time):
    """
    Method call to query the endpoint solution for newly created or
    modified entities for synchronization with IBM SOAR

    :param app_common: class for app API calls
    :type app_common: obj
    :param soar_common: class for SOAR API calls
    :type soar_common: obj
    :param last_poller_time: timestamp in milliseconds to collect the changed entities (alerts, cases, etc.)
    :type last_poller_time: int
    :return: list of entities to synchronize with SOAR
    :rtype: list
    """
    query_results = []

    # Get the sumo logic insights created in the specified time frame.
    query_results, _ = app_common.query_entities_since_ts(last_poller_time)

    # Get all of the active (open) sumo logic cases in SOAR.
    # Sumo Logic does not allow querying insights based on lastUpdateTime even though it is an insight field.
    # In order to implement bidirectional updating, we must get the SOAR cases with sumo logic insight id
    # and update them on each poll time - this is expensive in terms of API calls - we should get sumo logic
    # to add querying based on lasUpdateTime!
    all_open_sumo_logic_cases, _ = soar_common.get_soar_cases({SOAR_ENTITY_ID_FIELD: True}, open_cases=True)

    # Create a list of insights ids with cases in SOAR.
    insight_id_list = []
    for case in all_open_sumo_logic_cases:
        insight_id_list.append(case.get("properties", {}).get("sumo_logic_insight_id"))

    if insight_id_list:
        # De-dup the insight list and remove any insights already in the query results to minimize API calls
        for insight in query_results:
            if insight.get(ENTITY_ID) in insight_id_list:
                insight_id_list.remove(insight.get(ENTITY_ID))

        if insight_id_list:
            # Get the insights data from sumo logic for the list of insights.
            insight_list, _ = app_common.query_insights_list(insight_id_list)

            # Append cases to update to list of new cases to create.
            query_results.extend(insight_list)

    return query_results


def get_entity_id(entity: str) -> str:
    """
    Get the id for the entity returned in your query

    :param entity: data structure of an entity
    :type entity: dict
    :return: entity_id to use
    :rtype: str
    """
    return entity.get(ENTITY_ID)

def is_entity_closed(entity: str) -> bool:
    """
    Determine if your entity is in a closed state

    :param entity: data structure of an entity
    :type entity: dict
    :return: true/false if entity is closed
    :rtype: bool
    """
    status = entity.get(ENTITY_CLOSE_FIELD)
    name = status.get("name", "closed")
    closed = True if name == "closed" else False
    return closed

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
        # <::CHANGE_ME:: change this validation to include all the fields required in the app.config file >
        required_fields = ["polling_interval",
                           "polling_lookback",
                           "api_endpoint_url",
                           "access_id",
                           "access_key"]

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
        polling_lookback = options.get("polling_lookback") or 0
        self.last_poller_time = get_last_poller_date(int(polling_lookback))
        LOG.info("Poller lookback: %s", self.last_poller_time)

        self.polling_add_case_url_comment_in_sumo_logic = str_to_bool(options.get("polling_add_case_url_comment_in_sumo_logic", "True"))
        LOG.info("Poller add case URL comment to Sumo Logic Insight: %s", self.polling_add_case_url_comment_in_sumo_logic)

        # collect the override templates to use when creating, updating and closing cases
        self.soar_create_case_template = options.get("soar_create_case_template")
        self.soar_update_case_template = options.get("soar_update_case_template")
        self.soar_close_case_template = options.get("soar_close_case_template")

        # rest_client is used to make IBM SOAR API calls
        self.rest_client = self.rest_client()
        self.soar_common = SOARCommon(self.rest_client)
        self.app_common = init_app(options)

        return True

    @poller("polling_interval", "last_poller_time")
    def run(self, *args, **kwargs):
        """
        Process to query for changes in datasource entities and the corresponding update SOAR case.
        The steps taken are:
           1) query SOAR for all open entities associated with the datasource
           2) query datasource entities for changes based on these incidents
           3) determine SOAR actions to take: create, update, or close a case

        :param last_poller_time: time in milliseconds when the last poller ran
        :type last_poller_time: int
        """

        # get the list of entities (alerts, cases, etc.) to insert, update or close as cases in IBM SOAR
        query_results = query_entities(self.app_common, self.soar_common, kwargs["last_poller_time"])

        if query_results:
            # iterate over all the entities.
            self.process_query_list(query_results)

    def process_query_list(self, query_results):
        """
        Perform all the processing on the entity list, creating, updating and closing SOAR
        cases based on the states of the endpoint entities.

        The logic is to determine if a SOAR case needs to be created, updated or closed, and
        apply the correct template file to apply the field changes.

        :param query_results: list of endpoint entities to check against SOAR cases
        :type query_results: list
        """

        cases_insert = cases_closed = cases_updated = 0
        entity_id = None
        for entity in query_results:
            try:
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

                    if self.polling_add_case_url_comment_in_sumo_logic:
                        # Build a URL to the SOAR case and update Sumo Logic insight with a comment
                        soar_link = build_incident_url(
                            build_resilient_url(self.opts.get('host'), self.opts.get("port", 443)),
                            soar_case_id, create_soar_case.get("org_handle", None))

                        soar_link_note = f"Case - {soar_case_id}: {soar_link}"

                        _create_note, _error_msg = self.app_common.post_comment(entity_id, soar_link_note, SOAR_HEADER)

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
            except Exception as err:
                LOG.error("%s poller run failed for entity %s: %s", PACKAGE_NAME, entity_id, str(err))

        LOG.info("IBM SOAR cases created: %s, cases closed: %s, cases updated: %s",
                    cases_insert, cases_closed, cases_updated)
