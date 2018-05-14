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

            # Nested with-try-except-finally clauses are used here with raise so that the
            # files and are closed and deleted in the finally clause.  There is a bug in
            # FunctionError() which causes finally clause to not be executed...so use this
            # implementation till that is fixed.
            with tempfile.NamedTemporaryFile('w', bufsize=0) as temp_file_binary:
                try:
                    # Write data to a temporary file.
                    temp_file_binary.write(data)
                    yield StatusMessage("Binary file contents retrieved.")

                    with tempfile.NamedTemporaryFile(bufsize=0) as temp_file_strings:
                        try:
                            # Floss writes output to stdout so redirect stdout to temporary file
                            save_stdout = sys.stdout
                            f = open(temp_file_strings.name.encode("ascii"), 'w')
                            sys.stdout = temp_file_strings

                            # Call Floss to extract strings from the file.
                            yield StatusMessage("Decoding strings from input file.")
                            result = main.main(['main', '-q', '-s', temp_file_binary.name.encode("ascii")])
                            f.close()

                            # Create a list of strings to return.
                            yield StatusMessage("Prepare a list of string to return from the function.")
                            try:
                                inputStream = open(temp_file_strings.name.encode("ascii"), "r")
                                listResults = inputStream.read().splitlines()
                            except Exception as err:
                                raise err
                            finally:
                                inputStream.close()

                        except Exception as err:
                            raise err
                        finally:
                            # Restore stdout and close the file. The temporary file will be deleted on close.
                            sys.output = save_stdout
                            temp_file_strings.close()

                except Exception as err:
                    raise err
                finally:
                    # Close (delete) the temporary binary file.
                    temp_file_binary.close()

        except Exception as err:
            yield FunctionError(err)

        yield StatusMessage("Returning list of {} decoded strings".format(len(listResults)))
        yield FunctionResult({"value": listResults})
