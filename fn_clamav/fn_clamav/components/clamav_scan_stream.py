## -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run a ClamAV scan on a stream of data. """

# Set up:
# Destination: a Queue named "clamav".
# Manual Action: Execute a ClamAV scan stream against file or attachment in Resilient.
import logging
import sys
import base64
import json
if sys.version_info.major == 2:
    from StringIO import StringIO
else:
    from io import StringIO

import pyclamd

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_clamav.lib.helpers import validate_opts, validate_params
import fn_clamav.util.selftest as selftest



class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'clamav_scan_stream' of
    package fn_clamav.

    The Function takes the following parameters:
        base64content, file_name

    An example of a set of query parameter might look like the following:
            base64content  = "base64content: ..."
            filre_name     = "eicar.txt"

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
        validate_opts(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_clamav", {})
        validate_opts(self)

    @function("clamav_scan_stream")
    def _clamav_scan_stream_function(self, event, *args, **kwargs):
        """Function: Function to send a contents of a file as a data-stream to ClamAV to scan for viruses."""
        try:
            # Get the function parameters:
            base64content = kwargs.get("base64content")  # text
            file_name = kwargs.get("file_name")  # text

            validate_params(('base64content', 'file_name'), kwargs)

            log = logging.getLogger(__name__)
            log.info("base64content: %s", base64content)
            log.info("file_name : %s", file_name)

            yield StatusMessage("Scanning attachment with ClamAV ...")
            # Decode input which is base64 format.
            data = base64.b64decode(base64content)
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

            rtn = cd.scan_stream(StringIO(data))
            #Assume we got here and we have an empty dict then no virus found retrun result in common format.
            if not rtn:
                rtn = {u"stream": ("OK",'')}
            # Add in "file_name" values to results.
            results = {"response": json.loads(json.dumps(rtn)),"file_name": file_name}
            yield StatusMessage("Returning ClamAV scan_stream results for attachment name '{}'.".format(file_name))

            log.debug(json.dumps(results))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Cisco AMP for endpoints.")
            yield FunctionError()