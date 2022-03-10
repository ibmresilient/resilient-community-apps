# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Poller implementation"""

import logging
import os
from threading import Thread
from resilient_circuits import ResilientComponent
from resilient import get_client
from fn_extrahop.lib.poller_common import SOARCommon, poller, get_template_dir, get_last_poller_date
from fn_extrahop.lib.app_common import AppCommon
from fn_extrahop.lib.rx_client import validate_settings
from fn_extrahop.lib.templates_common import make_payload_from_template

PACKAGE_NAME = "fn_extrahop"
ENTITY_ID = "id"
SOAR_ENTITY_ID_FIELD = "extrahop_detection_id"
ENTITY_COMMENT_HEADER = "Created by ExtraHop"
ENTITY_LABEL = "Detection"
LOG = logging.getLogger(__name__)

# Default Templates
CREATE_INCIDENT_TEMPLATE = os.path.join(get_template_dir(), "soar_create_incident.jinja")
UPDATE_INCIDENT_TEMPLATE = os.path.join(get_template_dir(), "soar_update_incident.jinja")
CLOSE_INCIDENT_TEMPLATE = os.path.join(get_template_dir(), "soar_close_incident.jinja")

def init_app(opts, options):
    """ Intialize settings used for your app

    Args:
        opts (dict): app.config settings for the integration
        options (dict): app.config settings for the app

    Returns:
        obj: class to app class for ongoing API calls
    """
    # Initialize the class for making API calls to your endpoint
    endpoint_class = AppCommon(opts, options)

    return endpoint_class

def get_entities(app_common, last_poller_time):
    """Method call to query the endpoint solution for newly created or modified entities for
        synchronization with IBM SOAR

    Args:
        app_common ([obj]): [class for app API calls]
        last_poller_time ([int]): [timestamp in milliseconds to collect the changed entities (alerts, cases, etc.)]

    Returns:
        [list]: [list of entities to synchronize with SOAR]
    """
    entity_list = []

    # Enter the code needed to perform a query to the endpoint platform, using the last_poller_time to
    # identify entities changed since that timestamp.
    # Use options to collect urls, api_keys, etc. needed for the API call.
    # use rc.execute() to call your endpoint with your query to return entities changes since the last_poller_time
    entity_list = app_common.get_entities_since_ts(last_poller_time)

    return entity_list


def get_entity_id(entity):
    """Get the id for the entity returned in your query

    Args:
        entity ([dict]): [data structure of an entity]

    Returns:
        entity_id (str/int): [entity_id to use]
    """
    return entity.get(ENTITY_ID)

def is_entity_closed(entity):
    """Determine if your entity is in a closed state

    Args:
        entity ([dict]): [data structure of an entity]

    Returns
        ([bool]): [true/false if entity is closed]
    """
    return bool(entity.get("status", False))

class PollerComponent(ResilientComponent):
    """
    Poller for escalating SOAR incidents and synchronizing changes
    """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(PollerComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

        # Validate required fields in app.config are set
        # change this validation to include all the fields required in the app.config file
        validate_settings(self.options)

        # collect settings necessary and initialize libraries used by the poller
        if not self._init_env(opts, self.options):
            LOG.info("Poller interval is not configured.  Automated escalation is disabled.")
            return

        poller_thread = Thread(target=self.run)
        poller_thread.daemon = True
        poller_thread.start()

    def _init_env(self, opts, options):
        """Initialize the environment based on app.config settings

        Args:
            opts ([dict]): [all settings including SOAR settings]
            options ([dict]): [settings specific to datasource]

        Returns:
            [bool]: [True if poller is configured]
        """
        self.polling_interval = float(options.get("polling_interval", 0))
        if not self.polling_interval:
            return False

        LOG.info("Poller initiated, polling interval %s", self.polling_interval)
        self.last_poller_time = get_last_poller_date(int(options.get('polling_lookback', 0)))
        LOG.info("Poller lookback: %s", self.last_poller_time)

        # collect the override templates to use when creating, updating and closing cases
        self.soar_create_case_template = options.get("soar_create_case_template")
        self.soar_update_case_template = options.get("soar_update_case_template")
        self.soar_close_case_template = options.get("soar_close_case_template")

        # rest_client is used to make IBM SOAR API calls
        self.rest_client = get_client(opts)
        self.soar_common = SOARCommon(self.rest_client)
        self.app_common = init_app(opts, options)

        return True

    @poller('polling_interval', 'last_poller_time', PACKAGE_NAME)
    def run(self, *args, **kwargs):
        """Process to query for changes in datasource entities and the cooresponding update SOAR case
           The steps taken are to
           1) query SOAR for all open entities associated with the datasource
           2) query datasource entities for changes based on these incidents
           3) determine SOAR actions to take: create, update case or close

        Args:
            last_poller_time ([int]): [time in milliseconds when the last poller ran]
        """

        # get the list of entities (alerts, cases, etc.) to insert, update or close as cases in IBM SOAR
        entity_list = get_entities(self.app_common, kwargs['last_poller_time'])

        # iterate over all the entities.
        self.process_entity_list(entity_list)

    def process_entity_list(self, entity_list):
        """Perform all the processing on the entity list, creating, updating and closing SOAR
           cases based on the states of the endpoint entities.

           The logic is to determine if a SOAR case needs to be created, updated or closed, and
            apply the correct template file to apply the field changes.

        Args:
            entity_list (list): list of endpoint entities to check again SOAR cases
        """
        try:
            cases_insert = cases_closed = cases_updated = 0
            for entity in entity_list:
                entity_id = get_entity_id(entity)

                # create linkback url
                entity['detection_url'] = self.app_common.make_linkback_url(entity_id)

                # determine if this is an existing SOAR case
                soar_case, _error_msg = self.soar_common.get_soar_case({ SOAR_ENTITY_ID_FIELD: entity_id }, open_cases=False)

                # if case does not exist, create a new one
                if not soar_case:
                    # create the SOAR case
                    soar_create_payload = make_payload_from_template(
                                                        self.soar_create_case_template,
                                                        CREATE_INCIDENT_TEMPLATE,
                                                        entity
                                                    )
                    create_soar_case = self.soar_common.create_soar_case(
                                                        soar_create_payload
                                                    )

                    soar_case_id = create_soar_case['id'] # get newly created case_id

                    cases_insert += 1
                    LOG.info("Created SOAR case %s from %s %s", create_soar_case['id'], ENTITY_LABEL, entity_id)
                else:
                    soar_case_id = soar_case['id']

                    if is_entity_closed(entity):
                        if soar_case['plan_status'] == "A":
                            # close the SOAR case
                            soar_close_payload = make_payload_from_template(
                                                            self.soar_close_case_template,
                                                            CLOSE_INCIDENT_TEMPLATE,
                                                            entity
                                                        )
                            _close_soar_case = self.soar_common.update_soar_case(
                                                            soar_case_id,
                                                            soar_close_payload
                                                        )

                            cases_closed += 1
                            LOG.info("Closed SOAR case %s from %s %s", soar_case_id, ENTITY_LABEL, entity_id)
                    else:
                        # perform an update operation on the existing SOAR case
                        #soar_update_payload = make_payload_from_template(
                        #                                self.soar_update_case_template,
                        #                                UPDATE_INCIDENT_TEMPLATE,
                        #                                soar_case
                        #                            )
                        # Update description, tags, priority, assignee, stage, important
                        #_update_soar_case = self.soar_common.update_soar_case(
                        #                                soar_case,
                        #                                soar_update_payload
                        #                            )

                        cases_updated += 1
                        LOG.info("Updated SOAR case %s from %s %s", soar_case_id, ENTITY_LABEL, entity_id)
            LOG.info("IBM SOAR cases created: %s, cases closed: %s, cases updated: %s",
                     cases_insert, cases_closed, cases_updated)
        except Exception as err:
            LOG.error("%s poller run failed: %s", PACKAGE_NAME, str(err))
