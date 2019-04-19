# -*- coding: utf-8 -*-
# (c) Copyright IBM Corporation 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'URLHaus lookup"""

    HTTP_HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}
    JSON_HEADERS = {"Content-Type": "application/json"}
    INTEGRATION_NAME = "fn_urlhaus"

    # convert artifact type to type of API call to make
    TYPE_LOOKUP = {
        "DNS Name": "host",
        "IP Address": "host",
        "Malware MD5 Hash": "payload:md5_hash",
        "Malware SHA-256 Hash": "payload:sha256_hash",
        "Server Name": "host",
        "String": "tag",
        "URL": "url"
    }

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(FunctionComponent.INTEGRATION_NAME, {})
        self.url = self.options.get("url")
        self.submit_url = self.options.get("submit_url")
        self.api_key = self.options.get("submit_api_key")

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(FunctionComponent.INTEGRATION_NAME, {})
        self.url = self.options.get("url")
        self.submit_url = self.options.get("submit_url")
        self.api_key = self.options.get("submit_api_key")

    @function("fn_urlhaus")
    def _urlhaus_lookup(self, event, *args, **kwargs):
        """Function: Takes different artifacts such as URLs, domain names, IP addresses and hashes and sends it to urlhaus for analysis"""
        try:
            # Get the function parameters:
            artifact_value = kwargs.get("urlhaus_artifact_value")  # text
            artifact_type = kwargs.get("urlhaus_artifact_type")    # text

            log = logging.getLogger(__name__)
            log.info("artifact_value: %s", artifact_value)
            log.info("artifact_type: %s", artifact_type)

            # build a std payload
            payload_builder = ResultPayload(FunctionComponent.INTEGRATION_NAME, **self.options)

            submission_url, submission_payload = self.build_submission_payload(artifact_type, artifact_value)

            rc = requests.post(submission_url, submission_payload, headers=FunctionComponent.HTTP_HEADERS)
            if rc.status_code != 200:
                raise FunctionError(rc.status)

            yield StatusMessage("Query Status: {}".format(rc.json()["query_status"]))

            results_payload = payload_builder.done(True, rc.json())

            # Produce a FunctionResult with the results
            yield FunctionResult(results_payload)
        except Exception:
            yield FunctionError()

    def build_submission_payload(self, artifact_key, artifact_value):
        """
        transform an artifact type into the proper url and payload to submit
        :param artifact_key:
        :param artifact_value:
        :return:
        """
        lookup_type = FunctionComponent.TYPE_LOOKUP.get(artifact_key)
        if not lookup_type:
            raise KeyError("Unable to lookup: {}".format(artifact_key))

        lookup_type_parts = lookup_type.split(':')
        build_url = "/".join((self.url, lookup_type_parts[0]))

        part = lookup_type_parts[1] if len(lookup_type_parts) == 2 else lookup_type_parts[0]

        payload = { part: artifact_value }

        return build_url, payload

    @function("fn_urlhaus_submission")
    def _urlhaus_submission(self, event, *args, **kwargs):
        """Function: Takes a url and submits it to urlhaus as distributing malware"""
        try:
            # Get the function parameters:
            artifact_url = kwargs.get("urlhaus_artifact_value")  # text

            log = logging.getLogger(__name__)
            log.info("artifact_value: %s", artifact_url)

            payload_builder = ResultPayload(FunctionComponent.INTEGRATION_NAME, **self.options)

            jsonData = {
                'token' : self.api_key,
                'anonymous' : '0',
                'submission' : [
                    {
                        'url' : artifact_url,
                        'threat' : 'malware_download'
                    }
                ]
            }

            rc = requests.post(self.submit_url, json=jsonData, headers=FunctionComponent.JSON_HEADERS)

            if rc.status_code != 200:
                raise FunctionError(rc.status)

            results_payload = payload_builder.done(True, rc.text)

            # Produce a FunctionResult with the results
            yield FunctionResult(results_payload)
        except Exception:
            yield FunctionError()
