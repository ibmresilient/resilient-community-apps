# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

import sys
import json
from fn_exchange_online.lib.ms_graph_helper import MSGraphHelper
from resilient_lib.components.integration_errors import IntegrationError

if sys.version_info.major == 2:
    from mock import patch
else:
    from unittest.mock import patch

MOCKED_OPTS = {
    "microsoft_graph_token_url": "microsoft_graph_token_url",
    "microsoft_graph_url": "microsoft_graph_url",
    "tenant_id": "tenant_id",
    "client_id": "client_id",
    "client_secret": "client_secret"
}

def generate_response(content, status):
    class simResponse:
        def __init__(self, content, status):
            self.status_code = status
            self.content = content
            self.text = json.dumps(content)

        def json(self):
            return self.content

    return simResponse(content, status)

class TestMSGraphHelper(object):
    """ Tests for the MSGraphHelper functions"""

    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.get')
    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.authenticate')
    def test_get_user_profile(self, authenticate_mock, get_mock):
        """ Test Get User Profile"""
        print("Test Get User Profile\n")
        content = {"displayName": "Tester"}

        try:
            authenticate_mock.return_value = True
            MS_graph_helper = MSGraphHelper(MOCKED_OPTS.get("microsoft_graph_token_url"),
                                            MOCKED_OPTS.get("microsoft_graph_url"),
                                            MOCKED_OPTS.get("tenant_id"),
                                            MOCKED_OPTS.get("client_id"),
                                            MOCKED_OPTS.get("client_secret"),
                                            None)

            get_mock.return_value = generate_response(content, 200)

            response = MS_graph_helper.get_user_profile("tester@example.com")
            assert response.status_code == 200
            assert response.content["displayName"] == "Tester"

            get_mock.return_value = generate_response(content, 404)
            response = MS_graph_helper.get_user_profile("tester@example.com")
            assert response.status_code == 404
            assert response.content["displayName"] == "Tester"

            get_mock.return_value = generate_response(content, 300)
            response = MS_graph_helper.get_user_profile("tester@example.com")

        except IntegrationError as err:
            assert True