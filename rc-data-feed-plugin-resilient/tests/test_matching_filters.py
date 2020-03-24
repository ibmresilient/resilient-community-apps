import pytest
from data_feeder_plugins.resilientfeed.lib.filters import Filters
from resilient_lib import IntegrationError

def test_number():
    f = Filters('org_id == 123', 'all')
    assert f.match_payload_value('org_id', 123)
    assert not f.match_payload_value('org_id', 456)
    assert not f.match_payload_value('org_id', '123')
    assert not f.match_payload_value('org_id', None)
    assert not f.match_payload_value('org_id', True)

def test_none():
    f = Filters(None, 'all')
    assert f.match_payload_value('org_id', 123)
    assert f.match_payload_value('org_id', '123')
    assert f.match_payload_value('org_id', None)
    assert f.match_payload_value('org_id', True)

def test_unicode():
    f = Filters(u'org == "ƀ Ɓ Ƃ ƃ Ƅ ƅ Ɔ Ƈ ƈ"', 'all')
    assert f.match_payload_value('org', u'ƀ Ɓ Ƃ ƃ Ƅ ƅ Ɔ Ƈ ƈ')
    assert not f.match_payload_value('org', 123)
    assert not f.match_payload_value('org', '123')
    assert not f.match_payload_value('org', None)
    assert not f.match_payload_value('org', True)

def test_string():
    f = Filters('org == "12abc"', 'all')
    assert f.match_payload_value('org', '12abc')
    assert not f.match_payload_value('org', 123)
    assert not f.match_payload_value('org', None)
    assert not f.match_payload_value('org', True)

def test_bool():

    f = Filters('bool == true', 'all')
    assert f.match_payload_value('bool', True)
    assert not f.match_payload_value('bool', False)
    assert not f.match_payload_value('bool', '12abc')
    assert not f.match_payload_value('bool', 123)
    assert not f.match_payload_value('bool', None)

def test_int_gt():
    f = Filters('int > 10', 'all')
    assert f.match_payload_value('int', 11)
    assert not f.match_payload_value('int', 5)

def test_int_ge():
    f = Filters('int >= 10', 'all')
    assert f.match_payload_value('int', 11)
    assert f.match_payload_value('int', 10)
    assert not f.match_payload_value('int', 5)

def test_is_not_none():
    f = Filters('fld is not None', 'all')
    assert f.match_payload_value('fld', 123)
    assert f.match_payload_value('fld', True)
    assert f.match_payload_value('fld', 'abc')
    assert not f.match_payload_value('fld', None)

def test_in():
    f = Filters('fld in ["a","b", "c"]', 'all')
    assert f.match_payload_value('fld','a')
    assert f.match_payload_value('fld','b')
    assert not f.match_payload_value('fld','d')
    assert not f.match_payload_value('fld',None)

def test_in_string():
    f = Filters('fld in "this is a string"', 'all')
    assert f.match_payload_value('fld', 'is')
    assert not f.match_payload_value('fld', 'not')

def test_not_in_string():
    f = Filters('fld not in "here is a string"', 'all')
    assert f.match_payload_value('fld', 'not')
    assert not f.match_payload_value('fld', 'here')

def test_and():
    # and logic
    f = Filters('fld in "here is a string";org = "abc"', 'all')
    assert f.match_payload_value('fld', 'here')
    assert f.match_payload_value('fld', 'string')
    assert not f.match_payload_value('fld', 'isnt')
    assert not f.match_payload_value('org', 'abc')

def test_or():
    # or logic
    f = Filters('fld in "here is a string";org = "abc"', 'any')
    assert not f.match_payload_value('fld', 'isnt')
    assert f.match_payload_value('fld', 'is')
    assert f.match_payload_value('org', 'def')


def test_none_or():
    # no filter
    f = Filters(None, 'any')
    assert f.match_payload_value('fld_not_found', 'is')
    assert f.match_payload_value('fld_not_found', 'isnt')

def test_none_and():
    f = Filters(None, 'all')
    assert f.match_payload_value('fld_not_found', 'is')

def test_none_none():
    f = Filters(None, None)
    assert f.match_payload_value('fld_not_found', 'is')

def test_empty_string():
    f = Filters('', 'any')
    assert f.match_payload_value('fld_not_found', 'is')

    f = Filters('', 'all')
    assert f.match_payload_value('fld_not_found', 'is')

def test_filter_init_opr1():
    with pytest.raises(IntegrationError):
        f = Filters('fld !<> "abc"', 'any')

def test_filter_init_opr2():
    with pytest.raises(IntegrationError):
        f = Filters('fld doesnt match "abc"', 'any')

def test_filter_bad_opr():
    with pytest.raises(IntegrationError):
        f = Filters('fld ! "abc"', 'any')
