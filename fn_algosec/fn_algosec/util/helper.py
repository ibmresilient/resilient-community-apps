# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Helper code for AlgoSec

from resilient_lib import validate_fields, IntegrationError
from json import dumps

PACKAGE_NAME = "fn_algosec"
verify = None
proxies = None
on_prem_base_url = None
saas_base_url = None
header = None

class algosec_client(object):
    def __init__(self, options, rc):
        # Validate required configs
        validate_fields(["server_ip", "username", "password"], options)

        global verify
        global proxies
        global on_prem_base_url
        global saas_base_url
        global header

        # On-Prem configs
        server_ip = options.get("server_ip")
        self.username = options.get("username")
        self.password = options.get("password")
        # Set on_prem_base_url. Check if https:// was given in config server_ip and if not add it
        on_prem_base_url = f"https://{server_ip}" if not server_ip.startswith("https://") else server_ip
        # Check if config setting server_ip ends in a / and if it does remove it
        on_prem_base_url = on_prem_base_url if not on_prem_base_url.endswith("/") else on_prem_base_url[:len(on_prem_base_url)-1]

        # SaaS configs
        saas_base_url = options.get("saas_base_url", "https://app.algosec.com")
        self.tenantId = options.get("tenantid")
        self.clientId = options.get("clientid")
        self.clientSecret = options.get("clientsecret")

        verify = rc.get_verify()
        proxies = rc.get_proxies()
        self.rc = rc  # RequestCommon
        header = {"Accept": "application/json", "Content-Type": "application/json"}

    def appViz_auth(self) -> str:
        # Create connection to AlgoSec Business Flow (AppViz)
        res = self.rc.execute(
            "POST",
            f"{saas_base_url}/api/algosaas/auth/v1/access-keys/login",
            data=dumps({"tenantId": self.tenantId, "clientId": self.clientId, "clientSecret": self.clientSecret}),
            headers=header,
            verify=verify,
            proxies=proxies,
        ).json()
        return str(res.get("access_token"))

    def fire_flow_auth(self) -> str:
        # Create connect to AlgoSec FireFlow
        res = self.rc.execute(
            "POST",
            f"{on_prem_base_url}/FireFlow/api/authentication/authenticate",
            data=dumps({"username": self.username, "password": self.password}),
            headers=header,
            verify=verify,
            proxies=proxies,
        ).json()
        sessionID, faSessionID, phpSessionID = "", "", ""
        data = res.get("data", {})
        # Check if authentication was successful
        if res.get("status") and data:
            sessionID = data.get("sessionId")
            faSessionID = data.get("faSessionId")
            phpSessionID = data.get("phpSessionId")
        else:  # If not successful raise the returned error message
            raise IntegrationError(res.get("message"))

        return sessionID, faSessionID, phpSessionID

    def firewall_analyzer_auth(self) -> str:
        """Create connect to AlgoSec Firewall Analyzer (AFA).

        Raises:
            IntegrationError: If authentication is not successful raise returned error message.
        """
        res = self.rc.execute(
            "POST",
            f"{on_prem_base_url}/fa/server/connection/login",
            data=dumps({"username": self.username, "password": self.password}),
            headers=header,
            verify=verify,
            proxies=proxies,
        ).json()

        sessionID = ""
        # Check if authentication was successful
        if res.get("status"):
            sessionID = res.get("SessionID")
        else:  # If not successful raise the returned error message
            raise IntegrationError(res.get("message"))

        return sessionID

def string_to_list(string_list: str) -> list:
    """Convert string of comma separated values or just a normal string into a list.
    Args:
        string_list (str): String of comma separated values or just a normal string
    Returns:
        list: The string converted into a list.
    """
    return [string.strip() for string in string_list.split(",")] if "," in string_list else [string_list]

class firewall_analyzer:
    def __init__(self, rc, sessionID):
        self.rc = rc
        self.sessionID = sessionID

    def traffic_simulation_query(self, source: str, destination: str = "8.8.8.8", service: str = "any",
        target: str = "ALL_FIREWALLS", application: str = "any", user: str = "any", includeruleszones: bool = False,
        includedevicespaths: bool = False) -> dict:
        """Run a traffic simulation query on AlgoSec

        Args:
            source (str): Source(s) for the query. Multiple values are separated by commas (,).
            destination (str): Destination(s) for the query. Multiple values are separated by commas (,). Defaults to "8.8.8.8".
            service (str): Service(s) for the query. Multiple values are separated by commas (,). Defaults to "*".
            target (str, optional): Name of a device or group the query will run on. If empty, the query runs on the entire network and all permitted devices for the user.
            application (str, optional): Application(s) for the rule. Multiple values are separated by commas (,). If empty, the query runs on application: 'any'
            user (str, optional): User(s) who created the rule. Multiple values are separated by commas (,). If empty, the query runs on user: 'any'
            includeruleszones (bool, optional): True - Includes source/destination zones of rule of zone-based devices in response (sourceZone, destinationZone) .  Defaults to False.
            includedevicespaths (bool, optional): True - Includes devices paths section in response (devicesInPath). Defaults to False.
        """
        params = {
            "queryInput": [
                {
                    "application": string_to_list(application),
                    "user": string_to_list(user),
                    "destination": string_to_list(destination),
                    "service": string_to_list(service),
                    "source": string_to_list(source),
                }
            ],
            "queryTarget": target,
            "includeDevicesPaths": includedevicespaths,
            "includeRulesZones": includeruleszones,
        }

        return self.rc.execute(
            "POST",
            f"{on_prem_base_url}/afa/api/v1/query",
            cookies={"PHPSESSID": self.sessionID},
            data=dumps(params),
            headers=header,
            verify=verify,
            proxies=proxies,
        ).json()

class fireflow:
    def __init__(self, rc, sessionID: str=None, faSessionID: str=None, phpSessionID: str=None) -> None:
        self.rc = rc
        self.sessionID = sessionID
        self.faSessionID = faSessionID
        self.phpSessionID = phpSessionID

    def traffic_change_request(self, source: str="any", destination: str="any", service: str="any",
                               user: str="", application: str="any", action: str="Drop",
                               template: str="Basic Change Traffic Request", description: str="", subject: str="", devices: str="") -> dict:
        """Create a traffic change request on the AlgoSec server

        Args:
            source (str): Source(s). Comma separated list of sources. Defaults to "any".
            destination (str): Destination(s). Comma separated list of destinations. Defaults to "any".
            service (str): Service(s). Comma separated list if services. Defaults to "any".
            user (str, optional): User. Defaults to "any".
            application (str, optional): Application(s). Comma separated list of applications. Defaults to "any".
            action (str): Either Allow or Drop. Defaults to "Drop".
            template (str, optional): Name of the template to use. Defaults to "".
            description (str, optional): Description of the traffic change request. Defaults to "".
            subject (str, optional): Subject for the traffic change request. Defaults to "".
            devices (str, optional): Device(s). Comma separated list of devices. Defaults to "".

        Returns:
            dict: Response returned from AlgoSec from making the traffic change request.
        """
        params = {
            "template": template,
            "fields": [
                {"key": "subject", "values": [subject]},
                {"key": "Change Request Description", "values": [description]}
            ],
            "traffic": [
                {
                    "source": {"items": [{"name": sor} for sor in string_to_list(source)]},
                    "destination": {"items": [{"name": des} for des in string_to_list(destination)]},
                    "service": {"items": [{"name": ser} for ser in string_to_list(service)]},
                    "action": action
                }
            ]
        }

        if user:
            params["traffic"][0]["user"] = {"items": [{"name": usr} for usr in string_to_list(user)]}
        if application:
            params["traffic"][0]["application"] = {"items": [{"name": ap} for ap in string_to_list(application)]}
        if devices:
            params["fields"].append({"name": "devices", "values": string_to_list(devices)})

        return self.rc.execute("POST",
            f"{on_prem_base_url}/FireFlow/api/change-requests/traffic",
            cookies={"FireFlow_Session": self.sessionID},
            data=dumps(params),
            headers=header,
            verify=verify,
            proxies=proxies,
        ).json()

    def traffic_change_request_details(self, request_id: int) -> dict:
        """Get the details of a given traffic change request

        Args:
            request_id (int): The traffic change request ID
        """
        return self.rc.execute("GET",
                               f"{on_prem_base_url}/FireFlow/api/change-requests/traffic/{request_id}",
                               cookies={"FireFlow_Session": self.sessionID},
                               headers=header,
                               verify=verify,
                               proxies=proxies).json()
