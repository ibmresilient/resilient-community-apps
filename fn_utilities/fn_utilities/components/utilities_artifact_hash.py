# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

import logging
import hashlib
import json
import sys
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'artifact_hash"""

    @function("utilities_artifact_hash")
    def _artifact_hash_function(self, event, *args, **kwargs):
        """Function: Calculate hashes for a file artifact."""
        try:
            log = logging.getLogger(__name__)

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number

            log.info("incident_id: %s", incident_id)
            log.info("artifact_id: %s", artifact_id)
            if incident_id is None:
                raise FunctionError("Error: incident_id must be specified.")
            if artifact_id is None:
                raise FunctionError("Error: artifact_id must be specified.")

            yield StatusMessage("Reading artifact...")
            metadata_uri = "/incidents/{}/artifacts/{}".format(incident_id, artifact_id)
            data_uri = "/incidents/{}/artifacts/{}/contents".format(incident_id, artifact_id)

            client = self.rest_client()
            metadata = client.get(metadata_uri)
            data = client.get_content(data_uri)

            results = {
                "filename": metadata["attachment"]["name"],
                "content_type": metadata["attachment"]["content_type"],
                "size": metadata["attachment"]["size"],
                "created": metadata["attachment"]["created"]
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
                    results[algo] = impl.hexdigest(length=int(length_list[-1]))
                else:
                    results[algo] = impl.hexdigest()

            log.info(u"{} sha1={}".format(metadata["attachment"]["name"], results["sha1"]))

            # Produce a FunctionResult with the return value
            log.debug(json.dumps(results))
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
