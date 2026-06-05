# show app config information
import logging
import os
import resilient
import sys
from requests import Response

SESSION_URL = "/session"
APPS_URL = "/services_proxy/manager/tenants/{session_id}/apps"
APPS_FILE_URL = "/services_proxy/manager/app_files/{file_id}"
SECRETS_URL = "/services_proxy/manager/apps/{app_id}/secrets"

APP_SEPARATOR           = "========"
FILE_CONTENTS_SEPARATOR = "--------"

IGNORE_FILES = ["cert.cer"]

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.StreamHandler())
LOG.setLevel(logging.INFO)

class ShowAppConfig():
    """This script reads the installed apps in a SOAR organization and prints:
         - the contents of the files
         - the secrets defined (no values are possible to print)

       The goal is to capture settings used (ie from a Fyre instance) so they can be used in another instance

       Syntax: python3 show_app_config.py /path/to/app.config

       NOTE: Older versions of SOAR (ex. v46) require the use of email/password in app.config. 
             api_key_id nad api_key_secret will not work due to a permissions bug. 
             'Manage Apps' permission is required for api_key_id.

       Output Sample:
            ========
            app: fn_rest_api

            Secrets
            -------
            API_KEY_SECRET

            Files
            -----

            file: app.config
            path: /etc/rescircuits
            content:
            [fn_rest_api]

            #
            # Uncomment to add proxies
            # https_proxy = https://<your_proxy>:<port>
            # http_proxy = http://<your_proxy>:<port>
            #
            # Values can be assigned here in app.config and reference them in application
            # auth_header = sampleAPIToken123
            #
            # Alternatively, sensitive values can be stored as a SECRET in the Resilient platform
            # and assigned to a key as shown below.
            # auth_header = $SECRET_EXAMPLE
            #
            # This auth_header can later be accessed in the a playbook or a workflow as {{auth_header}}
            [resilient]
            api_key_id = 224df8ff-f1a7-4abf-891f-a66953ac0ff1
            api_key_secret = $API_KEY_SECRET
            cafile = /etc/rescircuits/cert.cer
            host = 9.30.1.151
            port = 443
            org = resilient

            --------
    """
    def __init__(self, path_to_app_config) -> None:
        self.rest_client: resilient.SimpleClient = self.get_rest_client(path_to_app_config)
        
    def check_auth(self) -> None:
        if self.rest_client.api_key_id:
            LOG.warning("'api_key_id' may not work with older versions of SOAR. Use 'email' and 'password' instead")

    def get_rest_client(self, path_to_app_config: str) -> resilient.SimpleClient:
        config_parser_opts = resilient.ArgumentParser(path_to_app_config).config

        return resilient.get_client(config_parser_opts._sections['resilient'])

    def run(self):
        session_id = self.get_session_id()

        if not session_id:
            error_and_exit("Session not found")

        apps_list: dict = self.get_apps(session_id)

        for apps in apps_list.get("apps", []):
            LOG.info(f"{APP_SEPARATOR}\napp: {apps['name']}")

            secrets_list: dict = self.get_secrets(apps["id"])

            LOG.info("\nSecrets\n-------")
            for secret in secrets_list["secrets"]:
                LOG.info(f"{secret['name']}")

            LOG.info("\nFiles\n-----")
            for file_id in apps.get("file_ids"):
                file_info: dict = self.get_file_info(file_id)

                if file_info["name"] not in IGNORE_FILES:
                    LOG.info(f"\nfile: {file_info['name']}\npath: {file_info['path']}")
                    LOG.info(f"content:\n{file_info['content']}\n{FILE_CONTENTS_SEPARATOR}")

    def get_file_info(self, file_id: str) -> dict:
        url = f"{self.rest_client.base_url}{APPS_FILE_URL.format(file_id=file_id)}"
        return self._execute(self.rest_client.session.get, url)

    
    def get_apps(self, session_id: str) -> dict:
        url = f"{self.rest_client.base_url}{APPS_URL.format(session_id=session_id)}"

        apps_list: dict = self._execute(self.rest_client.session.get, url)

        LOG.debug(apps_list)
        return apps_list
    
    def get_secrets(self, app_id: str) -> dict:
        url = f"{self.rest_client.base_url}{SECRETS_URL.format(app_id=app_id)}"

        secrets_list: dict = self._execute(self.rest_client.session.get, url)

        LOG.debug(secrets_list)
        return secrets_list

    def get_session_id(self) -> str:
        session_response: Response  = self.rest_client.get(SESSION_URL, is_uri_absolute=True)
        return session_response["orgs"][0]["uuid"] if session_response.get("orgs") else None

    def _execute(self, method, url: str) -> dict:
        response = self.rest_client._execute_request(method, 
                                                     url,
                                                     proxies=self.rest_client.proxies,
                                                     cookies=self.rest_client.cookies,
                                                     headers=self.rest_client.make_headers(additional_headers={ "X-ORG-ID": str(self.rest_client.org_id)}),
                                                     verify=self.rest_client.verify,
                                                     cert=self.rest_client.cert
                                                    )
        return response.json()

def error_and_exit(msg: str):
    print (msg)
    exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        error_and_exit ("Usage: python3 show_app_config.py /path/to/app.config")

    path_to_app_config = (os.path.abspath(sys.argv[1]))
    show_app_config = ShowAppConfig(path_to_app_config)
    show_app_config.run()
