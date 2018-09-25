# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run a Bigfix Query against a Bigfix server for an endpoint and return
BigFix properties for the endpoint"""

# Set up:
# Destination: a Queue named "bigfix_assets".
# Manual Action: Execute a REST query against a BigFix server return endpoint properties.

import logging
from fn_bigfix.util.helpers import validate_opts, validate_params, create_attachment
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_bigfix.lib.bigfix_client import BigFixClient
import json
import os
import datetime

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_bigfix_assets' of package fn_bigfix.

        The Function does a BigFix query to retrieve properties of a BigFix endpoint and takes the following
        parameters:

            bigfix_asset_name, bigfix_asset_id, bigfix_incident_id


        An example of a set of query parameter might look like the following:

                bigfix_asset_name
                bigfix_asset_id
                bigfix_incident_id

        The BigFix Query will execute a REST call against a Bigfix server and the Function returns a result
        in JSON format similar to the following.

            {'status': 'OK',
             'att_name': u'bigfix-properties-DESKTOP-TUKM3HF-20180718.xml'
            }
        The Function will also create an attachment with a name similar to following:
            bigfix-properties-DESKTOP-TUKM3HF-20180718.xml
    """
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_bigfix", {})
        validate_opts(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_bigfix", {})
        validate_opts(self)

    @function("fn_bigfix_assets")
    def _fn_bigfix_assets_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Bigfix assets - Get properties in BigFix for an endpoint."""
        try:
            # Get the function parameters:
            bigfix_asset_name = kwargs.get("bigfix_asset_name")  # text
            bigfix_asset_id = kwargs.get("bigfix_asset_id")  # number
            bigfix_incident_id = kwargs.get("bigfix_incident_id")  # number

            log = logging.getLogger(__name__)
            log.info("bigfix_asset_name: %s", bigfix_asset_name)
            log.info("bigfix_asset_id: %s", bigfix_asset_id)
            log.info("bigfix_incident_id: %s", bigfix_incident_id)

            params = {"asset_name": bigfix_asset_name, "asset_id": bigfix_asset_id,
                      "incident_id": bigfix_incident_id}

            validate_params(params, "fn_bigfix_assets")

            yield StatusMessage("Running BigFix Query for Endpoint id {0}, with name {1} ..."
                                .format(params["asset_id"], params["asset_name"]))
            bigfix_client = BigFixClient(self.options)

            try:
                rest_client = self.rest_client()
                # Perform the BigFix Query
                response = bigfix_client.get_bf_computer_properties(params["asset_id"])
            except Exception as e:
                log.exception("Got exception while trying to query a BigFix asset.", e)
                yield StatusMessage("Got exception '{}' while trying to query a BigFix asset".format(type(e).__name__))
                raise Exception("Got exception '{}' while trying to query a BigFix asset".format(type(e).__name__))

            if not response:
                yield StatusMessage("No properties retrieved for the asset id '{}'".format(params["asset_id"]))
                results = {}
            else:
                # Create a Resilient attachment
                file_name = "bigfix-properties-" + params["asset_name"] + "-" + \
                            datetime.datetime.today().strftime('%Y%m%d') + ".xml"
                att_report = create_attachment(self.rest_client(), file_name, response, params)
                results = {"status": "OK", "att_name": att_report["name"]}

            yield StatusMessage("done...")

            log.debug(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
