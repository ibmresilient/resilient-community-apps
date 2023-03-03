# -*- coding: utf-8 -*-

def get_mock_config():
    """ Mock configuration data """
    return {
        "url": "https://example.com",
        "auth_method": "BASIC",
        "user": "admin@example.com",
        "password": "PASSWORD1",
        "jira_dt_name": "jira_task_references",
        "verify_cert": "false"
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

        def __init__(self, **args):
            """ Mock """
            pass

        def add_comment():
            """ Mock add_comment return """
            return {
                "raw": {
                    "self": "https://team-111.atlassian.net/rest/api/2/issue/10055/comment/10350",
                    "id": "10350",
                    "author": {
                    "self": "https://team-111.atlassian.net/rest/api/2/user?accountId=123456",
                    "accountId": "123456",
                    "emailAddress": "test@example.com",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/2cfc976767db44422e9281fb012845a2?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FR-1.png",
                        "24x24": "https://secure.gravatar.com/avatar/2cfc976767db44422e9281fb012845a2?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FR-1.png",
                        "16x16": "https://secure.gravatar.com/avatar/2cfc976767db44422e9281fb012845a2?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FR-1.png",
                        "32x32": "https://secure.gravatar.com/avatar/2cfc976767db44422e9281fb012845a2?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FR-1.png"
                    },
                    "displayName": "test",
                    "active": True,
                    "timeZone": "America/New_York",
                    "accountType": "atlassian"
                    },
                    "body": "404 error is thrown",
                    "updateAuthor": {
                    "self": "https://team-111.atlassian.net/rest/api/2/user?accountId=123456",
                    "accountId": "123456",
                    "emailAddress": "test@example.com",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/2cfc976767db44422e9281fb012845a2?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FR-1.png",
                        "24x24": "https://secure.gravatar.com/avatar/2cfc976767db44422e9281fb012845a2?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FR-1.png",
                        "16x16": "https://secure.gravatar.com/avatar/2cfc976767db44422e9281fb012845a2?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FR-1.png",
                        "32x32": "https://secure.gravatar.com/avatar/2cfc976767db44422e9281fb012845a2?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FR-1.png"
                    },
                    "displayName": "test",
                    "active": True,
                    "timeZone": "America/New_York",
                    "accountType": "atlassian"
                    },
                    "created": "2023-01-31T09:52:58.464-0500",
                    "updated": "2023-01-31T09:52:58.464-0500",
                    "jsdPublic": True,
                    "jira_url": "<a href=\"https://team-111.atlassian.net/browse/JRA-45\">JRA-45</a>"
                }
            }

    return MockClient()
