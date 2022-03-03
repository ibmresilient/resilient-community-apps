# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, clean_html
from fn_sentinelone.lib.constants import FROM_SENTINELONE_COMMENT_HDR, SENT_TO_SENTINELONE_HDR
from fn_sentinelone.lib.sentinelone_common import SentinelOneClient

PACKAGE_NAME = "fn_sentinelone"
FN_NAME = "sentinelone_send_soar_note_to_sentinelone"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sentinelone_send_soar_note_to_sentinelone'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Send a note created in SOAR to corresponding SentinelOne threat.
        Inputs:
            -   fn_inputs.sentinelone_note_text
            -   fn_inputs.sentinelone_threat_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))
        note_text = fn_inputs.sentinelone_note_text
        threat_id = fn_inputs.sentinelone_threat_id

        reason = None
        success = False
        if FROM_SENTINELONE_COMMENT_HDR in note_text or SENT_TO_SENTINELONE_HDR in note_text:
            yield self.status_message("Bypassing synchronization of note: {}".format(note_text))
            success = True
        else:
            try:
                sentinelone_api = SentinelOneClient(self.opts, self.options)
                response = sentinelone_api.add_threat_note(threat_id, clean_html(note_text))

                data = response.get("data")
                affected = int(data.get("affected"))
                if affected >= 1:
                    success = True
                    yield self.status_message("Sentinel comment added to threatId: {}"\
                                    .format(threat_id))
                else:
                    errors = response.get("errors")
                    reason = errors.get("type")
                    yield self.status_message("Sentinel comment failure for threatId {}: {}"\
                                    .format(threat_id, reason))
            except IntegrationError as err:
                reason = str(err)

        results = {"success": success,
                   "reason:": reason}

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
