# -*- coding: utf-8 -*-
import pytest
from data_feeder_plugins.resilientfeed.lib.filters import Filters, parse_matching_criteria, MatchError
from resilient_lib import IntegrationError

def test_number():
    f = Filters({'org_id':('org_id', '==', 123)}, True)
    assert f.match_payload_value('org_id', 123)
    assert not f.match_payload_value('org_id', 456)
    assert not f.match_payload_value('org_id', '123')
    assert not f.match_payload_value('org_id', None)
    assert not f.match_payload_value('org_id', True)

def test_none():
    f = Filters(None, True)
    assert f.match_payload_value('org_id', 123)
    assert f.match_payload_value('org_id', '123')
    assert f.match_payload_value('org_id', None)
    assert f.match_payload_value('org_id', True)

def test_unicode():
    f = Filters({'org':('org', '==',  u"ƀ Ɓ Ƃ ƃ Ƅ ƅ Ɔ Ƈ ƈ")}, True)
    assert f.match_payload_value('org', u'ƀ Ɓ Ƃ ƃ Ƅ ƅ Ɔ Ƈ ƈ')
    assert not f.match_payload_value('org', 123)
    assert not f.match_payload_value('org', '123')
    assert not f.match_payload_value('org', None)
    assert not f.match_payload_value('org', True)

def test_string():
    f = Filters({'org':('org', '==', '12abc')}, True)
    assert f.match_payload_value('org', '12abc')

    f = Filters({'org':('org', '==', '12abc')}, False)
    assert not f.match_payload_value('org', 123)
    assert not f.match_payload_value('org', None)
    assert not f.match_payload_value('org', True)

def test_bool():
    f = Filters({'bool':('bool', '==', True)}, True)
    assert f.match_payload_value('bool', True)

    f = Filters({'bool':('bool', '==', True)}, False)
    assert not f.match_payload_value('bool', False)
    assert not f.match_payload_value('bool', '12abc')
    assert not f.match_payload_value('bool', 123)
    assert not f.match_payload_value('bool', None)

def test_int_gt():
    f = Filters({'int':('int', '>', 10)}, True)
    assert f.match_payload_value('int', 11)
    assert not f.match_payload_value('int', 5)

def test_int_ge():
    f = Filters({'int':('int', '>=', 10)}, True)
    assert f.match_payload_value('int', 11)
    assert f.match_payload_value('int', 10)
    assert not f.match_payload_value('int', 5)

def test_is_not_none():
    f = Filters({'fld':('fld', 'is not', None)}, True)
    assert f.match_payload_value('fld', 123)
    assert f.match_payload_value('fld', True)
    assert f.match_payload_value('fld', 'abc')
    assert not f.match_payload_value('fld', None)

def test_in():
    f = Filters({'fld':('fld', 'in', ["aa","bb", "cc"])}, True)
    assert f.match_payload_value('fld','aa')
    assert f.match_payload_value('fld','bb')
    assert not f.match_payload_value('fld','a')

    f = Filters({'fld':('fld', 'in', ["aa","bb", "cc"])}, True)
    assert not f.match_payload_value('fld','d')

    f = Filters({'fld':('fld', 'in', ["aa","bb", "cc"])}, True)
    assert not f.match_payload_value('fld', None)

def test_in_string():
    f = Filters({'fld':('fld', '~', 'malicious')}, True)
    assert f.match_payload_value('fld', 'this id a long description which contains malicious as the trigger word')
    assert not f.match_payload_value('fld', 'this id a long description which does not contain the trigger word')

def test_not_in_string():
    f = Filters({'fld':('fld', 'not in', 'here is a string')}, True)
    assert f.match_payload_value('fld', 'not')
    assert not f.match_payload_value('fld', 'here')

def test_and():
    # and logic
    f = Filters({'fld':('fld', 'in', 'here is a string'),'org':('org', '=', 'abc')}, True)
    assert f.match_payload_value('fld', 'here')
    assert f.match_payload_value('fld', 'string')
    assert not f.match_payload_value('fld', 'isnt')
    assert not f.match_payload_value('org', 'abc')

def test_or():
    # or logic
    f = Filters({'fld':('fld', 'in', 'here is a string'),'org':('org', '=', 'abc')}, False)
    assert not f.match_payload_value('fld', 'isnt')
    assert f.match_payload_value('fld', 'is')
    assert f.match_payload_value('org', 'def')

def test_none_or():
    # no filter
    f = Filters(None, False)
    assert f.match_payload_value('fld_not_found', 'is')
    assert f.match_payload_value('fld_not_found', 'isnt')

def test_none_and():
    f = Filters(None, True)
    assert f.match_payload_value('fld_not_found', 'is')

def test_none_none():
    f = Filters(None, None)
    assert f.match_payload_value('fld_not_found', 'is')

def test_empty_string():
    f = Filters([], False)
    assert f.match_payload_value('fld_not_found', 'is')

    f = Filters([], True)
    assert f.match_payload_value('fld_not_found', 'is')

def test_list_to_list():
    f = Filters({'fld':('fld', 'in', ['Phishing', 'Malicious'])}, True)
    assert f.match_payload_value('fld', ['Phishing'])
    assert f.match_payload_value('fld', ['Phishing', 'Malicious'])
    assert not f.match_payload_value('fld', [])

def test_string_to_list():
    f = Filters({'fld':('fld', 'in', ['Phishing', 'Malicious'])}, True)
    assert f.match_payload_value('fld', 'Phishing')
    assert not f.match_payload_value('fld', 'hish')

def test_parse_init_opr1():
    with pytest.raises(ValueError):
       parse_matching_criteria("fld!<> abc", "any")
    with pytest.raises(ValueError):
       parse_matching_criteria("fld !> abc", "any")

def test_parse_init_opr2():
    with pytest.raises(ValueError):
        parse_matching_criteria("fld doesnt match abc", "any")

def test_parse_bad_opr():
    with pytest.raises(ValueError):
        parse_matching_criteria("fld ! abc", "any")

def test_parse_field_operator():
    with pytest.raises(ValueError):
        parse_matching_criteria("fld == abc", "xxx")

def test_parse_field_matches():
    filter_dict, and_operator = parse_matching_criteria("fld == abc", "any")
    assert filter_dict == {"fld":("fld", "==", "abc")}
    assert not and_operator
    f = Filters(filter_dict, and_operator)
    assert f.match_payload_value('fld', 'abc')

    filter_dict, and_operator = parse_matching_criteria("fld > 10 ", "all")
    assert filter_dict == {"fld":("fld", ">", 10)}
    assert and_operator
    f = Filters(filter_dict, and_operator)
    assert f.match_payload_value('fld', 11)

    filter_dict, and_operator = parse_matching_criteria("fld = True", "all")
    assert filter_dict == {"fld":("fld", "==", True)}
    f = Filters(filter_dict, and_operator)
    assert f.match_payload_value('fld', True)

    filter_dict, and_operator = parse_matching_criteria("fld ~ list", "all")
    assert filter_dict == {"fld":("fld", "~", "list")}
    f = Filters(filter_dict, and_operator)
    assert f.match_payload_value('fld', 'something is in this list')

    filter_dict, and_operator = parse_matching_criteria("fld not in something is a list", "all")
    assert filter_dict == {"fld":("fld", "not in", "something is a list")}
    f = Filters(filter_dict, and_operator)
    assert f.match_payload_value('fld', 'nothing')

    filter_dict, and_operator = parse_matching_criteria("fld in ['Phishing', 'Malware']", "all")
    assert filter_dict == {"fld":("fld", " in ", ['Phishing', 'Malware'])}
    f = Filters(filter_dict, and_operator)
    assert f.match_payload_value('fld', 'Phishing')
