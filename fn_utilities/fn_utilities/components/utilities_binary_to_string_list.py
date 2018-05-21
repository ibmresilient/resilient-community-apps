# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""
import sys
import tempfile
import logging
from floss import main
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'binary_to_string_list"""

    def get_binary_data_from_file(self, incident_id, task_id, artifact_id, attachment_id):
        # get_binary_data_from_file calls the REST API to get the attachment or artifact data

        if artifact_id and incident_id:
            data_uri = "/incidents/{}/artifacts/{}/contents".format(incident_id, artifact_id)
        elif attachment_id:
            if task_id:
                data_uri = "/tasks/{}/attachments/{}/contents".format(task_id, attachment_id)
            elif incident_id:
                data_uri = "/incidents/{}/attachments/{}/contents".format(incident_id, attachment_id)
            else:
                raise ValueError("task_id or incident_id must be specified with attachment")
        else:
            raise ValueError("artifact or attachment or incident id must be specified")

        # Get the data
        client = self.rest_client()
        data = client.get_content(data_uri)
        return data

    def extract_strings_from_binary(self, data):
        # extract_strings_from_binary writes binary data to a file and calls get_strings to extract
        # the encoded strings
        with tempfile.NamedTemporaryFile('w', bufsize=0) as temp_file_binary:
            try:
                # Write binary data to a temporary file.
                temp_file_binary.write(data)

                list_string = self.get_strings(temp_file_binary)
            except Exception as err:
                raise err

            finally:
                # Close the temporary binary file. Closing the temp file will delete it.
                temp_file_binary.close()
        return list_string

    def get_strings(self, temp_file_binary):
        # get_strings extracts encoded string from file and returns a list of strings found in the
        # file.  Floss is called to extract the strings.  For more information on Floss:
        # https://github.com/fireeye/flare-floss/blob/master/doc/usage.md
        with tempfile.NamedTemporaryFile(bufsize=0) as temp_file_strings:
            try:
                # Floss writes output to stdout so redirect stdout to temporary file
                save_stdout = sys.stdout
                output_stream = open(temp_file_strings.name.encode("ascii"), 'w')
                sys.stdout = temp_file_strings

                # Call Floss to extract strings from the file.
                # Use commandline arguments: -q for quiet mode so that only the strings
                # are returned, no headers;  -s option directs floss to analyze binary
                # files containing shellcode. See floss documentation for other options
                # you can pass to floss.
                # https://github.com/fireeye/flare-floss/blob/master/doc/usage.md
                result_floss = main.main(['main', '-q', '-s', temp_file_binary.name.encode("ascii")])
                output_stream.close()

                if result_floss != 0:
                    raise Exception("Error running floss.")

                try:
                    # Read the output from floss and make a list of the decoded strings
                    floss_output = open(temp_file_strings.name.encode("ascii"), "r")
                    list_string = floss_output.read().splitlines()
                except Exception as err:
                    raise err
                finally:
                    # Close the file.
                    floss_output.close()

            except Exception as err:
                raise err
            finally:
                # Restore stdout and close the file. The temporary file will be deleted on close.
                sys.output = save_stdout
                temp_file_strings.close()

        return list_string

    @function("utilities_binary_to_string_list")
    def _binary_to_string_list_function(self, event, *args, **kwargs):
        """Function: This function takes a binary file and returns a list of decoded obfuscated strings from the binary file."""
        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("artifact_id: %s", artifact_id)
            log.info("attachment_id: %s", attachment_id)

            # Get the binary data from the artifact or the attachment
            data = self.get_binary_data_from_file(incident_id, task_id, artifact_id, attachment_id)
            yield StatusMessage("Binary file retrieved.")

            # Extract the strings from the binary file and put them in a list.
            list_results = self.extract_strings_from_binary(data)
            yield StatusMessage("Strings decoded from file.")

        except Exception as err:
            yield FunctionError(err)

        yield StatusMessage("Returning list of {} decoded strings".format(len(list_results)))
        yield FunctionResult({"value": list_results})
