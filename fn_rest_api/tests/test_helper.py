import pytest, unittest, logging

from requests.exceptions import HTTPError

from fn_rest_api.lib import helper
from urllib.error import URLError
from fn_rest_api.lib.helper import (validate_url,
    render_dict_components, build_dict, make_rest_call)

from resilient_lib import IntegrationError


def test_constants():
    assert helper.CONTENT_TYPE == "content-type"
    assert helper.CONTENT_TYPE_JSON == "application/json"

def test_str_dict_to_py_dict():
    processed_value = {"test_input" : {"sample1" : "normal plain text"}}
    render_dict_components(processed_value, {}),
    assert processed_value == {"test_input" : {'sample1': 'normal plain text'}}

def test_json_dict():
    # String to dict using json decoder
    processed_value = {"test_input" :  """ {"key" : "json text"} """}
    render_dict_components(processed_value, {}),
    assert processed_value == {"test_input" : {'key': 'json text'}}

def test_json_dict_with_none():
    # Null handling using json decoder
    processed_value = {"test_input" :  """ {"key" :  null} """}
    render_dict_components(processed_value, {}),
    assert processed_value == {"test_input" : {'key': None}}

def test_json_dict_multiline():
    # Multi-line string with to dict with \n character using json decoder
    processed_value = {"test_input" :  """ {"key1" : "multi line json text1",
        "key2" : "multi line json text2"}"""}
    render_dict_components(processed_value, {}),
    assert processed_value == {"test_input" : {'key1': 'multi line json text1', 'key2': 'multi line json text2'}}

def test_simple_dict():
    # Simple new line kv-pair to string
    processed_value = {"test_input" : """ key1 : new line separated text 1
        key2 : new line separated text 2 """}
    render_dict_components(processed_value, {})
    assert processed_value == {"test_input" : {'key1': 'new line separated text 1',
    'key2': 'new line separated text 2'}}

def test_simple_dict_with_leading_new_line():
    # Simple new line kv-pair with leading blank line to dict
    processed_value = {"test_input" : """
        key1 : new line separated text 1
        key2 : new line separated text 2 """}
    render_dict_components(processed_value, {})
    assert processed_value == {"test_input" : {'key1': 'new line separated text 1',
    'key2': 'new line separated text 2'}}

def test_simple_dict_with_numbers():
    # Simple new line kv-pair with numbers and decimals to dict
    processed_value = {"test_input" : """
        key1 : 1234
        key2 : 22.2345 """}
    render_dict_components(processed_value, {})
    assert processed_value == {"test_input" : {'key1': '1234',
    'key2': '22.2345'}}

def test_none_handling():
    # None handling
    processed_value = {"test_input" : None}
    render_dict_components(processed_value, {})
    assert processed_value == {"test_input" : None}

def test_empty_string():
    # Empty string
    processed_value = {"test_input" : ""}
    render_dict_components(processed_value, {})
    assert processed_value ==     {"test_input" : ""}

def test_json_dict_value_sub():
    processed_value = {"test_input" : """{"sample1" : "normal {{TO_BE_SUBED}}"}"""}
    render_dict_components(processed_value, {"TO_BE_SUBED" : "plain text but substituted"}),
    assert processed_value == {"test_input" : {'sample1': 'normal plain text but substituted'}}

def test_simple_dict_with_leading_new_line_and_sub():
    # Multiline kv pair with multiple secret substitutions
    processed_value = {"test_input" : """
        key1 : new line separated {{SECRET_001}} {{SECRET_002}}
        key2 : new line separated {{SECRET_002}} {{SECRET_001}}
        {{SECRET_KEY}} : new line separated secret
        {{SECRET_key}} : {{SECRET_value}}"""}

    render_dict_components(processed_value, {
        "SECRET_key"   : "thisisakey",
        "SECRET_001"   : "testsecret1",
        "SECRET_002"   : "testsecret@!$%^2",
        "SECRET_KEY"   : " test KEY ",
        "SECRET_value" : "testvaluesecret"})

    assert processed_value == {"test_input" : {
    'key1': 'new line separated testsecret1 testsecret@!$%^2',
    'key2': 'new line separated testsecret@!$%^2 testsecret1',
    'test KEY' : 'new line separated secret',
    "thisisakey" : "testvaluesecret"}}

def test_simple_dict_with_blank_lines():
    # Simple new line kv-pair with multiple blank lines to dict
    processed_value = {"test_input" : """

        key1 : new line separated text 1

        key2 : new line separated text 2

    """}
    render_dict_components(processed_value, {})
    assert processed_value == {"test_input" : {'key1': 'new line separated text 1',
    'key2': 'new line separated text 2'}}

def test_simple_dict_with_symbols():
    # Simple new line kv-pair with symbols to dict
    processed_value = {"test_input" : """

        key1 : new !@#$/%/%^^$#@!@#$!%

        key2 : new line separated text 2
    """}
    render_dict_components(processed_value, {})
    assert processed_value == {"test_input" : {'key1': 'new !@#$/%/%^^$#@!@#$!%',
    'key2': 'new line separated text 2'}}



def test_build_json_dict_basic():
    # String to dict using json decoder
    processed_value = build_dict(""" {"key" : "json text"} """)
    assert processed_value == {'key': 'json text'}

def test_build_json_dict_with_none():
    # Null handling using json decoder
    processed_value = build_dict(""" {"key" :  null} """)
    assert processed_value == {'key': None}

def test_build_json_dict():
    # Multi-line string to dict using json decoder
    processed_value = build_dict(""" {"key1" : "multi line json text1", "key2" : "multi line json text2"}""")
    assert processed_value == {'key1': 'multi line json text1', 'key2': 'multi line json text2'}

def test_build_json_dict_multiline():
    # Multi-line string with to dict with \n character using json decoder
    processed_value = build_dict(""" {"key1" : "multi line json text1",
                        "key2" : "multi line json text2"}""")
    assert processed_value == {'key1': 'multi line json text1', 'key2': 'multi line json text2'}

def test_build_simple_dict():
    # Simple new line kv-pair to string
    processed_value = build_dict(""" key1 : new line separated text 1
        key2 : new line separated text 2 """)
    assert processed_value == {'key1': 'new line separated text 1',
            'key2': 'new line separated text 2'}

def test_build_simple_dict_with_leading_new_line():
    # Simple new line kv-pair with leading blank line to dict
    processed_value = build_dict("""
        key1 : new line separated text 1
        key2 : new line separated text 2 """)
    assert processed_value == {'key1': 'new line separated text 1',
            'key2': 'new line separated text 2'}

def test_build_simple_dict_with_numbers():
    # Simple new line kv-pair with numbers and decimals to dict
    processed_value = build_dict("""
        key1 : 1234
        key2 : 22.2345 """)
    assert processed_value == {'key1': '1234',
            'key2': '22.2345'}

def test_build_none_handling():
    # None handling
    processed_value = build_dict("")
    assert processed_value == ""

def test_build_empty_string():
    # Empty string
    processed_value = build_dict(None)
    assert processed_value == {}

def test_valid_url():
    # Http adapter
    url_http = "http://www.example.com/uk-en"
    assert url_http == validate_url(url_http)

    # Https adapter
    url_https = "https://www.example.com/uk-en"
    validate_url(url_https)

def test_missing_invalid_adapter():
    # Missing adapter
    with pytest.raises(URLError) as err:
        validate_url("www.ibm.com/uk-en")

    # Invalid adapter
    with pytest.raises(URLError) as err:
        validate_url("hppt:www.ibm.com/uk-en")

def test_missing_schema():
    # missing schema
    with pytest.raises(URLError) as err:
        validate_url('www.example.com')

def test_missing_netloc():
    # missing netloc
    with pytest.raises(URLError) as err:
        validate_url('https://')

def test_missing_value():
    # empty string in url
    assert validate_url('') == None

def test_none_value():
    # None in url
    assert validate_url(None) == None

def test_empty_dict_value():
    # None in url
    assert validate_url({}) == None

def test_request_retry(caplog):
    RETRY_TRIES_COUNT   = 4
    RETRY_DELAY_COUNT   = .2
    RETRY_BACKOFF_COUNT = 3
    ENDPOINT = "https://postman-echo.com/status/404"

    caplog.set_level(logging.INFO)

    with pytest.raises(IntegrationError):
        make_rest_call(
            {}, {},
            method="GET",
            url=ENDPOINT,
            headers={},
            cookies={},
            body={},
            params=None,
            retry_tries=RETRY_TRIES_COUNT,
            retry_delay=RETRY_DELAY_COUNT,
            retry_backoff=RETRY_BACKOFF_COUNT,
            verify=True,
            timeout=60,
            clientauth=None)
    # For these values: RETRY_TRIES_COUNT = 4   RETRY_DELAY_COUNT = 2   RETRY_BACKOFF_COUNT = 3
    # requests must be executed in the following order:
    # failed request 1, retrying in .2 seconds...
    # failed request 2, retrying in .6 seconds...
    # failed request 3, retrying in 1.8 seconds...
    # request 4
    records = list(caplog.records)
    assert len(records) == RETRY_TRIES_COUNT * 2
    assert f"retrying in {RETRY_DELAY_COUNT} seconds..." in records[1].message
    assert f"retrying in {RETRY_DELAY_COUNT * RETRY_BACKOFF_COUNT} seconds..." in records[3].message
    assert f"retrying in {RETRY_DELAY_COUNT * RETRY_BACKOFF_COUNT * RETRY_BACKOFF_COUNT} seconds..." in records[5].message
    assert "404 Client Error:" in records[7].message

class TestMakeRestCall(unittest.TestCase):

    class MockResponse:
        def __init__(self, url, reason, status_code):
            self.url = url
            self.reason = reason
            self.status_code = status_code

        def raise_for_status(self):
            http_error_msg = ""
            if 400 <= self.status_code < 500:
                http_error_msg = (
                    f"{self.status_code} Client Error: {self.reason} for url: {self.url}")
            elif 500 <= self.status_code < 600:
                http_error_msg = (
                    f"{self.status_code} Server Error: {self.reason} for url: {self.url}")
            if http_error_msg:
                raise HTTPError(http_error_msg, response=self)

    class MockRC:
        def __init__(self, opts, options):
            self.status_code = None

        def execute(self,
            method, url, headers,
            cookies, verify=False,
            timeout=0, clientauth=None,
            callback=None, json=None, data=None,
            params=None, retry_tries=None,
            retry_delay=None, retry_backoff=None):

            if isinstance(method, int):
                response = TestMakeRestCall.MockResponse(url, "request failed", method)
                callback(response)
            return {
                "method"  : method,
                "url"     : url,
                "headers" : headers,
                "cookies" : cookies,
                "verify"  : verify,
                "timeout" : timeout,
                "params"  : params,
                "tries"   : retry_tries,
                "delay"   : retry_delay,
                "backoff" : retry_backoff,
                "json"    : json,
                "data"    : data,
                "clientauth" : clientauth}

    opts, options = {}, {}
    method = "GET"
    url = "http://www.example.com"

    def test_standard_request(self):
        helper.RequestsCommon = self.MockRC
        response = make_rest_call(
            self.opts, self.options,
            method=self.method,
            url=self.url,
            headers={"key1" : "header1"},
            cookies={"key1" : "cookie1"},
            body={"key1" : "body1"},
            params=None,
            retry_tries=None,
            retry_delay=None,
            retry_backoff=None,
            verify=True,
            timeout=60,
            clientauth=""" NOT A CERTIFICATE """)

        assert response["url"] == self.url
        assert response["method"] == self.method
        assert response["verify"]
        self.assertDictEqual(response["headers"], {"key1" : "header1"})
        self.assertDictEqual(response["cookies"], {"key1" : "cookie1"})
        self.assertDictEqual(response["data"], {"key1" : "body1"})
        self.assertEqual(response["tries"], None)
        self.assertEqual(response["delay"], None)
        self.assertEqual(response["backoff"], None)
        self.assertIsNone(response["json"])
        self.assertEqual(response["timeout"], 60)
        self.assertEqual(response["clientauth"], """ NOT A CERTIFICATE """)
        self.assertIsNone(response["json"])

    def test_json_request(self):
        helper.RequestsCommon = self.MockRC
        response = make_rest_call(
            self.opts, self.options,
            method=self.method,
            url=self.url,
            headers={"Content-type" : "application/json"},
            cookies=None,
            body={"key1" : "body1"},
            params=None,
            retry_tries=None,
            retry_delay=None,
            retry_backoff=None,
            verify=None,
            timeout=None,
            clientauth=None)

        assert response["url"] == self.url
        assert response["method"] == self.method
        self.assertDictEqual(response["headers"], {"Content-type" : "application/json"})
        self.assertDictEqual(response["json"], {"key1" : "body1"})
        self.assertIsNone(response["data"])

    def test_json_lowercase_content_type(self):
        helper.RequestsCommon = self.MockRC
        response = make_rest_call(
            self.opts, self.options,
            method=self.method,
            url=self.url,
            headers={"content-type" : "application/json"},
            cookies=None,
            body={"key1" : "body1"},
            params=None,
            retry_tries=None,
            retry_delay=None,
            retry_backoff=None,
            verify=None,
            timeout=None,
            clientauth=None)
        assert response["url"] == self.url
        assert response["method"] == self.method
        self.assertDictEqual(response["headers"], {"content-type" : "application/json"})
        self.assertDictEqual(response["json"], {"key1" : "body1"})
        self.assertIsNone(response["data"])

    def test_json_uppercase_content_type(self):
        helper.RequestsCommon = self.MockRC
        response = make_rest_call(
            self.opts, self.options,
            method=self.method,
            url=self.url,
            headers={"CONTENT-TYPE" : "application/json"},
            cookies=None,
            body={"key1" : "body1"},
            params=None,
            retry_tries=None,
            retry_delay=None,
            retry_backoff=None,
            verify=None,
            timeout=None,
            clientauth=None)
        assert response["url"] == self.url
        assert response["method"] == self.method
        self.assertDictEqual(response["headers"], {"CONTENT-TYPE" : "application/json"})
        self.assertDictEqual(response["json"], {"key1" : "body1"})
        self.assertIsNone(response["data"])

    def test_json_title_content_type(self):
        helper.RequestsCommon = self.MockRC
        response = make_rest_call(
            self.opts, self.options,
            method=self.method,
            url=self.url,
            headers={"Content-Type" : "application/json"},
            cookies=None,
            body={"key1" : "body1"},
            params=None,
            retry_tries=None,
            retry_delay=None,
            retry_backoff=None,
            verify=None,
            timeout=None,
            clientauth=None)
        assert response["url"] == self.url
        assert response["method"] == self.method
        self.assertDictEqual(response["headers"], {"Content-Type" : "application/json"})
        self.assertDictEqual(response["json"], {"key1" : "body1"})
        self.assertIsNone(response["data"])

    def test_json_mixed_content_type(self):
        helper.RequestsCommon = self.MockRC
        response = make_rest_call(
            self.opts, self.options,
            method=self.method,
            url=self.url,
            headers={"CoNtEnt-TyPe" : "application/json"},
            cookies=None,
            body={"key1" : "body1"},
            params=None,
            retry_tries=None,
            retry_delay=None,
            retry_backoff=None,
            verify=None,
            timeout=None,
            clientauth=None)
        assert response["url"] == self.url
        assert response["method"] == self.method
        self.assertDictEqual(response["headers"], {"CoNtEnt-TyPe" : "application/json"})
        self.assertDictEqual(response["json"], {"key1" : "body1"})
        self.assertIsNone(response["data"])

    def test_data_content_type(self):
        helper.RequestsCommon = self.MockRC
        response = make_rest_call(
            self.opts, self.options,
            method=self.method,
            url=self.url,
            headers={"ctype" : "application/json"},
            cookies=None,
            body={"key1" : "body1"},
            params=None,
            retry_tries=None,
            retry_delay=None,
            retry_backoff=None,
            verify=None,
            timeout=None,
            clientauth=None)
        assert response["url"] == self.url
        assert response["method"] == self.method
        self.assertDictEqual(response["headers"], {"ctype" : "application/json"})
        self.assertDictEqual(response["data"], {"key1" : "body1"})
        self.assertIsNone(response["json"])

    def test_request_raises_exceptions(self):
        helper.RequestsCommon = self.MockRC
        with pytest.raises(HTTPError) as err:
            make_rest_call(
                self.opts, self.options,
                method=400,
                url=self.url,
                headers=None,
                cookies=None,
                body=None,
                params=None,
                retry_tries=None,
                retry_delay=None,
                retry_backoff=None,
                verify=None,
                timeout=None,
                clientauth=None)

    def test_request_bypasses_exceptions(self):
        helper.RequestsCommon = self.MockRC
        assert make_rest_call(
            self.opts, self.options,
            method=401,
            url=self.url,
            headers=None,
            cookies=None,
            body=None,
            params=None,
            retry_tries=None,
            retry_delay=None,
            retry_backoff=None,
            verify=None,
            timeout=None,
            clientauth=None,
            allowed_status_codes=[400, 401, 402])

    def test_request_raises_exceptions_with_different_bypass(self):
        helper.RequestsCommon = self.MockRC
        with pytest.raises(HTTPError) as err:
            make_rest_call(
                self.opts, self.options,
                method=401,
                url=self.url,
                headers=None,
                cookies=None,
                body=None,
                params=None,
                retry_tries=None,
                retry_delay=None,
                retry_backoff=None,
                verify=None,
                timeout=None,
                clientauth=None,
                allowed_status_codes=[400, 403, 402])
