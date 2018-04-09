# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

import logging
import hashlib
import json
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'attachment_hash"""

    @function("utilities_attachment_hash")
    def _attachment_hash_function(self, event, *args, **kwargs):
        """Function: Calculate hashes for a file attachment."""
        try:
            log = logging.getLogger(__name__)

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number

            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("attachment_id: %s", attachment_id)
            if incident_id is None and task_id is None:
                raise FunctionError("Error: incident_id or task_id must be specified.")
            if attachment_id is None:
                raise FunctionError("Error: attachment_id must be specified.")

            yield StatusMessage("Reading attachment...")
            if task_id:
                metadata_uri = "/tasks/{}/attachments/{}".format(task_id, attachment_id)
                data_uri = "/tasks/{}/attachments/{}/contents".format(task_id, attachment_id)
            else:
                metadata_uri = "/incidents/{}/attachments/{}".format(incident_id, attachment_id)
                data_uri = "/incidents/{}/attachments/{}/contents".format(incident_id, attachment_id)

            client = self.rest_client()
            metadata = client.get(metadata_uri)
            data = client.get_content(data_uri)

            results = {
                "filename": metadata["name"],
                "content_type": metadata["content_type"],
                "size": metadata["size"],
                "created": metadata["created"]
            }

            # Hashlib provides a list of all "algorithms_available", but there's duplication, so
            # use the standard list: ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')
            for algo in hashlib.algorithms:
                impl = hashlib.new(algo)
                impl.update(data)
                results[algo] = impl.hexdigest()

            log.info(u"{} sha1={}".format(metadata["name"], results["sha1"]))

            # Produce a FunctionResult with the return value
            log.debug(json.dumps(results))
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
