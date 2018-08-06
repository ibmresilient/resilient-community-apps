# -*- coding: utf-8 -*-

import requests
import logging
from datetime import datetime

log = logging.getLogger(__name__)


class IBMCloudFoundryAPI:
    """
        Cloud Foundry Application utility
    """
    # class variables of the API end points
    CF_API_BASE     = "v2/apps"
    CF_APP_INFO     = "/{}/summary"
    CF_ALL_APPS     = ""
    CF_APP          = "/{}"
    CF_APP_RESTAGE  = "/{}/restage"
    CF_APP_INSTANCES= "/{}/instances"
    CF_DEL_INSTANCE = "/{}/instances/{}"

    APP_ACTIONS     = ["start", "stop", "restage", "delete", "update", "instances", "info", "recreate"]
    INSTANCE_ACTIONS= ["delete"]

    def __init__(self, base_url, authenticator):
        if base_url[-1] != "/":
            base_url += "/"
        self.base_url = base_url + self.CF_API_BASE
        self.authenticator = authenticator
        self.app_commands = {
            "start":        self.start_app,
            "stop":         self.stop_app,
            "restage":      self.restage_app,
            "delete":       self.delete_app,
            "update":       self.update_app,
            "instances":    self.get_app_instances,
            "info":         self.get_app_info,
            "recreate":     self.recreate_app
        }
        self.instance_commands = {
            "delete":       self.delete_app_instance
        }

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

    def get_app_guids(self, application_names):
        """
        Gets the guids for the list of application names provided
        :param application_names: list
             List of names that guid need to be found for
        :return: Dict - key: application name, value: guid
        """
        oauth_authorization_headers = {
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded",
            "charset": "utf-8"
        }
        self._add_authentication_headers(oauth_authorization_headers)

        result = {}

        response = requests.get(self.base_url+self.CF_ALL_APPS, headers=oauth_authorization_headers)
        if response.status_code == 200:
            app_resources = response.json()["resources"]
            for resource in app_resources:
                res_app_name = resource["entity"]["name"]
                guid = resource["metadata"]["guid"]
                if res_app_name in application_names:
                    result[res_app_name] = guid
                    # if all the apps have been identified, no need to keep looping
                    if len(result.keys()) == len(application_names):
                        break
        else:
            raise ValueError("Error while getting CF applications metadata")
        return result

    def get_app_guid(self, app_name):
        """
        Get guid for a single app.
        :param app_name: name of the applicaiton to get guid for
        :return: String - guid for the application
        """
        return self.get_app_guids([app_name])[app_name]

    def get_app_info(self, guid):
        """
        Extract JSON information for the application with given guid.
        :param guid: String
            GUID for the app to extract information for
        :return:
        """
        oauth_authorization_headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "charset": "utf-8"
        }
        self._add_authentication_headers(oauth_authorization_headers)

        response = requests.get(self.base_url + self.CF_APP_INFO.format(guid), headers=oauth_authorization_headers)
        if response.status_code == 200:
            apps_data = response.json()
        else:
            log.error("Error while getting CF application information.")
            log.debug(response)
            apps_data = {"status": response.status_code}

        return apps_data

    def update_app(self, app_guid, values=None):
        """
        PUT request with a body of values that need to be updated.
        :param app_guid: GUID of the app to be updated
        :param values: The fields to be updated
        :return: New information about the app
        """
        oauth_authorization_headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "charset": "utf-8"
        }
        self._add_authentication_headers(oauth_authorization_headers)

        app_status = {}
        response = requests.put(self.base_url + self.CF_APP.format(app_guid), headers=oauth_authorization_headers,
                                json=values)

        if response.status_code == 201: # return status code for update
            log.info("Successful update.")
            ret = response.json()
            app_status["success"] = True
            app_status["current_state"] = ret["entity"]["state"]
            app_status["last_updated"] = self.convert_timestamp_to_epoch_time(ret["metadata"]["updated_at"]) * 1000
        else:
            app_status["success"] = False
            app_status["current_state"] = "ERROR"
            app_status["last_updated"] = None
            log.error("Error while invoking cf application {} action ".format(values))
            log.debug(response)
        return app_status

    def start_app(self, guid):
        """
        Shortcut to start an app, using update.
        """
        return self.update_app(guid, values={"state": "STARTED"})

    def stop_app(self, guid):
        """
        Shortcut for stop an app, using update.
        """
        return self.update_app(guid, values={"state": "STOPPED"})

    def restage_app(self, guid):
        """
        Restages an app.
        :param guid: String
           GUID of the app to restage.
        :return: Information about the app.
        """
        oauth_authorization_headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "charset": "utf-8"
        }
        self._add_authentication_headers(oauth_authorization_headers)

        app_status = {}
        response = requests.post(self.base_url + self.CF_APP_RESTAGE.format(guid), headers=oauth_authorization_headers)
        if response.status_code == 201:  # return status code for update
            log.info("Successful restage of {}".format(guid))
            app_status = response.json()
            app_status["success"] = True
        else:
            app_status["success"] = False
            app_status["details"] = "Couldn't restage."
            app_status["last_updated"] = None
            log.error("Error while restaging cf application {}.".format(guid))
            log.debug(response)
        return app_status

    def delete_app(self, guid):
        """
        Deletes an app.
        :param guid: String
            GUID of the app to delete.
        :return: Information about the app.
        """
        oauth_authorization_headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "charset": "utf-8"
        }
        self._add_authentication_headers(oauth_authorization_headers)

        app_status = {}
        response = requests.delete(self.base_url + self.CF_APP.format(guid), headers=oauth_authorization_headers)
        if response.status_code == 204:  # return status code for update
            log.info("Successful deletion of {}".format(guid))
            app_status["success"] = True
        else:
            app_status["success"] = False
            app_status["details"] = "Couldn't delete."
            app_status["last_updated"] = None
            log.error("Error while deleting cf application {}.".format(guid))
            log.debug(response)
        return app_status

    def create_app(self, values=None):
        """
        Creating an app with the provided values.
        :param values: Values to be passed to the REST call.
        :return:
        """
        oauth_authorization_headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "charset": "utf-8"
        }
        self._add_authentication_headers(oauth_authorization_headers)

        app_status = {}
        response = requests.post(self.base_url + self.CF_ALL_APPS, headers=oauth_authorization_headers,
                                 json=values)
        if response.status_code == 201:  # return status code for update
            log.info("Successful creation ")
            app_status = response.json()
            app_status["success"] = True
        else:
            app_status["success"] = False
            app_status["details"] = "Couldn't create."
            app_status["last_updated"] = None
            log.error("Error while creating cf application {}.")
            log.debug(response)
        return app_status

    def recreate_app(self):
        pass

    def run_application_command(self, application_names, action_name, *args, **kwargs):
        results = {}
        if not isinstance(application_names, list):
            application_names = [application_names]
        if action_name in self.APP_ACTIONS:
            guids = self.get_app_guids(application_names)
            log.info(guids)
            for app in application_names:
                if app in guids:
                    results[app] = self.app_commands[action_name](guids[app], *args, **kwargs)
                else:
                    message = "App {} wasn't found.".format(app)
                    log.info(message)
                    results[app] = {
                        "details": message,
                        "success": False
                    }
        return results

    def run_application_instance_command(self, app_name, instances, action_name, *args, **kwargs):
        results = {}
        if not isinstance(instances, list):
            instances = [instances]
        if action_name in self.INSTANCE_ACTIONS:
            guid = self.get_app_guid(app_name)
            log.info(guid)
            if guid:
                results[app_name] = {}
                for instance in instances:
                    results[app_name][instance] = self.instance_commands[action_name](guid, instances, *args, **kwargs)
            else:
                message = "App {} wasn't found.".format(app_name)
                log.info(message)
                results[app_name] = {
                    "details": message,
                    "success": False
                }
        return results

    def get_app_instances(self, guid):
        """
        Gets instances' information for the app.
        :param guid: String
           Application to get the instances data for.
        :return: Information about all the app instances.
        """
        oauth_authorization_headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "charset": "utf-8"
        }
        self._add_authentication_headers(oauth_authorization_headers)

        app_status = {}
        response = requests.get(self.base_url + self.CF_APP_INSTANCES.format(guid), headers=oauth_authorization_headers)
        if response.status_code == 200:  # return status code for update
            log.info("Got instance information for {}".format(guid))
            app_status = response.json()
            app_status["success"] = True
        else:
            app_status["success"] = False
            app_status["details"] = "Couldn't get instances for {}.".format(guid)
            app_status["last_updated"] = None
            log.error("Error getting instance information for {}.".format(guid))
            log.debug(response)
        return app_status

    def delete_app_instance(self, guid, instance):
        """
        Deletes an app instance.
        :param guid: String
            GUID of the app whose instance needs to be deleted
        :param instance: String
            Instance id to be deleted
        :return: Success or not
        """
        oauth_authorization_headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "charset": "utf-8"
        }
        self._add_authentication_headers(oauth_authorization_headers)
        app_status = {}
        response = requests.delete(self.base_url + self.CF_DEL_INSTANCE.format(guid, instance),
                                   headers=oauth_authorization_headers)
        if response.status_code == 204:  # return status code for update
            log.info("Successful deletion of {} instance {}".format(guid, instance))
            app_status["success"] = True
        else:
            app_status["success"] = False
            app_status["details"] = "Couldn't delete instance {}.".format(instance)
            app_status["last_updated"] = None
            log.error("Error while deleting cf application {} instance {}.".format(guid, instance))
            log.debug(response)
        return app_status

    @staticmethod
    def convert_timestamp_to_epoch_time(ts, ts_format="%Y-%m-%dT%H:%M:%SZ"):
        utc_time = datetime.strptime(ts, ts_format)
        epoch_time = (utc_time - datetime(1970, 1, 1)).total_seconds()
        return epoch_time

