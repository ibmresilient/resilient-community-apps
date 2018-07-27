# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use,
"""Function implementation"""

import logging
import json
from ssl import create_default_context
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, \
FunctionResult, FunctionError
from elasticsearch import Elasticsearch
from fn_elasticsearch.util.helper import ElasticSearchHelper



class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_elasticsearch_query"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_elasticsearch", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_elasticsearch", {})

    @function("fn_elasticsearch_query")
    def _fn_elasticsearch_query_function(self, event, *args, **kwargs):
        """Function: Allows a user to query a specified ElasticSearch datastore for data."""
        try:

            yield StatusMessage("Starting")
            helper = ElasticSearchHelper(self.options)
            # Get Elasticsearch params
            ELASTICSEARCH_URL = helper.get_config_option("es_datastore_url")
            ELASTICSEARCH_CERT = helper.get_config_option("es_cafile", True)
            ELASTICSEARCH_SCHEME = helper.get_config_option("es_datastore_scheme", True)
            ELASTICSEARCH_USERNAME = helper.get_config_option("es_auth_username", True)
            ELASTICSEARCH_PASSWORD = helper.get_config_option("es_auth_password", True)
            # Get the function parameters:
            es_index = kwargs.get("es_index")  # text
            es_doc_type = kwargs.get("es_doc_type")  # text
            es_query = self.get_textarea_param(kwargs.get("es_query"))  # textarea

            log = logging.getLogger(__name__)
            log.info("index: %s", es_index)
            log.info("doc_type: %s", es_doc_type)
            log.info("es_query: %s", es_query)

            if not es_query:
                raise ValueError("An elasticsearch query is required")

            yield StatusMessage("Connecting to ElasticSearch...")

            '''

            verify_certs is set to false so self-signed certs won't throw an error
            cafile is the path to the cert; optional
            '''

            if not ELASTICSEARCH_CERT:
                yield StatusMessage("No Cafile found in app.config. Attempting connection without")
            try:
                if ELASTICSEARCH_SCHEME.lower() == 'https':
                    # Attempt to create an SSL context, should work fine if no CERT is provided
                    if ELASTICSEARCH_CERT is None:
                        context = create_default_context()
                    else:
                        context = create_default_context(cafile=ELASTICSEARCH_CERT)
                    # Connect to the ElasticSearch instance
                    es = Elasticsearch(ELASTICSEARCH_SCHEME.lower() + "://" + ELASTICSEARCH_URL, ssl_context=context, http_auth=(ELASTICSEARCH_USERNAME, ELASTICSEARCH_PASSWORD))
                else:
                    # Connect without to Elastic without HTTPS
                    es = Elasticsearch([ELASTICSEARCH_URL],
                                       verify_certs=False,
                                       cafile=ELASTICSEARCH_CERT)
            except:
                raise FunctionError("Encountered error while connecting to ElasticSearch")
            # Start query results as None
            query_results = None 

            try:
                es_results = es.search(index=es_index, doc_type=es_doc_type, body=es_query, ignore=[400, 404])
            except:
                raise FunctionError("Encountered error while submitting query to ElasticSearch")
            # If our results has a 'hits' attribute; inform the user
            if 'hits' in es_results:
                yield StatusMessage("Call to elasticsearch was successful. Returning results")
                # Could do some extra stuff with results here

                # Prepare the results object
                query_results = json.dumps(es_results["hits"]["hits"]) 
                
            # Check if we have a status attribute indicating an error we could raise
            elif 'status' in es_results:
                # If we encounter either a 404 (Not found) or 400 error return the reason
                
                if es_results['status'] in (400, 404):
                    # Can raise the root_cause of the failure
                    log.error(es_results["error"]["root_cause"])

                    if es_results['status'] is 400:
                        # es_results["error"]["root_cause"][1]["reason"] is only available on exceptions of type 400
                        raise FunctionError("Exception with code 400 encountered. Error: "+es_results["error"]["root_cause"][1]["reason"])
                    elif es_results['status'] is 404:
                        # Give reason that 404 happened; index not found?
                        raise FunctionError("Exception encounted during query :"+es_results["error"]["reason"])
                
           # Prepare the results object
            results = {
                "query_results": query_results,
                "success": (True if query_results is not None else False)
            }
            
            yield StatusMessage("done...")
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()