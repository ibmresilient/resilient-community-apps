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

        # Call SentinelOne to get the threat download URL
        results = sentinelOne_client.download_from_cloud(threat_id)

        data = results.get("data")
        downloadUrl = data.get("downloadUrl")
        threat_filename = data.get("fileName")

        response = self.rc.execute("GET", downloadUrl, self.timeout, callback=report_callback)

        datastream = BytesIO(response.content)
        attachment_name = u"SentinelOne--{0}".format(threat_filename)

        # Write the file as an attachment
        write_file_attachment(self.rest_client(), attachment_name, datastream, incident_id, None)
        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        results = {"attachment_name": attachment_name,
                   "downloadUrl": downloadUrl}

        yield FunctionResult(results)

def report_callback(response):
    """
    callback to review status code, 200 - report ready, 404 - report not ready
    :param response:
    :return: response
    """
    if response.status_code in [200, 400, 404]:
        return response
    else:
        raise IntegrationError(response.content)