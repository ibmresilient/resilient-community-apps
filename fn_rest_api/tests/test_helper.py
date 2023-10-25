import pytest, unittest

from requests.exceptions import HTTPError

from unittest.mock import MagicMock
from fn_rest_api.lib import helper
from urllib.error import URLError
from fn_rest_api.lib.helper import (validate_url,
    render_dict_components, build_dict, make_rest_call)


class TestRenderDictComponents(unittest.TestCase):

    def test_str_dict_to_py_dict(self):
        processed_value = {"test_input" : {"sample1" : "normal plain text"}}
        render_dict_components(processed_value, {}),
        self.assertDictEqual(processed_value,
            {"test_input" : {'sample1': 'normal plain text'}})

    def test_json_dict(self):
        # String to dict using json decoder
        processed_value = {"test_input" :  """ {"key" : "json text"} """}
        render_dict_components(processed_value, {}),
        self.assertDictEqual(processed_value,
            {"test_input" : {'key': 'json text'}})

    def test_json_dict_with_none(self):
        # Null handling using json decoder
        processed_value = {"test_input" :  """ {"key" :  null} """}
        render_dict_components(processed_value, {}),
        self.assertDictEqual(processed_value,
            {"test_input" : {'key': None}})

    def test_json_dict(self):
        # Multi-line string to dict using json decoder
        processed_value = {"test_input" :  """ {"key1" : "multi line json text1", "key2" : "multi line json text2"}"""}
        render_dict_components(processed_value, {}),
        self.assertDictEqual(processed_value,
            {"test_input" : {'key1': 'multi line json text1', 'key2': 'multi line json text2'}})

    def test_json_dict_multiline(self):
        # Multi-line string with to dict with \n character using json decoder
        processed_value = {"test_input" :  """ {"key1" : "multi line json text1",
                           "key2" : "multi line json text2"}"""}
        render_dict_components(processed_value, {}),
        self.assertDictEqual(processed_value,
            {"test_input" : {'key1': 'multi line json text1', 'key2': 'multi line json text2'}})

    def test_simple_dict(self):
        # Simple new line kv-pair to string
        processed_value = {"test_input" : """ key1 : new line separated text 1
            key2 : new line separated text 2 """}
        render_dict_components(processed_value, {})
        self.assertDictEqual(processed_value,
            {"test_input" : {'key1': 'new line separated text 1',
             'key2': 'new line separated text 2'}})

    def test_simple_dict_with_leading_new_line(self):
        # Simple new line kv-pair with leading blank line to dict
        processed_value = {"test_input" : """
            key1 : new line separated text 1
            key2 : new line separated text 2 """}
        render_dict_components(processed_value, {})
        self.assertDictEqual(processed_value,
            {"test_input" : {'key1': 'new line separated text 1',
             'key2': 'new line separated text 2'}})

    def test_simple_dict_with_numbers(self):
        # Simple new line kv-pair with numbers and decimals to dict
        processed_value = {"test_input" : """
            key1 : 1234
            key2 : 22.2345 """}
        render_dict_components(processed_value, {})
        self.assertDictEqual(processed_value,
            {"test_input" : {'key1': '1234',
             'key2': '22.2345'}})

    def test_none_handlig(self):
        # None handling
        processed_value = {"test_input" : None}
        render_dict_components(processed_value, {})
        self.assertDictEqual(processed_value,
            {"test_input" : None})

    def test_empty_string(self):
        # Empty string
        processed_value = {"test_input" : ""}
        render_dict_components(processed_value, {})
        self.assertDictEqual(processed_value,
               {"test_input" : ""})

    def test_json_dict_value_sub(self):
        processed_value = {"test_input" : """{"sample1" : "normal {{TO_BE_SUBED}}"}"""}
        render_dict_components(processed_value, {"TO_BE_SUBED" : "plain text but substituted"}),
        self.assertDictEqual(processed_value,
            {"test_input" : {'sample1': 'normal plain text but substituted'}})

    def test_simple_dict_with_leading_new_line_and_sub(self):
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

        self.assertDictEqual(processed_value,
            {"test_input" : {
                'key1': 'new line separated testsecret1 testsecret@!$%^2',
                'key2': 'new line separated testsecret@!$%^2 testsecret1',
                'test KEY' : 'new line separated secret',
                "thisisakey" : "testvaluesecret"}})

    def test_simple_dict_with_blank_lines(self):
        # Simple new line kv-pair with multiple blank lines to dict
        processed_value = {"test_input" : """

            key1 : new line separated text 1

            key2 : new line separated text 2

        """}
        render_dict_components(processed_value, {})
        self.assertDictEqual(processed_value,
            {"test_input" : {'key1': 'new line separated text 1',
             'key2': 'new line separated text 2'}})

    def test_simple_dict_with_symbols(self):
        # Simple new line kv-pair with symbols to dict
        processed_value = {"test_input" : """

            key1 : new !@#$/%/%^^$#@!@#$!%

            key2 : new line separated text 2
        """}
        render_dict_components(processed_value, {})
        self.assertDictEqual(processed_value,
            {"test_input" : {'key1': 'new !@#$/%/%^^$#@!@#$!%',
             'key2': 'new line separated text 2'}})


class TestBuildDict(unittest.TestCase):
    
    def test_json_dict(self):
        # String to dict using json decoder
        processed_value = build_dict(""" {"key" : "json text"} """)
        self.assertDictEqual(processed_value, {'key': 'json text'})

    def test_json_dict_with_none(self):
        # Null handling using json decoder
        processed_value = build_dict(""" {"key" :  null} """)
        self.assertDictEqual(processed_value, {'key': None})

    def test_json_dict(self):
        # Multi-line string to dict using json decoder
        processed_value = build_dict(""" {"key1" : "multi line json text1", "key2" : "multi line json text2"}""")
        self.assertDictEqual(processed_value, {'key1': 'multi line json text1', 'key2': 'multi line json text2'})

    def test_json_dict_multiline(self):
        # Multi-line string with to dict with \n character using json decoder
        processed_value = build_dict(""" {"key1" : "multi line json text1",
                            "key2" : "multi line json text2"}""")
        self.assertDictEqual(processed_value, {'key1': 'multi line json text1', 'key2': 'multi line json text2'})

    def test_simple_dict(self):
        # Simple new line kv-pair to string
        processed_value = build_dict(""" key1 : new line separated text 1
            key2 : new line separated text 2 """)
        self.assertDictEqual(processed_value, {'key1': 'new line separated text 1',
                'key2': 'new line separated text 2'})

    def test_simple_dict_with_leading_new_line(self):
        # Simple new line kv-pair with leading blank line to dict
        processed_value = build_dict("""
            key1 : new line separated text 1
            key2 : new line separated text 2 """)
        self.assertDictEqual(processed_value, {'key1': 'new line separated text 1',
                'key2': 'new line separated text 2'})

    def test_simple_dict_with_numbers(self):
        # Simple new line kv-pair with numbers and decimals to dict
        processed_value = build_dict("""
            key1 : 1234
            key2 : 22.2345 """)
        self.assertDictEqual(processed_value, {'key1': '1234',
                'key2': '22.2345'})

    def test_none_handling(self):
        # None handling
        processed_value = build_dict("")
        assert(processed_value, {})

    def test_empty_string(self):
        # Empty string
        processed_value = build_dict(None)
        self.assertDictEqual(processed_value, {})


class TestValidateURL(unittest.TestCase):

    def test_valid_url(self):
        # Http adapter
        url_http = "http://www.example.com/uk-en"
        assert url_http == validate_url(url_http)

        # Https adapter
        url_https = "https://www.example.com/uk-en"
        validate_url(url_https)

    def test_missing_invalid_adapter(self):
        # Missing adapter
        with pytest.raises(URLError) as err:
            validate_url("www.ibm.com/uk-en")

        # Invalid adapter
        with pytest.raises(URLError) as err:
            validate_url("hppt:www.ibm.com/uk-en")

    def test_missing_schema(self):
        # missing schema
        with pytest.raises(URLError) as err:
            validate_url('www.example.com')

    def test_missing_netloc(self):
        # missing netloc
        with pytest.raises(URLError) as err:
            validate_url('https://')

    def test_missing_value(self):
        # empty string in url
        assert validate_url('') == None

    def test_none_value(self):
        # None in url
        assert validate_url(None) == None
    
    def test_empty_dict_value(self):
        # None in url
        assert validate_url({}) == None


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
            cookies, verify,
            timeout, clientauth,
            callback, json=None, data=None):

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
                "json"    : json,
                "data"    : data,
                "clientauth" : clientauth}

    helper.RequestsCommon = MockRC
    opts, options = {}, {}
    method = "GET"
    url = "http://www.example.com"

    def test_standard_request(self):
        response = make_rest_call(
            self.opts, self.options,
            rest_method=self.method,
            rest_url=self.url,
            headers_dict={"key1" : "header1"},
            cookies_dict={"key1" : "cookie1"},
            body_dict={"key1" : "body1"},
            rest_verify=True,
            rest_timeout=60,
            rest_certificate=""" NOT A CERTIFICATE """)

        assert response["url"] == self.url
        assert response["method"] == self.method
        assert response["verify"]
        self.assertDictEqual(response["headers"], {"key1" : "header1"})
        self.assertDictEqual(response["cookies"], {"key1" : "cookie1"})
        self.assertDictEqual(response["data"], {"key1" : "body1"})
        self.assertIsNone(response["json"])
        self.assertEqual(response["timeout"], 60)
        self.assertEqual(response["clientauth"], """ NOT A CERTIFICATE """)
        self.assertIsNone(response["json"])

    def test_json_request(self):
        response = make_rest_call(
            self.opts, self.options,
            rest_method=self.method,
            rest_url=self.url,
            headers_dict={"Content-type" : "application/json"},
            cookies_dict=None,
            body_dict={"key1" : "body1"},
            rest_verify=None,
            rest_timeout=None,
            rest_certificate=None)
        assert response["url"] == self.url
        assert response["method"] == self.method
        self.assertDictEqual(response["headers"], {"Content-type" : "application/json"})
        self.assertDictEqual(response["json"], {"key1" : "body1"})
        self.assertIsNone(response["data"])

    def test_json_lowercase_content_type(self):
        response = make_rest_call(
            self.opts, self.options,
            rest_method=self.method,
            rest_url=self.url,
            headers_dict={"content-type" : "application/json"},
            cookies_dict=None,
            body_dict={"key1" : "body1"},
            rest_verify=None,
            rest_timeout=None,
            rest_certificate=None)
        assert response["url"] == self.url
        assert response["method"] == self.method
        self.assertDictEqual(response["headers"], {"content-type" : "application/json"})
        self.assertDictEqual(response["json"], {"key1" : "body1"})
        self.assertIsNone(response["data"])

    def test_json_uppercase_content_type(self):
        response = make_rest_call(
            self.opts, self.options,
            rest_method=self.method,
            rest_url=self.url,
            headers_dict={"CONTENT-TYPE" : "application/json"},
            cookies_dict=None,
            body_dict={"key1" : "body1"},
            rest_verify=None,
            rest_timeout=None,
            rest_certificate=None)
        assert response["url"] == self.url
        assert response["method"] == self.method
        self.assertDictEqual(response["headers"], {"CONTENT-TYPE" : "application/json"})
        self.assertDictEqual(response["json"], {"key1" : "body1"})
        self.assertIsNone(response["data"])

    def test_json_title_content_type(self):
        response = make_rest_call(
            self.opts, self.options,
            rest_method=self.method,
            rest_url=self.url,
            headers_dict={"Content-Type" : "application/json"},
            cookies_dict=None,
            body_dict={"key1" : "body1"},
            rest_verify=None,
            rest_timeout=None,
            rest_certificate=None)
        assert response["url"] == self.url
        assert response["method"] == self.method
        self.assertDictEqual(response["headers"], {"Content-Type" : "application/json"})
        self.assertDictEqual(response["json"], {"key1" : "body1"})
        self.assertIsNone(response["data"])

    def test_request_raises_exceptions(self):
        with pytest.raises(HTTPError) as err:
            make_rest_call(
                self.opts, self.options,
                rest_method=400,
                rest_url=self.url,
                headers_dict=None,
                cookies_dict=None,
                body_dict=None,
                rest_verify=None,
                rest_timeout=None,
                rest_certificate=None)

    def test_request_bypasses_exceptions(self):
        assert make_rest_call(
            self.opts, self.options,
            rest_method=401,
            rest_url=self.url,
            headers_dict=None,
            cookies_dict=None,
            body_dict=None,
            rest_verify=None,
            rest_timeout=None,
            rest_certificate=None,
            allowed_status_codes=[400, 401, 402])

    def test_request_raises_exceptions_with_different_bypass(self):
        with pytest.raises(HTTPError) as err:
            make_rest_call(
                self.opts, self.options,
                rest_method=401,
                rest_url=self.url,
                headers_dict=None,
                cookies_dict=None,
                body_dict=None,
                rest_verify=None,
                rest_timeout=None,
                rest_certificate=None,
                allowed_status_codes=[400, 403, 402])
