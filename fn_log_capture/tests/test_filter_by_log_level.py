# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

import os
import sys
from fn_log_capture.components.funct_fn_log_capture import filter_log_level, get_log_by_filter

"""
pytest --resilient_app_config=/<path>/<to>/app.config tests/test_filter_by_log_level.py
"""

LOG_TEMPLATE = u"2019-10-21 15:08:42,990 {} Sample Message  Ā ā Ă ă Ą ą Ć ć Ĉ ĉ"

class TestFnLogCaptureFilter:
    def test_filter_by_log_level(self):
        debug_msg = LOG_TEMPLATE.format("DEBUG")
        info_msg = LOG_TEMPLATE.format("INFO")
        warning_msg = LOG_TEMPLATE.format("WARNING")
        error_msg = LOG_TEMPLATE.format("ERROR")

        assert filter_log_level("Debug", debug_msg) is not None
        assert filter_log_level("Debug", info_msg) is not None
        assert filter_log_level("Debug", warning_msg) is not None
        assert filter_log_level("Debug", error_msg) is not None

        assert filter_log_level("Info", info_msg) is not None
        assert filter_log_level("Info", warning_msg) is not None
        assert filter_log_level("Info", error_msg) is not None

        assert filter_log_level("Warning", warning_msg) is not None
        assert filter_log_level("Warning", error_msg) is not None

        assert filter_log_level("Error", error_msg) is not None

    def test_multi_line(self):
        debug_msg = LOG_TEMPLATE.format("DEBUG")

        multi_line = filter_log_level("Debug", debug_msg)
        assert multi_line is not None

        multi_line_result = filter_log_level("Debug", "1 2 3", multi_line=multi_line)
        assert multi_line_result == "1 2 3"

    def test_error_results(self):
        ERROR_RESULTS = u"""2019-10-21 14:11:42,990 ERROR Sample Message Ā ā Ă ă Ą ą Ć ć Ĉ ĉ
Sample Message Ā ā Ă ă Ą ą Ć ć Ĉ ĉ
1
2
3
2019-10-21 15:11:42,990 ERROR Sample Message
Sample Message
1
2
3
2019-10-21 16:11:42,990 ERROR Sample Message
"""
        results = get_filtered_results('Error')
        if sys.version_info.major < 3:
            assert ERROR_RESULTS == unicode(results, encoding='utf-8')
        else:
            assert ERROR_RESULTS == results

    def test_warning_results(self):
        WARNING_RESULTS = u"""2019-10-21 14:10:42,990 WARNING Sample Message Ā ā Ă ă Ą ą Ć ć Ĉ ĉ
2019-10-21 14:11:42,990 ERROR Sample Message Ā ā Ă ă Ą ą Ć ć Ĉ ĉ
Sample Message Ā ā Ă ă Ą ą Ć ć Ĉ ĉ
1
2
3
2019-10-21 15:10:42,990 WARNING Sample Message
2019-10-21 15:11:42,990 ERROR Sample Message
Sample Message
1
2
3
2019-10-21 16:10:42,990 WARNING Sample Message
2019-10-21 16:11:42,990 ERROR Sample Message
"""
        results = get_filtered_results('Warning')
        if sys.version_info.major < 3:
            assert WARNING_RESULTS == unicode(results, encoding='utf-8')
        else:
            assert WARNING_RESULTS == results

    def test_maxlen(self):
        MAXLEN_RESULTS = """3
2019-10-21 16:08:42,990 DEBUG Sample Message
2019-10-21 16:09:42,990 INFO Sample Message
2019-10-21 16:10:42,990 WARNING Sample Message
2019-10-21 16:11:42,990 ERROR Sample Message
"""
        log_file = get_sample_logfile_path()
        num, results = get_log_by_filter(log_file, "Debug", 5)

        if sys.version_info.major < 3:
            assert MAXLEN_RESULTS == unicode(results, encoding='utf-8')
        else:
            assert MAXLEN_RESULTS == results

    def test_maxlen_none(self):
        log_file = get_sample_logfile_path()
        num, results = get_log_by_filter(log_file, "Debug", 0)

        NONE_RESULTS = get_log_file()
        if sys.version_info.major < 3:
            assert unicode(''.join(NONE_RESULTS), encoding='utf-8') == unicode(results, encoding='utf-8')
        else:
            assert ''.join(NONE_RESULTS) == results

def get_log_file():
    log_file = get_sample_logfile_path()

    with open(log_file, 'r') as f:
        return f.readlines()

def get_sample_logfile_path():
    log_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(log_dir, "data", "sample.log")

def get_filtered_results(log_level):
    sample_lines = get_log_file()

    captured_list = []

    filter_results = None
    for line in sample_lines:
        filter_results =  filter_log_level(log_level, line, multi_line=filter_results)
        if filter_results:
            captured_list.append(line)

    return ''.join(captured_list)
