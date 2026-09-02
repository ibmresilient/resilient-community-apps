# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
# Generated with resilient-sdk v51.0.1.1.824
"""Poller implementation"""

from logging import getLogger
from os import path
from threading import Thread
from json import loads
from datetime import datetime, timezone
from fn_pagerduty.lib.pd_common import PDClient, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, is_this_a_selftest
from resilient_lib import (SOARCommon, get_last_poller_date, clean_html,
                           make_payload_from_template, poller, str_to_bool)
from fn_pagerduty.poller.configure_tab import init_PagerDuty_tab

LOG = getLogger(__name__)

# Directory of default templates
TEMPLATE_DIR = path.join(path.dirname(__file__), "data")

# Default Templates used to create/update/close SOAR cases.
#   Mostly they will be modified to include custom SOAR fields
CREATE_CASE_TEMPLATE = path.join(TEMPLATE_DIR, "soar_create_case.jinja")
UPDATE_CASE_TEMPLATE = path.join(TEMPLATE_DIR, "soar_update_case.jinja")
CLOSE_CASE_TEMPLATE = path.join(TEMPLATE_DIR, "soar_close_case.jinja")

def query_entities(pdClient, last_poller_time, poller_filters: str):
    """
    Method call to query the endpoint solution for newly created or 
    modified entities for synchronization with IBM SOAR


    :param last_poller_time: datetime object to collect the changed entities (alerts, cases, etc.)
    :type last_poller_time: datetime object
    :return: list of entities to synchronize with SOAR
    :rtype: list
    """
    PD_incidents = []
    poller_filters = loads("{"+poller_filters+"}")
    poller_filters["time_zone"] = "UTC"

    for incident in pdClient.PDsession().iter_all("incidents", params=poller_filters, page_size=50):
        # Compare the last updated time of the PagerDuty incident to the last poller time.
        if datetime.strptime(incident.get("updated_at"), '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc) > last_poller_time:
            PD_incidents.append(incident)
    return PD_incidents

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
        super(PollerComponent, self).__init__(opts, PACKAGE_NAME, required_app_configs=["api_token"])
        init_PagerDuty_tab() # Create PagerDuty Incident tab on SOAR.

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
        self.pdClient = PDClient(self.options)

        return True

    @poller("polling_interval", "last_poller_time")
    def run(self, *args, **kwargs):
        """
        Process to query for changes in PagerDuty incidents and the corresponding update SOAR case.
        The steps taken are:
           1) Query SOAR for all open incidents that have a value assigned to the pd_incident_id property.
           2) Query PagerDuty incidents for changes based on these incidents.
           3) Determine SOAR actions to take: create, update, or close a case.

        :param last_poller_time: Time in milliseconds when the last poller ran
        :type last_poller_time: int
        """
        self.last_poller_time = datetime.fromtimestamp(int(kwargs.get("last_poller_time") / 1000), timezone.utc)
        # Get a list of SOAR incidents that have a value assigned to field pd_incident_id.
        SOAR_incidents, _errors = self.soar_common.get_soar_cases({"pd_incident_id": True}, uri_filters="return_level=normal&handle_format=names")

        # Get the list of PagerDuty incidents to insert, update or close as cases in IBM SOAR.
        PD_incidents = query_entities(self.pdClient, self.last_poller_time, self.options.get("pd_poller_filters"))

        # List of PagerDuty incidents that need to be pulled from PagerDuty.
        # These are the PagerDuty incidents that are on SOAR, but where not returned by the query_entities call to PagerDuty.
        pd_incidents_to_get = []
        for soar_inc in SOAR_incidents:
            in_returned_pd_incidents = False
            SOAR_PD_incident_id = soar_inc.get("properties", {}).get("pd_incident_id")
            for pd_inc in PD_incidents:
                if SOAR_PD_incident_id == pd_inc.get("id"):
                    in_returned_pd_incidents = True
                    break
            if not in_returned_pd_incidents:
                pd_incidents_to_get.append(SOAR_PD_incident_id)

        # Get the PagerDuty incidents that where not returned by the query_entities call to PagerDuty.
        if pd_incidents_to_get:
            payload = {"incidents": [{"id": pd_id, "type": "incident_reference"} for pd_id in pd_incidents_to_get]}
            # Create an update put call to PagerDuty, but do not give anything to update. This will return the PagerDuty incident
            #  details of the incidents that were specified.
            PD_incidents.extend(self.pdClient.update_incidents(payload).get("incidents", []))

        if PD_incidents:
            # Iterate over all the PagerDuty incidents.
            self.process_query_list(PD_incidents, SOAR_incidents)

    def process_query_list(self, PD_incidents: list, SOAR_incidents: list):
        """
        Perform all the processing on the PagerDuty incident list, creating, updating and closing SOAR
        cases based on the states of the PagerDuty incident.

        The logic is to determine if a SOAR case needs to be created, updated or closed, and
        apply the correct template file to apply the field changes.

        :param PD_incidents (list): List of PagerDuty incidents to check against SOAR cases
        :param SOAR_incidents (list): List of SOAR incidents that have a value assigned to the pd_incident_id property
        """
        try:
            cases_insert = cases_closed = cases_updated = 0
            # Create a list of the PagerDuty incident IDs that have linked SOAR incident.
            soar_inc_pd_ids = [inc.get("properties", {}).get("pd_incident_id") for inc in SOAR_incidents]
            for pd_inc in PD_incidents: # Loop through PagerDuty incidents
                pd_inc_id = pd_inc.get("id") # Current PagerDuty incident ID
                # Determine if this is an existing SOAR case
                # If case does not exist, create a new one
                if pd_inc_id not in soar_inc_pd_ids:
                    # Create the SOAR case
                    soar_create_payload = make_payload_from_template(
                        self.soar_create_case_template,
                        CREATE_CASE_TEMPLATE,
                        pd_inc)
                    create_soar_case = self.soar_common.create_soar_case(
                        soar_create_payload)

                    soar_case_id = create_soar_case.get("id") # Get newly created case_id

                    cases_insert += 1
                    LOG.info("Created SOAR case %s from PagerDuty incident with ID %s", soar_case_id, pd_inc_id)
                else:
                    # Get the SOAR incident that is linked to the PagerDuty incident.
                    soar_inc = {} 
                    for inc in SOAR_incidents:
                        if inc.get("properties", {}).get("pd_incident_id") == pd_inc_id:
                            soar_inc = SOAR_incidents.pop(SOAR_incidents.index(inc))
                            del inc # Delete the inc variable
                            break

                    soar_case_id = soar_inc.get("id")
                    # Determine if the PagerDuty incident is closed.
                    if pd_inc.get("status") == "resolved" and soar_inc.get("plan_status", "C") == "A":
                        # Close the SOAR case
                        soar_close_payload = make_payload_from_template(
                            self.soar_close_case_template,
                            CLOSE_CASE_TEMPLATE,
                            pd_inc)
                        _close_soar_case = self.soar_common.update_soar_case(
                            soar_case_id,
                            soar_close_payload)

                        cases_closed += 1
                        LOG.info("Closed SOAR case %s from PagerDuty incident with ID %s", soar_case_id, pd_inc_id)
                    else:
                        # Perform an update operation on the existing SOAR case
                        # Check if the case was updated after the last time the poller ran.
                        if datetime.strptime(pd_inc.get("updated_at"), '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc) > self.last_poller_time:
                            # Create the update payload
                            soar_update_payload = make_payload_from_template(
                                self.soar_update_case_template,
                                UPDATE_CASE_TEMPLATE,
                                pd_inc)

                            # Loop through the soar_update_payload to make sure it has different values than the current SOAR incident.
                            payload_dif = False
                            for key in soar_update_payload:
                                if key == "properties":
                                    for prop in soar_update_payload.get(key, {}):
                                        if soar_update_payload.get(key, {}).get(prop) != soar_inc.get(key, {}).get(prop):
                                            payload_dif = True
                                            del prop
                                            break
                                elif soar_update_payload.get(key) != soar_inc.get(key):
                                    payload_dif = True
                                    break
                            del key

                            if payload_dif: # If the payload has different values than what is currently on the SOAR incident.
                                _update_soar_case = self.soar_common.update_soar_case(
                                    soar_case_id,
                                    soar_update_payload)

                                cases_updated += 1
                                LOG.info("Updated SOAR case %s from PagerDuty incident with ID %s", soar_case_id, pd_inc_id)

                    # When a note is added the PagerDuty updated_at time does not get changed, so we have to check every PagerDuty incident.
                    if str_to_bool(self.options.get("pd_sync_notes", False)): # If pd_sync_notes in the app.config is enabled
                        # Get notes that are on the PagerDuty incident but not on the SOAR incident
                        pd_inc_notes = [pd_note.get("content") for pd_note in self.pdClient.list_incident_notes(pd_inc_id).get("notes", [])]
                        soar_inc_notes = [clean_html(soar_inc_note.get("text")).replace("\nAdded From PagerDuty", "") for soar_inc_note in self.soar_common.get_case_comments(soar_case_id)]
                        notes_to_add = [n for n in pd_inc_notes if clean_html(n) not in soar_inc_notes]
                        if notes_to_add:
                            for note in notes_to_add:
                                # Add PagerDuty note to the SOAR incident
                                self.soar_common.create_case_comment(soar_case_id, f"{note}\nAdded From PagerDuty")

            LOG.info("IBM SOAR cases created: %s, cases closed: %s, cases updated: %s",
                     cases_insert, cases_closed, cases_updated)
        except Exception as err:
            LOG.error("%s poller run failed: %s", PACKAGE_NAME, str(err))
