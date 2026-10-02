# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v51.0.2.2.1096
"""Poller implementation"""

import logging
import time
import traceback

from bs4 import BeautifulSoup
from threading import Thread

from resilient_circuits import AppFunctionComponent, is_this_a_selftest
from resilient_lib import get_last_poller_date, poller, soar_datetimeformat

from fn_teams.lib.microsoft_messages import MessageClient
from fn_teams.lib.microsoft_authentication import  MicrosoftAuthentication
from fn_teams.lib.configure_tab import init_msteams_tab


PACKAGE_NAME = "fn_teams"
APPROVAL_CONFIG_DATA = "fn_teams_approval_process" # app.config section for poller settings

LOG = logging.getLogger(__name__)

APPROVAL_DATATABLE = "msteams_approval_process"
DATATABLE_ROW_URI = "/incidents/{inc_id}/table_data/{table_name}/row_data/{row_id}"

DATATABLE_ROW_ID = "id"
DATATABLE_SOAR_MESSAGE_ID = "soar_message_id"
DATATABLE_MESSAGE_ID = "message_id"
DATATABLE_STATUS = "status"
DATATABLE_STATUS_PENDING = "Pending"
DATATABLE_STATUS_APPROVED = "Approved"
DATATABLE_STATUS_EXPIRED = "Expired"
DATATABLE_STATUS_REJECTED = "Rejected"
DATATABLE_STATUS_INVALID = "Invalid"
DATATABLE_RESPONSE_DATE = "response_date"
DATATABLE_RESPONSE_COMMENTS = "response_comments"
DATATABLE_RESPONDER = "responder"
DATATABLE_EXPIRATION = "expiration"
DATATABLE_GROUP = "group"
DATATABLE_GROUP_ID = "group_id"
DATATABLE_CHANNEL = "channel"
DATATABLE_CHANNEL_ID = "channel_id"

EMPTY_LINE = "\\n"

def update_datatable_cell_value(cells, cell_name, cell_value):
    """change a datatable row cell value

    :param cells: definition of datatable row cells
    :type cells: dict
    :param cell_name: cell name to change
    :type cell_name: str
    :param cell_value: cell value to change
    :type cell_value: [str, int, bool]
    :return: cell definition which may or may not have changed
    :rtype: dict
    """
    new_cells = dict(cells)

    for _cell_id, cell in new_cells.items():
        if cell.get("id", {}).get("name") == cell_name:
            cell["value"] = cell_value

    return new_cells

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

        # collect settings necessary and initialize libraries used by the poller
        if not self._init_env(opts, self.options):
            LOG.info("Poller interval is not configured. Approval process is disabled.")
            return

        poller_thread = Thread(target=self.run)
        poller_thread.daemon = True
        poller_thread.start()

    def _init_poller(self, opts):
        """
        Initialize the app environment based on app.config settings

        :param opts: all settings including SOAR settings
        :type opts: dict
        :return: True if poller is configured
        :rtype: bool
        """
        approval_options = opts.get(APPROVAL_CONFIG_DATA, {})

        self.polling_interval = float(approval_options.get("polling_interval", 0))
        if not self.polling_interval or is_this_a_selftest(self):
            LOG.debug("Exiting poller because polling interval set to 0 or this run is a selftest.")
            return False

        LOG.info("Poller initiated, polling interval %s", self.polling_interval)

        # enable the tab
        init_msteams_tab()

        self.last_poller_time = get_last_poller_date(0)
        self.approval_words = [word.lower().strip() for word in approval_options.get("approval_words", "").split(",")]
        self.rejection_words = [word.lower().strip() for word in approval_options.get("rejection_words", "").split(",")]

        return True
    
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

        # rest_client is used to make IBM SOAR API calls
        self.rest_client = self.rest_client()
        self.message_client = MessageClient(self.rc)
        self.refresh_token = options.get("refresh_token")

        #return self._init_poller(opts) # not in v3.0
        return False

    @poller("polling_interval", "last_poller_time")
    def run(self, *args, **kwargs):
        """
        Process to query for changes in datasource entities and the corresponding update SOAR case.
        The steps taken are:
           1) query SOAR for all open cases with a Pending MS Teams approval request datatable row
           2) query MS Teams channel for changes looking for message approval replies
           3) Update the case with the approval status, if any

        Datatable rows which are incomplete or where the approval has expired will be change so
          polling will no longer occur

        :param last_poller_time: time in milliseconds when the last poller ran
        :type last_poller_time: int
        """

        # Get all the outstanding approvals in 'Pending' state
        dt_approval_requests = self.query_pending_approvals()

        if dt_approval_requests:
            # iterate over all the entities.
            self.process_approval_requests(dt_approval_requests.get("results", []))

    def process_approval_requests(self, dt_approval_requests):
        """
        Perform all the processing on the cases with Pending approvals, updating the approvals
          with updates made.

        :param dt_approval_requests: list of datatable rows in Pending state
        :type dt_approval_requests: list
        """

        # reauthenticate to MS
        authenticator = MicrosoftAuthentication(self.rc, self.options)
        dual_headers = {
            "application": authenticator.authenticate_application_permissions(),
            "delegated": authenticator.authenticate_delegated_permissions(self.refresh_token)
        }

        current_ts = int(time.time() * 1000) # used to determine if an approval has expired

        for dt_approval_request in dt_approval_requests:
            try:
                inc_id = dt_approval_request.get("inc_id")
                table_row_id = dt_approval_request.get("result", {}).get("id")
                table_row_cells = dt_approval_request.get("result", {}).get("cells", {})

                # organize the datatable cell information for internal methods
                poller_options = self.build_options(table_row_cells)

                # determine if the datatable data is complete to continue and has not expired
                failed_validation_status = self.is_valid(table_row_cells, current_ts)
                if failed_validation_status:
                    LOG.warning("Approval request validation criteria failed: %s for incident: %s table_row_id %s", failed_validation_status, inc_id, table_row_id)
                    poller_options[DATATABLE_STATUS] = failed_validation_status

                    self.refresh_datatable_row(inc_id, table_row_id, dt_approval_request["result"], poller_options)
                    continue

                # If we don't have the specific message_id, query the channel and read messages looking for
                #  our own uuid
                if not poller_options.get("message_id"):
                    internal_message_id = self.get_cell_value(table_row_cells, DATATABLE_SOAR_MESSAGE_ID)

                    poller_options["message_id"] = self.find_request_by_internal_message_id(poller_options,
                                                                                     dual_headers,
                                                                                     internal_message_id)

                # may have found the message_id from reading all content above
                # If we know the specific message_id, query for replies for that specific message
                if poller_options.get("message_id"):
                    # process message replies
                    self.process_message_replies(poller_options, dual_headers)

                # determine if there are any changes to the datatable
                self.refresh_datatable_row(inc_id, table_row_id, dt_approval_request["result"], poller_options)

            except Exception as err:
                LOG.error(traceback.format_exc())
                LOG.error("%s poller run failed for table_row %s: %s", PACKAGE_NAME, table_row_id, str(err))
                LOG.error(dt_approval_request)

    def build_options(self, table_row_cells):
        """track all the information we need for tracking approval status in one dictionary

        :param table_row_cells: datatable row with Pending approval
        :type table_row_cells: dict
        :return: dictionary with necessary information for process replies
        :rtype: dict
        """
        return {
            "message_id": self.get_cell_value(table_row_cells, DATATABLE_MESSAGE_ID),
            "channel_name": self.get_cell_value(table_row_cells, DATATABLE_CHANNEL),
            "channel_id": self.get_cell_value(table_row_cells, DATATABLE_CHANNEL_ID),
            "group_name": self.get_cell_value(table_row_cells, DATATABLE_GROUP),
            "group_id": self.get_cell_value(table_row_cells, DATATABLE_GROUP_ID)
        }

    def is_valid(self, table_row_cells, current_ts):
        """determine if datatable row if both valid and not expired

        :param table_row_cells: datatable approval row
        :type table_row_cells: dict
        :param current_ts: current timestamp
        :type current_ts: int
        :return: An error status of None if no error
        :rtype: str or None
        """
        # validate table entry
        if not self.is_datatable_valid(table_row_cells):
            return DATATABLE_STATUS_INVALID

        # confirm request has not expired
        if self.has_request_expired(table_row_cells, current_ts):
            return DATATABLE_STATUS_EXPIRED

        return None

    def find_request_by_internal_message_id(self, poller_options, dual_headers, internal_message_id):
        """Read channel messages looking for our internal UUID id

        :param poller_options: dictionary of MS Teams information to track
        :type poller_options: dict
        :param dual_headers: headers needed for MS Teams API calls
        :type dual_headers: dict
        :param internal_message_id: internal Id identifying our approval request
        :type internal_message_id: str
        :return: found MS Teams message_id
        :rtype: str
        """
        results = self.message_client.read_messages(dual_headers, poller_options)

        # find the message associated with our soar message id
        for msg in results:
            for card in msg.get("attachments", []):
                if internal_message_id in card.get("content", ""): # "content" is string-encoded json
                    return msg.get("id")

        return None

    def process_message_replies(self, poller_options, dual_headers):
        """read replies to our approval message, looking for keywords to our approval request

        :param poller_options: dictionary of MS Teams information to track
        :type poller_options: dict
        :param dual_headers: headers needed for MS Teams API calls
        :type dual_headers: dict
        :return: updated dictionary of MS Teams information to track
        :rtype: dict
        """
        results = self.message_client.read_messages(dual_headers, poller_options, replies=True)

        if results:
            for card in results.get("value", []):
                if card.get("body", {}).get("content"):
                    # replies with approval status
                    approved_status, comments = self.parse_replies_for_response(card)

                    if approved_status is not None:
                        poller_options["status"] = approved_status.capitalize()
                        poller_options["response_comments"] = " ".join(comments)
                        poller_options["responder"] = card.get("from", {}).get("user", {}).get("displayName")
                        # Use timestamp minus milliseconds: "2024-08-09T13:12:37.005Z"
                        poller_options["response_date"] = soar_datetimeformat(card.get("lastModifiedDateTime").split(".")[0])

        return poller_options

    def parse_replies_for_response(self, card):
        """parse reply messages for our keywords associated with an approval or rejection

        :param card: dictionary of an MS Teams message reply
        :type card: dict
        :return: tuple or approval/rejection and additional comments
        :rtype: str, list
        """
        bs = BeautifulSoup(card["body"]["content"], "html.parser")

        content = list(bs.stripped_strings)

        approved = None
        comments = []
        first_line = content[0].lower()
        if first_line in self.approval_words or first_line in self.rejection_words:
            approved = first_line
            comments =  [line for line in content[1:] if line != EMPTY_LINE]

        return approved, comments

    def refresh_datatable_row(self, inc_id, row_id, table_row, poller_options):
        """Update the cells for a datatable row with any changes associated with the approval request

        :param inc_id: incident id
        :type inc_id: int
        :param row_id: row id for the datatable
        :type row_id: int
        :param table_row: dictionary of a datatable row
        :type table_row: dict
        :param poller_options: dictionary of an MS Teams message reply information
        :type poller_options: dict
        :return: True/False if the datatable row was changed
        :rtype: bool
        """
        table_row_cells = table_row.get("cells", {})

        is_changed = False
        results = None
        for cell_change in [DATATABLE_STATUS,
                            DATATABLE_MESSAGE_ID,
                            DATATABLE_GROUP_ID, DATATABLE_CHANNEL_ID,
                            DATATABLE_RESPONDER, DATATABLE_RESPONSE_DATE,
                            DATATABLE_RESPONSE_COMMENTS]:
            if poller_options.get(cell_change) and poller_options.get(cell_change) != self.get_cell_value(table_row_cells, cell_change):
                update_datatable_cell_value(table_row_cells, cell_change, poller_options[cell_change])
                is_changed = True

        if is_changed:
            uri = DATATABLE_ROW_URI.format(inc_id=inc_id, table_name=APPROVAL_DATATABLE, row_id=row_id)
            LOG.debug(table_row)
            results = self.rest_client.put(uri=uri, payload=table_row)

        return results

    def query_pending_approvals(self):
        """Query open cases for and Pending approval requests

        :return: list of datatables with pending requests
        :rtype: list
        """
        query = {
            "org_id": self.rest_client.org_id,
            "query": DATATABLE_STATUS_PENDING,
            "filters": {
                "incident": [
                    {
                        "conditions": [
                            {
                                "field_name": "plan_status",
                                "method": "equals",
                                "value": "A"
                            }
                        ]
                    }
                ],
                APPROVAL_DATATABLE: [
                    {
                        "conditions": [
                            {
                                "field_name": "status",
                                "method": "equals",
                                "value": DATATABLE_STATUS_PENDING
                            }
                        ]
                    }
                ]
            },
            "types": [
                "datatable"
            ]
        }

        return self.rest_client.search(query)

    def has_request_expired(self, approval_request_row_data, current_ts):
        """determine if the approval request has expired

        :param approval_request_row_data: datatable row data
        :type approval_request_row_data: dict
        :param current_ts: timestamp to compare for expiration
        :type current_ts: int
        :return: True/False if request has expired
        :rtype: bool
        """
        if current_ts > self.get_cell_value(approval_request_row_data, DATATABLE_EXPIRATION, 0):
            return True

        return False

    def is_datatable_valid(self, approval_request_row_data):
        """Check for invalid datatable row data or approval request has expired

        :param approval_request_row_data: approval request row data
        :type approval_request_row_data: dict
        :return: True/False if row is valid
        :rtype: bool
        """
        if not (self.get_cell_value(approval_request_row_data, DATATABLE_SOAR_MESSAGE_ID) or self.get_cell_value(approval_request_row_data, DATATABLE_MESSAGE_ID)):
            return False

        if not (self.get_cell_value(approval_request_row_data, DATATABLE_GROUP) or self.get_cell_value(approval_request_row_data, DATATABLE_GROUP_ID)):
            return False

        if not self.get_cell_value(approval_request_row_data, DATATABLE_CHANNEL):
            return False

        return True

    def get_cell_value(self, cells, cell_name, default_value=None):
        """get cell data from an approval request datatable row

        :param cells: row cell data
        :type cells: dict
        :param cell_name: cell name to search for
        :type cell_name: str
        :param default_value: return default value if no data is found, defaults to None
        :type default_value: str/int/bool, optional
        :return: cell value if found
        :rtype: str/int/bool
        """
        for _cell_id, cell in cells.items():
            if cell.get("id", {}).get("name") == cell_name:
                return cell.get("value")

        return default_value
