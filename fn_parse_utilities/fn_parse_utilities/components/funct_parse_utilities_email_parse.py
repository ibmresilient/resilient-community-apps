# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

from os import path
from io import BytesIO
from json import loads
from re import compile
from shutil import rmtree
from base64 import b64decode
from logging import getLogger

from mailparser import parse_from_bytes, parse_from_file_msg
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields, get_file_attachment_metadata, get_file_attachment, write_to_tmp_file, b_to_s, s_to_b

ARTIFACT_URI = "/incidents/{0}/artifacts/files"

RE_CONTENT_TYPE = compile("Content-Transfer-Encoding:base64")
RE_BASE64 = compile("^[A-Za-z0-9+/\r\n]+={0,2}$")
RE_START_BASE64 = compile("\n\n")

LOG = getLogger(__name__)
PACKAGE_NAME = 'fn_parse_utilities'

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'email_message_parts"""

    @function("parse_utilities_email_parse")
    def _email_parse_function(self, event, *args, **kwargs):
        """Function: Extract message headers and body parts from an email message (.eml or .msg).
        Any attachments found are added to the Incident as Artifacts if 'parse_utilities_email_attachments' is set to True"""

        try:
            # Set variables
            parsed_email = path_tmp_file = path_tmp_dir = reason = results = None

            # Get the function inputs:
            fn_inputs = validate_fields(["parse_utilities_incident_id"], kwargs)

            # Instantiate ResultPayload
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # If its just base64content as input, use parse_from_string
            if fn_inputs.get("parse_utilities_base64content"):
                yield StatusMessage("Processing provided base64content")
                parsed_email = parse_from_bytes(b64decode(fn_inputs.get("parse_utilities_base64content")))
                yield StatusMessage("Provided base64content processed")

            else:
                # Validate that either: (incident_id AND attachment_id OR artifact_id) OR (task_id AND attachment_id) is defined
                if not (fn_inputs.get("parse_utilities_incident_id") and (fn_inputs.get("parse_utilities_attachment_id") or fn_inputs.get("parse_utilities_artifact_id"))) and \
                   not (fn_inputs.get("parse_utilities_task_id") and fn_inputs.get("parse_utilities_attachment_id")):
                    raise FunctionError("You must define either: (parse_utilities_incident_id AND (parse_utilities_attachment_id OR parse_utilities_artifact_id)) OR (parse_utilities_task_id AND parse_utilities_attachment_id)")

                # Instantiate new SOAR API object
                res_client = self.rest_client()

                # Get attachment metadata
                attachment_metadata = get_file_attachment_metadata(
                    res_client=res_client,
                    incident_id=fn_inputs.get("parse_utilities_incident_id"),
                    artifact_id=fn_inputs.get("parse_utilities_artifact_id"),
                    task_id=fn_inputs.get("parse_utilities_task_id"),
                    attachment_id=fn_inputs.get("parse_utilities_attachment_id")
                )

                # Get attachment content
                attachment_contents = get_file_attachment(
                    res_client=res_client,
                    incident_id=fn_inputs.get("parse_utilities_incident_id"),
                    artifact_id=fn_inputs.get("parse_utilities_artifact_id"),
                    task_id=fn_inputs.get("parse_utilities_task_id"),
                    attachment_id=fn_inputs.get("parse_utilities_attachment_id")
                )

                # Get the file_extension
                file_extension = path.splitext(attachment_metadata.get("name"))[1]

                if file_extension.lower() == ".msg":
                    yield StatusMessage("Processing MSG File")
                    # Write the attachment_contents to a temp file
                    path_tmp_file, path_tmp_dir = write_to_tmp_file(attachment_contents)

                    try:
                        parsed_email = parse_from_file_msg(path_tmp_file)
                        yield StatusMessage("MSG File processed")
                    except Exception as err:
                        reason = f"Could not parse {attachment_metadata.get('name')} MSG File"
                        yield StatusMessage(reason)
                        results = rp.done(success=False, content=None, reason=reason)
                        LOG.error(err)

                else:
                    yield StatusMessage(f"Processing Raw Email File: {attachment_metadata.get('name')}")
                    try:
                        parsed_email = parse_from_bytes(attachment_contents)
                        yield StatusMessage("Raw Email File processed")
                    except Exception as err:
                        reason = f"Could not parse {attachment_metadata.get('name')} Email File"
                        yield StatusMessage(reason)
                        results = rp.done(success=False, content=None, reason=reason)
                        LOG.error(err)

            if parsed_email is not None:
                if not parsed_email.mail:
                    reason = f"Raw email in unsupported format. Failed to parse {'provided base64content' if fn_inputs.get('parse_utilities_base64content') else attachment_metadata.get('name')}"
                    yield StatusMessage(reason)
                    results = rp.done(success=False, content=None, reason=reason)

                else:
                    # Load all parsed email attributes into a Python Dict
                    parsed_email_dict = loads(parsed_email.mail_json)
                    parsed_email_dict["body"] = convert_base64_encoding(parsed_email.body)
                    parsed_email_dict["plain_body"] = ", ".join(convert_base64_encoding(parsed_email.text_plain))
                    parsed_email_dict["html_body"] = parsed_email.text_html_json
                    yield StatusMessage("Email parsed")

                    # If the input 'parse_utilities_email_attachments' is true and some attachments were found
                    if fn_inputs.get("parse_utilities_email_attachments") and parsed_email_dict.get("attachments"):

                        yield StatusMessage("Attachments found in email message")
                        attachments_found = parsed_email_dict.get("attachments")

                        # Loop attachments found
                        for attachment in attachments_found:

                            yield StatusMessage(f"Attempting to add {attachment.get('filename')} to Incident: {fn_inputs.get('parse_utilities_incident_id')}")

                            # Write the attachment.payload to a temp file
                            file_content = BytesIO(s_to_b(attachment.get("payload")))

                            artifact_description = f"This email attachment was found in the parsed email message from: '{'provided base64content' if fn_inputs.get('parse_utilities_base64content') else attachment_metadata.get('name')}'"

                            # POST the artifact to SOAR as an 'Email Attachment' Artifact
                            res_client.post_artifact_file(uri=ARTIFACT_URI.format(fn_inputs.get("parse_utilities_incident_id")),
                                                          artifact_type=7,
                                                          artifact_filepath=None,
                                                          description=artifact_description,
                                                          value=attachment.get("filename"),
                                                          mimetype=attachment.get("mail_content_type"),
                                                          bytes_handle=file_content)

                    results = rp.done(True, parsed_email_dict)

            else:
                reason = f"Raw email in unsupported format. Failed to parse {'provided base64content' if fn_inputs.get('parse_utilities_base64content') else attachment_metadata.get('name')}"
                yield StatusMessage(reason)
                results = rp.done(success=False, content=None, reason=reason)

            LOG.info("Done")

            yield FunctionResult(results)
        except Exception:
            yield FunctionError()

        finally:
            # Remove the tmp directory
            if path_tmp_dir and path.isdir(path_tmp_dir):
                rmtree(path_tmp_dir)

def decode_mail_body(value):
    """ Decode data. There's no guarantee that data is in base64"""
    try:
        return b64decode(value)
    except Exception:
        return value

def convert_base64_encoding(payload):
    """ Look for base64 mime type and convert the data that follows.
    return: Payload with the base64 encoded data substituted
    """
    if isinstance(payload, list):
        return [convert_base64_encoding(item) for item in payload]

    result = payload
    # Determine if we have embedded base64
    match = RE_CONTENT_TYPE.search(payload)
    if match:
        LOG.INFO("Found bas64 encoded content")
        # Find the start of the data which is marked by an empty line
        match_base64 = RE_START_BASE64.search(payload[match.end():])
        if match_base64:
            base64_data = payload[match.end()+match_base64.end():]
        else:
            base64_data = payload[match.end():]  # Just start where we found the mime information
        # Ensure we are really dealing with base64 data
        if RE_BASE64.search(base64_data):
            LOG.debug(base64_data)
            decoded_data = b_to_s(decode_mail_body(base64_data))
            # Insert where we found it
            result = "\n".join([payload[:match.end()], decoded_data])
    return result
