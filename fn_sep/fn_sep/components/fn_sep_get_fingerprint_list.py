# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a Symantec SEPM query - get fingerprint list. """

# Set up:
# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
import json
import logging

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_sep.lib.sep_client import Sepclient
from fn_sep.lib.helpers import CONFIG_DATA_SECTION, transform_kwargs

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_get_fingerprint_list' of
    package fn_sep.

    The Function takes the following parameter:
            sep_domainid, sep_fingerprintlist_name , sep_fingerprintlist_id

    An example of a set of query parameter might look like the following:
            sep_domainid = 'A9B4B7160946C25D24B6AA458EF5557F'
            sep_fingerprintlist_name = 'Blacklist_2'
            sep_fingerprintlist_id = None

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.

    {
          'inputs': {u'sep_fingerprintlist_name': u'Blacklist_2', u'sep_domainid': u'A9B4B7160946C25D24B6AA458EF5557F'},
          'metrics': {'package': 'fn-sep', 'timestamp': '2019-05-14 10:41:01', 'package_version': '1.0.0',
                      'host': 'myhost', 'version': '1.0', 'execution_time_ms': 1059},
          'success': True,
          'content': {u'description': u'Hash of type Malware MD5 Hash', u'hashType': u'MD5',
                      u'source': u'WEBSERVICE', u'groupIds': [],
                      u'data': [u'482F9B6E0CC4C1DBBD772AAAF088CB3A'],
                      u'id': u'D132F4BA85D64E9F941906C2ECBF3F5F',
                      u'name': u'Blacklist'},
          'raw': '{"description": "Hash of type Malware MD5 Hash", "hashType": "MD5",
                   "source": "WEBSERVICE", "groupIds": [],
                   "data": ["482F9B6E0CC4C1DBBD772AAAF088CB3A"],
                   "id": "D132F4BA85D64E9F941906C2ECBF3F5F",
                   "name": "Blacklist"}',
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

    @function("fn_sep_get_fingerprint_list")
    def _fn_sep_get_fingerprint_list_function(self, event, *args, **kwargs):
        """Function: Get the file fingerprint list for a specified name or id as a set of hash values."""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object.
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_domainid = kwargs.get("sep_domainid")  # text
            sep_fingerprintlist_name = kwargs.get("sep_fingerprintlist_name")  # text
            sep_fingerprintlist_id = kwargs.get("sep_fingerprintlist_id")  # text

            LOG.info("sep_domainid: %s", sep_domainid)
            LOG.info("sep_fingerprintlist_name: %s", sep_fingerprintlist_name)
            LOG.info("sep_fingerprintlist_id: %s", sep_fingerprintlist_id)

            validate_fields(["sep_domainid"], kwargs)

            yield StatusMessage("Running Symantec SEP Get File Fingerprint List query...")

            sep = Sepclient(self.options, params)
            rtn = sep.get_fingerprint_list(**params)

            results = rp.done(True, rtn)

            if "errorCode" in rtn and int(rtn["errorCode"]) == 410:
                # If this error was trapped user probably tried to get an invalid fingerprint list.
                yield StatusMessage(
                    u"Got a 410 error while attempting to get a fingerprint list for fingerprint name '{0}' and "
                    "domain id '{1}' because of a possible invalid or deleted id.".format(sep_fingerprintlist_name,
                                                                                          sep_domainid))
            else:
                yield StatusMessage(u"Returning 'Symantec SEP Get File Fingerprint List' results for fingerprint name "
                                    "'{0}' and domain id '{1}' .".format(sep_fingerprintlist_name, sep_domainid))

            LOG.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            LOG.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
