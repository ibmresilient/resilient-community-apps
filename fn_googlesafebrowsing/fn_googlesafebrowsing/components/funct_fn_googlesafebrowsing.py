# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""AppFunction implementation"""

import logging
import json
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_googlesafebrowsing.lib import constants

PACKAGE_NAME = "fn_googlesafebrowsing"
FN_NAME = "fn_googlesafebrowsing"

LOG = logging.getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_googlesafebrowsing'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def lookup_urls(self, fn_inputs):
        """Lookup a URL"""

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        artifact_type = fn_inputs.googlesafebrowsing_artifact_type
        artifact_value = fn_inputs.googlesafebrowsing_artifact_value

        validate_fields([
            {"name": "googlesafebrowsing_api_key"},
            {"name": "googlesafebrowsing_url"}],
            self.app_configs)

        # SOAR will always send one artifact value at a time
        threat_entries = [{'url' : artifact_value}]

        LOG.info("Google Safe Browsing lookup started for Artifact Type %s - Artifact Value %s",
                 artifact_type, artifact_value)


        reqbody = {
            'client': {
                 'clientId': constants.SB_CLIENT_ID,
                 'clientVersion': constants.SB_CLIENT_VER
            },
            'threatInfo': {
                'threatTypes': ['THREAT_TYPE_UNSPECIFIED',
                             'MALWARE',
                             'SOCIAL_ENGINEERING',
                             'UNWANTED_SOFTWARE',
                             'POTENTIALLY_HARMFUL_APPLICATION'],
                'platformTypes': ['ANY_PLATFORM'],
                'threatEntryTypes': ['URL'],
                'threatEntries': threat_entries
            }
        }

        LOG.debug(reqbody)

        response = self.rc.execute('post', '{}{}'.format(self.app_configs.googlesafebrowsing_url,
                                    self.app_configs.googlesafebrowsing_api_key),
                                    headers={'Content-Type': 'application/json'},
                                    data=json.dumps(reqbody))

        results = response.json()

        yield self.status_message("Endpoint reached successfully and returning results for App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
