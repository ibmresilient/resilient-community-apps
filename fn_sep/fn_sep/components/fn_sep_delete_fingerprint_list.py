# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a Symantec SEPM query - get fingerprint list """

# Set up:
# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
import json
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_sep.lib.sep_client import Sepclient
from resilient_lib import ResultPayload
from fn_sep.lib.helpers import transform_kwargs

CONFIG_DATA_SECTION = "fn_sep"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_delete_fingerprint_list' of
    package fn_sep.

    The Function takes the following parameters:
            sep_fingerprintlist_id

    An example of a set of query parameter might look like the following:
            sep_fingerprintlist_id = '2728515A08A4481B8207623558254F60'

    The function will execute a REST api get request against a SYMANTEC SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.

    {
        'inputs': {u'sep_fingerprintlist_id': u'2728515A08A4481B8207623558254F60'},
        'metrics': {'package': 'fn-sep', 'timestamp': '2019-05-14 11:49:38', 'package_version': '1.0.0',
                    'host': 'myhost', 'version': '1.0', 'execution_time_ms': 1137
                    },
         'success': True,
         'content': '',
         'raw': '""',
         'reason': None,
         'version': '1.0'
    }
    """
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("fn_sep_delete_fingerprint_list")
    def _fn_sep_delete_fingerprint_list_function(self, event, *args, **kwargs):
        """Function: Returns a list of computers with agents deployed on them. You can use parameters to narrow the search by IP address or hostname."""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}

            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_fingerprintlist_id = kwargs.get("sep_fingerprintlist_id")  # text


            log = logging.getLogger(__name__)
            log.info("sep_fingerprintlist_id: %s", sep_fingerprintlist_id)

            yield StatusMessage("Running Symantec SEP Delete Fingerprint List action ...")

            sep = Sepclient(self.options, params)
            rtn = sep.delete_fingerprint_list(**params)

            results = rp.done(True, rtn)

            if "errors" in rtn and rtn["errors"][0]["error_code"] == 410:
                # If this error was trapped user probably tried to get information on invalid connector guid.
                yield StatusMessage(
                    "Got a 410 error while attempting to delete fingerprint list fingerprint id  '{0}' "
                    "because of a possible deleted id.".format(params["sep_fingerprintlist_id"]))
            else:
                yield StatusMessage("Returning 'Symantec SEP Delete Fingerprint List' results for fingerprint id '{}'."
                                    .format(sep_fingerprintlist_id))

            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
