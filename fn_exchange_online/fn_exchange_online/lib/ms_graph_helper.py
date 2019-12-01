
import logging
from resilient_circuits import FunctionError
from resilient_lib import OAuth2ClientCredentialsSession

log = logging.getLogger(__name__)

MS_GRAPH_TOKEN_URL = u'https://login.microsoftonline.com/{0}/oauth2/v2.0/token'

class MSGraphHelper:
    """
    Helper object MSGraphHelper.
    """
    def __init__(self, ms_graph_url, tenant_id, client_id, client_secret, proxies=None):
        self.__ms_graph_url = ms_graph_url
        self.__tenant_id = tenant_id
        self.__client_id = client_id,
        self.__client_secret = client_secret

        self.__proxies = proxies
        self.__ms_graph_session = self.authenticate()

    def authenticate(self):
        """
        Authenticate and get oauth2 token for the session.
        """
        token_url = MS_GRAPH_TOKEN_URL.format(self.__tenant_id)
        return OAuth2ClientCredentialsSession(token_url,
                                              client_id=self.__client_id,
                                              client_secret=self.__client_secret,
                                              scope=['.default'],
                                              proxies=self.__proxies)

    def get_user_profile(self, email_address):
        """
        Query MS Graph user profile endpoint using the MS graph session.
        :param email_address: email address of the user profile requested
        :return: requests response from the users/profile endpoint
        """
        ms_graph_user_profile_url = u'{0}/users/{1}'.format(self.__ms_graph_url, email_address)
        response = self.__ms_graph_session.get(ms_graph_user_profile_url)

        if response.status_code >= 300 and response.status_code != 404:
            raise FunctionError("Invalid response from Microsoft Graph")

        return response