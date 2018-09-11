# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import dkim


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'email_header_validation_using_dkimarc"""

    @function("email_header_validation_using_dkimarc")
    def _email_header_validation_using_dkimarc_function(self, event, *args, **kwargs):
        """Function: Analyzes the DKIM and ARC headers for an RFC822 formatted email."""

        def get_content(client, incident_id, attachment_id, artifact_id):
            entity = {"incident_id": incident_id, "id": None, "type": "", "meta_data": None, "data": None}

            if (attachment_id):
                return client.get_content(
                    "/incidents/{0}/attachments/{1}/contents".format(entity["incident_id"], attachment_id))

            elif (artifact_id):
                entity["meta_data"] = client.get(
                    "/incidents/{0}/artifacts/{1}".format(entity["incident_id"], artifact_id))

                # handle if artifact has attachment
                if (entity["meta_data"]["attachment"]):
                    return client.get_content(
                        "/incidents/{0}/artifacts/{1}/contents".format(entity["incident_id"], artifact_id))
                else:
                    raise FunctionError("Artifact has no attachment or supported URI")

            else:
                raise ValueError('attachment_id AND artifact_id both None')

        try:
            # Get the function parameters:
            email_header_validation_target_email = kwargs.get("email_header_validation_target_email")  # text
            incident_id = kwargs.get('optional_incident_id') # number
            attachment_id = kwargs.get('attachment_id') # number
            artifact_id = kwargs.get('artifact_id') # number

            if email_header_validation_target_email is None and incident_id is None:
                raise FunctionError('Either an RFC822 email must be provided or an incident id and attachment_id '
                                    'or artifact_id must be provided')

            log = logging.getLogger(__name__)
            log.info("email_header_validation_target_email: %s", email_header_validation_target_email)

            yield StatusMessage("Analyzing email headers")
            # Initialize DKIM object from string or attachment and check for DKIM header
            if email_header_validation_target_email:
                target_email = email_header_validation_target_email
            else:
                client = self.rest_client()
                target_email = get_content(client, incident_id, attachment_id, artifact_id)

            dkim_email = dkim.DKIM(target_email)
            dkim_header_exists = b"dkim-signature" in [header[0].lower() for header in dkim_email.headers]

            # Do header analysis
            dkim_results = dkim.dkim_verify(target_email)
            arc_results = dkim.arc_verify(target_email)

            if arc_results == 'success':
                arc_results = 'Validation successful'

            # Form DKIM results statement
            if dkim_header_exists:
                if dkim_results:
                    dkim_message = 'Validation successful'
                else:
                    dkim_message = 'Most recent DKIM-Message-Signature did not validate'
            else:
                dkim_message = 'Message is not DKIM signed'

            results = {
                "dkim_verify": dkim_results,
                "arc_verify": arc_results[0] == 'pass',
                "dkim_message": dkim_message,
                "arc_message": arc_results[2]
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()