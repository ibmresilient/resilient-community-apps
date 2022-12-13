# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import os
import jbxapi
import time
import tempfile
import re
from urllib.parse import urlparse
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import str_to_bool, validate_fields

REQUESTS_VERIFY_ENV_VAR = "REQUESTS_CA_BUNDLE"

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'fn_joe_sandbox_analysis"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_joe_sandbox_analysis", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_joe_sandbox_analysis", {})

    @function("fn_joe_sandbox_analysis")
    def _fn_joe_sandbox_analysis_function(self, event, *args, **kwargs):
        """Function: A function that allows an Attachment or Artifact (File/URL) to be analyzed by Joe Sandbox"""

        # Get the workflow_instance_id so we can raise an error if the workflow was terminated by the user
        workflow_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

        # List to store paths of created temp files
        TEMP_FILES = []

        # Dict to reference related mimetype
        MIMETYPES = {"pdf": "application/pdf",
                     "json": "application/json",
                     "html": "text/html"}

        def get_workflow_status(workflow_instance_id, res_client):
            """Function to get the status of the current running workflow"""
            res = res_client.get(f"/workflow_instances/{workflow_instance_id}")
            return res["status"]

        def remove_temp_files(files):
            for f in files:
                os.remove(f)

        def get_input_entity(client, incident_id, attachment_id, artifact_id):

            re_uri_match_pattern = r"""(?:(?:https?|ftp):\/\/|\b(?:[a-z\d]+\.))(?:(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))?\))+(?:\((?:[^\s()<>]+|(?:\(?:[^\s()<>]+\)))?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))?"""
            entity = {"incident_id": incident_id, "id": None,
                      "type": "", "meta_data": None, "data": None}

            if (attachment_id):
                entity["id"] = attachment_id
                entity["type"] = "attachment"
                entity["meta_data"] = client.get(f"/incidents/{entity['incident_id']}/attachments/{entity['id']}")
                entity["data"] = client.get_content(f"/incidents/{entity['incident_id']}/attachments/{entity['id']}/contents")

            elif (artifact_id):
                entity["id"] = artifact_id
                entity["type"] = "artifact"
                entity["meta_data"] = client.get(f"/incidents/{entity['incident_id']}/artifacts/{entity['id']}")

                # handle if artifact has attachment
                if (entity["meta_data"]["attachment"]):
                    entity["data"] = client.get_content(f"/incidents/{entity['incident_id']}/artifacts/{entity['id']}/contents")

                # else handle if artifact.value contains an URI using RegEx
                else:
                    match = re.match(re_uri_match_pattern,entity["meta_data"]["value"])

                    if (match):
                        entity["uri"] = match.group()
                    else:
                        raise FunctionError("Artifact has no attachment or supported URI")

            else:
                raise ValueError('attachment_id AND artifact_id both None')

            return entity

        def submit_sample(entity):
            # id of the sample that gets returned from Joe Sandbox
            sample_webid = None

            # Handle if entity is an attachment or an artifact (with an attachmet)
            if (entity["type"] == "attachment" or (entity["type"] == "artifact" and entity["data"] != None)):

                # Generate attachment name
                sample_name = None

                if(entity["type"] == "attachment"):
                    sample_name = "[{0}_{1}] - {2}".format(
                        entity["meta_data"]["inc_id"], entity["meta_data"]["id"], entity["meta_data"]["name"])

                else:
                    sample_name = "[{0}_{1}] - {2}".format(
                        entity["meta_data"]["inc_id"], entity["meta_data"]["id"], entity["meta_data"]["attachment"]["name"])

                # Write to temp file
                path = write_temp_file(entity["data"], sample_name)

                # Submit to Joe Sandbox
                sample_webid = submit_file(joesandbox, path)

            # Else if the artifact.value contains a url
            elif (entity["type"] == "artifact" and entity["uri"] != None):
                sample_webid = submit_uri(joesandbox, entity["uri"])

            return sample_webid

        def fetch_report(joesandbox, sample_webid, ping_delay):
            time.sleep(ping_delay)
            return get_sample_info(joesandbox, sample_webid)

        def generate_report_name(entity, jsb_report_type, sample_webid):
            report_name = None

            if (entity["type"] == "attachment"):
                report_name = "js-report: {0}.{1}".format(
                    entity["meta_data"]["name"], jsb_report_type)

            elif (entity["type"] == "artifact" and entity["data"] != None):
                report_name = "js-report: {0}.{1}".format(
                    entity["meta_data"]["attachment"]["name"], jsb_report_type)

            elif (entity["type"] == "artifact" and entity["uri"] != None):
                parsed_uri = urlparse(entity["uri"])
                if(parsed_uri.hostname):
                    report_name = "js-report: {0}.{1}".format(
                        parsed_uri.hostname, jsb_report_type)
                else:
                    report_name = "js-report: URL Analysis: {0}.{1}".format(
                        sample_webid, jsb_report_type)

            return report_name

        def write_temp_file(data, name=None):
            path = None

            if (name):
                path = "{0}/{1}".format(tempfile.gettempdir(), name)

            else:
                tf = tempfile.mkstemp()
                path = tf[1]

            fo = open(path, 'wb')
            TEMP_FILES.append(path)
            fo.write(data)
            fo.close()
            return path

        def submit_file(joesandbox, path):
            f = open(path, "rb")
            sample_response = joesandbox.submit_sample(f)
            f.close()
            return sample_response["webids"][0]

        def submit_uri(joesandbox, uri):
            sample_response = joesandbox.submit_sample_url(uri)
            return sample_response["webids"][0]

        def get_sample_info(joesandbox, sample_webid):
            return joesandbox.info(sample_webid)

        def should_timeout(ping_timeout, start_time):
            returnValue = (time.time() - start_time) > ping_timeout
            return returnValue

        ##############################
        ###### END HELPER FUNCS ######
        ##############################


        try:
            # Get Joe Sandbox options from app.config file
            API_KEY = self.options.get("jsb_api_key")
            ACCEPT_TAC = str_to_bool(self.options.get("jsb_accept_tac"))
            ANALYSIS_URL = self.options.get("jsb_analysis_url")
            ANALYSIS_REPORT_PING_DELAY = int(
                self.options.get("jsb_analysis_report_ping_delay"))
            ANALYSIS_REPORT_REQUEST_TIMEOUT = float(
                self.options.get("jsb_analysis_report_request_timeout"))

            # Get proxies from app.config
            proxies = {}
            HTTP_PROXY = self.options.get("jsb_http_proxy", None)
            if HTTP_PROXY:
                proxies["http"] = HTTP_PROXY
            HTTPS_PROXY = self.options.get("jsb_https_proxy", None)
            if HTTPS_PROXY:
                proxies["https"] = HTTPS_PROXY

            # Get verify setting from app.config
            verify_ssl = self.options.get("jsb_verify", False)
            if verify_ssl:
                verify_ssl = False if verify_ssl.lower() == "false" else (True if verify_ssl.lower() == "true" else verify_ssl)

            # Validate required input fields
            validate_fields(["incident_id", "jsb_report_type"], kwargs)

            # Define inputs
            incident_id = kwargs.get("incident_id")
            jsb_report_type = kwargs.get("jsb_report_type")["name"]

            # Get optional inputs, one of these must be defined
            attachment_id = kwargs.get("attachment_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number

            if not attachment_id and not artifact_id:
                raise ValueError("attachment_id or artifact_id is required")

            # Instansiate new Joe Sandbox object
            joesandbox = jbxapi.JoeSandbox(
                apikey=API_KEY, apiurl=ANALYSIS_URL, accept_tac=ACCEPT_TAC, proxies=proxies, verify_ssl=verify_ssl)

            # Instansiate new SOAR API object
            client = self.rest_client()

            # Get entity we are dealing with (either attachment or artifact)
            entity = get_input_entity(client, incident_id, attachment_id, artifact_id)

            # Submit the sample and get its related webid
            yield StatusMessage("Submitting sample to Joe Sandbox")
            sample_webid = submit_sample(entity)

            # get the status of the sample
            sample_status = get_sample_info(joesandbox, sample_webid)

            # Get current time in seconds
            start_time = time.time()

            # Generate report name
            report_name = generate_report_name(entity, jsb_report_type, sample_webid)

            yield StatusMessage("{} being analyzed by Joe Sandbox".format(report_name))

            # Keep requesting sample status until the analysis report is ready for download or ANALYSIS_REPORT_REQUEST_TIMEOUT in seconds has passed
            while (sample_status["status"].lower() != "finished"):

                # Check workflow status, if "terminated, raise error"
                workflow_status = get_workflow_status(
                    workflow_instance_id, client)

                if workflow_status == "terminated":
                    raise ValueError(
                        "Analysis report not fetched. Workflow was Terminated")

                if (should_timeout(ANALYSIS_REPORT_REQUEST_TIMEOUT, start_time)):
                    raise ValueError("Timed out trying to get Analysis Report after {0} seconds".format(
                        ANALYSIS_REPORT_REQUEST_TIMEOUT))

                yield StatusMessage("Analysis Status: {0}. Fetch every {1}s".format(sample_status["status"], ANALYSIS_REPORT_PING_DELAY))
                sample_status = fetch_report(
                    joesandbox, sample_webid, ANALYSIS_REPORT_PING_DELAY)

            yield StatusMessage("Analysis Finished. Getting report & attaching to this incident")
            download = joesandbox.download(sample_webid, jsb_report_type)

            # Write temp file of report
            path = write_temp_file(download[1], report_name)

            # POST report as attachment to incident
            jsb_analysis_report = client.post_attachment(
                '/incidents/{}/attachments'.format(incident_id), path, mimetype=MIMETYPES[jsb_report_type])

            yield StatusMessage("Upload of attachment complete")

            results = {
                "analysis_report_name": report_name,
                "analysis_report_id": jsb_analysis_report["id"],
                "analysis_report_url": "{0}/{1}".format(ANALYSIS_URL, sample_webid),
                "analysis_status": sample_status["runs"][0]["detection"]
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception:
            yield FunctionError()

        finally:
            remove_temp_files(TEMP_FILES)
