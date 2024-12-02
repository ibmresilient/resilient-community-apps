# -*- coding: utf-8 -*-
# helper for tests


def mock_init_client():

    class MockClient(object):
        """Add Mock connection data"""

        def __init__(self, options=None, rc=None) -> None:
            self.options = options
            self.rc = rc

        def fire_flow_auth(self) -> str:
            # Create mock connect to AlgoSec FireFlow
            return "mockSessionID", "mockFaSessionId", "mockPhpSessionId"

        def firewall_analyzer_auth(self) -> str:
            # Create mock connect to AlgoSec Firewall Analyzer (AFA).
            return "mockSessionId"

        def appViz_auth(self) -> str:
            # Create mock connection to AlgoSec Business Flow (AppViz)
            return "mockAccessToken"

    return MockClient()


def mock_firewall_analyzer():
    class MockFirewallAnalyzer(object):
        def __init__(self, rc=None, sessionID=None) -> None:
            self.rc = rc
            self.sessionID = sessionID

        def traffic_simulation_query(
            self,
            source: str = "1.1.1.1",
            destination: str = "8.8.8.8",
            service: str = "any",
            target: str = "ALL_FIREWALLS",
            application: str = "any",
            user: str = "any",
            includeruleszones: bool = False,
            includedevicespaths: bool = False,
        ) -> dict:
            """Mock Run a traffic simulation query on AlgoSec"""
            return {
                "queryUIResult": "https://aglosec/fa/query/results/#/work/ALL_FIREWALLS_query-1722608134438/",
                "queryResult": [
                    {
                        "queryDescription": "1.2.3.5=>8.8.8.8:any:any:any",
                        "fipResult": "Unreachable",
                        "finalResult": "Not routed",
                        "queryHTMLPath": "https://local.algosec.com/fa/query/results/#/work/ALL_FIREWALLS_query-1722608134438/",
                    }
                ],
            }

    return MockFirewallAnalyzer()


def mock_fireflow():
    class MockFireflow(object):
        def __init__(
            self,
            rc = None,
            sessionID: str = None,
            faSessionID: str = None,
            phpSessionID: str = None,
        ) -> None:
            self.rc = rc
            self.sessionID = sessionID
            self.faSessionID = faSessionID
            self.phpSessionID = phpSessionID

        def traffic_change_request(
            self,
            source: str = "any",
            destination: str = "any",
            service: str = "any",
            user: str = "",
            application: str = "any",
            action: str = "Drop",
            template: str = "Basic Change Traffic Request",
            description: str = "",
            subject: str = "",
            devices: str = "",
        ) -> dict:
            """Mock create a traffic change request on the AlgoSec server"""
            return {
                "status": "Success",
                "messages": [],
                "data": {
                    "changeRequestId": 11,
                    "redirectUrl": "https://1.2.3.4/FireFlow/Ticket/Display.html?id=11",
                },
            }

        def traffic_change_request_details(self, request_id: int = 11) -> dict:
            """Mock get the details of a given traffic change request"""
            return {
                "status": "Success",
                "messages": [],
                "data": {
                    "id": 11,
                    "fields": [
                        {"name": "Owner", "values": ["admin<admin@example.com>"]},
                        {"name": "Workflow", "values": ["Basic"]},
                        {"name": "Creator", "values": ["admin<admin@example.com>"]},
                        {
                            "name": "Subject",
                            "values": ["IBM SOAR Isolation Request for 1.1.1.1"],
                        },
                        {
                            "name": "Ticket Template Name",
                            "values": ["Basic Change Traffic Request"],
                        },
                        {
                            "name": "Change Request Description",
                            "values": [
                                "Isolation Request initiated by the IBM SOAR Integration."
                            ],
                        },
                        {"name": "LastUpdated", "values": ["2024-08-02 09:26:26"]},
                        {"name": "Requestor", "values": ["admin<admin@example.com>"]},
                        {"name": "Form Type", "values": ["Traffic Change"]},
                        {"name": "status", "values": ["open"]},
                    ],
                    "originalTraffic": [
                        {
                            "source": {
                                "items": [{"value": "1.1.1.1"}, {"value": "any"}]
                            },
                            "destination": {
                                "items": [{"value": "any"}, {"value": "1.1.1.1"}]
                            },
                            "service": {"items": [{"value": "any"}]},
                            "application": {"items": [{"value": "any"}]},
                            "user": {"items": [{"value": "any"}]},
                            "fields": [
                                {"name": "Requested URL Category", "values": ["any"]}
                            ],
                            "action": "Drop",
                        }
                    ],
                    "plannedTraffic": [
                        {
                            "source": {
                                "items": [{"value": "1.1.1.1"}, {"value": "any"}]
                            },
                            "destination": {
                                "items": [{"value": "any"}, {"value": "1.1.1.1"}]
                            },
                            "service": {"items": [{"value": "*"}]},
                            "application": {"items": [{"value": "any"}]},
                            "user": {"items": [{"value": "any"}]},
                            "fields": [
                                {"name": "Change URL Category", "values": ["any"]}
                            ],
                            "action": "Drop",
                        }
                    ],
                },
            }

    return MockFireflow()
