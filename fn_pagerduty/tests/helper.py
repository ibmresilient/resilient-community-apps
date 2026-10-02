# -*- coding: utf-8 -*-
"""Helper for tests"""

class MockClient:
    def __init__(self, appDict: dict=None):
        # Mock
        pass

    def create_incident(self):
        return mock_create_incident()

    def create_note(self, incident_id: str=None, note: str=None):
        return mock_create_note()

    def create_service(self):
        return mock_create_service()

    def list_incidents(self, timestamp=None):
        return mock_list_incidents()

    def list_services(self):
        return mock_list_services()

    def update_incident(self, incident_id=None, status=None, priority=None, resolution=None, severity=None):
        return mock_update_incident()

def mock_create_incident():
    return {
        "incident": {
            "incident_number": 3,
            "title": "SOAR: Test1",
            "description": "SOAR: Test1",
            "created_at": "2024-04-16T14:16:44Z",
            "updated_at": "2024-04-16T14:16:44Z",
            "status": "triggered",
            "incident_key": "RES-2123",
            "service": {
                "id": "P2BUF3J",
                "type": "service_reference",
                "summary": "Default Service",
                "self": "https://api.pagerduty.com/services/P2BUF3J",
                "html_url": "https://ibmtest-8.pagerduty.com/service-directory/P2BUF3J",
            },
            "assignments": [
                {
                    "at": "2024-04-16T14:16:44Z",
                    "assignee": {
                        "id": "PZ8LY8P",
                        "type": "user_reference",
                        "summary": "John Doe",
                        "self": "https://api.pagerduty.com/users/PZ8LY8P",
                        "html_url": "https://ibmtest-8.pagerduty.com/users/PZ8LY8P",
                    },
                }
            ],
            "assigned_via": "escalation_policy",
            "last_status_change_at": "2024-04-16T14:16:44Z",
            "resolved_at": None,
            "first_trigger_log_entry": {
                "id": "R0D5Q149ACTOT09DXWE8JNPYKA",
                "type": "trigger_log_entry_reference",
                "summary": "Triggered through the website.",
                "self": "https://api.pagerduty.com/log_entries/R0D5Q149ACTOT09DXWE8JNPYKA",
                "html_url": "https://ibmtest-8.pagerduty.com/incidents/Q06KVFVBOFHPI7/log_entries/R0D5Q149ACTOT09DXWE8JNPYKA",
            },
            "alert_counts": {"all": 0, "triggered": 0, "resolved": 0},
            "is_mergeable": True,
            "escalation_policy": {
                "id": "PNR45CQ",
                "type": "escalation_policy_reference",
                "summary": "Default",
                "self": "https://api.pagerduty.com/escalation_policies/PNR45CQ",
                "html_url": "https://ibmtest-8.pagerduty.com/escalation_policies/PNR45CQ",
            },
            "teams": [],
            "impacted_services": [
                {
                    "id": "P2BUF3J",
                    "type": "service_reference",
                    "summary": "Default Service",
                    "self": "https://api.pagerduty.com/services/P2BUF3J",
                    "html_url": "https://ibmtest-8.pagerduty.com/service-directory/P2BUF3J",
                }
            ],
            "pending_actions": [],
            "acknowledgements": [],
            "basic_alert_grouping": None,
            "alert_grouping": None,
            "last_status_change_by": {
                "id": "P2BUF3J",
                "type": "service_reference",
                "summary": "Default Service",
                "self": "https://api.pagerduty.com/services/P2BUF3J",
                "html_url": "https://ibmtest-8.pagerduty.com/service-directory/P2BUF3J",
            },
            "priority": {
                "id": "PODCA25",
                "type": "priority",
                "summary": "P3",
                "self": "https://api.pagerduty.com/priorities/PODCA25",
                "html_url": None,
                "account_id": "PSHM5T7",
                "color": "f9b406",
                "created_at": "2024-04-15T11:57:37Z",
                "description": "",
                "name": "P3",
                "order": 300000000,
                "schema_version": 0,
                "updated_at": "2024-04-15T11:57:37Z",
            },
            "incidents_responders": [],
            "responder_requests": [],
            "subscriber_requests": [],
            "urgency": "high",
            "id": "Q06KVFVBOFHPI7",
            "type": "incident",
            "summary": "[#3] SOAR: Test1",
            "self": "https://api.pagerduty.com/incidents/Q06KVFVBOFHPI7",
            "html_url": "https://ibmtest-8.pagerduty.com/incidents/Q06KVFVBOFHPI7",
            "body": {
                "details": "https://example.SOAR.com:443/#incidents/2123?orgId=Org4\n"
            },
        }
    }

def mock_create_note():
    return {
        "note": {
            "id": "PK0LFV9",
            "user": {
                "id": "PZ8LY8P",
                "type": "user_reference",
                "summary": "John Doe",
                "self": "https://api.pagerduty.com/users/PZ8LY8P",
                "html_url": "https://ibmtest-8.pagerduty.com/users/PZ8LY8P"
            },
            "content": "test",
            "created_at": "2024-04-16T10:20:15-04:00",
            "channel": {
                "summary": "The PagerDuty website or APIs"
            }
        }
    }

def mock_create_service():
    return {
        "service": {
        "id": "PRRX0IZ",
        "name": "test1",
        "description": "something ",
        "created_at": "2024-04-16T10:18:31-04:00",
        "updated_at": "2024-04-16T10:18:31-04:00",
        "status": "active",
        "teams": [],
        "alert_creation": "create_alerts_and_incidents",
        "addons": [],
        "scheduled_actions": [],
        "support_hours": None,
        "last_incident_timestamp": None,
        "escalation_policy": {
        "id": "PP43S9F",
        "type": "escalation_policy_reference",
        "summary": "testService1-ep",
        "self": "https://api.pagerduty.com/escalation_policies/PP43S9F",
        "html_url": "https://ibmtest-8.pagerduty.com/escalation_policies/PP43S9F"
        },
        "incident_urgency_rule": {
        "type": "constant",
        "urgency": "high"
        },
        "acknowledgement_timeout": None,
        "auto_resolve_timeout": None,
        "alert_grouping": None,
        "alert_grouping_timeout": None,
        "alert_grouping_parameters": {
        "type": None,
        "config": None,
        "is_global_configuration": False
        },
        "integrations": [],
        "response_play": None,
        "type": "service",
        "summary": "test1",
        "self": "https://api.pagerduty.com/services/PRRX0IZ",
        "html_url": "https://ibmtest-8.pagerduty.com/service-directory/PRRX0IZ"
        }
    }

def mock_list_incidents():
    return {
        "incidents": [
        {
            "incident_number": 1,
            "title": "Example Incident",
            "description": "Example Incident",
            "created_at": "2024-04-15T12:04:38Z",
            "updated_at": "2024-04-15T12:05:05Z",
            "status": "acknowledged",
            "incident_key": "6a2982771c8e4cdf890142d7d678b475",
            "service": {
            "id": "P2BUF3J",
            "type": "service_reference",
            "summary": "Default Service",
            "self": "https://api.pagerduty.com/services/P2BUF3J",
            "html_url": "https://ibmtest-8.pagerduty.com/service-directory/P2BUF3J"
            },
            "assignments": [
            {
                "at": "2024-04-15T12:04:38Z",
                "assignee": {
                "id": "PZ8LY8P",
                "type": "user_reference",
                "summary": "John Doe",
                "self": "https://api.pagerduty.com/users/PZ8LY8P",
                "html_url": "https://ibmtest-8.pagerduty.com/users/PZ8LY8P"
                }
            }
            ],
            "assigned_via": "escalation_policy",
            "last_status_change_at": "2024-04-15T12:05:04Z",
            "resolved_at": None,
            "first_trigger_log_entry": {
            "id": "RQG4YTG7S22XOHNY12DLEXQKOT",
            "type": "trigger_log_entry_reference",
            "summary": "Triggered through the website.",
            "self": "https://api.pagerduty.com/log_entries/RQG4YTG7S22XOHNY12DLEXQKOT",
            "html_url": "https://ibmtest-8.pagerduty.com/incidents/Q2F1BG6LBQ69MG/log_entries/RQG4YTG7S22XOHNY12DLEXQKOT"
            },
            "alert_counts": {
            "all": 0,
            "triggered": 0,
            "resolved": 0
            },
            "is_mergeable": True,
            "escalation_policy": {
            "id": "PNR45CQ",
            "type": "escalation_policy_reference",
            "summary": "Default",
            "self": "https://api.pagerduty.com/escalation_policies/PNR45CQ",
            "html_url": "https://ibmtest-8.pagerduty.com/escalation_policies/PNR45CQ"
            },
            "teams": [],
            "pending_actions": [],
            "acknowledgements": [
            {
                "at": "2024-04-15T12:05:04Z",
                "acknowledger": {
                "id": "PZ8LY8P",
                "type": "user_reference",
                "summary": "John Doe",
                "self": "https://api.pagerduty.com/users/PZ8LY8P",
                "html_url": "https://ibmtest-8.pagerduty.com/users/PZ8LY8P"
                }
            }
            ],
            "basic_alert_grouping": None,
            "alert_grouping": None,
            "last_status_change_by": {
            "id": "PZ8LY8P",
            "type": "user_reference",
            "summary": "John Doe",
            "self": "https://api.pagerduty.com/users/PZ8LY8P",
            "html_url": "https://ibmtest-8.pagerduty.com/users/PZ8LY8P"
            },
            "priority": None,
            "incidents_responders": [],
            "responder_requests": [],
            "subscriber_requests": [],
            "urgency": "high",
            "id": "Q2F1BG6LBQ69MG",
            "type": "incident",
            "summary": "[#1] Example Incident",
            "self": "https://api.pagerduty.com/incidents/Q2F1BG6LBQ69MG",
            "html_url": "https://ibmtest-8.pagerduty.com/incidents/Q2F1BG6LBQ69MG"
        },
        {
            "incident_number": 2,
            "title": "SOAR: Test123",
            "description": "SOAR: Test123",
            "created_at": "2024-04-15T18:20:42Z",
            "updated_at": "2024-04-15T18:20:42Z",
            "status": "triggered",
            "incident_key": "RES-2122",
            "service": {
            "id": "P2BUF3J",
            "type": "service_reference",
            "summary": "Default Service",
            "self": "https://api.pagerduty.com/services/P2BUF3J",
            "html_url": "https://ibmtest-8.pagerduty.com/service-directory/P2BUF3J"
            },
            "assignments": [
            {
                "at": "2024-04-15T18:20:43Z",
                "assignee": {
                "id": "PZ8LY8P",
                "type": "user_reference",
                "summary": "John Doe",
                "self": "https://api.pagerduty.com/users/PZ8LY8P",
                "html_url": "https://ibmtest-8.pagerduty.com/users/PZ8LY8P"
                }
            }
            ],
            "assigned_via": "escalation_policy",
            "last_status_change_at": "2024-04-15T18:20:42Z",
            "resolved_at": None,
            "first_trigger_log_entry": {
            "id": "RO8RV55CPFX6921ZPS6KG9S9VD",
            "type": "trigger_log_entry_reference",
            "summary": "Triggered through the website.",
            "self": "https://api.pagerduty.com/log_entries/RO8RV55CPFX6921ZPS6KG9S9VD",
            "html_url": "https://ibmtest-8.pagerduty.com/incidents/Q2JZLNGU7QQGDP/log_entries/RO8RV55CPFX6921ZPS6KG9S9VD"
            },
            "alert_counts": {
            "all": 0,
            "triggered": 0,
            "resolved": 0
            },
            "is_mergeable": True,
            "escalation_policy": {
            "id": "PNR45CQ",
            "type": "escalation_policy_reference",
            "summary": "Default",
            "self": "https://api.pagerduty.com/escalation_policies/PNR45CQ",
            "html_url": "https://ibmtest-8.pagerduty.com/escalation_policies/PNR45CQ"
            },
            "teams": [],
            "pending_actions": [],
            "acknowledgements": [],
            "basic_alert_grouping": None,
            "alert_grouping": None,
            "last_status_change_by": {
            "id": "P2BUF3J",
            "type": "service_reference",
            "summary": "Default Service",
            "self": "https://api.pagerduty.com/services/P2BUF3J",
            "html_url": "https://ibmtest-8.pagerduty.com/service-directory/P2BUF3J"
            },
            "priority": {
            "id": "PODCA25",
            "type": "priority",
            "summary": "P3",
            "self": "https://api.pagerduty.com/priorities/PODCA25",
            "html_url": None,
            "account_id": "PSHM5T7",
            "color": "f9b406",
            "created_at": "2024-04-15T11:57:37Z",
            "description": "",
            "name": "P3",
            "order": 300000000,
            "schema_version": 0,
            "updated_at": "2024-04-15T11:57:37Z"
            },
            "incidents_responders": [],
            "responder_requests": [],
            "subscriber_requests": [],
            "urgency": "high",
            "id": "Q2JZLNGU7QQGDP",
            "type": "incident",
            "summary": "[#2] SOAR: Test123",
            "self": "https://api.pagerduty.com/incidents/Q2JZLNGU7QQGDP",
            "html_url": "https://ibmtest-8.pagerduty.com/incidents/Q2JZLNGU7QQGDP"
        },
        {
            "incident_number": 3,
            "title": "SOAR: Test1",
            "description": "SOAR: Test1",
            "created_at": "2024-04-16T14:16:44Z",
            "updated_at": "2024-04-16T14:16:44Z",
            "status": "triggered",
            "incident_key": "RES-2123",
            "service": {
            "id": "P2BUF3J",
            "type": "service_reference",
            "summary": "Default Service",
            "self": "https://api.pagerduty.com/services/P2BUF3J",
            "html_url": "https://ibmtest-8.pagerduty.com/service-directory/P2BUF3J"
            },
            "assignments": [
            {
                "at": "2024-04-16T14:16:44Z",
                "assignee": {
                "id": "PZ8LY8P",
                "type": "user_reference",
                "summary": "John Doe",
                "self": "https://api.pagerduty.com/users/PZ8LY8P",
                "html_url": "https://ibmtest-8.pagerduty.com/users/PZ8LY8P"
                }
            }
            ],
            "assigned_via": "escalation_policy",
            "last_status_change_at": "2024-04-16T14:16:44Z",
            "resolved_at": None,
            "first_trigger_log_entry": {
            "id": "R0D5Q149ACTOT09DXWE8JNPYKA",
            "type": "trigger_log_entry_reference",
            "summary": "Triggered through the website.",
            "self": "https://api.pagerduty.com/log_entries/R0D5Q149ACTOT09DXWE8JNPYKA",
            "html_url": "https://ibmtest-8.pagerduty.com/incidents/Q06KVFVBOFHPI7/log_entries/R0D5Q149ACTOT09DXWE8JNPYKA"
            },
            "alert_counts": {
            "all": 0,
            "triggered": 0,
            "resolved": 0
            },
            "is_mergeable": True,
            "escalation_policy": {
            "id": "PNR45CQ",
            "type": "escalation_policy_reference",
            "summary": "Default",
            "self": "https://api.pagerduty.com/escalation_policies/PNR45CQ",
            "html_url": "https://ibmtest-8.pagerduty.com/escalation_policies/PNR45CQ"
            },
            "teams": [],
            "pending_actions": [],
            "acknowledgements": [],
            "basic_alert_grouping": None,
            "alert_grouping": None,
            "last_status_change_by": {
            "id": "P2BUF3J",
            "type": "service_reference",
            "summary": "Default Service",
            "self": "https://api.pagerduty.com/services/P2BUF3J",
            "html_url": "https://ibmtest-8.pagerduty.com/service-directory/P2BUF3J"
            },
            "priority": {
            "id": "PODCA25",
            "type": "priority",
            "summary": "P3",
            "self": "https://api.pagerduty.com/priorities/PODCA25",
            "html_url": None,
            "account_id": "PSHM5T7",
            "color": "f9b406",
            "created_at": "2024-04-15T11:57:37Z",
            "description": "",
            "name": "P3",
            "order": 300000000,
            "schema_version": 0,
            "updated_at": "2024-04-15T11:57:37Z"
            },
            "incidents_responders": [],
            "responder_requests": [],
            "subscriber_requests": [],
            "urgency": "high",
            "id": "Q06KVFVBOFHPI7",
            "type": "incident",
            "summary": "[#3] SOAR: Test1",
            "self": "https://api.pagerduty.com/incidents/Q06KVFVBOFHPI7",
            "html_url": "https://ibmtest-8.pagerduty.com/incidents/Q06KVFVBOFHPI7"
        }
        ],
        "limit": 25,
        "offset": 0,
        "total": None,
        "more": False
    }

def mock_list_services():
    return {
        "services": [
        {
            "id": "P2BUF3J",
            "name": "Default Service",
            "description": "Your first service - describe what this service is monitoring and any information that will help responders.\n\nFor example: What is the SLA of this service? Where are the runbooks for this service stored? What tier level is this service?",
            "created_at": "2024-04-15T07:57:42-04:00",
            "updated_at": "2024-04-15T07:57:42-04:00",
            "status": "critical",
            "teams": [],
            "alert_creation": "create_alerts_and_incidents",
            "addons": [],
            "scheduled_actions": [],
            "support_hours": None,
            "last_incident_timestamp": "2024-04-16T14:16:44Z",
            "escalation_policy": {
            "id": "PNR45CQ",
            "type": "escalation_policy_reference",
            "summary": "Default",
            "self": "https://api.pagerduty.com/escalation_policies/PNR45CQ",
            "html_url": "https://ibmtest-8.pagerduty.com/escalation_policies/PNR45CQ"
            },
            "incident_urgency_rule": {
            "type": "constant",
            "urgency": "high"
            },
            "acknowledgement_timeout": None,
            "auto_resolve_timeout": None,
            "alert_grouping": None,
            "alert_grouping_timeout": None,
            "alert_grouping_parameters": {
            "type": None,
            "config": None,
            "is_global_configuration": False
            },
            "integrations": [],
            "response_play": None,
            "type": "service",
            "summary": "Default Service",
            "self": "https://api.pagerduty.com/services/P2BUF3J",
            "html_url": "https://ibmtest-8.pagerduty.com/service-directory/P2BUF3J"
        },
        {
            "id": "PRRX0IZ",
            "name": "test1",
            "description": "something ",
            "created_at": "2024-04-16T10:18:31-04:00",
            "updated_at": "2024-04-16T10:18:31-04:00",
            "status": "active",
            "teams": [],
            "alert_creation": "create_alerts_and_incidents",
            "addons": [],
            "scheduled_actions": [],
            "support_hours": None,
            "last_incident_timestamp": None,
            "escalation_policy": {
            "id": "PP43S9F",
            "type": "escalation_policy_reference",
            "summary": "testService1-ep",
            "self": "https://api.pagerduty.com/escalation_policies/PP43S9F",
            "html_url": "https://ibmtest-8.pagerduty.com/escalation_policies/PP43S9F"
            },
            "incident_urgency_rule": {
            "type": "constant",
            "urgency": "high"
            },
            "acknowledgement_timeout": None,
            "auto_resolve_timeout": None,
            "alert_grouping": None,
            "alert_grouping_timeout": None,
            "alert_grouping_parameters": {
            "type": None,
            "config": None,
            "is_global_configuration": False
            },
            "integrations": [],
            "response_play": None,
            "type": "service",
            "summary": "test1",
            "self": "https://api.pagerduty.com/services/PRRX0IZ",
            "html_url": "https://ibmtest-8.pagerduty.com/service-directory/PRRX0IZ"
        },
        {
            "id": "P14YD92",
            "name": "testService1",
            "description": None,
            "created_at": "2024-04-15T13:57:56-04:00",
            "updated_at": "2024-04-15T13:57:56-04:00",
            "status": "active",
            "teams": [],
            "alert_creation": "create_alerts_and_incidents",
            "addons": [],
            "scheduled_actions": [],
            "support_hours": None,
            "last_incident_timestamp": None,
            "escalation_policy": {
            "id": "PP43S9F",
            "type": "escalation_policy_reference",
            "summary": "testService1-ep",
            "self": "https://api.pagerduty.com/escalation_policies/PP43S9F",
            "html_url": "https://ibmtest-8.pagerduty.com/escalation_policies/PP43S9F"
            },
            "incident_urgency_rule": {
            "type": "constant",
            "urgency": "high"
            },
            "acknowledgement_timeout": None,
            "auto_resolve_timeout": None,
            "alert_grouping": "intelligent",
            "alert_grouping_timeout": None,
            "alert_grouping_parameters": {
            "type": "intelligent",
            "config": {
                "time_window": 300,
                "recommended_time_window": 300
            },
            "is_global_configuration": False
            },
            "integrations": [
            {
                "id": "P0CMKFP",
                "type": "generic_email_inbound_integration_reference",
                "summary": "Email",
                "self": "https://api.pagerduty.com/services/P14YD92/integrations/P0CMKFP",
                "html_url": "https://ibmtest-8.pagerduty.com/services/P14YD92/integrations/P0CMKFP"
            }
            ],
            "response_play": None,
            "type": "service",
            "summary": "testService1",
            "self": "https://api.pagerduty.com/services/P14YD92",
            "html_url": "https://ibmtest-8.pagerduty.com/service-directory/P14YD92"
        }
        ],
        "limit": 25,
        "offset": 0,
        "total": None,
        "more": False
    }

def mock_update_incident():
    return {
        "incident": {
        "incident_number": 3,
        "title": "SOAR: Test1",
        "description": "SOAR: Test1",
        "created_at": "2024-04-16T14:16:44Z",
        "updated_at": "2024-04-16T14:20:12Z",
        "status": "resolved",
        "incident_key": "RES-2123",
        "service": {
            "id": "P2BUF3J",
            "type": "service_reference",
            "summary": "Default Service",
            "self": "https://api.pagerduty.com/services/P2BUF3J",
            "html_url": "https://ibmtest-8.pagerduty.com/service-directory/P2BUF3J"
        },
        "assignments": [],
        "assigned_via": "escalation_policy",
        "last_status_change_at": "2024-04-16T14:20:12Z",
        "resolved_at": "2024-04-16T14:20:12Z",
        "first_trigger_log_entry": {
            "id": "R0D5Q149ACTOT09DXWE8JNPYKA",
            "type": "trigger_log_entry_reference",
            "summary": "Triggered through the website.",
            "self": "https://api.pagerduty.com/log_entries/R0D5Q149ACTOT09DXWE8JNPYKA",
            "html_url": "https://ibmtest-8.pagerduty.com/incidents/Q06KVFVBOFHPI7/log_entries/R0D5Q149ACTOT09DXWE8JNPYKA"
        },
        "alert_counts": {
            "all": 0,
            "triggered": 0,
            "resolved": 0
        },
        "is_mergeable": True,
        "escalation_policy": {
            "id": "PNR45CQ",
            "type": "escalation_policy_reference",
            "summary": "Default",
            "self": "https://api.pagerduty.com/escalation_policies/PNR45CQ",
            "html_url": "https://ibmtest-8.pagerduty.com/escalation_policies/PNR45CQ"
        },
        "teams": [],
        "impacted_services": [
            {
            "id": "P2BUF3J",
            "type": "service_reference",
            "summary": "Default Service",
            "self": "https://api.pagerduty.com/services/P2BUF3J",
            "html_url": "https://ibmtest-8.pagerduty.com/service-directory/P2BUF3J"
            }
        ],
        "pending_actions": [],
        "acknowledgements": [],
        "basic_alert_grouping": None,
        "alert_grouping": None,
        "last_status_change_by": {
            "id": "PZ8LY8P",
            "type": "user_reference",
            "summary": "John Doe",
            "self": "https://api.pagerduty.com/users/PZ8LY8P",
            "html_url": "https://ibmtest-8.pagerduty.com/users/PZ8LY8P"
        },
        "priority": {
            "id": "PSQ0AEV",
            "type": "priority",
            "summary": "P2",
            "self": "https://api.pagerduty.com/priorities/PSQ0AEV",
            "html_url": None,
            "account_id": "PSHM5T7",
            "color": "eb6016",
            "created_at": "2024-04-15T11:57:37Z",
            "description": "",
            "name": "P2",
            "order": 400000000,
            "schema_version": 0,
            "updated_at": "2024-04-15T11:57:37Z"
        },
        "resolve_reason": None,
        "incidents_responders": [],
        "responder_requests": [],
        "subscriber_requests": [],
        "urgency": "low",
        "id": "Q06KVFVBOFHPI7",
        "type": "incident",
        "summary": "[#3] SOAR: Test1",
        "self": "https://api.pagerduty.com/incidents/Q06KVFVBOFHPI7",
        "html_url": "https://ibmtest-8.pagerduty.com/incidents/Q06KVFVBOFHPI7"
        }
    }
