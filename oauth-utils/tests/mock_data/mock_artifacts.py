# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Generate Mock responses to simulate ZIA for Unit and function tests """
from requests.models import Response
import json
import re

mocked_response = '{\n  "access_token": "07Gd6TUwZA_INCgYIARAAGAcSNwF",\n  "expires_in": 3599,\n  "refresh_token": "1//07Gd6TUwZA_INCgYIARAAGAcSNwF",\n  "scope": "https://test.ibm.com/SMTP.Send",\n  "token_type": "Bearer"\n}'

# This method will be used by the mock to replace requests.post
def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, content, status_code):
            self.content = content
            self.status_code = status_code

        def json(self):
            return json.loads(self.content)

    return MockResponse(mocked_response, 200)

# This method will be used by the mock to replace OAuth2
def mocked_oauth2(*args, **kwargs):
    class MockResponse:
        def __init__(self, content, status_code):
            pass

        def json(self):
            return json.loads(self.content)

    return MockResponse(mocked_response, 200)