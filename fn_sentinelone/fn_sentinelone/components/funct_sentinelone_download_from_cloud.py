# -*- coding: utf-8 -*-

"""AppFunction implementation"""
from io import BytesIO
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields, write_file_attachment
from fn_sentinelone.lib.resilient_common import ResilientCommon
from fn_sentinelone.lib.sentinelone_common import SentinelOneClient

PACKAGE_NAME = "fn_sentinelone"
FN_NAME = "sentinelone_download_from_cloud"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sentinelone_download_from_cloud'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Download a threat from SentinelOne.
        Inputs:
            -   fn_inputs.incident_id
            -   fn_inputs.sentinelone_threat_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        sentinelOne_client = SentinelOneClient(self.opts, self.options)
        incident_id = fn_inputs.incident_id
        threat_id = fn_inputs.sentinelone_threat_id

        # Call SentinelOne to get the threat download URL and download the threat file.
        download_results = sentinelOne_client.download_from_cloud(threat_id)

        threat_filename = download_results.get("threat_filename")
        datastream = download_results.get("datastream")
        download_url = download_results.get("download_url")

        attachment_name = u"SentinelOne--{0}".format(threat_filename)

        # Write the file as an attachment
        write_file_attachment(self.rest_client(), attachment_name, datastream, incident_id, None)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        results = { "status": "success",
                    "attachment_name": attachment_name,
                    "threat_filename": threat_filename,
                    "downloadUrl": download_url
                    }

        yield FunctionResult(results)

