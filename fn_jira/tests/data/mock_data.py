# -*- coding: utf-8 -*-

PACKAGE_NAME = "fn_jira"

def get_mock_config():
    """ Mock configuration data """
    return """
        [fn_jira:my-server]
        url=https://example.com
        auth_method=BASIC
        user=admin@example.com
        password=PASSWORD1
        jira_dt_name=jira_task_references
        verify_cert=False"""

def add_comment_results():
    return {
        "self": "https://example.com/rest/api/2/issue/10055/comment/10350",
        "id": "10350",
        "author": {
            "self": "https://example.com/rest/api/2/user?accountId=123456",
            "accountId": "123456",
            "emailAddress": "test@example.com",
            "displayName": "test",
            "active": True,
            "timeZone": "America/New_York",
            "accountType": "atlassian"
        },
        "body": "404 error is thrown",
        "updateAuthor": {
            "self": "https://example.com/rest/api/2/user?accountId=123456",
            "accountId": "123456",
            "emailAddress": "test@example.com",
            "displayName": "test",
            "active": True,
            "timeZone": "America/New_York",
            "accountType": "atlassian"
        },
        "created": "2023-01-31T09:52:58.464-0500",
        "updated": "2023-01-31T09:52:58.464-0500",
        "jsdPublic": True,
        "jira_url": "<a href=\"https://example.com/browse/JRA-45\">JRA-45</a>"
    }

def create_issue_results():
    return {
        "issue_url": "https://example.com/browse/JRA-47",
        "issue_url_internal": "https://example.com/rest/api/2/issue/10058",
        "issue_key": "JRA-47",
        "issue": {
            "expand": "renderedFields,names,schema,operations,editmeta,changelog,versionedRepresentations,customfield_10010.requestTypePractice",
            "id": "10058",
            "self": "https://example.com/rest/api/2/issue/10058",
            "key": "JRA-47",
            "fields": {
                "statuscategorychangedate": "2023-01-31T12:57:59.508-0500",
                "issuetype": {
                    "self": "https://example.com/rest/api/2/issuetype/10007",
                    "id": "10007",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://example.com/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "28f65659-xxxx-43ad-xxxx-1d00d8d6d9ac",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://example.com/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "JRA",
                    "name": "Test Project",
                    "projectTypeKey": "software",
                    "simplified": True,
                },
                "customfield_10031": None,
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10035": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "issuerestriction": {
                    "issuerestrictions": {},
                    "shouldDisplay": True
                },
                "watches": {
                    "self": "https://example.com/rest/api/2/issue/JRA-47/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "lastViewed": None,
                "created": "2023-01-31T12:57:59.000-0500",
                "customfield_10020": None,
                "customfield_10021": None,
                "customfield_10022": None,
                "customfield_10023": None,
                "priority": {
                    "self": "https://example.com/rest/api/2/priority/4",
                    "iconUrl": "https://example.com/images/icons/priorities/low.svg",
                    "name": "Low",
                    "id": "4"
                },
                "customfield_10024": None,
                "customfield_10025": None,
                "labels": [],
                "customfield_10026": None,
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i0000v:",
                "timeestimate": None,
                "aggregatetimeoriginalestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": {
                    "self": "https://example.com/rest/api/2/user?accountId=123456",
                    "accountId": "123456",
                    "emailAddress": "test@example.com",
                    "displayName": "test",
                    "active": True,
                    "timeZone": "America/New_York",
                    "accountType": "atlassian"
                },
                "updated": "2023-01-31T12:57:59.000-0500",
                "status": {
                    "self": "https://example.com/rest/api/2/status/10003",
                    "description": "",
                    "iconUrl": "https://example.com/",
                    "name": "To Do",
                    "id": "10003",
                    "statusCategory": {
                        "self": "https://example.com/rest/api/2/statuscategory/2",
                        "id": 2,
                        "key": "new",
                        "colorName": "blue-gray",
                        "name": "To Do"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": "IBM SOAR Link: https://test.com:443/#incidents/2231\n\nCreated in IBM SOAR",
                "customfield_10010": None,
                "customfield_10014": None,
                "timetracking": {},
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "customfield_10007": None,
                "security": None,
                "customfield_10008": None,
                "customfield_10009": None,
                "aggregatetimeestimate": None,
                "attachment": [],
                "summary": "IBM SOAR: h",
                "creator": {
                    "self": "https://example.com/rest/api/2/user?accountId=123456",
                    "accountId": "123456",
                    "emailAddress": "test@example.com",
                    "displayName": "test",
                    "active": True,
                    "timeZone": "America/New_York",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://example.com/rest/api/2/user?accountId=123456",
                    "accountId": "123456",
                    "emailAddress": "test@example.com",
                    "displayName": "test",
                    "active": True,
                    "timeZone": "America/New_York",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "comment": {
                    "comments": [],
                    "self": "https://example.com/rest/api/2/issue/10058/comment",
                    "maxResults": 0,
                    "total": 0,
                    "startAt": 0
                },
                "votes": {
                    "self": "https://example.com/rest/api/2/issue/JRA-47/votes",
                    "votes": 0,
                    "hasVoted": False
                },
                "worklog": {
                    "startAt": 0,
                    "maxResults": 20,
                    "total": 0,
                    "worklogs": []
                }
            }
        },
        "jira_dt_name": "jira_task_references"
    }

def mock_init():
    class MockClient(object):
        """ Add Mock connection data """
        AGILE_BASE_URL = "{server}/rest/{agile_rest_path}/{agile_rest_api_version}/{path}"
        DEFAULT_OPTIONS = {
            'server': 'http://localhost:2990/jira',
            'auth_url': '/rest/auth/1/session',
            'context_path': '/',
            'rest_path': 'api',
            'rest_api_version': '2',
            'agile_rest_path': 'agile',
            'agile_rest_api_version': '1.0',
            'verify': True,
            'resilient': True,
            'async': False,
            'async_workers': 5,
            'client_cert': None,
            'check_update': False,
            'delay_reload': 0,
            'headers': {
                'Cache-Control': 'no-cache',
                'Content-Type': 'application/json',
                'X-Atlassian-Token': 'no-check'
            }
        }
        JIRA_BASE_URL = "{server}/rest/{rest_path}/{rest_api_version}/{path}"
        auth = None
        checked_version = False
        deploymentType = "Cloud"
        server_url = "https://example.com"

        def __init__(self):
            """ Mock """
            pass

        def add_comment(self, jira_issue_id, jira_comment):
            """ Mock add_comment return """
            class MockAddComment(object):
                raw = add_comment_results()
                def __init__(self):
                    """ Mock """
                    pass

            return MockAddComment()

        def create_issue(self, fields):
            class MockCreateIssue(object):
                self = "https://example.com/rest/api/2/issue/10058"
                key = "JRA-47"
                raw = {
                        "expand": "renderedFields,names,schema,operations,editmeta,changelog,versionedRepresentations,customfield_10010.requestTypePractice",
                        "id": "10058",
                        "self": "https://example.com/rest/api/2/issue/10058",
                        "key": "JRA-47",
                        "fields": {
                            "statuscategorychangedate": "2023-01-31T12:57:59.508-0500",
                            "issuetype": {
                                "self": "https://example.com/rest/api/2/issuetype/10007",
                                "id": "10007",
                                "description": "Stories track functionality or features expressed as user goals.",
                                "iconUrl": "https://example.com/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                                "name": "Story",
                                "subtask": False,
                                "avatarId": 10315,
                                "entityId": "28f65659-xxxx-43ad-xxxx-1d00d8d6d9ac",
                                "hierarchyLevel": 0
                            },
                            "timespent": None,
                            "customfield_10030": None,
                            "project": {
                                "self": "https://example.com/rest/api/2/project/10001",
                                "id": "10001",
                                "key": "JRA",
                                "name": "Test Project",
                                "projectTypeKey": "software",
                                "simplified": True,
                            },
                            "customfield_10031": None,
                            "fixVersions": [],
                            "aggregatetimespent": None,
                            "resolution": None,
                            "customfield_10035": None,
                            "customfield_10027": None,
                            "customfield_10028": None,
                            "customfield_10029": None,
                            "resolutiondate": None,
                            "workratio": -1,
                            "issuerestriction": {
                                "issuerestrictions": {},
                                "shouldDisplay": True
                            },
                            "watches": {
                                "self": "https://example.com/rest/api/2/issue/JRA-47/watchers",
                                "watchCount": 1,
                                "isWatching": True
                            },
                            "lastViewed": None,
                            "created": "2023-01-31T12:57:59.000-0500",
                            "customfield_10020": None,
                            "customfield_10021": None,
                            "customfield_10022": None,
                            "customfield_10023": None,
                            "priority": {
                                "self": "https://example.com/rest/api/2/priority/4",
                                "iconUrl": "https://example.com/images/icons/priorities/low.svg",
                                "name": "Low",
                                "id": "4"
                            },
                            "customfield_10024": None,
                            "customfield_10025": None,
                            "labels": [],
                            "customfield_10026": None,
                            "customfield_10016": None,
                            "customfield_10017": None,
                            "customfield_10018": {
                                "hasEpicLinkFieldDependency": False,
                                "showField": False,
                                "nonEditableReason": {
                                    "reason": "PLUGIN_LICENSE_ERROR",
                                    "message": "The Parent Link is only available to Jira Premium users."
                                }
                            },
                            "customfield_10019": "0|i0000v:",
                            "timeestimate": None,
                            "aggregatetimeoriginalestimate": None,
                            "versions": [],
                            "issuelinks": [],
                            "assignee": {
                                "self": "https://example.com/rest/api/2/user?accountId=123456",
                                "accountId": "123456",
                                "emailAddress": "test@example.com",
                                "displayName": "test",
                                "active": True,
                                "timeZone": "America/New_York",
                                "accountType": "atlassian"
                            },
                            "updated": "2023-01-31T12:57:59.000-0500",
                            "status": {
                                "self": "https://example.com/rest/api/2/status/10003",
                                "description": "",
                                "iconUrl": "https://example.com/",
                                "name": "To Do",
                                "id": "10003",
                                "statusCategory": {
                                    "self": "https://example.com/rest/api/2/statuscategory/2",
                                    "id": 2,
                                    "key": "new",
                                    "colorName": "blue-gray",
                                    "name": "To Do"
                                }
                            },
                            "components": [],
                            "timeoriginalestimate": None,
                            "description": "IBM SOAR Link: https://test.com:443/#incidents/2231\n\nCreated in IBM SOAR",
                            "customfield_10010": None,
                            "customfield_10014": None,
                            "timetracking": {},
                            "customfield_10015": None,
                            "customfield_10005": None,
                            "customfield_10006": None,
                            "customfield_10007": None,
                            "security": None,
                            "customfield_10008": None,
                            "customfield_10009": None,
                            "aggregatetimeestimate": None,
                            "attachment": [],
                            "summary": "IBM SOAR: h",
                            "creator": {
                                "self": "https://example.com/rest/api/2/user?accountId=123456",
                                "accountId": "123456",
                                "emailAddress": "test@example.com",
                                "displayName": "test",
                                "active": True,
                                "timeZone": "America/New_York",
                                "accountType": "atlassian"
                            },
                            "subtasks": [],
                            "reporter": {
                                "self": "https://example.com/rest/api/2/user?accountId=123456",
                                "accountId": "123456",
                                "emailAddress": "test@example.com",
                                "displayName": "test",
                                "active": True,
                                "timeZone": "America/New_York",
                                "accountType": "atlassian"
                            },
                            "aggregateprogress": {
                                "progress": 0,
                                "total": 0
                            },
                            "customfield_10001": None,
                            "customfield_10002": None,
                            "customfield_10003": None,
                            "customfield_10004": None,
                            "environment": None,
                            "duedate": None,
                            "progress": {
                                "progress": 0,
                                "total": 0
                            },
                            "comment": {
                                "comments": [],
                                "self": "https://example.com/rest/api/2/issue/10058/comment",
                                "maxResults": 0,
                                "total": 0,
                                "startAt": 0
                            },
                            "votes": {
                                "self": "https://example.com/rest/api/2/issue/JRA-47/votes",
                                "votes": 0,
                                "hasVoted": False
                            },
                            "worklog": {
                                "startAt": 0,
                                "maxResults": 20,
                                "total": 0,
                                "worklogs": []
                            }
                        }
                    }
                def __init__(self):
                    """ Mock """
                    pass

                def permalink(self):
                    return "https://example.com/browse/JRA-47"
            return MockCreateIssue()

        def transition_issue(self, issue, transition, fields={}):
            """ Mock transition_issue return """
            class MockTransitionIssue(object):
                def __init__(self):
                    """ Mock init """
                    pass

            return MockTransitionIssue()

        def issue(self, issue_id):
            """ Mock issue return """
            class MockIssue(object):
                def __init__(self):
                    """ Mock init """
                    pass

                def update(self, comment, fields={}):
                    """ Mock update return """
                    class MockUpdate(object):
                        def __init__(self):
                            """ Mock init """
                            pass
                    return MockUpdate()

            return MockIssue()

    return MockClient()
