## -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run a ClamAV scan on a stream of data. """

# Set up:
# Destination: a Queue named "fn_clamav".
# Manual Action: Execute a ClamAV scan stream against file or attachment in Resilient.
import logging
import json
from io import BytesIO

import pyclamd

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_clamav.lib.helpers import validate_opts, validate_params, get_file_attachment
import fn_clamav.util.selftest as selftest

class FunctionPayload:
    """Class that contains the payload sent back to UI and available in the post-processing script"""

    def __init__(self, inputs):
        self.inputs = inputs
        self.file_name = None
        self.response = {}

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'clamav_scan_stream' of
    package fn_clamav.

    The Function takes the following parameters:
        clamav_base64content, clamav_file_name

    An example of a set of query parameter might look like the following:
            clamav_base64content  = "base64content: ..."
            clamav_file_name     = "eicar.txt"

    The function will stream  contents of a file to a ClamAV server to check for virus signature and returns a result
    in JSON format similar to the following.
    # Virus found:
        Result: {
                    "file_name": "eicar.txt",
                    "response": {"stream": ["FOUND", "Eicar-Test-Signature"]},
           }
    # No virus detected:
        Result: {
                    "file_name": "test.txt",
                    "response": {"stream": ["OK", '']},
           }
    # Got an error:
        Result: {
                    "file_name": "test.txt",
                    "response": {"stream": ["ERROR", '<reason>']},
        }
    """
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_clamav", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_clamav", {})

    @function("clamav_scan_stream")
    def _clamav_scan_stream_function(self, event, *args, **kwargs):
        """Function: Function to send a contents of a file as a data-stream to ClamAV to scan for viruses."""
        try:
            # Validate configuration settings.
            validate_opts(self)
            # Get the function parameters:

            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("attachment_id: %s", attachment_id)
            log.info("artifact_id: %s", artifact_id)

            payload = FunctionPayload({
                "incident_id": incident_id,
                "artifact_id": artifact_id,
                "task_id": task_id,
                "attachment_id": attachment_id
            })

            validate_params(payload.inputs, ['incident_id'])

            yield StatusMessage("Scanning attachment with ClamAV ...")
            # Decode input which is base64 format.
            attachment = get_file_attachment(self.rest_client(), incident_id, artifact_id, task_id, attachment_id)

            data_content = attachment["content"]

            # Setup ClamAV socket instance and test to see if we can connect.
            try:
                cd = pyclamd.ClamdNetworkSocket(host=str(self.options['host']),
                                                port=int(self.options['port']),
                                                timeout=int(self.options['timeout'])
                                                )
                cd.ping()
            except pyclamd.ConnectionError as e:
                log.exception("'Could not connect to ClamAV server network socket': exception type: %s,"
                              " msg: %s" % (e.__repr__(), getattr(e, 'message', str(e))))
                raise ValueError('Could not connect to ClamAV server network socket')

            payload.response = cd.scan_stream(BytesIO(data_content))
            #Assume we got here and we have an empty dict then no virus found return result in common format.
            if not payload.response:
                payload.response = {u"stream": ("OK",'Clean')}

            payload.file_name = attachment["filename"]

            if payload.response["stream"][0] == "ERROR":
                yield StatusMessage("ClamAV scan stream returned an 'ERROR': msg: '{}'.".format(payload.response["stream"][1]))
            else:
                # Add "file_name" values to results.
                yield StatusMessage(u"Returning ClamAV scan stream results for attachment name '{}'.".format(payload.file_name))

            log.debug(json.dumps(payload.as_dict()))

            # Produce a FunctionResult with the results
            yield FunctionResult(payload.as_dict())
            log.info("Complete")
        except Exception:
            log.exception("Exception in Resilient Function ClamAV scan stream.")
            yield FunctionError()