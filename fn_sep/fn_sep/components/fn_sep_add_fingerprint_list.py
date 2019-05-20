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
    """Component that implements Resilient function 'fn_sep_add_fingerprint_list' of
    package fn_sep.

    The Function takes the following parameters:
            sep_fingerprintlist_name, sep_description, sep_domainid, sep_hash_value

    An example of a set of query parameter might look like the following:
            sep_fingerprintlist_name = 'Blacklist'
            sep_description = 'List of Hashes of type Malware MD5 Hash'
            sep_domainid = 'A9B4B7160946C25D24B6AA458EF5557F'
            sep_hash_value = 'A9B4B7160946C25D24B6AA458EF5557F'

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.
    {
        'inputs': {u'sep_description': u'Hash of type Malware MD5 Hash',
                   u'sep_fingerprintlist_name': u'Blacklist',
                   u'sep_hash_value': u'482F9B6E0CC4C1DBBD772AAAF088CB3A',
                   u'sep_domainid': u'A9B4B7160946C25D24B6AA458EF5557F'
                   },
        'metrics': {'package': 'fn-sep', 'timestamp': '2019-05-14 12:02:37', 'package_version': '1.0.0',
                    'host': 'myhost', 'version': '1.0', 'execution_time_ms': 1417
                    },
        'success': True,
        'content': {u'id': u'AB29BEA5333C488694B9533E65858BF2'},
        'raw': '{"id": "AB29BEA5333C488694B9533E65858BF2"}',
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

    @function("fn_sep_add_fingerprint_list")
    def _fn_sep_add_fingerprint_list_function(self, event, *args, **kwargs):
        """Function: Returns a list of computers with agents deployed on them. You can use parameters to narrow the search by IP address or hostname."""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}

            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_fingerprintlist_name = kwargs.get("sep_fingerprintlist_name")  # text
            sep_description = kwargs.get("sep_description")  # text
            sep_domainid = kwargs.get("sep_domainid")  # text
            sep_hash_value = kwargs.get("sep_hash_value")  # text

            log = logging.getLogger(__name__)
            log.info("sep_fingerprintlist_name: %s", sep_fingerprintlist_name)
            log.info("sep_description: %s", sep_description)
            log.info("sep_domainid: %s", sep_domainid)
            log.info("sep_hash_value: %s", sep_hash_value)

            yield StatusMessage("Running Symantec SEP Add Fingerprint List action ...")

            sep = Sepclient(self.options, params)

            rtn = sep.add_fingerprint_list(**params)
            if "errors" in rtn and rtn["errors"][0]["error_code"] == 409:
                # If this error was trapped user probably tried to re-add a hash to a fingerprint list.
                yield StatusMessage(
                    "Got a 410 error while attempting to get a fingerprint list for fingerprint name '{0}' "
                    "because of a possible invalid or deleted id.".format(sep_fingerprintlist_name))
            else:
                yield StatusMessage("Returning 'Symantec SEP Add Fingerprint List' results for fingerprint name '{}'."
                                    .format(sep_fingerprintlist_name))

            results = rp.done(True, rtn)

            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
