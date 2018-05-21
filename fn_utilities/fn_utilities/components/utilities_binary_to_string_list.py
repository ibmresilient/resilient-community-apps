# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-useFunctionError
"""Function implementation"""
import sys
import tempfile
import logging
from floss import main
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'binary_to_string_list"""

    def get_data_from_file(self, incident_id, task_id, artifact_id, attachment_id):
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
            data = self.get_data_from_file(incident_id, task_id, artifact_id, attachment_id)

            # Nested with-try-except-finally clauses are used here with raise so that the
            # files and are closed and deleted in the finally clause.  There is a bug in
            # FunctionError() which causes finally clause to not be executed...so use this
            # implementation till that is fixed.
            with tempfile.NamedTemporaryFile('w', bufsize=0) as temp_file_binary:
                try:
                    # Write data to a temporary file.
                    temp_file_binary.write(data)
                    yield StatusMessage("Binary file contents retrieved and written to temporary file.")

                    with tempfile.NamedTemporaryFile(bufsize=0) as temp_file_strings:
                        try:
                            # Floss writes output to stdout so redirect stdout to temporary file
                            save_stdout = sys.stdout
                            f = open(temp_file_strings.name.encode("ascii"), 'w')
                            sys.stdout = temp_file_strings

                            # Call Floss to extract strings from the file.
                            # Use commandline arguments: -q for quiet mode so that only the strings
                            # are returned, no headers;  -s option directs floss to analyze binary
                            # files containing shellcode. See floss documentation for other options
                            # you can pass to floss.
                            # https://github.com/fireeye/flare-floss/blob/master/doc/usage.md
                            yield StatusMessage("Decoding strings from input file.")
                            result_floss = main.main(['main', '-q', '-s', temp_file_binary.name.encode("ascii")])
                            f.close()

                            if result_floss == 1:
                                raise Exception("Error running floss.")

                            # Create a list of strings to return.
                            yield StatusMessage("Prepare a list of string to return from the function.")
                            try:
                                #Read the input stream of and make a list of the decoded strings
                                input_stream = open(temp_file_strings.name.encode("ascii"), "r")
                                list_results = input_stream.read().splitlines()
                            except Exception as err:
                                raise err
                            finally:
                                input_stream.close()

                        except Exception as err:
                            raise err
                        finally:
                            # Restore stdout and close the file. The temporary file will be deleted on close.
                            sys.output = save_stdout
                            temp_file_strings.close()

                except Exception as err:
                    raise err
                finally:
                    # Close the temporary binary file. Closing the temp file will delete it.
                    temp_file_binary.close()

        except Exception as err:
            yield FunctionError(err)

        yield StatusMessage("Returning list of {} decoded strings".format(len(list_results)))
        yield FunctionResult({"value": list_results})
