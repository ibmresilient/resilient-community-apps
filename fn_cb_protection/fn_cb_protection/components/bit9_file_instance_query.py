# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cb_protection.util.bit9_client import CbProtectClient, escape

log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'bit9_file_instance_query"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cb_protection", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cb_protection", {})

    @function("bit9_file_instance_query")
    def _bit9_file_instance_query_function(self, event, *args, **kwargs):
        """Function: Return file instance objects that match the given criteria."""
        try:
            # Get the function parameters:
            bit9_computer_id = kwargs.get("bit9_computer_id")  # number
            bit9_file_catalog_id = kwargs.get("bit9_file_catalog_id")  # number
            bit9_file_path = kwargs.get("bit9_file_path")  # text
            bit9_file_instance_localstate = kwargs.get("bit9_file_instance_localstate")  # number

            log.info(u"bit9_computer_id: %s", bit9_computer_id)
            log.info(u"bit9_file_catalog_id: %s", bit9_file_catalog_id)
            log.info(u"bit9_file_path: %s", bit9_file_path)
            log.info(u"bit9_file_instance_localstate: %s", bit9_file_instance_localstate)

            # At least the file catalog id or computer id must be specified.
            if bit9_computer_id is None and bit9_file_catalog_id is None:
                raise ValueError("At least the file catalog id or computer id must be specified.")

            # Construct the query string.
            query = []
            if bit9_computer_id:
                query.append(u"computerId:{}".format(bit9_computer_id))
            if bit9_file_catalog_id:
                query.append(u"fileCatalogId:{}".format(bit9_file_catalog_id))
            if bit9_file_path:
                query.append(u"pathName:{}".format(escape(bit9_file_path)))
            if bit9_file_instance_localstate:
                query.append(u"localState:{}".format(bit9_file_instance_localstate))
            bit9_query = u"&q=".join(query)
            bit9_client = CbProtectClient(self.options)
            results = bit9_client.query_file_instance(bit9_query)

            # Query results should be a list
            if isinstance(results, list):
                log.info("%d results", len(results))
                results = {
                    "count": len(results),
                    "item_list": results
                }
                log.debug(results)
            else:
                log.warn(u"Expected a list but received:")
                log.warn(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            log.error(err)
            yield FunctionError(err)
