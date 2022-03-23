# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

import logging
import hashlib
import json
import sys
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from resilient_lib import get_file_attachment, get_file_attachment_metadata

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'attachment_hash"""

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

            client = self.rest_client()
            data = get_file_attachment(client, incident_id, task_id=task_id, attachment_id=attachment_id)
            metadata = get_file_attachment_metadata(client, incident_id, task_id=task_id, attachment_id=attachment_id)

            results = {
                "filename": metadata["name"],
                "content_type": metadata["content_type"],
                "size": metadata["size"],
                "created": metadata["created"]
            }

            # Hashlib provides a list of all "algorithms_available", but there's duplication, so
            # use the standard list: ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')
            # Hashlib in 3.2 and above does not supports hashlib.algorithms_guaranteed this contains a longer
            # list but will be used instead of hashlib.algorithms
            if sys.version_info.major >= 3:
                algorithms = hashlib.algorithms_guaranteed
            else:
                algorithms = hashlib.algorithms

            for algo in algorithms:
                impl = hashlib.new(algo)
                impl.update(data)
                # shake algorithms require a 'length' parameter
                if algo.startswith("shake_"):
                    length_list = algo.split('_')
                    results[algo] = impl.hexdigest(int(length_list[-1]))
                else:
                    results[algo] = impl.hexdigest()

            log.info(u"{} sha1={}".format(metadata["name"], results["sha1"]))

            # Produce a FunctionResult with the return value
            log.debug(json.dumps(results))
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
