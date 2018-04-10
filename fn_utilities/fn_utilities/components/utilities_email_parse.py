# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

import logging
import sys
import time
import email
import json
import base64
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

    @function("utilities_email_parse")
    def _email_parse_function(self, event, *args, **kwargs):
        """Function: Extract message headers and body parts from an EML email message."""
        try:
            log = logging.getLogger(__name__)

            # NOTE: This function only works when run on Python2
            # (due to the way the current version of the utility function is written).
            if sys.version_info[0] >= 3:
                raise FunctionError("This function cannot run on Python 3")

            # Get the function parameters:
            base64content = kwargs.get("base64content")  # text
            if base64content is None or base64content == "":
                raise FunctionError("No message was supplied.")

            log = logging.getLogger(__name__)
            log.debug("base64content: %s", base64content)

            yield StatusMessage("Reading email message...")
            data = base64.b64decode(base64content)

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
