# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""
import subprocess
import os
import tempfile
import json
import logging
import floss
import mimetypes
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_strings_from_binary"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_utilities_strings_from_binary", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_utilities_strings_from_binary", {})

    @function("utilities_strings_from_binary")
    def _utilities_strings_from_binary_function(self, event, *args, **kwargs):
        """Function: This function takes an attachment binary file and returns a file attachment which contains the strings within the binary file."""
        try:
            # Get the function parameters:

            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number
            file_path = kwargs.get("file_path")  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("artifact_id: %s", artifact_id)
            log.info("attachment_id: %s", attachment_id)
            log.info("file_path: %s", file_path)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")
            if file_path is None:
                yield FunctionError("Error: file_path must be specified.")

            # Get the binary data from the artifact or the attachment
            if artifact_id:
                data_uri = "/incidents/{}/artifacts/{}/contents".format(incident_id, artifact_id)
            elif attachment_id:
                if task_id:
                    data_uri = "/tasks/{}/attachments/{}/contents".format(task_id, attachment_id)
                elif incident_id:
                    data_uri = "/incidents/{}/attachments/{}/contents".format(incident_id, attachment_id)
                else:
                    yield FunctionError("Error: incident_id or task_id must be specified.")
            else:
                yield FunctionError("Error: attachment_id or article_id must be specified.")

            # Get the data
            client = self.rest_client()
            data = client.get_content(data_uri)

            with tempfile.NamedTemporaryFile('w', 0, dir=file_path, delete=False) as temp_file_binary:
                try:
                    # Write data to a temporary file.
                    temp_file_binary.write(data)
                    temp_file_binary.close()
                    log.info("binary data written %s", temp_file_binary.name)

                    with tempfile.NamedTemporaryFile('w', 0, dir=file_path, delete=False) as temp_file_strings:
                        try:
                            #listFloss = dir(floss)
                            # Spawn a subprocess to call floss to strip strings from the file.
                            env = os.environ.copy()
                            p = subprocess.Popen(["floss", "-sq", temp_file_binary.name],
                                                 shell=False,
                                                 stderr=subprocess.PIPE,
                                                 stdout=temp_file_strings,
                                                 env=env)
                            p.communicate()
                            temp_file_strings.close()

                                # Post the output from Floss as an attachment file.
                            if task_id:
                                attachment_uri = "/tasks/{}/attachments".format(task_id)
                            else:
                                # The resulting attachment is posted to Incident attachments for
                                # both the incident attachments and artifact files. Is this correct?
                                attachment_uri = "/incidents/{}/attachments".format(incident_id)
                            new_attachment = client.post_attachment(attachment_uri,
                                                                    temp_file_strings.name,
                                                                    filename="~/attachment.txt",
                                                                    mimetype="text/plain")
                            # Produce a FunctionResult with the new attachment as return value
                            if isinstance(new_attachment, list):
                                new_attachment = new_attachment[0]
                            log.info(json.dumps(new_attachment))


                        except Exception:
                            log.info("Error: running Floss and creating attachment.")
                            raise
                        finally:
                            # Remove temporary file of strings
                            os.unlink(temp_file_strings.name)
                except Exception:
                    log.info("Error: opening binary file")
                    raise
                finally:
                    # Remove temporary binary file
                    os.unlink(temp_file_binary.name)

        except Exception:
            yield FunctionError("Error: in utilities_strings_from_binary")

        yield FunctionResult(new_attachment)
