# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

import logging
import sys
import os
import time
import email
import json
import base64
import mailparser
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, get_file_attachment_metadata, get_file_attachment, get_app_config_option, get_all_function_inputs, write_to_tmp_file, remove_dir


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'email_message_parts"""

    @function("utilities_email_parse")
    def _email_parse_function(self, event, *args, **kwargs):
        """Function: Extract message headers and body parts from an EML email message."""
        try:
            log = logging.getLogger(__name__)

            # Set variables
            parsed_email = path_tmp_file = path_tmp_dir = reason = results = None

            # Get the function inputs:
            fn_inputs = get_all_function_inputs(kwargs, ["incident_id"])

            # Instansiate ResultPayload
            rp = ResultPayload("utilities_email_parse", **kwargs)

            # If its just base64content as input, use parse_from_string
            if fn_inputs.get("base64content"):
                yield StatusMessage("Processing provided base64content")
                parsed_email = mailparser.parse_from_string(base64.b64decode(fn_inputs.get("base64content")))
                yield StatusMessage("Provided base64content processed")

            else:
                # Instansiate new Resilient API object
                res_client = self.rest_client()

                # Get attachment metadata
                attachment_metadata = get_file_attachment_metadata(
                    res_client=res_client,
                    incident_id=fn_inputs.get("incident_id"),
                    artifact_id=fn_inputs.get("artifact_id"),
                    task_id=fn_inputs.get("task_id"),
                    attachment_id=fn_inputs.get("attachment_id")
                )

                # Get attachment content
                attachment_contents = get_file_attachment(
                    res_client=res_client,
                    incident_id=fn_inputs.get("incident_id"),
                    artifact_id=fn_inputs.get("artifact_id"),
                    task_id=fn_inputs.get("task_id"),
                    attachment_id=fn_inputs.get("attachment_id")
                )

                # Write the attachment_contents to a temp file
                path_tmp_file, path_tmp_dir = write_to_tmp_file(attachment_contents, tmp_file_name=attachment_metadata.get("name"))

                # Get the file_extension
                file_extension = os.path.splitext(path_tmp_file)[1]

                if file_extension == ".msg":
                    yield StatusMessage("Processing MSG File")
                    try:
                        parsed_email = mailparser.parse_from_file_msg(path_tmp_file)
                        yield StatusMessage("MSG File processed")
                    except Exception as err:
                        reason = u"Could not parse {0} MSG File".format(attachment_metadata.get("name"))
                        yield StatusMessage(reason)
                        results = rp.done(success=False, content=None, reason=reason)
                        log.error(err)

                else:
                    yield StatusMessage("Processing Raw Email File")
                    try:
                        parsed_email = mailparser.parse_from_file(path_tmp_file)
                        yield StatusMessage("Raw Email File processed")
                    except Exception as err:
                        reason = u"Could not parse {0} Email File".format(attachment_metadata.get("name"))
                        yield StatusMessage(reason)
                        results = rp.done(success=False, content=None, reason=reason)
                        log.error(err)

            if parsed_email is not None:
                if not parsed_email.mail:
                    reason = u"Raw email in unsupported format. Failed to parse {0}".format(u"provided base64content" if fn_inputs.get("base64content") else attachment_metadata.get("name"))
                    yield StatusMessage(reason)
                    results = rp.done(success=False, content=None, reason=reason)

                else:
                    # Load all parsed email attributes into a Python Dict
                    parsed_email_dict = json.loads(parsed_email.mail_json, encoding="utf-8")
                    parsed_email_dict["plain_body"] = parsed_email.text_plain_json
                    parsed_email_dict["html_body"] = parsed_email.text_html_json
                    results = rp.done(True, parsed_email_dict)
                    yield StatusMessage("Email parsed")

            else:
                reason = u"Raw email in unsupported format. Failed to parse {0}".format(u"provided base64content" if fn_inputs.get("base64content") else attachment_metadata.get("name"))
                yield StatusMessage(reason)
                results = rp.done(success=False, content=None, reason=reason)

            yield FunctionResult(results)
        except Exception:
            yield FunctionError()

        finally:
            # Remove the tmp directory
            remove_dir(path_tmp_dir)
