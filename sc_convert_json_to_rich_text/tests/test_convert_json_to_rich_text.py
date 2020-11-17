# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# to run: pytest -vv tests/test_convert_json_to_rich_text.py
#
import sys

if sys.version_info[0] == 2:
    import imp
else:
    import importlib

import inspect
import pytest
import os

tst_text = "some text here"
tst_text_py2= u"<strong>test_json</strong>: some text here<br />"

tst_unciode = u"ƀ Ɓ Ƃ ƃ Ƅ ƅ Ɔ Ƈ ƈ Ɖ"
tst_unciode_py2 = u"<strong>test_json</strong>: ƀ Ɓ Ƃ ƃ Ƅ ƅ Ɔ Ƈ ƈ Ɖ<br />"

tst_list = ['c', 'a', 'b']
tst_list_py2 = u"<strong>test_json</strong>: <ul><li>c</li><li>a</li><li>b</li></ul>"

tst_empty_list = []
tst_empty_list_py2 = u"<strong>test_json</strong>: None<br>"

tst_mixed_type_dict = {
    "int": 1,
    "float": 1.1,
    "bool": True,
    "text": "some text here"
}
tst_mixed_type_dict_py2 = u"<strong>test_json</strong>: <div style='padding:10px'><strong>int</strong>: 1<br /><strong>text</strong>: some text here<br /><strong>float</strong>: 1.1<br /><strong>bool</strong>: True</div>"
tst_mixed_type_dict_py3 = u"<strong>test_json</strong>: <div style='padding:10px'><strong>int</strong>: 1<br /><strong>float</strong>: 1.1<br /><strong>bool</strong>: True<br /><strong>text</strong>: some text here</div>"

tst_links = "https://abc1.com and http://abc2.com?a=b&c=d and more https://abc3.com:3212#something here"
tst_links_py2 = u"<strong>test_json</strong>: <a target='blank' href='https://abc1.com'>https://abc1.com</a> and <a target='blank' href='http://abc2.com?a=b&c=d'>http://abc2.com?a=b&c=d</a> and more <a target='blank' href='https://abc3.com:3212#something'>https://abc3.com:3212#something</a> here<br />"

tst_nested_mixed_type_list = ['b', 'a', 'c', [3, 1, 2], [], ['b', 1, 1.1, True]]
tst_nested_mixed_type_list_py2 = u"<strong>test_json</strong>: <ul><li>b</li><li>a</li><li>c</li><ul><li>3</li><li>1</li><li>2</li></ul>None<br><ul><li>b</li><li>1</li><li>1.1</li><li>True</li></ul></ul>"

tst_nested_mixed_type_dict = {
    "bool": True,
    "text": "some text here",
    "int": 1,
    "nested": {
        "text1": "some text here",
        "bool1": True,
        "int1": 1
    },
    'empty': {}
}
tst_nested_mixed_type_dict_py2 = u"<strong>test_json</strong>: <div style='padding:10px'><strong>int</strong>: 1<br /><strong>text</strong>: some text here<br /><strong>bool</strong>: True<br /><strong>empty</strong>: None<br><br /><strong>nested</strong>: <div style='padding:10px'><strong>int1</strong>: 1<br /><strong>text1</strong>: some text here<br /><strong>bool1</strong>: True</div></div>"
tst_nested_mixed_type_dict_py3 = u"<strong>test_json</strong>: <div style='padding:10px'><strong>bool</strong>: True<br /><strong>text</strong>: some text here<br /><strong>int</strong>: 1<br /><strong>nested</strong>: <div style='padding:10px'><strong>text1</strong>: some text here<br /><strong>bool1</strong>: True<br /><strong>int1</strong>: 1</div><strong>empty</strong>: None<br></div>"

tst_nested_dict_list = {
    "bool": True,
    "int": 1,
    "text": "some text here",
    "nested": {
        "bool1": True,
        "int1": 1,
        "text1": "some text here",
        "nested list": ['a', 'b', 'c', ['d', 'e', 'f']],
    }
}
tst_nested_dict_list_py2 = u"<strong>test_json</strong>: <div style='padding:10px'><strong>int</strong>: 1<br /><strong>text</strong>: some text here<br /><strong>bool</strong>: True<br /><strong>nested</strong>: <div style='padding:10px'><strong>int1</strong>: 1<br /><strong>text1</strong>: some text here<br /><strong>bool1</strong>: True<br /><strong>nested list</strong>: <ul><li>a</li><li>b</li><li>c</li><ul><li>d</li><li>e</li><li>f</li></ul></ul></div></div>"
tst_nested_dict_list_py3 = u"<strong>test_json</strong>: <div style='padding:10px'><strong>bool</strong>: True<br /><strong>int</strong>: 1<br /><strong>text</strong>: some text here<br /><strong>nested</strong>: <div style='padding:10px'><strong>bool1</strong>: True<br /><strong>int1</strong>: 1<br /><strong>text1</strong>: some text here<br /><strong>nested list</strong>: <ul><li>a</li><li>b</li><li>c</li><ul><li>d</li><li>e</li><li>f</li></ul></ul></div></div>"

tst_everything = {
    "bool": True,
    "int": 1,
    "float": 1.1,
    "text": tst_text,
    "None": None,
    "unicode": tst_unciode,
    "empty str": "",
    "list": tst_list,
    "empty list": [],
    "dict": tst_mixed_type_dict,
    "emtpy dict": { },
    "links": tst_links,
    "nested list": tst_nested_mixed_type_list,
    "nested dict": tst_mixed_type_dict,
    "nested dict list": tst_nested_dict_list
}

test_omit_json = {
    "version": 1.0,
    "header": "omit",
    "json": tst_nested_dict_list,
    "json_omit_list": ["nested"]
}
test_omit_result_py3 = u"<strong>bool</strong>: True<br><strong>int</strong>: 1<br><strong>text</strong>: some text here<br>"
test_omit_result_py2 = u"<strong>int</strong>: 1<br><strong>text</strong>: some text here<br><strong>bool</strong>: True<br>"

test_empty_json = {
    "version": 1.0,
    "header": "empty",
    "padding": 10,
    "separator": u"<br>",
    "sort": True,
    "json": { },
    "json_omit_list": ["omit"],
    "incident_field": None
}
test_empty_result = ""

test_sort_json = {
    "version": 1.0,
    "header": "sort",
    "sort": True,
    "json": tst_nested_dict_list
}
test_sort_result_py3 = u"<strong>bool</strong>: True<br><strong>int</strong>: 1<br><strong>nested</strong>: <div style='padding:10px'><strong>bool1</strong>: True<br><strong>int1</strong>: 1<br><strong>nested list</strong>: <ul><li>a</li><li>b</li><li>c</li><ul><li>d</li><li>e</li><li>f</li></ul></ul><strong>text1</strong>: some text here</div><strong>text</strong>: some text here<br>"
test_sort_result_py2 = u"<strong>bool</strong>: True<br><strong>int</strong>: 1<br><strong>nested</strong>: <div style='padding:10px'><strong>bool1</strong>: True<br><strong>int1</strong>: 1<br><strong>nested list</strong>: <ul><li>a</li><li>b</li><li>c</li><ul><li>d</li><li>e</li><li>f</li></ul></ul><strong>text1</strong>: some text here</div><strong>text</strong>: some text here<br>"

test_separator_json = {
    "version": 1.0,
    "header": "separator",
    "separator": [u"<div>", u"</div>"],
    "json": tst_nested_dict_list,
}
test_separator_result_py3 = u"<div><strong>bool</strong>: True</div><div><strong>int</strong>: 1</div><div><strong>text</strong>: some text here</div><div><strong>nested</strong>: <div style='padding:10px'><div><strong>bool1</strong>: True</div><div><strong>int1</strong>: 1</div><div><strong>text1</strong>: some text here</div><div><strong>nested list</strong>: <ul><li>a</li><li>b</li><li>c</li><ul><li>d</li><li>e</li><li>f</li></ul></ul></div></div></div>"
test_separator_result_py2 = u"<div><strong>int</strong>: 1</div><div><strong>text</strong>: some text here</div><div><strong>bool</strong>: True</div><div><strong>nested</strong>: <div style='padding:10px'><div><strong>int1</strong>: 1</div><div><strong>text1</strong>: some text here</div><div><strong>bool1</strong>: True</div><div><strong>nested list</strong>: <ul><li>a</li><li>b</li><li>c</li><ul><li>d</li><li>e</li><li>f</li></ul></ul></div></div></div>"

test_padding_json = {
    "version": 1.0,
    "header": "padding",
    "padding": 15,
    "json": tst_nested_dict_list,
}
test_padding_result_py3 = u"<strong>bool</strong>: True<br><strong>int</strong>: 1<br><strong>text</strong>: some text here<br><strong>nested</strong>: <div style='padding:15px'><strong>bool1</strong>: True<br><strong>int1</strong>: 1<br><strong>text1</strong>: some text here<br><strong>nested list</strong>: <ul><li>a</li><li>b</li><li>c</li><ul><li>d</li><li>e</li><li>f</li></ul></ul></div>"
test_padding_result_py2 = u"<strong>int</strong>: 1<br><strong>text</strong>: some text here<br><strong>bool</strong>: True<br><strong>nested</strong>: <div style='padding:15px'><strong>int1</strong>: 1<br><strong>text1</strong>: some text here<br><strong>bool1</strong>: True<br><strong>nested list</strong>: <ul><li>a</li><li>b</li><li>c</li><ul><li>d</li><li>e</li><li>f</li></ul></ul></div>"

test_everything_json = {
    "version": 1.0,
    "header": "everything",
    "padding": 15,
    "separator": [u"<div>", u"</div>"],
    "sort": True,
    "json_omit_list": ["nested"],
    "json": tst_everything,
}
test_everything_py2 = u"<div><strong>None</strong>: None</div><div><strong>bool</strong>: True</div><div><strong>dict</strong>: <div style='padding:15px'><div><strong>bool</strong>: True</div><div><strong>float</strong>: 1.1</div><div><strong>int</strong>: 1</div><div><strong>text</strong>: some text here</div></div></div><div><strong>empty list</strong>: None<br></div><div><strong>empty str</strong>: </div><div><strong>emtpy dict</strong>: None<br></div><div><strong>float</strong>: 1.1</div><div><strong>int</strong>: 1</div><div><strong>links</strong>: <a target='blank' href='https://abc1.com'>https://abc1.com</a> and <a target='blank' href='http://abc2.com?a=b&c=d'>http://abc2.com?a=b&c=d</a> and more <a target='blank' href='https://abc3.com:3212#something'>https://abc3.com:3212#something</a> here</div><div><strong>list</strong>: <ul><li>c</li><li>a</li><li>b</li></ul></div><div><strong>nested dict</strong>: <div style='padding:15px'><div><strong>bool</strong>: True</div><div><strong>float</strong>: 1.1</div><div><strong>int</strong>: 1</div><div><strong>text</strong>: some text here</div></div></div><div><strong>nested dict list</strong>: <div style='padding:15px'><div><strong>bool</strong>: True</div><div><strong>int</strong>: 1</div><div><strong>text</strong>: some text here</div></div></div><div><strong>nested list</strong>: <ul><li>b</li><li>a</li><li>c</li><ul><li>3</li><li>1</li><li>2</li></ul>None<br><ul><li>b</li><li>1</li><li>1.1</li><li>True</li></ul></ul></div><div><strong>text</strong>: some text here</div><div><strong>unicode</strong>: ƀ Ɓ Ƃ ƃ Ƅ ƅ Ɔ Ƈ ƈ Ɖ</div>"
test_everything_py3 = u"<div><strong>None</strong>: None</div><div><strong>bool</strong>: True</div><div><strong>dict</strong>: <div style='padding:15px'><div><strong>bool</strong>: True</div><div><strong>float</strong>: 1.1</div><div><strong>int</strong>: 1</div><div><strong>text</strong>: some text here</div></div></div><div><strong>empty list</strong>: None<br></div><div><strong>empty str</strong>: </div><div><strong>emtpy dict</strong>: None<br></div><div><strong>float</strong>: 1.1</div><div><strong>int</strong>: 1</div><div><strong>links</strong>: <a target='blank' href='https://abc1.com'>https://abc1.com</a> and <a target='blank' href='http://abc2.com?a=b&c=d'>http://abc2.com?a=b&c=d</a> and more <a target='blank' href='https://abc3.com:3212#something'>https://abc3.com:3212#something</a> here</div><div><strong>list</strong>: <ul><li>c</li><li>a</li><li>b</li></ul></div><div><strong>nested dict</strong>: <div style='padding:15px'><div><strong>bool</strong>: True</div><div><strong>float</strong>: 1.1</div><div><strong>int</strong>: 1</div><div><strong>text</strong>: some text here</div></div></div><div><strong>nested dict list</strong>: <div style='padding:15px'><div><strong>bool</strong>: True</div><div><strong>int</strong>: 1</div><div><strong>text</strong>: some text here</div></div></div><div><strong>nested list</strong>: <ul><li>b</li><li>a</li><li>c</li><ul><li>3</li><li>1</li><li>2</li></ul>None<br><ul><li>b</li><li>1</li><li>1.1</li><li>True</li></ul></ul></div><div><strong>text</strong>: some text here</div><div><strong>unicode</strong>: ƀ Ɓ Ƃ ƃ Ƅ ƅ Ɔ Ƈ ƈ Ɖ</div>"

test_list_json = [
    {
      'item1': '1',
      'item2': '2',
    },
    {
      'item1': '3',
      'item2': '4',
    }
]

test_list_result_py3 = u"<strong>test_json</strong>: <ul><li><strong>item1</strong>: 1<br /><strong>item2</strong>: 2<br /></li><li><strong>item1</strong>: 3<br /><strong>item2</strong>: 4<br /></li></ul>"
test_list_result_py2 = u"<strong>test_json</strong>: <ul><li><strong>item2</strong>: 2<br /><strong>item1</strong>: 1<br /></li><li><strong>item2</strong>: 4<br /><strong>item1</strong>: 3<br /></li></ul>"

class Workflow:
    def __init__(self):
        self.properties = {'convert_json_to_rich_text': tst_everything}

class Incident:
    def addNote(self, text):
        pass

class Helper:
    def createRichText(self, text):
        pass
    def fail(self, message):
        pass

def get_properties(json_dict):
    return json_dict.get('padding', 10), json_dict.get('separator','<br>'), json_dict.get('header'), \
           json_dict.get('json_omit_list',[]), json_dict.get('incident_field'), json_dict.get('json'), \
           json_dict.get('sort', False)

workflow = Workflow()
helper = Helper()
incident = Incident()

abs_path = os.path.abspath('convert_json_to_rich_text.py')

if sys.version_info[0] == 2:
    module = imp.load_source('convert_json_to_rich_text', abs_path)
else:
    module_spec = importlib.util.spec_from_file_location('convert_json_to_rich_text.py', abs_path)
    module = importlib.util.module_from_spec(module_spec)

module.incident = incident
module.helper = helper
module.workflow = workflow

if sys.version_info[0] >= 3:
    module_spec.loader.exec_module(module)

cls = None
for member in inspect.getmembers(module):
    if member[0] == "ConvertJson":
        cls = member[1]


@pytest.mark.parametrize("test_header, json_fragment, expected_results_py2, expected_results_py3", [
    ("tst_text", tst_text, tst_text_py2, tst_text_py2),
    ("tst_unicode", tst_unciode, tst_unciode_py2, tst_unciode_py2),
    ("tst_links", tst_links, tst_links_py2, tst_links_py2),
    ("tst_list", tst_list, tst_list_py2, tst_list_py2),
    ("tst_empty_list", tst_empty_list, tst_empty_list_py2, tst_empty_list_py2),
    ("tst_nested_mixed_type_list", tst_nested_mixed_type_list, tst_nested_mixed_type_list_py2, tst_nested_mixed_type_list_py2),
    ("tst_nested_dict_list", tst_nested_dict_list, tst_nested_dict_list_py2, tst_nested_dict_list_py3),
    ("tst_mixed_type_dict", tst_mixed_type_dict, tst_mixed_type_dict_py2, tst_mixed_type_dict_py3),
    ("tst_nested_mixed_type_dict", tst_nested_mixed_type_dict, tst_nested_mixed_type_dict_py2, tst_nested_mixed_type_dict_py3),
    ("test_list_json", test_list_json, test_list_result_py2, test_list_result_py3)
])
def test_simple_success(test_header, json_fragment, expected_results_py2, expected_results_py3):
    json_test = {"test_json": json_fragment}
    print(test_header)
    convert = cls()
    converted_json = convert.convert_json_to_rich_text(json_test)
    print(converted_json)
    if sys.version_info[0] == 2:
        assert converted_json == expected_results_py2
    else:
        assert converted_json == expected_results_py3


@pytest.mark.parametrize("workflow_properties, expected_results_py2, expected_results_py3", [
    (test_omit_json, test_omit_result_py2, test_omit_result_py3),
    (test_sort_json, test_sort_result_py2, test_sort_result_py3),
    (test_empty_json, test_empty_result, test_empty_result),
    (test_separator_json, test_separator_result_py2, test_separator_result_py3),
    (test_padding_json, test_padding_result_py2, test_padding_result_py3)
])
def test_success(workflow_properties, expected_results_py2, expected_results_py3):
    padding, separator, header, json_omit_list, incident_field, json, sort_keys = get_properties(workflow_properties)
    print(header)
    convert = cls(omit_keys=json_omit_list, padding=padding, separator=separator, sort_keys=sort_keys)
    converted_json = convert.convert_json_to_rich_text(json)
    print(converted_json)
    if sys.version_info[0] == 2:
        assert converted_json == expected_results_py2
    else:
        assert converted_json == expected_results_py3

@pytest.mark.parametrize("workflow_properties, expected_results_py2, expected_results_py3", [
    (test_everything_json, test_everything_py2, test_everything_py3),
])
def test_everything_success(workflow_properties, expected_results_py2, expected_results_py3):
    padding, separator, header, json_omit_list, incident_field, json, sort_keys = get_properties(workflow_properties)
    print(header)
    convert = cls(omit_keys=json_omit_list, padding=padding, separator=separator, sort_keys=sort_keys)
    converted_json = convert.convert_json_to_rich_text(json)
    print(converted_json)
    if sys.version_info[0] == 2:
        assert converted_json == expected_results_py2
    else:
        assert converted_json == expected_results_py3
