# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a Symantec SEPM action - assign fingerprint list to group. """

# Set up:
# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST action against a SYMANTEC SEPM server.
import json
import logging

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_sep.lib.sep_client import Sepclient
from fn_sep.lib.helpers import CONFIG_DATA_SECTION, transform_kwargs

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_assign_fingerprint_list_to_group' of
    package fn_sep.

    The Function takes the following parameters:
            sep_fingerprintlist_id, sep_group_id

    An example of a set of query parameter might look like the following:
            sep_fingerprintlist_id =
            sep_group_id =

    The function will execute a REST api get request against a SYMANTEC SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.

    {   'inputs': {u'sep_fingerprintlist_id': u'E60B061FDD844EBF9778D4BD2AC3942A', u'sep_groupid': u'7E4BB119A9FE9DC526EDABFB1EE261B8'},
        'metrics': {'package': 'fn-sep', 'timestamp': '2019-05-28 17:53:52', 'package_version': '1.0.0', 'host': 'myhost',
                   'version': '1.0', 'execution_time_ms': 1225},
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

    @function("fn_sep_assign_fingerprint_list_to_group")
    def _fn_sep_assign_fingerprint_list_to_group_function(self, event, *args, **kwargs):
        """Function: Assign a fingerprint list to a group for lock-down."""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}

            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_fingerprintlist_id = kwargs.get("sep_fingerprintlist_id")  # text
            sep_groupid = kwargs.get("sep_groupid")  # text

            LOG.info("sep_fingerprintlist_id: %s", sep_fingerprintlist_id)
            LOG.info("sep_groupid: %s", sep_groupid)

            validate_fields(["sep_fingerprintlist_id", "sep_groupid"], kwargs)

            yield StatusMessage("Running Symantec SEP Assign Fingerprint List to Group for Lock-down action ...")

            sep = Sepclient(self.options, params)

            rtn = sep.assign_fingerprint_list_to_group(**params)

            results = rp.done(True, rtn)

            if "errorCode" in rtn and int(rtn["errorCode"]) == 400:
                # If this error was trapped user probably tried to get an invalid fingerprint list.
                yield StatusMessage("Symantec SEP Assign Fingerprint List to Group for Lock-down: Got a 400 error "
                                    "while attempting to assign a fingerprint list for fingerprint id '{0}' because of a "
                                    "possible invalid or deleted fingerprintlist id.".format(sep_fingerprintlist_id))
            else:
                yield StatusMessage("Returning 'Symantec SEP Assign Fingerprint List to Group for Lock-down' results for "
                                    "fingerprintlist_id '{0}' and groupid '{1}'".format(sep_fingerprintlist_id, sep_groupid))

            LOG.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            LOG.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
