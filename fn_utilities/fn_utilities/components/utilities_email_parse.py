# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

import logging
import os
import shutil
import json
import base64
import mailparser
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields, get_file_attachment_metadata, get_file_attachment, write_to_tmp_file

CONFIG_DATA_SECTION = 'fn_utilities'
EMAIL_ATTACHMENT_ARTIFACT_ID = 7
ARTIFACT_URI = "/incidents/{0}/artifacts/files"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'email_message_parts"""

    @function("utilities_email_parse")
    def _email_parse_function(self, event, *args, **kwargs):
        """Function: Extract message headers and body parts from an email message (.eml or .msg).
        Any attachments found are added to the Incident as Artifacts if 'utilities_parse_email_attachments' is set to True"""

        try:
            log = logging.getLogger(__name__)

            # Set variables
            parsed_email = path_tmp_file = path_tmp_dir = reason = results = None

            # Get the function inputs:
            fn_inputs = validate_fields(["incident_id"], kwargs)

            # Instansiate ResultPayload
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

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
                    yield StatusMessage("Email parsed")

                    # If the input 'utilities_parse_email_attachments' is true and some attachments were found
                    if fn_inputs.get("utilities_parse_email_attachments") and parsed_email_dict.get("attachments"):

                        yield StatusMessage("Attachments found in email message")
                        attachments_found = parsed_email_dict.get("attachments")

                        # Loop attachments found
                        for attachment in attachments_found:

                            yield StatusMessage(u"Attempting to add {0} to Incident: {1}".format(attachment.get("filename"), fn_inputs.get("incident_id")))

                            # Write the attachment.payload to a temp file
                            path_tmp_file, path_tmp_dir = write_to_tmp_file(data=attachment.get("payload"),
                                                                            tmp_file_name=attachment.get("filename"),
                                                                            path_tmp_dir=path_tmp_dir)

                            artifact_description = u"This email attachment was found in the parsed email message from: '{0}'".format(u"provided base64content" if fn_inputs.get("base64content") else attachment_metadata.get("name"))

                            # POST the artifact to Resilient as an 'Email Attachment' Artifact
                            res_client.post_artifact_file(uri=ARTIFACT_URI.format(fn_inputs.get("incident_id")),
                                                          artifact_type=EMAIL_ATTACHMENT_ARTIFACT_ID,
                                                          artifact_filepath=path_tmp_file,
                                                          description=artifact_description,
                                                          value=attachment.get("filename"),
                                                          mimetype=attachment.get("mail_content_type"))

                    results = rp.done(True, parsed_email_dict)

            else:
                reason = u"Raw email in unsupported format. Failed to parse {0}".format(u"provided base64content" if fn_inputs.get("base64content") else attachment_metadata.get("name"))
                yield StatusMessage(reason)
                results = rp.done(success=False, content=None, reason=reason)

            log.info("Done")

            yield FunctionResult(results)
        except Exception:
            yield FunctionError()

        finally:
            # Remove the tmp directory
            if path_tmp_dir and os.path.isdir(path_tmp_dir):
                shutil.rmtree(path_tmp_dir)
