
import pytest
from fn_watsonx_analyst.util import retry
from fn_watsonx_analyst.util.errors import WatsonxTooManyRequestsException


class TestRetryDecorator:

    def get_count(self, exception: Exception) -> int:
        @retry.retry_with_backoff()
        def failing_func(e: Exception):
            pytest.counter = pytest.counter + 1
            raise e

        pytest.counter = 0
        with pytest.raises(exception.__class__):
            failing_func(exception)
        return pytest.counter
    def test_ignore_unkown_exc(self):
        assert self.get_count(ValueError()) == 1

    def test_retry_known_exc(self):
        assert self.get_count(WatsonxTooManyRequestsException()) == 3
