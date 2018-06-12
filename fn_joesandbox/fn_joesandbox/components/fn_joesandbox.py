# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import os
import jbxapi
import time
import base64
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_joesandbox"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_joesandbox", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_joesandbox", {})

    @function("fn_joesandbox")
    def _fn_joesandbox_function(self, event, *args, **kwargs):
        """Function: An integration with JoeSandbox"""
        try:
            # Check required inputs are defined
            incident_id = kwargs.get("joesandbox_incident_id")  # number (required)
            if not incident_id:
              raise ValueError('incident_id is required')

            attachment_id = kwargs.get("joesandbox_attachment_id")  # number (required)
            if not attachment_id:
              raise ValueError("attachment_id is required")

            log = logging.getLogger(__name__)
            log.info("joesandbox_incident_id: %s", incident_id)
            log.info("joesandbox_attachment_id: %s", attachment_id)

            # TOD:: Add as input
            ANALYSIS_INFO_FETCH_SECONDS = 30

            # Get Joe Sandbox API Key from appconfig file
            API_KEY= self.options.get("fn_joesandbox_api_key")

            # Set to True if you agree to the Terms and Conditions.
            ACCEPT_TAC = True

            ANALYSIS_URL = self.options.get("fn_joesandbox_analysis_url")

            joesandbox = jbxapi.JoeSandbox(apikey=API_KEY,accept_tac=ACCEPT_TAC)

            # Get attachment contents from Resilient
            metadata_uri = "/incidents/{}/attachments/{}".format(incident_id, attachment_id)
            data_uri = "/incidents/{}/attachments/{}/contents".format(incident_id, attachment_id)

            client = self.rest_client()
            metadata = client.get(metadata_uri)
            data = client.get_content(data_uri)

            # Path for temporary file
            TEMP_FILE = "./{}".format(metadata["name"])
            print TEMP_FILE

            # Write temp file
            with open(TEMP_FILE, "wb") as out_file:
                out_file.write(data)
            yield StatusMessage("Attachment {} downloaded from incident {}".format(attachment_id, incident_id))

            # Open temp file and submit to joe
            with open(TEMP_FILE, "rb") as f:
                yield StatusMessage("Submitting attachment {} to Joe Sandbox".format(attachment_id))
                
                try:
                  submit_sample_response = joesandbox.submit_sample(f)
                  pass

                except Exception:
                  raise FunctionError("Failed to submit to Joe Sandbox")

            webid = submit_sample_response["webids"][0]
            # webid = "588962"

            sample_info = joesandbox.info(webid)
            # sample_info = {"status": "submitted"}
            
            yield StatusMessage("Sample {} being analyized by Joe Sandbox".format(webid))

            while sample_info["status"].lower() != "finished":
              yield StatusMessage("Analysis Status: {0}. Fetch every {1} seconds".format(sample_info["status"], ANALYSIS_INFO_FETCH_SECONDS))
              time.sleep(ANALYSIS_INFO_FETCH_SECONDS)
              sample_info = joesandbox.info(webid)

            yield StatusMessage("Analysis Status: {0}".format(sample_info["status"]))

            TEMP_FILE_REPORT_PDF = "PDF Analysis[{0}]:{1}.pdf".format(webid, metadata["name"])
            TEMP_FILE_REPORT_IOC = "IOC Analysis[{0}]:{1}.ioc".format(webid, metadata["name"])
            
            with open(TEMP_FILE_REPORT_PDF, "wb") as f:
                try:
                  joesandbox.download(webid, "pdf", file=f)
                except Exception:
                  raise FunctionError("Failed to get analysis report from Joe Sandbox")

            attachment_pdf_report = client.post_attachment('/incidents/{}/attachments'.format(incident_id), TEMP_FILE_REPORT_PDF, mimetype="application/pdf")

            with open(TEMP_FILE_REPORT_IOC, "wb") as f:
                try:
                  joesandbox.download(webid, "openioc", file=f)
                except Exception:
                  raise FunctionError("Failed to get IOC report from Joe Sandbox")

            artifact_ioc_report = client.post_attachment('/incidents/{}/attachments'.format(incident_id), TEMP_FILE_REPORT_IOC, mimetype="application/pdf")

            results = {
                "report_pdf_attachment_id": attachment_pdf_report["id"],
                "report_ioc_attachment_id": artifact_ioc_report["id"],
                "report_url": "{0}/{1}".format(ANALYSIS_URL, webid)
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception:
            yield FunctionError()

        finally:
          try:
            os.remove(TEMP_FILE)
            os.remove(TEMP_FILE_REPORT_PDF)
            os.remove(TEMP_FILE_REPORT_IOC)

          except OSError:
              pass