# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

from json import dumps
from logging import getLogger
from hashlib import algorithms_guaranteed, new
from resilient_lib import get_file_attachment, get_file_attachment_metadata, validate_fields
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'artifact_hash"""

    @function("utilities_artifact_hash")
    def _artifact_hash_function(self, event, *args, **kwargs):
        """Function: Calculate hashes for a file artifact."""
        try:
            log = getLogger(__name__)
            # Validate required inputs
            validate_fields(["incident_id", "artifact_id"], kwargs)

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number

            log.info("incident_id: %s", incident_id)
            log.info("artifact_id: %s", artifact_id)

            yield StatusMessage("Reading artifact...")

            client = self.rest_client()
            metadata = get_file_attachment_metadata(client, incident_id, artifact_id=artifact_id)
            data = get_file_attachment(client, incident_id, artifact_id=artifact_id)

            results = {
                "filename": metadata["name"],
                "content_type": metadata["content_type"],
                "size": metadata["size"],
                "created": metadata["created"]
            }

            # Hashlib provides a list of all "algorithms_available", but there's duplication, so
            # use the standard list: ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')
            for algo in algorithms_guaranteed:
                impl = new(algo)
                impl.update(data)
                # shake algorithms require a 'length' parameter
                if algo.startswith("shake_"):
                    results[algo] = impl.hexdigest(int(algo.split('_')[-1]))
                else:
                    results[algo] = impl.hexdigest()

            log.info(u"{} sha1={}".format(metadata["name"], results["sha1"]))

            # Produce a FunctionResult with the return value
            log.debug(dumps(results))
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
