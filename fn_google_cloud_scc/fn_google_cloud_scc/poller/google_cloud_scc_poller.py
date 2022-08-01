# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import logging
import os
from threading import Thread

from fn_google_cloud_scc.poller.configure_tab import init_scc_tab
from fn_google_cloud_scc.poller.soar_common import (SOARCommon,
                                                    get_last_poller_date,
                                                    get_template_dir, poller)
from fn_google_cloud_scc.util.scc_common import (DT_NAME, PACKAGE_NAME,
                                                 SOAR_ID_MARK, GoogleSCCCommon,
                                                 linkify)
from resilient import get_client
from resilient_circuits import AppFunctionComponent, is_this_a_selftest
from resilient_lib import (make_payload_from_template, str_to_bool,
                           validate_fields)

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

class PollerComponent(AppFunctionComponent):
    """
    poller for escalating SOAR incidents and synchronizing changes
    """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        required_fields = [
            "polling_interval",
            "polling_lookback"
        ]
        super(PollerComponent, self).__init__(opts, PACKAGE_NAME, required_app_configs=required_fields)

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
        if not self.polling_interval or is_this_a_selftest(self):
            return False

        LOG.info(u"Poller initiated, polling interval %s", self.polling_interval)
        self.last_poller_time = get_last_poller_date(int(options.get('polling_lookback', 0)))
        LOG.info("Poller lookback: %s", self.last_poller_time)

        # collect the override templates to use when creating, updating and closing cases
        self.soar_create_case_template = options.get("soar_create_case_template")
        self.soar_close_case_template = options.get("soar_close_case_template")
        self.soar_update_case_template = options.get("soar_update_case_template")

        # check whether or not to create the security mark with the SOAR ID when
        # findings are synced to SOAR
        self.add_mark_on_sync = str_to_bool(options.get("add_soar_id_as_security_mark", "False"))

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

        LOG.debug("Polling Google SCC")

        query_results = query_entities(self.app_common, kwargs['last_poller_time'])

        if query_results:
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
                    finding["notes"] = self.app_common.create_initial_note(finding)

                    # create the SOAR case
                    soar_create_payload = make_payload_from_template(
                        self.soar_create_case_template,
                        CREATE_INCIDENT_TEMPLATE,
                        finding
                    )

                    create_soar_case = self.soar_common.create_soar_case(
                        soar_create_payload
                    )


                    soar_case_id = create_soar_case.get("id") # get newly created case_id
                    _add_source_properties_dt(finding, soar_case_id, self.soar_common, DT_NAME)

                    if self.add_mark_on_sync:
                        LOG.debug("'add_soar_id_as_security_mark' is turned on -- adding mark { %s : %s} as a security mark to SCC",
                            SOAR_ID_MARK, soar_case_id)
                        self.app_common.update_security_mark(finding.get("name"), SOAR_ID_MARK, soar_case_id)
                    else:
                        LOG.debug("'add_soar_id_as_security_mark' is turned off -- not adding SOAR ID to security marks")

                    cases_insert += 1
                    LOG.info("Created SOAR case %s from %s %s", soar_case_id, ENTITY_LABEL, finding_id)

                    # check if inactive on SCC AND still active on SOAR; close if so
                    _, close_count = _close_case_if_finding_inactive(finding, create_soar_case, self.soar_common, self.soar_close_case_template)
                    cases_closed += close_count
                else:
                    soar_case_id = soar_case.get("id")

                    # check if inactive on SCC AND still active on SOAR; close if so
                    closed_case, close_count = _close_case_if_finding_inactive(finding, soar_case, self.soar_common, self.soar_close_case_template)
                    cases_closed += close_count

                    if not closed_case:
                        if not is_entity_closed(finding) and soar_case.get("plan_status", "A") != "A":
                            # the SOAR case is closed, but the finding was reopened
                            note = "Finding reopened in Google SCC. {0}".format(linkify(finding.get("finding_url"), "Finding link."))
                            self.soar_common.create_case_comment(soar_case_id, None, None, note)

                            LOG.info("Added comment to SOAR case %s from %s %s", 
                                soar_case_id, ENTITY_LABEL, finding_id)

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


def _close_case_if_finding_inactive(finding, soar_case, soar_common, close_tempate_path):
    """
    Helper method to close a case from the template if a given finding is inactive and the case is open
    in SOAR

    Returns the closed case and 1 if needed to be closed
    Returns None and 0 if didn't close
    """

    finding_id = finding.get("finding_id", "")
    soar_case_id = soar_case.get("id", "")
    case_status = soar_case.get("plan_status", "")

    if is_entity_closed(finding) and case_status == "A":
        # close the SOAR case
        soar_close_payload = make_payload_from_template(
            close_tempate_path,
            CLOSE_INCIDENT_TEMPLATE,
            finding
        )
        close_soar_case = soar_common.update_soar_case(
            soar_case_id,
            soar_close_payload
        )

        LOG.info("Closed SOAR case %s from %s %s", soar_case_id, ENTITY_LABEL, finding_id)

        return close_soar_case, 1
    return None, 0

def _add_source_properties_dt(finding, soar_case_id, soar_common, dt_name):
    """
    Helper method to add all source properties as rows to a datatable
    """
    LOG.debug("Adding source properties to datatable %s in incident %s", dt_name, soar_case_id)

    source_properties = finding.get("source_properties")

    for prop in source_properties:
        val = linkify(str(source_properties.get(prop, "UNKNOWN")))

        row_data = {
            "google_scc_source_property": prop,
            "google_scc_source_property_value": val
        }

        soar_common.create_datatable_row(soar_case_id, dt_name, row_data)
