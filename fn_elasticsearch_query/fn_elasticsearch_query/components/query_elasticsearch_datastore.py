# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'query_elasticsearch_datastore"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_elasticsearch_query", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_elasticsearch_query", {})

    @function("query_elasticsearch_datastore")
    def _query_elasticsearch_datastore_function(self, event, *args, **kwargs):
        """Function: Allows a user to query a specified ElasticSearch datastore for data."""
        try:
            # Get the function parameters:
            index = kwargs.get("index")  # text
            doc_type = kwargs.get("doc_type")  # text
            es_query = self.get_textarea_param(kwargs.get("es_query"))  # textarea

            log = logging.getLogger(__name__)
            log.info("index: %s", index)
            log.info("doc_type: %s", doc_type)
            log.info("es_query: %s", es_query)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()