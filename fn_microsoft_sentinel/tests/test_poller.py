import pytest
from fn_microsoft_sentinel.poller.poller import check_incident_filters, check_incident_template_filters

# Tests for filtering with the original poller filter.
TEST_INCIDENT_1 = {
    "status": "A",
    "severity": "Low",
    "list": ["a", "b", "c"],
    "num_value": 5,
    "title": "TEST-"
}

TEST_INCIDENT_2 = {
    "status": "C",
    "severity": "High",
    "list": ["a", "f", "k", "s"],
    "num_value": 2,
    "title": "Example124"
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

TEST_FILTERS_SUCCESS6 = {
    "title": "TEST-"
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

TEST_FILTERS_FAIL4 = {
    "status": ["A", "C"],
    "title": "TEST-"
}

TEST_FILTERS_FAIL5 = {
    "num_value": 9,
    "severity": "High"
}

class TestSentinelPollerfilter:
    @pytest.mark.parametrize("incident, filter, result", [
        (TEST_INCIDENT_1, TEST_FILTERS_SUCCESS1, True),
        (TEST_INCIDENT_1, TEST_FILTERS_SUCCESS2, True),
        (TEST_INCIDENT_1, TEST_FILTERS_SUCCESS3, True),
        (TEST_INCIDENT_1, TEST_FILTERS_SUCCESS4, True),
        (TEST_INCIDENT_1, TEST_FILTERS_SUCCESS5, True),
        (TEST_INCIDENT_1, TEST_FILTERS_SUCCESS6, True),
        (TEST_INCIDENT_1, TEST_FILTERS_FAIL1, False),
        (TEST_INCIDENT_1, TEST_FILTERS_FAIL2, False),
        (TEST_INCIDENT_1, TEST_FILTERS_FAIL3, False),
        (TEST_INCIDENT_2, TEST_FILTERS_FAIL4, False),
        (TEST_INCIDENT_2, TEST_FILTERS_FAIL5, False)
    ])
    def test_check_incident_filters(self, incident, filter, result):
        assert check_incident_filters(incident, filter) == result

# Tests for filtering with the poller_filters_template.jinja
test_incident_1 = { # Should pass filters
    "title": "Test incident title",
    "description": "Something",
    "severity": "High",
    "status": "New",
    "email": "a@example.com",
    "assignedTo": "Jeff",
    "userPrincipalName": None,
    "labels": [{"labelName": "tag1"}, {"labelName": "tag4"}],
    "alertsCount": 2,
    "bookmarksCount": 1,
    "commentsCount": 5,
    "alertProductNames": None,
    "tactics": "PreAttack",
    "relatedAnalyticRuleIds": None,
    "providerName": None
}

test_incident_2 = { # Should pass filters
    "title": "Test incident 2 title",
    "description": "Hello World",
    "severity": "Low",
    "status": "Active",
    "email": "hi@example.com",
    "assignedTo": "Fred",
    "userPrincipalName": None,
    "labels": [],
    "alertsCount": 45,
    "bookmarksCount": 0,
    "commentsCount": 2,
    "alertProductNames": None,
    "tactics": "InitialAccess",
    "relatedAnalyticRuleIds": None,
    "providerName": None
}

test_incident_3 = { # Should fail filters
    "title": "Test incident 3 title",
    "description": "Hello",
    "severity": "Highest", # Reason for fail
    "status": "Closed", # Reason for fail
    "email": "a@example.com",
    "assignedTo": "Jeff",
    "userPrincipalName": None,
    "labels": [{"labelName": "tag1"}, {"labelName": "tag4"}],
    "alertsCount": 2,
    "bookmarksCount": 1,
    "commentsCount": 5,
    "alertProductNames": None,
    "tactics": "PreAttack",
    "relatedAnalyticRuleIds": None,
    "providerName": None
}

test_incident_4 = { # Should fail filters
    "title": "Test incident 4",
    "description": "Hi",
    "severity": "Medium",
    "status": "Active",
    "email": "e@example.com",
    "assignedTo": "Henry",
    "userPrincipalName": None,
    "labels": [],
    "alertsCount": 45,
    "bookmarksCount": 0,
    "commentsCount": 2,
    "alertProductNames": None,
    "tactics": "SomethingElse", # Reason for fail
    "relatedAnalyticRuleIds": None,
    "providerName": None
}

test_incident_5 = { # Should fail filters
    "title": "Test incident 5",
    "description": "Bye",
    "severity": "Medium",
    "status": "Closed", # Reason for fail
    "email": "y@example.com",
    "assignedTo": "Bill",
    "userPrincipalName": None,
    "labels": [],
    "alertsCount": 8,
    "bookmarksCount": 2,
    "commentsCount": 41,
    "alertProductNames": None,
    "tactics": [],
    "relatedAnalyticRuleIds": None,
    "providerName": None
}

class TestSentinelTemplatePollerFilter:
    @pytest.mark.parametrize("incident, custom_filter_template, result", [
        (test_incident_1, None, True),
        (test_incident_2, None, True),
        (test_incident_3, None, False),
        (test_incident_4, None, False),
        (test_incident_5, None, False)
    ])
    def test_check_incident_template_filters(self, incident, custom_filter_template, result):
        assert check_incident_template_filters(incident, custom_filter_template) == result
