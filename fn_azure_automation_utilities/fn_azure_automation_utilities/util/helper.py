from logging import getLogger
from resilient_lib import IntegrationError
import time

PACKAGE_NAME = "fn_azure_automation_utilities"

LOG = getLogger(__name__)

# Classes for Exception Handling
class RunPlaybookRequestError(Exception):
    def __init__(self, *args, **kwargs):
        self.msg = args
        LOG.exception(self.msg)

class AzureRunJobFailed(Exception):
    def __init__(self, *args, **kwargs):
        self.msg = args
        LOG.exception(self.msg)

class AzureClient(object):
    """ Class for interacting with Azure Automation API """

    def __init__(self, rc, client_id: str, client_secret: str, tenant_id: str, subscription_id: str, scope: str,
                 proxies: dict, resource_group_name: str = None, automation_account_name: str = None,
                 refresh_token: str = None):
        """
        Constructor for Azure client
        :paran rc: RequestsCommon object
        :param client_id: Client id credential
        :type client_id: str
        :param: client_secret: Client secret key
        :type client_secret: str
        :param: tenant_id:
        :type tenant_id: str
        :param: subscription_id:
        :type subscription_id: str
        :param scope: Permissions the access token needs
        :type scope: str
        :param proxies:
        :type proxies: dict
        :param resource_group_name:
        :type resource_group_name: str | None
        :param automation_account_name:
        :type automation_account_name: str | None
        :ivar token: Token for request to Azure Automation
        :type token: None
        """
        self.rc = rc
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.subscription_id = subscription_id
        self.scope = scope
        self.resource_group_name = resource_group_name
        self.automation_account_name = automation_account_name
        self.proxies = proxies
        self.refresh_token = refresh_token
        self.token = self.get_token()
        self.header = {'Authorization': f'Bearer {self.token}'}
        self.base_url = f"https://management.azure.com/subscriptions/{self.subscription_id}/resourceGroups/{self.resource_group_name}/providers/Microsoft.Automation"

    def get_token(self):
        """
        Generate token for communication with Azure Automation
        :return token: validation token
        :rtype token: str
        :raises: :class: `AzureTokenRequestError`, :class: `HTTPError`
        """
        url = f'https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token'
        payload = {
            'client_id': self.client_id,
            "scope": self.scope,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token,
            'grant_type': 'refresh_token'
        }
        try:
            response = self.rc.execute("POST", url, data=payload)
            response.raise_for_status()
            if response.status_code == 200:
                response = response.json()
                self.token = response['access_token']
                return response['access_token']

        except Exception as err:
            raise IntegrationError(str(err))

    def create_update_automation_account(self, payload: dict):
        """
        Create or update an Azure automation account.
        :param payload: Payload to send to azure that contains automation account properties.
        :type payload: dict
        :return: Response from the PUT request to create/update Azure automation account.
        :return type: dict

        Example payload:
        {
            "name": "testAutomationAccount",
            "location": "eastus",
            "tags": {
                "client": "sentinel"
            },
            "properties": {
                "publicNetworkAccess": True,
                "disableLocalAuth": False,
                "sku": {
                    "name": "Basic",
                    "family": None,
                    "capacity": None
                }
            }
        }
        """
        url = f"{self.base_url}/automationAccounts/{self.automation_account_name}?api-version=2021-06-22"
        headers = self.header
        headers['Content-Type'] = 'application/json'

        try:
            return self.rc.execute("PUT", url, headers=headers, json=payload).json()
        except Exception as err:
            raise IntegrationError(str(err))

    def delete_automation_acount(self):
        """
        Delete an Azure automation account
        :return: Response from Delete request to delete an Azure automation account.
        :return type: request object
        """
        url = f"{self.base_url}/automationAccounts/{self.automation_account_name}?api-version=2021-06-22"
        try:
            return self.rc.execute("Delete", url, headers=self.header)
        except Exception as err:
            raise IntegrationError(str(err))

    def get_automation_account(self):
        """
        Get an Azure automation accounts information.
        :return: Response from GET request to get an Azure automation account
        :return type: dict
        """
        url = f"{self.base_url}/automationAccounts/{self.automation_account_name}?api-version=2021-06-22"
        headers = self.header
        headers['Content-Type'] = 'application/json'

        try:
            return self.rc.execute("GET", url, headers=headers).json()
        except Exception as err:
            raise IntegrationError(str(err))

    def list_automation_accounts(self):
        """
        Lists the Automation Accounts within an Azure subscription
        :return: Response from GET request to list Azure automation accounts
        :return type: dict
        """
        url = f"https://management.azure.com/subscriptions/{self.subscription_id}/providers/Microsoft.Automation/automationAccounts?api-version=2021-06-22"
        headers = self.header
        headers['Content-Type'] = 'application/json'

        try:
            return self.rc.execute("GET", url, headers=headers).json()
        except Exception as err:
            raise IntegrationError(str(err))

    def list_automation_accounts_by_resource_group(self):
        """
        Retrieve a list of accounts within a given resource group
        :return: Response from GET request to list Azure automation accounts
        :return type: dict
        """
        url = f"{self.base_url}/automationAccounts?api-version=2021-06-22"
        headers = self.header
        headers['Content-Type'] = 'application/json'

        try:
            return self.rc.execute("GET", url, headers=headers).json()
        except Exception as err:
            raise IntegrationError(str(err))

    def get_automation_module_activity(self, moduleName: str, activityName: str):
        """
        Retrieve the activity in the module identified by module name and activity name.
        :param moduleName: The name of module.
        :type moduleName: str
        :param activityName: The name of activity.
        :type activityName: str
        :return: Response from GET request to Azure
        :return type: dict
        """
        url = f"{self.base_url}/automationAccounts/{self.automation_account_name}/modules/{moduleName}/activities/{activityName}?api-version=2019-06-01"
        headers = self.header
        headers['Content-Type'] = 'application/json'

        try:
            return self.rc.execute("GET", url, headers=headers).json()
        except Exception as err:
            raise IntegrationError(str(err))

    def list_automation_module_activities(self, moduleName: str):
        """
        Retrieve a list of activities in the module identified by module name.
        :param moduleName: The name of module.
        :type moduleName: str
        :return: Response from GET request to Azure
        :return type: dict
        """
        url = f"{self.base_url}/automationAccounts/{self.automation_account_name}/modules/{moduleName}/activities?api-version=2019-06-01"
        headers = self.header
        headers['Content-Type'] = 'application/json'

        try:
            return self.rc.execute("GET", url, headers=headers).json()
        except Exception as err:
            raise IntegrationError(str(err))
