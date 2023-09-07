import pytest
from urllib.error import URLError
from fn_rest_api.lib.helper import validate_url, render_dict_components

def test_validate_url():
    with pytest.raises(URLError) as err:
        validate_url("www.ibm.com/uk-en")
    validate_url("https://www.ibm.com/uk-en")
    validate_url("https://www.ibm.com/uk-en")


def test_render_dict_components():

    properties = {
        "sample1" : "normal plain text",
        "sample2" : """ {"key" : "json text"} """,
        "sample3" : """ {"key1" : "multi line json text1", "key2" : "multi line json text2"}""",
        "sample4" : "key : new line separated text",
        "sample5" : """ key1 : new line separated text 1
                        key2 : new line separated text 2 """,
        "sample6" : None,
        "sample7" : {},
        "sample8" : ""}

    render_dict_components(properties, {})

    expected = {'sample1': 'normal plain text',
    'sample2': {'key': 'json text'},
    'sample3': {'key1': 'multi line json text1', 'key2': 'multi line json text2'},
    'sample4': {'key': 'new line separated text'},
    'sample5': {'key1': 'new line separated text 1',
    'key2': 'new line separated text 2'},
    'sample6': None,
    'sample7': {},
    'sample8': ''}

    for key in expected:
        assert properties[key] == expected[key]