# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_elasticsearch_query.util.helper import ElasticSearchHelper
from elasticsearch import Elasticsearch

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

            yield StatusMessage("Starting")
            helper = ElasticSearchHelper(self.options)
            # Get Elasticsearch params 
            ELASTICSEARCH_URL = helper.get_config_option("es_datastore_url")
            # Get the function parameters:
            index = kwargs.get("index")  # text
            doc_type = kwargs.get("doc_type")  # text
            es_query = self.get_textarea_param(kwargs.get("es_query"))  # textarea

            
            log = logging.getLogger(__name__)
            log.info("index: %s", index)
            log.info("doc_type: %s", doc_type)
            log.info("es_query: %s", es_query)
            log.info("es_datastore_url: %s", ELASTICSEARCH_URL)

            if not es_query:
                raise ValueError("An elasticsearch query is required")

            yield StatusMessage("Connecting to ElasticSearch...")
            es = Elasticsearch([ELASTICSEARCH_URL])
            cluster_name = es.info()['cluster_name']
            yield StatusMessage("ElasticSearch cluster_name:"+cluster_name)

            es_results = es.search(index=index, doc_type=doc_type,body=es_query)
            log.info(es_results)
            # If our results has a 'hits' attribute; inform the user
            if es_results["hits"]:
                yield StatusMessage("Call to elasticsearch was successful. Returning results")
            
                
            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")
            query_results = json.dumps(es_results["hits"]["hits"])
            yield StatusMessage(query_results)

            results = {
                "query_results": query_results
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()