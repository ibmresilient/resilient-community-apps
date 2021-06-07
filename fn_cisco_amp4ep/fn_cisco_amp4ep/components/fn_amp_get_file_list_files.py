# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run a Cisco AMP for endpoints query - get file lists files """

# Set up:
# Destination: a Queue named "amp_get_file_list_files".
# Manual Action: Execute a REST query against a Cisco AMP for endpoints server.
import logging
import json
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_amp4ep.lib.amp_client import Ampclient
from fn_cisco_amp4ep.lib.helpers import validate_opts, validate_params, is_none
from fn_cisco_amp4ep.lib.amp_ratelimit import AmpRateLimit

RATE_LIMITER = AmpRateLimit()

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'amp_set_file_list_files' of
    package fn_cisco_amp4ep.

    The Function takes the following parameter:
        amp_file_list_guid, amp_file_sha256, amp_limit, amp_offset

    An example of a set of query parameter might look like the following:
            amp_file_list_guid  = "e773a9eb-296c-40df-98d8-bed46322589d"
            amp_file_sha256     = "8a68fc7ffd25e12cb92e3cb8a51bf219cada775baef73991bee384b3656fa284"
            amp_limit           = None
            amp_offset          = None

    The function will execute a REST api get request against a Cisco AMP for endpoints server and returns a result in
    JSON format similar to the following.
    {
      "input_params": {"file_list_guid": "e773a9eb-296c-40df-98d8-bed46322589d",
                       "file_sha256": "8a68fc7ffd25e12cb92e3cb8a51bf219cada775baef73991bee384b3656fa284", "limit": null,
                       "offset": null},
      "response": {u'version': u'v1.2.0',
                          u'data': {u'items': [],
                                    u'guid': u'9710a198-b95a-462a-b184-9e688968fd94',
                                    u'name': u'File Blacklist',
                                    u'policies': [{ u'guid': u'a98a0f97-4d54-4175-9eef-b8dee9c8e74b',
                                                    u'name': u'Audit',
                                                    u'links': {
                                                        u'policy': u'https://api.amp.cisco.com/v1/policies/a98a0f97-4d54-4175-9eef-b8dee9c8e74b'
                                                    }
                                                  },
                                                  { u'guid': u'fdf4c7f9-b0de-41bf-9d86-d0fae7aa5267',
                                                    u'name': u'Audit',
                                                    u'links': {
                                                        u'policy': u'https://api.amp.cisco.com/v1/policies/fdf4c7f9-b0de-41bf-9d86-d0fae7aa5267'
                                                    }
                                                  }
                                                ]
                                                },
                                                u'metadata': {u'results':
                                                                {u'index': 10,
                                                                    u'total': 1,
                                                                    u'items_per_page': 500,
                                                                    u'current_item_count': 0
                                                                },
                                                                u'links': {
                                                                    u'self': u'https://api.amp.cisco.com/v1/file_lists/e773a9eb-296c-40df-98d8-bed46322589d/files'
                                                                }
                                                            }
                                                        }
                                                },
      "query_execution_time": "2018-08-09 11:56:02"
    }
    """
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cisco_amp4ep", {})
        validate_opts(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_amp4ep", {})
        validate_opts(self)

    @function("fn_amp_get_file_list_files")
    def _fn_amp_get_file_list_files_function(self, event, *args, **kwargs):
        """Function: Returns a list of items for a particular file_list. You need to provide file_list_guid
        to retrieve these items."""
        try:
            # Get the function parameters:
            amp_file_list_guid = kwargs.get("amp_file_list_guid")  # text
            amp_file_sha256 = kwargs.get("amp_file_sha256")  # text
            amp_limit = kwargs.get("amp_limit")  # number
            amp_offset = kwargs.get("amp_offset")  # number

            log = logging.getLogger(__name__)
            log.info("amp_file_list_guid: %s", amp_file_list_guid)
            log.info("amp_file_sha256: %s", amp_file_sha256)
            log.info("amp_limit: %s", amp_limit)
            log.info("amp_offset: %s", amp_offset)

            if is_none(amp_file_list_guid):
                raise ValueError("Required parameter 'amp_file_list_guid' not set.")

            yield StatusMessage("Running Cisco AMP for endpoints get file lists files by guid...")

            params = {"file_list_guid": amp_file_list_guid, "file_sha256": amp_file_sha256, "limit": amp_limit,
                      "offset": amp_offset  }

            validate_params(params)

            amp = Ampclient(self.options, RATE_LIMITER)

            rtn = amp.get_paginated_total(amp.get_file_list_files, **params)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Add in "query_execution_time" and "ip_address" to result to facilitate post-processing.
            results = {"response": rtn, "query_execution_time": query_execution_time, "input_params": params}
            yield StatusMessage("Returning 'file list files' results for file list guid '{}'.".format(params["file_list_guid"]))

            log.debug(json.dumps(results))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Cisco AMP for endpoints.")
            yield FunctionError()