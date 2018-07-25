# -*- coding: utf-8 -*-

import requests
import logging
from datetime import datetime

log = logging.getLogger(__name__)


class IBMCloudFoundryAPI:
    """
        Cloud Foundry Application utility
    """
    def __init__(self, api_key, bx_api_url, bx_apps_url, bx_app_details_url, authenticator):
        self.api_key = api_key
        self.bx_api_url = bx_api_url
        self.bx_apps_url = bx_apps_url
        self.bx_app_details_url = bx_app_details_url + "/{}"
        self.authenticator = authenticator

    def _add_authentication_headers(self, request):
        """
        Adds authentication headers to the request.
        Will overwrite headers with the same name already set.

        :param request: Dict
            A dict object that's going to be sent in a request
        :return: Dict
            Request object with authentication headers.
        """
        return request.update(self.authenticator.get_headers())

    def _get_bx_app_guid(self, app_name):
        oauth_authorization_headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "charset": "utf-8"
        }
        oauth_authorization_headers = self._add_authentication_headers(oauth_authorization_headers)

        response = requests.get(self.bx_apps_url, headers=oauth_authorization_headers)
        if response.status_code == 200:
            app_resources = response.json()["resources"]
            for resource in app_resources:
                res_app_name = resource["entity"]["name"]
                guid = resource["metadata"]["guid"]
                if app_name == res_app_name:
                    return guid
        else:
            print("Error while getting bluemix applications metadata")
        return None

    def _get_bx_apps_metadata(self):
        apps_metadata = []
        oauth_authorization_headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "charset": "utf-8"
        }
        oauth_authorization_headers = self._add_authentication_headers(oauth_authorization_headers)

        response = requests.get(self.bx_apps_url, headers=oauth_authorization_headers)
        if response.status_code == 200:
            app_resources = response.json()["resources"];
            for resource in app_resources:
                app_metadata = {}
                entity = resource["entity"]
                metadata = resource["metadata"]
                guid = metadata["guid"]
                app_name = entity["name"]
                app_metadata["guid"] = guid
                app_metadata["app_name"] = app_name
                app_metadata["space_guid"] = entity["space_guid"]
                app_metadata["production"] = entity["production"]
                app_metadata["current_state"] = entity["state"]
                app_metadata["memory"] = entity["memory"]
                app_metadata["disk_quota"] = entity["disk_quota"]
                app_metadata["enable_ssh"] = entity["enable_ssh"]
                app_metadata["last_updated"] = self.convert_timestamp_to_epoch_time(metadata["updated_at"]) * 1000

                oauth_authorization_headers = {
                    "accept": "application/json",
                    "charset": "utf-8"
                }
                oauth_authorization_headers = self._add_authentication_headers(oauth_authorization_headers)

                response = requests.get(self.get_bx_app_url(guid), headers=oauth_authorization_headers)
                if response.status_code == 200:
                    bx_app_metadata = response.json()
                    routes = bx_app_metadata["metadata"]["routes"]
                    for route in routes:
                        app_metadata["app_domain"] = route["name"]
                        app_metadata["app_port"] = route["port"]
                    log.debug(app_metadata)
                else:
                    log.error("Error while getting app details for app - {}".format(app_name))
                    log.debug(response)

                apps_metadata.append(app_metadata)

        else:
            log.error("Error while getting bluemix applications metadata")
            log.debug(response)

        return apps_metadata

    def _bx_invoke(self, app_name, action_name):
        app_guid = self._get_bx_app_guid(app_name)
        if app_guid is None:
            return None

        oauth_authorization_headers = {
            "accept": "application/json",
            "charset": "utf-8"
        }
        oauth_authorization_headers = self._add_authentication_headers(oauth_authorization_headers)

        app_status = {}
        response = requests.get(self.get_bx_app_url(app_guid, action_name), headers=oauth_authorization_headers)
        if response.status_code == 200:
            log.info("Done")
            ret = response.json()
            app_status["current_state"] = ret["state"]
            app_status["last_updated"] = self.convert_timestamp_to_epoch_time(ret["updated_at"]) * 1000
        else:
            app_status["current_state"] = "ERROR"
            app_status["last_updated"] = None
            log.error("Error while invoking bluemix application ({}) {} action ".format(app_name, action_name))
            log.debug(response)
        return app_status

    def _execute_cmd(self, application_name, action_name):
        if action_name == "metadata":
            return self._get_bx_apps_metadata()
        if action_name == "start" or action_name == "stop":
            return self._bx_invoke(application_name, action_name)

    def get_app_guid(self, application_name):
        pass

    def get_metadata(self):
        pass

    def application_metadata(self, application_name):
        pass

    def run(self, application_names, action_name):
        if application_names is not None:
            # to allow user path in both a string and a list of strings
            if not isinstance(application_names, list):
                application_names = list(application_names)

            for app_name in application_names:
                log.info("Invoking {} action for {} application".format(action_name, app_name.strip(" ")))
                ret_value = self._execute_cmd(app_name, action_name)
        else:
            ret_value = self._execute_cmd(application_names, action_name)

        results = {"value": ret_value}
        return results

    @staticmethod
    def convert_timestamp_to_epoch_time(ts, ts_format="%Y-%m-%dT%H:%M:%SZ"):
        utc_time = datetime.strptime(ts, ts_format)
        epoch_time = (utc_time - datetime(1970, 1, 1)).total_seconds()
        return epoch_time

class App():
    def __init__(self):
        pass

if __name__ == "__main__":
    api_key2 = "nlbp-C1HCzV-m9g2ZccvirA0VRUAewHoK9JevLOAH6M6"
    bx_apps_url2 = "http://api.ng.bluemix.net/v2/apps"
    bx_api_url2 = "http://api.ng.bluemix.net/info"
    bx_app_details_url2 = "https://console.bluemix.net/events/apps"
    application_names2 = "[Z2C-rbadvelu, Python-demo-log-app]"

    auth_url = "https://iam.bluemix.net/identity/token"

    from .authentication.ibm_cf_bearer import IBMCloudFoundryAuthenticator

    bx_service = IBMCloudFoundry(api_key2, bx_api_url2, bx_apps_url2, bx_app_details_url2,
                                 IBMCloudFoundryAuthenticator(bx_api_url2, api_key2))
    results = bx_service.run(application_names2, "start")
#     yitd_jXTSnP8J8xg4p4tSDdLVZEspbxASbSNOzbcTMA_  -- key
#     SFZu3mliDuJ_pNXPEc8B_BUqAuOmfjup94i_qkvCBYsO
# service key: YSzOLtdrtwaZ66YWR3YMaSJKId4u9Zpvoj9ig5K7BK2R

# final staging pTGbVhnA8TbZNMr2X6ENC6tl82QyidedsJWtYlWi5Tof
