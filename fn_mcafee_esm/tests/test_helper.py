import json


def string_test_config():
    return u"""[fn_mcafee_esm]
esm_url=https://mockesmurl.com
esm_username=fake_user
esm_password=fake_password
trust_cert=False
"""


def get_test_config():
    config = {
        "esm_url": "https://mockesmurl.com",
        "esm_username": "fake_user",
        "esm_password": "fake_password",
        "trust_cert": "False"
    }
    return config


def get_default_test_config():
    config = {
        "esm_url": "<your_esm_url>",
        "esm_username": "<your_esm_username>",
        "esm_password": "<your_esm_password>",
        "trust_cert": "[True|False]"
    }
    return config


def generate_response(content, status):
    class simResponse:
        def __init__(self, content, status):
            self.status_code = status
            self.content = content
            self.text = json.dumps(content)
            self.cookies = {"JWTToken": "mock_cookie_token"}
            self.headers = {"Xsrf-Token": "mock_header_token"}

        def json(self):
            return self.content

    return simResponse(content, status)
