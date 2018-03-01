# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import hashlib
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'attachment_hash"""

    @function("attachment_hash")
    def _attachment_hash_function(self, event, *args, **kwargs):
        """Function: Calculate hashes for a file attachment."""
        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number

            log = logging.getLogger(__name__)
            log.info("Incident ID: %s", incident_id)
            log.info("Attachment ID: %s", attachment_id)
            if not incident_id:
                raise FunctionError("Error: Incident ID must be specified.")
            if not attachment_id:
                raise FunctionError("Error: Attachment ID must be specified.")

            yield StatusMessage("Reading attachment...")
            metadata_uri = "/incidents/{}/attachments/{}".format(incident_id, attachment_id)
            metadata = self.rest_client().get(metadata_uri)
            data_uri = "/incidents/{}/attachments/{}/contents".format(incident_id, attachment_id)
            data = self.rest_client().get_content(data_uri)

            result = {
                "filename": metadata["name"],
                "content-type": metadata["content_type"],
                "size": metadata["size"],
                "created": metadata["created"]
            }

            # Hashlib provides a list of all "algorithms_available", but there's duplication, so
            # use the standard list: ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')
            for algo in hashlib.algorithms:
                impl = hashlib.new(algo)
                impl.update(data)
                result[algo] = impl.hexdigest()

            # Produce a FunctionResult with the return value
            log.info(json.dumps(result))
            yield FunctionResult(result)
        except Exception:
            yield FunctionError()