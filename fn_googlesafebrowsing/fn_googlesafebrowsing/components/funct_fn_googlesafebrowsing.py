# -*- coding: utf-8 -*-

"""AppFunction implementation"""

import logging
import json
import re
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

PACKAGE_NAME = "fn_googlesafebrowsing"
FN_NAME = "fn_googlesafebrowsing"

LOG = logging.getLogger(__name__)

SB_CLIENT_ID = "Resilient"
SB_CLIENT_VER = "0.0.3"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_googlesafebrowsing'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def lookup_urls(self, fn_inputs):
        """
        Utility class to access the Google Safe Browsing Lookup API
        https://developers.google.com/safe-browsing/v4/get-started
        >>> sb = SafeBrowsingAPI(os.environ.get("SAFEBROWSING_API_KEY"))
        # {u'matches': [{u'threatType': u'SOCIAL_ENGINEERING', u'threatEntryType': u'URL', u'platformType': u'ANY_PLATFORM', u'threat': {u'url': u'ihaveaproblem.info'}, u'cacheDuration': u'300s'}]}
        >>> result = sb.lookup_urls("ihaveaproblem.info")
        >>> len(result["matches"]) > 0
        True
        """

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
                 'clientId': SB_CLIENT_ID,
                 'clientVersion': SB_CLIENT_VER
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
        
        response = self.rc.execute('post', '{}{}'.format(self.app_configs.googlesafebrowsing_url, self.app_configs.googlesafebrowsing_api_key), headers={'Content-Type': 'applciation/json'}, data=json.dumps(reqbody))

        results = response.json()

        yield self.status_message("Endpoint reached successfully and returning results for App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
