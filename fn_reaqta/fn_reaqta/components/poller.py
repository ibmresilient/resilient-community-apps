# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Function implementation"""

import datetime
import logging
import os
from threading import Thread
from resilient_circuits import ResilientComponent
from resilient_lib import validate_fields, RequestsCommon, make_payload_from_template
from resilient import get_client
from fn_reaqta.lib.poller_common import SOARCommon, poller, get_template_dir
from fn_reaqta.lib.app_common import AppCommon, PACKAGE_NAME, get_hive_options
from fn_reaqta.lib.configure_tab import init_reaqta_tab


ENTITY_ID = "id"  # name of field in the endpoint entity (alert, case, etc) with the ID value
SOAR_ENTITY_ID_FIELD = "reaqta_id" # name of custom IBM SOAR case field to retain the endpoint entity_id
ENTITY_COMMENT_HEADER = "Created by ReaQta" # header used to identify comments create by the endpoint entity

ENTITY_LABEL = "alert" # name to label the case, alert, event, etc. native to your endpoint solution
LOG = logging.getLogger(__name__)

# Default Templates
CREATE_INCIDENT_TEMPLATE = os.path.join(get_template_dir(), "soar_create_incident.jinja")
CLOSE_INCIDENT_TEMPLATE = os.path.join(get_template_dir(), "soar_close_incident.jinja")

def init_app(rc, options):
    """ intialize settings used for your app

    Args:
        rc (obj): RequestsCommon class for making API calls
        options (dict): app.config settings for the app

    Returns:
        obj: class to app class for ongoing API calls
    """
    # initialize the class for making API calls to your endpoint
    endpoint_class = AppCommon(rc, options)

    # create the tab for ReaQta custom fields and datatables
    init_reaqta_tab()

    return endpoint_class

def get_entities(app_common, query_field_name, last_poller_time, refresh_authentication=False):
    """[method call to query the endpoint solution for newly created or modified entities for
        synchronization with IBM SOAR]

    Args:
        app_common ([obj]): [class for app API calls]
        last_poller_time ([int]): [timestamp in milliseconds to collect the changed entities (alerts, cases, etc.)]
        refresh_authentication (bool): True if need to reauthenticate
    Returns:
        [list]: [list of entities to synchronize with SOAR]
        [str]: [error message or None]
    """

    # enter the code needed to perform a query to the endpoint platform, using the last_poller_time to
    # identify entities changed since that timestamp.
    # use options to collect urls, api_keys, etc. needed for the API call.
    # use rc.execute() to call your endpoint with your query to return entities changes since the last_poller_time
    return app_common.get_entities_since_ts(query_field_name,
                                            last_poller_time,
                                            app_common.get_filters(),
                                            refresh_authentication=refresh_authentication)


def get_entity_id(entity):
    """[get the id for the entity returned in your query]

    Args:
        entity ([dict]): [data structure of an entity]

    Returns:
        entity_id (str/int): [entity_id to use]
    """
    return entity.get(ENTITY_ID)

def is_entity_closed(entity):
    """[determine if your entity is in a closed state]

    Args:
        entity ([dict]): [data structure of an entity]

    Returns
        ([bool]): [true/false if entity is closed]
    """
    return bool(entity.get("closed", False))

class PollerComponent(ResilientComponent):
    """
    poller for escalating SOAR incidents and synchronizing changes
    """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(PollerComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

        # Validate required fields in app.config are set
        validate_fields([
                            "polling_interval",
                            "polling_lookback",
                        ],
                        self.options)

        # collect settings necessary and initialize libraries used by the poller
        if not self._init_env(opts, self.options):
            LOG.info(u"Poller interval is not configured.  Automated escalation is disabled.")
            return

        poller_thread = Thread(target=self.run)
        poller_thread.daemon = True
        poller_thread.start()

    def _init_env(self, opts, options):
        """[initialize the environment based on app.config settings]

        Args:
            opts ([dict]): [all settings including SOAR settings]
            options ([dict]): [settings specific to datasource]

        Returns:
            [bool]: [True if poller is configured]
        """
        self.polling_interval = float(options.get("polling_interval", 0))
        if not self.polling_interval:
            return False

        LOG.info(u"Poller initiated, polling interval %s", self.polling_interval)
        self.last_poller_time = self._get_last_poller_date(int(options.get('polling_lookback', 0)))
        LOG.info("Poller lookback: %s", self.last_poller_time)

        # collect the override templates to use when creating, updating and closing cases
        self.soar_create_case_template = options.get("soar_create_case_template")
        self.soar_close_case_template = options.get("soar_close_case_template")

        # rest_client is used to make IBM SOAR API calls
        self.rest_client = get_client(opts)
        self.rc = RequestsCommon(opts, options)
        self.soar_common = SOARCommon(self.rest_client)

        # initialize the hives
        self.hives_list = {}
        for hive in [hive_name.strip() for hive_name in options.get('polling_hives', "").split(",")]:
            hive_settings = get_hive_options(hive, opts)
            if hive_settings:
                self.hives_list[hive] = init_app(self.rc, hive_settings)

        return True

    @poller('polling_interval', 'last_poller_time', PACKAGE_NAME)
    def run(self, *args, **kwargs):
        """[Process to query for changes in datasource entities and the cooresponding update SOAR case]
           The steps taken are to
           1) query SOAR for all open entities associated with the datasource
           2) query datasource entities for changes based on these incidents
           3) determine SOAR actions to take: create, update case or close

        Args:
            last_poller_time ([int]): [time in milliseconds when the last poller ran]
        """

        for hive_label, app_common in self.hives_list.items():
            refresh_authentication = True # first time reauthenicate
            try:
                LOG.info("%s Polling hive: %s", PACKAGE_NAME, hive_label)
                # query for both new and closed alerts
                for query_field_name in ["receivedAfter", "closedAfter"]:
                    # get the list of entities (alerts, cases, etc.) to insert, update or close as cases in IBM SOAR
                    entity_list, err_msg = get_entities(app_common,
                                                        query_field_name,
                                                        kwargs['last_poller_time'],
                                                        refresh_authentication=refresh_authentication)

                    if err_msg:
                        LOG.error("Failure in get_entities for hive: %s. %s", hive_label, err_msg)
                        break

                    refresh_authentication = False # multiple times through don't need to reauthenticate

                    # iterate over all the entities. Some apps have paged results
                    while True:
                        self.process_entity_list(entity_list.get('result', []), hive_label, app_common)
                        if not entity_list.get('nextPage') or not entity_list.get('remainingItems'):
                            break

                        entity_list = app_common.get_next_page(entity_list['nextPage'])
            except Exception as err:
                LOG.error("Failure in poller for hive: %s. %s", hive_label, str(err))

    def process_entity_list(self, entity_list, hive_label, app_common):
        """Perform all the processing on the entity list, creating, updating and closing SOAR
           cases based on the states of the endpoint entities

        Args:
            hive_label: (str): name of hive to include when creating a new case
            entity_list (list): list of endpoint entities to check again SOAR cases
            app_common (class object): functions used for communication with the specific hive
        """
        try:
            alerts_processed = cases_insert = cases_closed = 0
            LOG.debug(entity_list)
            for entity in entity_list:
                entity_id = get_entity_id(entity)

                # create linkback url
                entity['alert_url'] = app_common.make_linkback_url(entity_id)
                entity['hive_label'] = hive_label

                # determine if this is an existing SOAR case
                soar_case, error_msg = self.soar_common.get_soar_case({ SOAR_ENTITY_ID_FIELD: entity_id }, open_cases=False)
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
                        # reaQta doesn't have a capability to collect updated fields. So update logic is unused.
                        pass

                alerts_processed += 1

            LOG.info("Alerts processed: %s, IBM SOAR cases created: %s, cases closed: %s",
                     alerts_processed,
                     cases_insert,
                     cases_closed)
        except Exception as err:
            LOG.error("%s poller run failed: %s", PACKAGE_NAME, str(err))


    def _get_last_poller_date(self, polling_lookback):
        """get the last poller datetime based on a lookback value
        Args:
            polling_lookback ([number]): # of minutes to lookback
        Returns:
            [datetime]: [datetime to use for last poller run time]
        """
        return self._get_timestamp() - datetime.timedelta(minutes=polling_lookback)

    def _get_timestamp(self):
        """get the existing timestamp

        Returns:
            datetime: current datetime
        """
        return datetime.datetime.now()
