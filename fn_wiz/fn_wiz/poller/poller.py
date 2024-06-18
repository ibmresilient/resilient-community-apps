# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
# Generated with resilient-sdk v51.0.1.0.695
"""Poller implementation"""

import logging
import os
from threading import Thread

from resilient_circuits import AppFunctionComponent, is_this_a_selftest
from resilient_lib import (SOARCommon, get_last_poller_date,
                           make_payload_from_template, poller)

from fn_wiz.lib.app_common import AppCommon
from fn_wiz.poller.configure_tab import init_wiz_tab


PACKAGE_NAME = "fn_wiz"
ENTITY_ID = "id"  # name of field in the endpoint entity (alert, case, etc) with the ID value
ENTITY_CLOSE_FIELD = "status" # name of field in endpoint entity to reference the close state
SOAR_ENTITY_ID_FIELD = "wiz_issue_id" # name of custom IBM SOAR case field to retain the endpoint entity_id
ENTITY_LABEL = "Wiz Issue" # label the name the case, alert, event, etc. native to your endpoint solution
ENTITY_COMMENT_HEADER = "Created by Wiz" # header used to identify comments create by the endpoint entity
ENTITY_CLOSED_STATUSES = ["RESOLVED", "REJECTED"] # A Wiz issue can have status "RESOLVED" or "REJECTED" to indicate a closed status

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
    Initialize settings used for your app

    :param rc:  RequestsCommon class for making API calls
    :type rc: ``resilient_lib.RequestsCommon``
    :param options: app.config settings for the app
    :type options: dict
    :return: class to app class for ongoing API calls
    :rtype: ``AppCommon``
    """
    # initialize the class for making API calls to your endpoint
    app_common = AppCommon(rc, PACKAGE_NAME, options)

    # Initialize Wiz tab
    init_wiz_tab()

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

    query_results = app_common.query_new_entities_since_ts(last_poller_time)
    query_results_changed = app_common.query_changed_entities_since_ts(last_poller_time)

    # combine all the issues that have been created or where the status has been updated since the last poll
    query_results.extend(query_results_changed)
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
    
    return True if entity.get(ENTITY_CLOSE_FIELD, None) in ENTITY_CLOSED_STATUSES else False

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
        required_fields = ["polling_interval",
                        "polling_lookback",
                        "api_url",
                        "endpoint_url",
                        "token_url",
                        "client_id",
                        "client_secret"]

        super(PollerComponent, self).__init__(opts, PACKAGE_NAME, required_app_configs=required_fields)

        # collect settings necessary and initialize libraries used by the poller
        if not self._init_env(opts, self.options):
            LOG.info("Poller interval is not configured. Automated escalation is disabled.")
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

        # collect the override templates to use when creating, updating and closing cases
        self.soar_create_case_template = options.get("soar_create_case_template")
        self.soar_update_case_template = options.get("soar_update_case_template")
        self.soar_close_case_template = options.get("soar_close_case_template")

        # rest_client is used to make IBM SOAR API calls
        self.rest_client = self.rest_client()
        self.soar_common = SOARCommon(self.rest_client)
        self.app_common = init_app(self.rc, options)

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
        query_results = query_entities(self.app_common, kwargs["last_poller_time"])

        if query_results:
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

        cases_insert = cases_closed = cases_updated = 0     # track number of case creations, closes, and updates
        processed_issues = []       # track issue IDs that have been processed for debugging purposes

        for entity in query_results:
            try:
                entity_id = get_entity_id(entity)

                linkback_url = "issues#~(issue~'{})"
                entity["entity_url"] = self.app_common.make_linkback_url(entity_id, linkback_url)

                # determine if this is an existing SOAR case
                soar_case, _error_msg = self.soar_common.get_soar_case({ SOAR_ENTITY_ID_FIELD: entity_id }, open_cases=False)

                # if case does not exist and the Wiz issue status is *not* already closed, create a new one
                if not soar_case:
                    if not is_entity_closed(entity):
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
                        LOG.info("%s already marked closed in Wiz. Skipping case creation", ENTITY_LABEL)
                        continue
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

                # Add entity to processed list
                processed_issues.append(entity_id)
                LOG.debug("Wiz Issue ID %s added to processed list", entity_id)

            except Exception as err:
                LOG.error("%s poller run failed: %s", PACKAGE_NAME, str(err))
        
        LOG.info("IBM SOAR cases created: %s, cases closed: %s, cases updated: %s",
                    cases_insert, cases_closed, cases_updated)
