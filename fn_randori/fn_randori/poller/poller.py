# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Poller implementation"""

import logging
import os
from threading import Thread

from resilient import get_client
from resilient_circuits import AppFunctionComponent, is_this_a_selftest
from resilient_lib import (SOARCommon, get_last_poller_date,
                           make_payload_from_template, poller)

from fn_randori.lib.app_common import AppCommon, PACKAGE_NAME



ENTITY_ID = "target_id"  # name of field in the endpoint entity (alert, case, etc) with the ID value
ENTITY_CLOSE_FIELD = "status" # name of field in endpoint entity to reference the close state
SOAR_ENTITY_ID_FIELD = "randori_target_id" # name of custom IBM SOAR case field to retain the endpoint entity_id
ENTITY_LABEL = "Randori Target" # label the name the case, alert, event, etc. native to your endpoint solution
ENTITY_COMMENT_HEADER = "Created by Randori" # header used to identify comments create by the endpoint entity

LOG = logging.getLogger(__name__)

# Directory of default templates
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "data")

# Default Templates used to create/update/close SOAR cases.
#   Mostly they will be modified to include custom SOAR fields
CREATE_INCIDENT_TEMPLATE = os.path.join(TEMPLATE_DIR, "soar_create_incident.jinja")
UPDATE_INCIDENT_TEMPLATE = os.path.join(TEMPLATE_DIR, "soar_update_incident.jinja")
CLOSE_INCIDENT_TEMPLATE = os.path.join(TEMPLATE_DIR, "soar_close_incident.jinja")

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

    return app_common

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
    return bool(entity.get(ENTITY_CLOSE_FIELD, False) in ['Accepted', 'Mitigated'])

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
                           "endpoint_url",
                           "verify",
                           "api_token",
                           "api_version",
                           "tenant_name"]

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
        self.rest_client = get_client(opts)
        self.soar_common = SOARCommon(self.rest_client)
        self.app_common = init_app(self.rc, options)

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
                        CREATE_INCIDENT_TEMPLATE,
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
                                CLOSE_INCIDENT_TEMPLATE,
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
                            UPDATE_INCIDENT_TEMPLATE,
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
