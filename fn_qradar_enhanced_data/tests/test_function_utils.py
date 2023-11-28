# encoding: utf-8
# Unit tests for function_utils.py

from fn_qradar_enhanced_data.util.function_utils import make_query_string, filter_comments

def test_query_string():
    """
    Test the make_query_string function and verify that the substitution works fine
    :return: None
    """
    # One test with real data
    input_string = "SELECT %param1% FROM events WHERE INOFFENSE(%param2%) LAST %param3% MINUTES"
    params = ["DATEFORMAT(starttime, 'YYYY-MM-dd HH:mm') as StartTime, CATEGORYNAME(category), LOGSOURCENAME(logsourceid), PROTOCOLNAME(protocolid), RULENAME(creeventlist)",
              "38",
              "100"]
    query_str = make_query_string(input_string, params)
    str_expect = "SELECT DATEFORMAT(starttime, 'YYYY-MM-dd HH:mm') as StartTime, CATEGORYNAME(category), LOGSOURCENAME(logsourceid), PROTOCOLNAME(protocolid), RULENAME(creeventlist)" \
                 " FROM events WHERE INOFFENSE(38) LAST 100 MINUTES"

    assert query_str == str_expect

    # one more random test
    str1 = "First part string "
    str2 = " Second part string "
    str3 = " Third part string "
    str4 = " Forth part string "
    str5 = " Fifth part string"

    input_string = f"{str1}%param1%{str2}%param2%{str3}%param3%{str4}%param4%{str5}"
    params = ["Param1", "Param2", "Param3", "Param4"]
    query_str = make_query_string(input_string, params=params)
    str_expect = f"{str1}{params[0]}{str2}{params[1]}{str3}{params[2]}{str4}{params[3]}{str5}"
    assert query_str == str_expect

def test_filter_comments():
    """
    Test the filter_comments function and verify that the filtering works
    :return: None
    """
    # Test that only the new comment is returned
    notes_from_qradar = ["test1", "Hello World", "test2"]
    new_comments = filter_comments(soar_common(), 123, notes_from_qradar, soar_str_to_remove="\nAdded from QRadar")
    assert new_comments == ["Hello World"]

    # Test that no comments are returned because all given comments are already on SOAR
    notes_from_qradar = ["test1", "admin@example.com: test2", "test4"]
    new_comments = filter_comments(soar_common(), 123, notes_from_qradar, soar_str_to_remove="\nAdded from QRadar", qradar_header_to_remove="admin@example.com: ")
    assert new_comments == []

    # Test having data after the '\nAdded from QRadar'
    notes_from_qradar = ["test1", "test2", "test4\nsomething else"]
    new_comments = filter_comments(soar_common(), 1, notes_from_qradar, "\nAdded from QRadar")
    assert new_comments == []

class soar_common():
    """ Mock soar_common class for testing """
    def __init__(self) -> None:
        pass

    def get_case_comments(self, soar_id: str):
        """ Mock get case comments return """
        if soar_id == "1":
            return [{"text": "test1\nAdded from QRadar"}, {"text": "test2"}, {"text": "test3\nAdded from QRadar"}, {"text": "test4\nAdded from QRadar\nsomething else"}]
        else:
            return [{"text": "test1\nAdded from QRadar"}, {"text": "test2"}, {"text": "test3\nAdded from QRadar"}, {"text": "test4"}]
