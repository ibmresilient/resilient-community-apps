import pytest, unittest
from urllib.error import URLError
from fn_rest_api.lib.helper import validate_url, render_dict_components


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


class TestValidateURL(unittest.TestCase):

    def test_validate_url(self):
        # valid url
        validate_url("http://www.example.com/uk-en")
        validate_url("https://www.example.com/uk-en")

        # missing adapter
        with pytest.raises(URLError) as err:
            validate_url("www.ibm.com/uk-en")

        # missing schema
        with pytest.raises(URLError) as err:
            validate_url('www.example.com')

        # missing netloc
        with pytest.raises(URLError) as err:
            validate_url('https://')

        # empty url
        validate_url('')