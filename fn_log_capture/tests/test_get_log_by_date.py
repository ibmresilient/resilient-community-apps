# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

import os
import pytest
import sys
from fn_log_capture.components.funct_fn_log_capture import get_log_by_date

BEFORE_RESULTS = u"""2019-10-21 14:08:42,990 DEBUG Sample Message Ā ā Ă ă Ą ą Ć ć Ĉ ĉ
2019-10-21 14:09:42,990 INFO Sample Message Ā ā Ă ă Ą ą Ć ć Ĉ ĉ
2019-10-21 14:10:42,990 WARNING Sample Message Ā ā Ă ă Ą ą Ć ć Ĉ ĉ
2019-10-21 14:11:42,990 ERROR Sample Message Ā ā Ă ă Ą ą Ć ć Ĉ ĉ
Sample Message Ā ā Ă ă Ą ą Ć ć Ĉ ĉ
1
2
3
"""

BEFORE_MAXLEN_RESULTS = u"""2019-10-21 14:11:42,990 ERROR Sample Message Ā ā Ă ă Ą ą Ć ć Ĉ ĉ
Sample Message Ā ā Ă ă Ą ą Ć ć Ĉ ĉ
1
2
3
"""

AFTER_RESULTS = """2019-10-21 15:08:42,990 DEBUG Sample Message
2019-10-21 15:09:42,990 INFO Sample Message
2019-10-21 15:10:42,990 WARNING Sample Message
2019-10-21 15:11:42,990 ERROR Sample Message
Sample Message
1
2
3
2019-10-21 16:08:42,990 DEBUG Sample Message
2019-10-21 16:09:42,990 INFO Sample Message
2019-10-21 16:10:42,990 WARNING Sample Message
2019-10-21 16:11:42,990 ERROR Sample Message
"""

AFTER_MAXLEN_RESULTS = """3
2019-10-21 16:08:42,990 DEBUG Sample Message
2019-10-21 16:09:42,990 INFO Sample Message
2019-10-21 16:10:42,990 WARNING Sample Message
2019-10-21 16:11:42,990 ERROR Sample Message
"""

class TestFnLogByDate:

    @pytest.mark.parametrize("log_capture_maxlen, log_capture_date, log_capture_date_option, log_min_level, "
                             " expected_results", [
                                (None, 1571684880000, "before", "Debug", BEFORE_RESULTS),
                                (5, 1571684880000, "before", "Debug", BEFORE_MAXLEN_RESULTS),
                                (None, 1571684880000, "after", "Debug", AFTER_RESULTS),
                                (5, 1571684880000, "after", "Debug", AFTER_MAXLEN_RESULTS),
                             ])
    def test_success(self,
                     log_capture_maxlen, log_capture_date, log_capture_date_option,
                     log_min_level, expected_results):
        """ Test calling with sample values for the parameters """

        num, result_list = get_log_by_date(get_sample_logfile_path(), log_capture_date, log_capture_date_option, log_capture_maxlen, log_min_level)

        if sys.version_info.major < 3:
            assert expected_results == unicode(result_list, encoding='utf-8')
        else:
            assert expected_results == result_list

def get_sample_logfile_path():
    log_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(log_dir, "data", "sample.log")
