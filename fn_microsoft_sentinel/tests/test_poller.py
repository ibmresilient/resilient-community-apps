import pytest
from fn_microsoft_sentinel.components.sentinel_poller import check_incident_filters

TEST_INCIDENT = {
    "status": "A",
    "severity": "Low",
    "list": ["a", "b", "c"],
    "num_value": 5
}

TEST_FILTERS_SUCCESS1 = {
    "status": ["A"],
    "severity": ["Low", "Medium", "High"]
}

TEST_FILTERS_SUCCESS2 = {
    "status": "A",
    "severity": ["Low", "Medium", "High"],
    "extra": "a"
}

TEST_FILTERS_SUCCESS3 = {
    "status": ["A"],
    "severity": "Low",
    "num_value": 5
}

TEST_FILTERS_SUCCESS4 = {
    "status": ["A"],
    "severity": "Low",
    "list": ["a"]
}

TEST_FILTERS_SUCCESS5 = {
    "status": ["A"],
    "severity": "Low",
    "list": "a"
}

TEST_FILTERS_FAIL1 = {
    "status": ["A"],
    "severity": ["Medium", "High"]
}

TEST_FILTERS_FAIL2 = {
    "status": ["A"],
    "severity": "Low",
    "list": "x"
}

TEST_FILTERS_FAIL3 = {
    "status": ["A"],
    "severity": "Low",
    "list": ["x"]
}

class TestSentinel:
    @pytest.mark.parametrize("incident, filter, result", [
        (TEST_INCIDENT, TEST_FILTERS_SUCCESS1, True),
        (TEST_INCIDENT, TEST_FILTERS_SUCCESS2, True),
        (TEST_INCIDENT, TEST_FILTERS_SUCCESS3, True),
        (TEST_INCIDENT, TEST_FILTERS_SUCCESS4, True),
        (TEST_INCIDENT, TEST_FILTERS_SUCCESS5, True),
        (TEST_INCIDENT, TEST_FILTERS_FAIL1, False),
        (TEST_INCIDENT, TEST_FILTERS_FAIL2, False),
        (TEST_INCIDENT, TEST_FILTERS_FAIL3, False)
    ])
    def test_check_incident_filters(self, incident, filter, result):
        assert check_incident_filters(incident, filter) == result
