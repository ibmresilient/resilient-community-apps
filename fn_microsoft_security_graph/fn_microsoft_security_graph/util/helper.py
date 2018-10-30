import requests


class MicrosoftGraphHelper:
    def __init__(self, tenant_id, client_id, client_secret):
        self.__tenant_id = tenant_id
        self.__client_id = client_id,
        self.__client_secret = client_secret
        self.__access_token = self.get_access_token()

    def __refresh_access_token(self):
        token_url = 'https://login.microsoftonline.com/{}/oauth2/v2.0/token'.format(self._tenant_id)
        post_data = {
            "client_id": self._client_id,
            "scope": ["https://graph.microsoft.com/.default"],
            "client_secret": self._client_secret,
            "grant_type": "client_credentials"
        }
        r = requests.post(token_url, data=post_data)
        self.check_status_code(r)
        r_json = r.json()

        return r_json.get("access_token")

    def check_status_code(self, response):
        if 200 <= response.status_code <= 299:
            return
        # Access token has expired, request a new one
        elif response.status_code == 401:
            r = self.get_access_token()
            self.check_status_code(r)
        else:
            raise ValueError("Invalid response from Microsoft Security Graph")

    def get_access_token(self):
        return self._access_token
