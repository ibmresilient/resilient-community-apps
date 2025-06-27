import pytest
from fn_microsoft_defender.components.defender_poller import check_incident_filters, check_alert_filters

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

TEST_ALERTS = [
    {
        "serviceSource":"MicrosoftDefenderForEndpoint",
        "title":"shreya hash ",
        "description":"shreya hash ",
        "category":"SuspiciousActivity",
        "status":"Resolved",
        "severity":"High",
        "classification":None,
        "determination":None,
        "detectionSource":"CustomerTI",
        "detectorId":"360fdb3b-18a9-471b-9ad0-ad80a4cbcb00",
        "assignedTo":None,
        "actorName":None,
        "threatFamilyName":None
    },
    {
        "serviceSource":"MicrosoftDefenderForEndpoint",
        "title":"shreya hash ",
        "description":"shreya hash ",
        "category":"SuspiciousActivity",
        "status":"New",
        "severity":"Low",
        "classification":None,
        "determination":None,
        "detectionSource":"CustomerTI",
        "detectorId":"360fdb3b-18a9-471b-9ad0-ad80a4cbcb00",
        "assignedTo":None,
        "actorName":None,
        "threatFamilyName":None
    }
]

SUCCESS_ALERT_FILTERS_ONE = {"serviceSource": "MicrosoftDefenderForEndpoint"}

SUCCESS_ALERT_FILTERS_TWO = {
    "serviceSource": "MicrosoftDefenderForEndpoint",
    "severity": "Low"
}

SUCCESS_ALERT_FILTERS_TWO_MISSPELLED = {
    "serviceSource": "MicrosoftDefenderForEndpoint",
    "7everity": "Medium"
}

FAILURE_ALERT_FILTERS_ONE = {"serviceSource": "something"}

FAILURE_ALERT_FILTERS_TWO = {"serviceSource": "something", "severity": "Medium"}

FAILURE_ALERT_FILTERS_TWO_MIXED = {
    "serviceSource": "MicrosoftDefenderForEndpoint",
    "severity": "Medium"
}

FAILURE_ALERT_FILTERS_NULL = {"classification": "MicrosoftDefenderForEndpoint"}

FAILURE_ALERT_FILTERS_MISPELLED = {"clazzification": "MicrosoftDefenderForEndpoint"}

class TestSentinel:
    @pytest.mark.parametrize("incident, filter, result", [
        (TEST_INCIDENT, None, True),
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

    @pytest.mark.parametrize("alert_list, alert_filters, result", [
        (TEST_ALERTS, None, True),
        (TEST_ALERTS, SUCCESS_ALERT_FILTERS_ONE, True),
        (TEST_ALERTS, SUCCESS_ALERT_FILTERS_TWO, True),
        (TEST_ALERTS, SUCCESS_ALERT_FILTERS_TWO_MISSPELLED, True),
        (TEST_ALERTS, FAILURE_ALERT_FILTERS_ONE, False),
        (TEST_ALERTS, FAILURE_ALERT_FILTERS_TWO, False),
        (TEST_ALERTS, FAILURE_ALERT_FILTERS_TWO_MIXED, False),
        (TEST_ALERTS, FAILURE_ALERT_FILTERS_NULL, False),
        (TEST_ALERTS, FAILURE_ALERT_FILTERS_MISPELLED, False)
    ])
    def test_check_alert_filters(self, alert_list, alert_filters, result):
        assert check_alert_filters(alert_list, alert_filters) == result
