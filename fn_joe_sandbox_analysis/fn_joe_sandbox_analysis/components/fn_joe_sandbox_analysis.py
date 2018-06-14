# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import os
import jbxapi
import time
import tempfile
import thread
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
        
        # List to store created paths of temp files
        TEMP_FILES = []
        
        def remove_temp_files(files):
          for f in files:
            print "Removing ", f
            os.remove(f)

        def get_input_entity(client, incident_id, attachment_id, artifact_id):
          
          entity = {"incident_id": incident_id, "id": None, "type": "", "meta_data": None, "data": None}

          if (attachment_id):
            entity["id"] = attachment_id
            entity["type"] = "attachment"
            entity["meta_data"] = client.get("/incidents/{0}/attachments/{1}".format(entity["incident_id"], entity["id"]))
            entity["data"] = client.get_content("/incidents/{}/attachments/{}/contents".format(entity["incident_id"], entity["id"]))
            return entity
          
          elif (artifact_id):
            entity["id"] = artifact_id
            
            # entity["type"] = "artifact_file"
            # entity["meta_uri"] = "/incidents/{}/attachments/{}".format(entity["incident_id"], attachment_id)
            # entity["data_uri"] = "/incidents/{}/attachments/{}/contents".format(entity["incident_id"], attachment_id)
            return entity
          
          else:
            raise ValueError('attachment_id AND artifact_id both None')
        
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

        # def read_temp_file(path):
        #   content = None
        #   fo = open(path, 'rb')
        #   content = fo.read()
        #   fo.close()
        #   # with open(path, 'rb') as content_file:
        #     # content = content_file.read()
        #   return content

        def submit_file(joesandbox, path):
          f = open(path, "rb")
          sample_response = joesandbox.submit_sample(f)
          f.close()
          return sample_response["webids"][0]

        def get_sample_info(webid):
          return joesandbox.info(webid)
          # return {"status": "submitted"}

        try:
            log = logging.getLogger(__name__)
            # log.info("incident_id: %s", incident_id)
            # log.info("attachment_id: %s", attachment_id)
            # log.info("artifact_id: %s", artifact_id)
            # log.info("ping_delay: %s", ping_delay)

            # Check required inputs are defined
            incident_id = kwargs.get("incident_id")  # number (required)
            if not incident_id:
              raise ValueError('incident_id is required')

            # Check for ping_delay, else set to 30 seconds by default
            ping_delay = kwargs.get("ping_delay")  # number
            if not ping_delay:
              ping_delay = 30

            # Get optional inputs
            attachment_id = kwargs.get("attachment_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number

            # Get Joe Sandbox API Key and Analysis_URL from appconfig file
            API_KEY = self.options.get("joe_sandbox_api_key")
            ANALYSIS_URL = self.options.get("joe_sandbox_analysis_url")

            # Set to True to agree with Joe Sandbox Terms and Conditions.
            ACCEPT_TAC = True

            # Instansiate new Joe Sandbox object
            joesandbox = jbxapi.JoeSandbox(apikey=API_KEY, accept_tac=ACCEPT_TAC)

            # Instansiate new Resilient API object
            client = self.rest_client()

            # Get entity we are dealing with (either attachment or artifact)
            entity = get_input_entity(client, incident_id, attachment_id, artifact_id)

            sample_webid = None

            if (entity["type"] == "attachment"):
              attachment_name = "[{0}_{1}] - {2}".format(entity["meta_data"]["inc_id"], entity["meta_data"]["id"], entity["meta_data"]["name"])
              path = write_temp_file(entity["data"], attachment_name)
              # sample_webid = submit_file(joesandbox, path)
              sample_webid = 589069

            sample_info = get_sample_info(sample_webid)
            print sample_info

            thread

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
        
        finally:
          remove_temp_files(TEMP_FILES)
