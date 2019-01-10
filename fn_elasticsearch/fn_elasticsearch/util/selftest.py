# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Function implementation
   test with: resilient-circuits selftest -l fn-elasticsearch
"""

import logging
from ssl import create_default_context
from elasticsearch import Elasticsearch


from fn_elasticsearch.util.helper import ElasticSearchHelper


def selftest_function(opts):
    """
    A self test function which attempts to set up a connection with your ElasticSearch instance and then ping it.
    The self test attempts to use as much code from the function as possible to mimic the functionality.

    Success state is achieved if both a connection is made and a succesful ping is done after this.
    """
    helper = ElasticSearchHelper(opts.get("fn_elasticsearch", {}))
    # Get Elasticsearch params
    ELASTICSEARCH_URL = helper.get_config_option("es_datastore_url")
    ELASTICSEARCH_CERT = helper.get_config_option("es_cafile", True)
    ELASTICSEARCH_SCHEME = helper.get_config_option("es_datastore_scheme", True)
    ELASTICSEARCH_USERNAME = helper.get_config_option("es_auth_username", True)
    ELASTICSEARCH_PASSWORD = helper.get_config_option("es_auth_password", True)

    log = logging.getLogger(__name__)

    log.info("Connecting to ElasticSearch...")

    if not ELASTICSEARCH_CERT:
       log.info("No Cafile found in app.config. Attempting connection without")
    try:
        if ELASTICSEARCH_SCHEME.lower() == 'https':
            # Attempt to create an SSL context, should work fine if no CERT is provided
            if ELASTICSEARCH_CERT is None:
                context = create_default_context()
            else:
                context = create_default_context(cafile=ELASTICSEARCH_CERT)
            # Connect to the ElasticSearch instance
            es = Elasticsearch(ELASTICSEARCH_SCHEME.lower() + "://" + ELASTICSEARCH_URL, ssl_context=context,
                               http_auth=(ELASTICSEARCH_USERNAME, ELASTICSEARCH_PASSWORD))
        else:
            # Connect without to Elastic without HTTPS
            es = Elasticsearch([ELASTICSEARCH_URL],
                               verify_certs=False,
                               cafile=ELASTICSEARCH_CERT)

        try:
            # If we cant ping the ES instance we can't query it
            if not es.ping():
                return {"state": "failed",
                        "reason": "Could not Ping the ElasticSearch instance. Your host may be down or your config is needs changing"}
            else:
                # We can ping the ES instance so selftest passes
                return {"state": "success"}

        # Catch exceptions for when the es service is down, sometimes an exception is returned rather than False
        except Exception as e:
            return {"state": "failed",
                    "reason": "Could not Ping the ElasticSearch instance, there may be an issue with your config. Reason : {0}".format(e)}

    except Exception as e:
        return {"state": "failed",
                "reason": "Encountered error while connecting to ElasticSearch. Please check your config. Reason {0}".format(e)}
