# -*- coding: utf-8 -*-

import requests
import logging
from datetime import datetime

log = logging.getLogger(__name__)


class IBMBluemixConnectService:
    """
        IBM Bluemix Cloud Foundry Application utility
    """
    def __init__(self, api_key, bx_api_url, bx_apps_url, bx_app_details_url):
            self.api_key = api_key
            self.bx_api_url = bx_api_url
            self.bx_apps_url = bx_apps_url
            self.bx_app_details_url = bx_app_details_url + "/{}"

    def _get_bx_oauth_token(self):
        response = requests.get(self.bx_api_url)
        if response.status_code == 200:
            # read authorization end point
            auth_url = response.json()["authorization_endpoint"]
            # prepare authorization token endpoint url
            oauth_token_url = "{}/{}".format(auth_url, "oauth/token")
            # request grant_type=password&username=apikey&password=myAPIkey
            oauth_key = {
                "grant_type": "password",
                "username":"apikey",
                "password": self.api_key
            }
            oauth_headers = {
                "content-type":"application/x-www-form-urlencoded",
                "charset":"utf-8",
                "accept":"application/json",
                "authorization": "Basic Y2Y6"
            }

            response = requests.post(oauth_token_url, headers=oauth_headers, data=oauth_key)

            if response.status_code == 200:
                oauth_token = response.json()
                return oauth_token
            else:
                log.error("Error getting authorization code: status code {}".format(response.status_code))
                log.debug(response)
        else:
            log.error("Error connecting to bluemix api server")
            log.debug(response)

    def _get_bx_oauth_authorization_header(self):
        oauth_token = self._get_bx_oauth_token()
        return "{} {}".format(oauth_token["token_type"], oauth_token["access_token"])

    def get_bx_app_url(self, guid, action=None):
        if action is None:
            return self.bx_app_details_url.format(guid)
        if action == "start":
            return self.bx_app_details_url.format(guid) + "/start"
        if action == "stop":
            return self.bx_app_details_url.format(guid) + "/stop"

    def _get_bx_app_guid(self, authorization, app_name):
        oauth_authorization_headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "charset": "utf-8",
            "authorization": authorization
        }

        response = requests.get(self.bx_apps_url, headers=oauth_authorization_headers)
        if response.status_code == 200:
            app_resources = response.json()["resources"];
            for resource in app_resources:
                res_app_name = resource["entity"]["name"]
                guid = resource["metadata"]["guid"]
                if app_name == res_app_name:
                    return guid
        else:
            print "Error while getting bluemix applications metadata"
        return None

    def _get_bx_apps_metadata(self):
        authorization = self._get_bx_oauth_authorization_header()
        apps_metadata = []
        oauth_authorization_headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "charset": "utf-8",
            "authorization": authorization
        }

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
                    "charset": "utf-8",
                    "authorization": authorization
                }
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
        authorization = self._get_bx_oauth_authorization_header()
        app_guid = self._get_bx_app_guid(authorization, app_name)
        if app_guid is None:
            return None

        oauth_authorization_headers = {
            "accept": "application/json",
            "charset": "utf-8",
            "authorization": authorization
        }
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

    @staticmethod
    def convert_timestamp_to_epoch_time(ts, ts_format="%Y-%m-%dT%H:%M:%SZ"):
            utc_time = datetime.strptime(ts, ts_format)
            epoch_time = (utc_time - datetime(1970, 1, 1)).total_seconds()
            return long(epoch_time)

    def _execute_cmd(self, application_name, action_name):
        if action_name == "metadata":
            return self._get_bx_apps_metadata()
        if action_name == "start" or action_name == "stop":
            return self._bx_invoke(application_name, action_name)

    def run(self, application_names, action_name):

        if application_names is not None:
            app_names_str = str(application_names).lstrip("[").rstrip("]")
            app_names = list(app_names_str.split(","))
            for app_name in app_names:
                log.info("Invoking {} action for {} application".format(action_name, app_name.strip(" ")))
                ret_value = self._execute_cmd(app_name.strip(" "), action_name)
        else:
            ret_value = self._execute_cmd(application_names, action_name)

        results = {"value": ret_value}
        return results


if __name__ == "__main__":

    api_key2 = "nlbp-C1HCzV-m9g2ZccvirA0VRUAewHoK9JevLOAH6M6"
    bx_apps_url2 = "http://api.ng.bluemix.net/v2/apps"
    bx_api_url2 = "http://api.ng.bluemix.net/info"
    bx_app_details_url2 = "https://console.bluemix.net/events/apps"
    application_names2 = "[Z2C-rbadvelu, Python-demo-log-app]"
    bx_service = IBMBluemixConnectService(api_key2, bx_api_url2, bx_apps_url2, bx_app_details_url2)
    results = bx_service.run(application_names2, "start")
    print results

