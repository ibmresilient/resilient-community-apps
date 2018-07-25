import logging
import requests
from .authenticator_base import AuthenticatorBase

log = logging.getLogger(__name__)


class IBMCloudFoundryAuthenticator(AuthenticatorBase):
    """
    Authenticates into IBM's Cloud Foundry Platform
    """
    def __init__(self, url, api_key):
        self.base_url = url
        self.api_key = api_key
        self.get_token()

    def get_token(self):
        """
        Gets authentication token from the IBM CF's UAA server.
        """
        response = requests.get(self.base_url)
        if response.status_code == 200:
            # read authorization end point
            auth_url = response.json()["authorization_endpoint"]
            # prepare authorization token endpoint url
            oauth_token_url = "{}/{}".format(auth_url, "oauth/token")
            # request grant_type=password&username=apikey&password=myAPIkey
            oauth_key = {
                "grant_type": "password",
                "username": "apikey",
                "password": self.api_key
            }
            oauth_headers = {
                "content-type": "application/x-www-form-urlencoded",
                "charset": "utf-8",
                "accept": "application/json",
                "authorization": "Basic Y2Y6"
            }
            response = requests.post(oauth_token_url, headers=oauth_headers, data=oauth_key)

            if response.status_code == 200:
                self.oauth_token = response.json()
            else:
                log.error("Error getting authorization code: status code {}".format(response.status_code))
                log.debug(response)
                raise ValueError("Couldn't retrieve access token from Bluemix")
        else:
            log.error("Error connecting to bluemix api server")
            log.debug(response)
            raise ValueError("Bluemix CF server not responding")

    def get_headers(self):
        """
        Returns a dictionary of headers that need to be added to the request for it to be authenticated.
        For that it extracts the access token from the authentication token.
        :return: Dict
        """
        oauth_token = self.oauth_token
        return "{} {}".format(oauth_token["token_type"], oauth_token["access_token"])