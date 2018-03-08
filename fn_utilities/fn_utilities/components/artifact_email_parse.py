# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import datetime
import time
import email
import json
from fn_utilities.util.mailtojson import MailJson
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError


def _parse_date_millis(value):
    if value is None:
        return int(time.time() * 1000)

    ttuple = email.utils.parsedate_tz(value)

    if ttuple is None:
        return int(time.time() * 1000)

    timestamp = email.utils.mktime_tz(ttuple)
    return int(timestamp * 1000)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'email_message_parts"""

    @function("artifact_email_parse")
    def _artifact_email_parse_function(self, event, *args, **kwargs):
        """Function: Extract message headers and body parts from an email message artifact."""
        try:
            log = logging.getLogger(__name__)

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number

            log.info("incident_id: %s", incident_id)
            log.info("artifact_id: %s", artifact_id)

            if not incident_id:
                raise FunctionError("Error: Incident ID must be specified.")
            if not artifact_id:
                raise FunctionError("Error: Artifact ID must be specified.")

            yield StatusMessage("Reading email artifact...")
            client = self.rest_client()
            metadata_uri = "/incidents/{}/artifacts/{}".format(incident_id, artifact_id)
            metadata = client.get(metadata_uri)
            data_uri = "/incidents/{}/artifacts/{}/contents".format(incident_id, artifact_id)
            data = client.get_content(data_uri)

            # Parse the email content
            mmj = MailJson(data.decode("utf-8"))
            mmj.parse()
            results = mmj.get_data()

            # For convenience, produce an epoch-millis timestamp
            results["timestamp"] = _parse_date_millis(results["headers"].get("date", None))

            # For convenience, find the plaintext and html body
            results["body_text"] = None
            results["body_html"] = None
            for part in results.get("parts", []):
                if part.get("content_type") == "text/plain":
                    results["body_text"] = part.get("content")
                if part.get("content_type") == "text/html":
                    results["body_html"] = part.get("content")

            log.info(json.dumps(results, indent=2))

            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
