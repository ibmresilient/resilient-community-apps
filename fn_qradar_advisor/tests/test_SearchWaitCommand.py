#
#   Unit test for SearchWaitCommand.py
#
#   This is common code, just need to be test in one function
#
#   100% coverage
#
from fn_qradar_advisor.lib.search_wait_command import SearchWaitCommand
from fn_qradar_advisor.lib.search_wait_command import SearchJobFailure
from fn_qradar_advisor.lib.search_wait_command import SearchFailure
from fn_qradar_advisor.lib.search_wait_command import SearchTimeout
import time


def test_search_and_wait_command():

    class DummySearchAndWait(SearchWaitCommand):
        def __init__(self, timeout, period):
            self.search_status = self.SEARCH_STATUS_ERROR_STOP
            self.search_id = ""
            self.search_result = ""
            super(DummySearchAndWait, self).__init__(timeout, period)

        def check_status(self, search_id):
            return self.search_status

        def get_search_id(self, query):
            return self.search_id

        def get_search_result(self, search_id):
            return self.search_result

    # Test data
    timeout = 2
    period = 1

    search_cmd = DummySearchAndWait(timeout, period)

    assert search_cmd.search_timeout == timeout
    assert search_cmd.polling_period == period

    # 1. Test normal case

    try:
        expected_result = "Expected search result"
        search_cmd.search_result = expected_result
        search_cmd.search_id = "Fake id"
        search_cmd.search_status = SearchWaitCommand.SEARCH_STATUS_COMPLETED

        ret = search_cmd.perform_search("fake query")

        assert ret == expected_result

    except Exception as e:
        assert False

    # 2. Test search job failure by simulating search_id = None
    try:
        search_cmd.search_id = None
        ret = search_cmd.perform_search("fake query")
        # It should stop here
        assert False
    except SearchJobFailure as e:
        assert True
    except Exception:
        assert False

    # 3. Test failed to get status

    search_cmd.search_id = "fake id"
    search_cmd.search_status = SearchWaitCommand.SEARCH_STATUS_ERROR_STOP
    try:
        ret = search_cmd.perform_search("fake query")
        # It should stop here
        assert False
    except SearchFailure as e:
        assert True
    except Exception:
        assert False

    # 4. Test timeout
    start_time = time.time()
    search_cmd.search_status = SearchWaitCommand.SEARCH_STATUS_WAITING
    try:
        ret = search_cmd.perform_search("fake query")
        # It should stop here
        assert False
    except SearchTimeout as e:
        print("Times out after {} sec.".format(str(time.time()-start_time)))
        assert True
    except Exception:
        assert False

    # 5. Same effect for unknown and continue

    search_cmd.search_status = SearchWaitCommand.SEARCH_STATUS_UNKNOWN_CONTINUE
    try:
        ret = search_cmd.perform_search("fake query")
        # It should stop here
        assert False
    except SearchTimeout as e:
        print("Times out after {} sec.".format(str(time.time() - start_time)))
        assert True
    except Exception:
        assert False

    # 6. Test super class method before overriden by subclass
    base_cmd = SearchWaitCommand()
    assert base_cmd.get_search_id("fake query") == ""
    assert base_cmd.get_search_result("fake id") == {}
    assert base_cmd.check_status("fake id") == SearchWaitCommand.SEARCH_STATUS_ERROR_STOP
