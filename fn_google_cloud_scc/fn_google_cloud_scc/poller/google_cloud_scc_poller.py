# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

from curses import isendwin
import datetime
import logging
import os
import traceback
from threading import Thread

from fn_google_cloud_scc.poller.soar_common import (SOARCommon,
                                                    get_last_poller_date,
                                                    get_template_dir, poller)
from fn_google_cloud_scc.util.scc_common import PACKAGE_NAME, GoogleSCCCommon, linkify
from fn_google_cloud_scc.poller.configure_tab import init_scc_tab
from resilient import get_client
from resilient_circuits import ResilientComponent
from resilient_lib import (build_incident_url, build_resilient_url,
                           make_payload_from_template, validate_fields)

ENTITY_ID = "finding"  # name of field in the endpoint entity (alert, case, etc) with the ID value
ENTITY_CLOSE_FIELD = "state" # name of field in endpoint entity to reference the close state
SOAR_ENTITY_ID_FIELD = "google_scc_id" # name of custom IBM SOAR case field to retain the endpoint entity_id
ENTITY_LABEL = "finding" # label the name the case, alert, event, etc. native to your endpoint solution
ENTITY_COMMENT_HEADER = "Created by Google Cloud Security Command Center" # header used to identify comments create by the endpoint entity
ENTITY_UNCHANGED_STATE = "UNCHANGED"

LOG = logging.getLogger(__name__)

# Default Templates used to create/update/close SOAR cases.
#   Mostly they will be modified to include custom SOAR fields
CREATE_INCIDENT_TEMPLATE = os.path.join(get_template_dir(), "soar_create_incident.jinja")
UPDATE_INCIDENT_TEMPLATE = os.path.join(get_template_dir(), "soar_update_incident.jinja")
CLOSE_INCIDENT_TEMPLATE = os.path.join(get_template_dir(), "soar_close_incident.jinja")

def init_scc_app(options):
    """
    Intialize the app common code and create the tab in the platform if it doesn't already exist
    """
    app_common = GoogleSCCCommon(options)

    init_scc_tab()

    return app_common


def query_entities(app_common, last_poller_time):
    """[method call to query the endpoint solution for newly created or modified entities for
        synchronization with IBM SOAR]

    Args:
        app_common ([obj]): [class for app API calls]
        last_poller_time ([int]): [timestamp in milliseconds to collect the changed entities (alerts, cases, etc.)]

    Returns:
        [list]: [list of entities to synchronize with SOAR]
    """
    query_results = []

    # enter the code needed to perform a query to the endpoint platform, using the last_poller_time to
    # identify entities changed since that timestamp.
    # use *args and **kwargs to collect urls, api_keys, etc. needed for API call(s).
    #   query_entities_since_ts(last_poller_time, *args, **kwargs)
    query_results = app_common.query_entities_since_ts(last_poller_time)

    return query_results

def get_entity_id(finding):
    """[get the id for the entity returned in your query]

    Args:
        entity ([dict]): [data structure of an entity]

    Returns:
        entity_id (str/int): [entity_id to use]
    """
    return GoogleSCCCommon.get_finding_id(finding, ENTITY_ID)

def is_entity_closed(finding):
    """[determine if your entity is in a closed state]

    Args:
        entity ([dict]): [data structure of an entity]

    Returns
        ([bool]): [true/false if entity is closed]
    """
    return GoogleSCCCommon.is_finding_closed(finding, ENTITY_CLOSE_FIELD)

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
        self.last_poller_time = get_last_poller_date(int(options.get('polling_lookback', 0)))
        LOG.info("Poller lookback: %s", self.last_poller_time)

        # collect the override templates to use when creating, updating and closing cases
        self.soar_create_case_template = options.get("soar_create_case_template")
        self.soar_close_case_template = options.get("soar_close_case_template")
        self.soar_update_case_template = options.get("soar_update_case_template")

        self.soar_common = SOARCommon(get_client(opts))

        self.app_common = init_scc_app(options)

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

        LOG.info("polling!")

        query_results = query_entities(self.app_common, kwargs['last_poller_time'])

        self.process_entity_list(query_results)


    def process_entity_list(self, entity_list):
        """Perform all the processing on the entity list, creating, updating and closing SOAR
           cases based on the states of the endpoint entities

        Args:
            entity_list (list): list of endpoint entities to check again SOAR cases
        """
        try:
            cases_insert = cases_closed = cases_updated = 0
            for finding_result_obj in entity_list:
                finding = finding_result_obj.get(ENTITY_LABEL)

                finding_id = get_entity_id(finding)
                finding["finding_id"] = finding_id

                # determine if this is an existing SOAR case
                soar_case, _error_msg = self.soar_common.get_soar_case({ SOAR_ENTITY_ID_FIELD: finding_id }, open_cases=False)

                # if case does not exist, create a new one
                if not soar_case:

                    # create initial finding note
                    finding['notes'] = self.app_common.create_initial_note(finding)

                    # create the SOAR case
                    soar_create_payload = make_payload_from_template(
                        self.soar_create_case_template,
                        CREATE_INCIDENT_TEMPLATE,
                        finding
                    )

                    create_soar_case = self.soar_common.create_soar_case(
                        soar_create_payload
                    )

                    soar_case_id = create_soar_case['id'] # get newly created case_id

                    self.app_common.add_security_mark(finding, soar_case_id)

                    cases_insert += 1
                    LOG.info("Created SOAR case %s from %s %s", create_soar_case['id'], ENTITY_LABEL, finding_id)
                else:
                    soar_case_id = soar_case["id"]

                    if is_entity_closed(finding) and soar_case["plan_status"] == "A":
                        # close the SOAR case
                        soar_close_payload = make_payload_from_template(
                            self.soar_close_case_template,
                            CLOSE_INCIDENT_TEMPLATE,
                            finding
                        )
                        _close_soar_case = self.soar_common.update_soar_case(
                            soar_case_id,
                            soar_close_payload
                        )

                        cases_closed += 1
                        LOG.info("Closed SOAR case %s from %s %s", soar_case_id, ENTITY_LABEL, finding_id)

                    else:
                        if not is_entity_closed(finding) and soar_case["plan_status"] != "A":
                            # the SOAR case is closed, but the finding was reopened
                            note = "Finding reopened in Google SCC. {0}".format(linkify(finding["finding_url"], "Finding link."))
                            self.soar_common.create_case_comment(soar_case_id, None, None, note)

                            LOG.info("Added comment to SOAR case %s from %s %s", 
                                soar_case_id,
                                ENTITY_LABEL,
                                finding_id
                            )

                        # perform an update operation on the existing SOAR case
                        soar_update_payload = make_payload_from_template(
                            self.soar_update_case_template,
                            UPDATE_INCIDENT_TEMPLATE,
                            finding
                        )
                        # Update state, security marks, vulnerabilities, etc...
                        _update_soar_case = self.soar_common.update_soar_case(
                            soar_case_id,
                            soar_update_payload
                        )

                        cases_updated += 1
                        LOG.info("Updated SOAR case %s from %s %s", soar_case_id, ENTITY_LABEL, finding_id)

            LOG.info("IBM SOAR cases created: %s, cases closed: %s, cases updated: %s",
                        cases_insert, cases_closed, cases_updated)
        except Exception as err:
            LOG.error("%s poller run failed: %s", PACKAGE_NAME, str(err))
