#
#   Unit tests for function_utils.py
#
from fn_qradar_integration.util import function_utils

def test_query_string():
    """
    test the make_query_string function and verify that the substitution works fine
    :return:
    """
    # One test with real data
    input_string = "SELECT %param1% FROM events WHERE INOFFENSE(%param2%) LAST %param3% MINUTES"
    params = ["DATEFORMAT(starttime, 'YYYY-MM-dd HH:mm') as StartTime, CATEGORYNAME(category), LOGSOURCENAME(logsourceid), PROTOCOLNAME(protocolid), RULENAME(creeventlist)",
              "38",
              "100"]
    query_str = function_utils.make_query_string(input_string, params)
    str_expect = "SELECT DATEFORMAT(starttime, 'YYYY-MM-dd HH:mm') as StartTime, CATEGORYNAME(category), LOGSOURCENAME(logsourceid), PROTOCOLNAME(protocolid), RULENAME(creeventlist)" \
                 " FROM events WHERE INOFFENSE(38) LAST 100 MINUTES"

    assert query_str == str_expect

    # one more random test
    str1 = "First part string "
    str2 = " Second part string "
    str3 = " Third part string "
    str4 = " Forth part string "
    str5 = " Fifth part string "

    input_string = str1 + "%param1%" + str2 + "%param2%" + str3 + "%param3%" + str4 + "%param4%" + str5
    params = ["Param1", "Param2", "Param3", "Param4"]
    query_str = function_utils.make_query_string(input_string, params=params)
    str_expect = str1 + params[0] + str2 + params[1] + str3 + params[2] + str4 + params[3] + str5
    assert query_str == str_expect

def test_fix_dict():
    """

    :return:
    """
    input_dict = {"key1": 10,
                  "key2": "string",
                  "key3": ["l1", "l2"],
                  "key4": {"k1": "v1",
                           "k2": "v2"}}
    ret_dicts = function_utils.fix_dict_value([input_dict])

    assert ret_dicts[0]["key1"] == "10"
    assert ret_dicts[0]["key2"] == "string"
    assert ret_dicts[0]["key3"] == str(input_dict["key3"])
    assert ret_dicts[0]["key4"] == str(input_dict["key4"])


