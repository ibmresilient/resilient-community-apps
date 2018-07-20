# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_elasticsearch_query.util.helper import ElasticSearchHelper
from elasticsearch import Elasticsearch
from ssl import create_default_context

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
            ELASTICSEARCH_CERT = helper.get_config_option("es_cafile", True)
            # Get the function parameters:
            index = kwargs.get("index")  # text
            doc_type = kwargs.get("doc_type")  # text
            es_query = self.get_textarea_param(kwargs.get("es_query"))  # textarea

            if not ELASTICSEARCH_CERT:
                yield StatusMessage("No Cafile found in app.config. Attempting connection without")
            
            log = logging.getLogger(__name__)
            log.info("index: %s", index)
            log.info("doc_type: %s", doc_type)
            log.info("es_query: %s", es_query)

            # TODO: Remove these logs before finishing
            log.info("es_datastore_url: %s", ELASTICSEARCH_URL)
            log.info("es_cafile: %s", ELASTICSEARCH_CERT)

            if not es_query:
                raise ValueError("An elasticsearch query is required")

            yield StatusMessage("Connecting to ElasticSearch...")

            '''

            verify_certs is set to false so self-signed certs won't throw an error
            cafile is the path to the cert; optional
            '''
            es = Elasticsearch([ELASTICSEARCH_URL], 
                verify_certs=False,
                cafile=ELASTICSEARCH_CERT)

            # Optional, Yield the cluster name
            cluster_name = es.info()['cluster_name']
            yield StatusMessage("ElasticSearch cluster_name:"+cluster_name)

            es_results = es.search(index=index, doc_type=doc_type,body=es_query, ignore=[400, 404])
            #log.info(es_results)

            # If our results has a 'hits' attribute; inform the user
            if 'hits' in es_results:
                yield StatusMessage("Call to elasticsearch was successful. Returning results")
            
                
            
            query_results = json.dumps(es_results["hits"]["hits"])

            # TODO: Remove before finishing
            yield StatusMessage(query_results)
            # Prepare the results object
            results = {
                "query_results": query_results
            }
            yield StatusMessage("done...")
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()