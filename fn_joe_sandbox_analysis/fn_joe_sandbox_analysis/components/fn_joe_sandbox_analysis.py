# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import os
import jbxapi
import time
import tempfile
import re
from urlparse import urlparse
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_joe_sandbox_analysis"""

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
        
        # List to store paths of created temp files
        TEMP_FILES = []

        # Dict to reference related mimetype
        MIMETYPES = {"pdf": "application/pdf", "json": "application/json", "html": "text/html"}
        
        def remove_temp_files(files):
          for f in files:
            os.remove(f)

        def get_input_entity(client, incident_id, attachment_id, artifact_id):
          
          re_uri_match_pattern = r"""(?:(?:https?|ftp):\/\/|\b(?:[a-z\d]+\.))(?:(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))?\))+(?:\((?:[^\s()<>]+|(?:\(?:[^\s()<>]+\)))?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))?"""
          entity = {"incident_id": incident_id, "id": None, "type": "", "meta_data": None, "data": None}

          if (attachment_id):
            entity["id"] = attachment_id
            entity["type"] = "attachment"
            entity["meta_data"] = client.get("/incidents/{0}/attachments/{1}".format(entity["incident_id"], entity["id"]))
            entity["data"] = client.get_content("/incidents/{0}/attachments/{1}/contents".format(entity["incident_id"], entity["id"]))
          
          elif (artifact_id):
            entity["id"] = artifact_id
            entity["type"] = "artifact"
            entity["meta_data"] = client.get("/incidents/{0}/artifacts/{1}".format(entity["incident_id"], entity["id"]))

            # handle if artifact has attachment
            if (entity["meta_data"]["attachment"]):
              entity["data"] = client.get_content("/incidents/{0}/artifacts/{1}/contents".format(entity["incident_id"], entity["id"]))

            # else handle if artifact.value contains an URI using RegEx
            else:
              match = re.match(re_uri_match_pattern, entity["meta_data"]["value"])

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
              sample_name = "[{0}_{1}] - {2}".format(entity["meta_data"]["inc_id"], entity["meta_data"]["id"], entity["meta_data"]["name"])
            
            else:
              sample_name = "[{0}_{1}] - {2}".format(entity["meta_data"]["inc_id"], entity["meta_data"]["id"], entity["meta_data"]["attachment"]["name"])

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
            report_name = "js-report: {0}.{1}".format(entity["meta_data"]["name"], jsb_report_type)
          
          elif (entity["type"] == "artifact" and entity["data"] != None):
            report_name = "js-report: {0}.{1}".format(entity["meta_data"]["attachment"]["name"], jsb_report_type)
          
          elif (entity["type"] == "artifact" and entity["uri"] != None):
            parsed_uri = urlparse(entity["uri"])
            if(parsed_uri.hostname):
              report_name = "js-report: {0}.{1}".format(parsed_uri.hostname, jsb_report_type)
            else:
              report_name = "js-report: URL Analysis: {0}.{1}".format(sample_webid, jsb_report_type)
          
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
          returnValue = (time.time() - start_time) > float(ping_timeout)
          return returnValue

        try:
            # Get Joe Sandbox API Key, Accept TAC, Analysis_URL, PING_TIMEOUT HTTP/HTTPS Proxy details from appconfig file
            API_KEY = self.options.get("jsb_api_key")
            ACCEPT_TAC = self.options.get("jsb_accept_tac") == "True"
            ANALYSIS_URL = self.options.get("jsb_analysis_url")
            ANALYSIS_REPORT_DEFAULT_PING_DELAY = int(self.options.get("jsb_analysis_report_default_ping_delay"))
            ANALYSIS_REPORT_REQUEST_TIMEOUT = self.options.get("jsb_analysis_report_request_timeout")
            HTTP_PROXY = self.options.get("jsb_http_proxy")
            HTTPS_PROXY = self.options.get("jsb_https_proxy")

            # Check required inputs are defined
            incident_id = kwargs.get("incident_id")  # number (required)
            if not incident_id:
              raise ValueError("incident_id is required")
            
            jsb_report_type = kwargs.get("jsb_report_type")["name"]  # select (required)
            if not jsb_report_type:
              raise ValueError("jsb_report_type is required")

            # Check for ping_delay, else set to ANALYSIS_REPORT_DEFAULT_PING_DELAY
            ping_delay = kwargs.get("jsb_ping_delay")  # number
            if not ping_delay:
              ping_delay = ANALYSIS_REPORT_DEFAULT_PING_DELAY

            # Get optional inputs
            attachment_id = kwargs.get("attachment_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number

            # Setup proxies parameter if exist in appconfig file
            proxies = {}

            if (HTTP_PROXY):
              proxies["HTTP"] = HTTP_PROXY
            
            if (HTTPS_PROXY):
              proxies["HTTPS"] = HTTPS_PROXY
            
            if (len(proxies) == 0):
              proxies = None

            # Instansiate new Joe Sandbox object
            joesandbox = jbxapi.JoeSandbox(apikey=API_KEY, accept_tac=ACCEPT_TAC, proxies=proxies)

            # Instansiate new Resilient API object
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
            
            yield StatusMessage("Sample {} being analyized by Joe Sandbox".format(sample_webid))

            # Keep requesting sample status until the analysis report is ready for download or ANALYSIS_REPORT_REQUEST_TIMEOUT in seconds has passed
            while (sample_status["status"].lower() != "finished"):
              if (should_timeout(ANALYSIS_REPORT_REQUEST_TIMEOUT, start_time)):
                raise FunctionError("Timed out trying to get Analysis Report after {0} seconds".format(ANALYSIS_REPORT_REQUEST_TIMEOUT))
              
              yield StatusMessage("Analysis Status: {0}. Fetch every {1}s".format(sample_status["status"], ping_delay))
              sample_status = fetch_report(joesandbox, sample_webid, ping_delay)

            yield StatusMessage("Analysis Finished. Getting report & attaching to this incident")
            download = joesandbox.download(sample_webid, jsb_report_type)
            
            # Generate report name
            report_name = generate_report_name(entity, jsb_report_type, sample_webid)

            # Write temp file of report
            path = write_temp_file(download[1], report_name)
            
            # POST report as attachment to incident
            jsb_analysis_report = client.post_attachment('/incidents/{}/attachments'.format(incident_id), path, mimetype=MIMETYPES[jsb_report_type])

            yield StatusMessage("Upload of attachment complete")

            results = {
                "analysis_report_name": report_name,
                "analysis_report_pdf_id": jsb_analysis_report["id"],
                "analysis_report_url": "{0}/{1}".format(ANALYSIS_URL, sample_webid),
                "analysis_status": sample_status["runs"][0]["detection"]
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception:
            yield FunctionError()
        
        finally:
          remove_temp_files(TEMP_FILES)
