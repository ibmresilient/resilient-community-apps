# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

from logging import getLogger
from hashlib import algorithms_guaranteed, new
from json import dumps
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from resilient_lib import get_file_attachment, get_file_attachment_metadata, validate_fields

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'attachment_hash"""

    @function("soar_utils_attachment_hash")
    def _attachment_hash_function(self, event, *args, **kwargs):
        """Function: Calculate hashes for a file attachment."""
        try:
            validate_fields(["attachment_id"], kwargs)
            log = getLogger(__name__)

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number

            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("attachment_id: %s", attachment_id)
            if not incident_id and not task_id:
                raise FunctionError("Error: incident_id or task_id must be specified.")

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
            algorithms = algorithms_guaranteed

            for algo in algorithms:
                impl = new(algo)
                impl.update(data)
                # shake algorithms require a 'length' parameter
                if algo.startswith("shake_"):
                    length_list = algo.split('_')
                    results[algo] = impl.hexdigest(int(length_list[-1]))
                else:
                    results[algo] = impl.hexdigest()

            log.info(f"{metadata['name']} sha1={results['sha1']}")

            # Produce a FunctionResult with the return value
            log.debug(dumps(results))
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
