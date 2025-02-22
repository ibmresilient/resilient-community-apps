# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, clean_html
from fn_sentinelone.lib.app_common import (AppCommon, PACKAGE_NAME, SOAR_HEADER)

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

        try:
            app_common = AppCommon(self.rc, PACKAGE_NAME, self.options)
            response = app_common.add_threat_note(threat_id, 
                                                  clean_html(note_text), 
                                                  SOAR_HEADER)

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
