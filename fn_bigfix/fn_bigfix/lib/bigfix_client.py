# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
""" Helper module containing REST API client for BigFix  """

from json import loads
from time import sleep
from ntpath import split
from textwrap import dedent
from logging import getLogger
from resilient_lib import RequestsCommon
import xml.etree.ElementTree as elementTree

LOG = getLogger(__name__)

class BigFixClient(object):
    """Client class used to expose BigFix Rest API for BigFix Query"""

    def __init__(self, opts, options):
        """Class constructor"""
        self.rc = RequestsCommon(opts, options)
        self.base_url = f"{options.get('bigfix_url')}:{options.get('bigfix_port')}"
        self.bf_user = options.get("bigfix_user")
        self.bf_pass = options.get("bigfix_pass")
        self.headers = {'content-type': 'application/json'}
        self.verify = options.get("bigfix_verify", False)
        self.retry_interval = int(options.get("bigfix_polling_interval"))
        self.retry_timeout = int(options.get("bigfix_polling_timeout"))
        if options.get("bigfix_endpoints_wait"):
            self.endpoints_wait = int(options.get("bigfix_endpoints_wait"))
        # Endpoints
        self.client_query_endpoint = '/api/clientquery'
        self.client_query_results_endpoint = '/api/clientqueryresults/'
        self.client_query_names_computers = '/api/query?relevance=names+of+bes+computers'
        self.computers_endpoint = '/api/computers'
        self.computer_endpoint = '/api/computer/{id}'

    def test_connectivity(self):
        """Connectivity Test which is used by resilient_circuits selftest.
        Calls http 'get' request against 'api/computers' endpoint.
        :return: Response
        """
        return self.rc.execute("get", f"{self.base_url}{self.computers_endpoint}", auth=(self.bf_user, self.bf_pass), verify=self.verify)

    def get_bf_computer_properties(self, computer_id):
        """ Bigfix query - Get endpoint properties.
        :param computer_id: BigFix Endpoint id
        :return : Return response in XML format
        """
        query_str = f'api/query?relevance=if(number of property results of bes computers whose (id of it = {computer_id}) < 10000) '\
            'then((name of source analysis of property of it|"Retrieved Property",name of property of it,values of it) of '\
            f'property results of bes computers whose(id of it = {computer_id})) else error "Too Many Results"'

        response = self.rc.execute("get", f"{self.base_url}/{query_str}", auth=(self.bf_user, self.bf_pass), verify=self.verify)
        if response.status_code == 200:
            try:
                qr_to_attachment = self._process_bf_computer_query_response_to_attachment(response,
                                                                                          f"Computer ID {computer_id} Properties",
                                                                                          3)
                if not qr_to_attachment:
                    LOG.info(f"No properties returned for computer_id: {computer_id}")

                return qr_to_attachment

            except Exception as e:
                LOG.exception(f"XML processing, Got exception type: {e.__repr__()}, msg: {e.message}")
                raise e
        else:
            LOG.exception(f"Unexpected HTTP status code: {response.status_code}")

    def get_bf_computer_by_service_name(self, service_name):
        """ Bigfix query - Get endpoints by service name.
        :param service_name: Service name
        :return resp: Response from query
        """
        LOG.debug("get_bf_computer_by_service_name triggered")

        q_id = self.post_bfclientquery(
            "if (windows of operating system) then (disjunction of (exists matches(case insensitive "\
            f"regex(\"%22{service_name}%22.*%22running%22\")) of it ) of (services as string as lowercase)) else (false)")
        return self.get_bfclientquery(q_id, self.retry_interval, self.retry_timeout)

    def get_bf_computer_by_process_name(self, process_name):
        """ Bigfix query - Get endpoints by process name.
        :param process_name: Process name
        :return resp: Response from query
        """
        LOG.debug("get_bf_computer_by_process_name triggered")

        q_id = self.post_bfclientquery(
            f"if (windows of operating system) then (exists process whose(name of it as lowercase = \"{process_name}\" as lowercase)) "\
            f"else if (name of it contains \"Linux\") of operating system then (exists process whose(name of it = \"{process_name}\")) else (false)")
        return self.get_bfclientquery(q_id, self.retry_interval, self.retry_timeout)

    def get_bf_computer_by_file_path(self, file_path):
        """ Bigfix query - Get endpoints by file path.
        :param file_path: File path
        :return resp: Response from query
        """
        LOG.debug("get_bf_computer_by_file_path triggered")

        head, tail = split(file_path)
        q_id = self.post_bfclientquery(f'exists file \"{tail}\" of folder \"{head}\"' if tail else f'exists file \"{head}\"')
        return self.get_bfclientquery(q_id, self.retry_interval, self.retry_timeout)

    def get_bf_computer_by_ip(self, ip):
        """ Bigfix query - Get endpoints by ip address.
        :param ip: ip address
        :return resp: Response from query
        """
        LOG.debug("get_bf_computer_by_ip triggered")
        q_id = self.post_bfclientquery(
            f"exists remote addresses whose(it=\"{ip}\") of sockets whose(established of tcp state of it) of network")
        return self.get_bfclientquery(q_id, self.retry_interval, self.retry_timeout)

    def get_bf_computer_by_registry_key_name_value(self, key, name, value):
        """ Bigfix query - Get endpoints by registry entry (MS Windows).
        :param key: Registry key
        :param name: Value name
        :param value: Value data
        :return resp: Response from query
        """
        # strip off the prefix if it exists for current user
        key = key.split('\\', 1)[1]
        namevaluekey = "exists values \"{}\" whose (it=\"{}\") of keys \"{}\" of keys whose (exists "\
            "matches(regex(\"S-\d+-\d+-\d+(-\d+-\d+\-\d+\-\d+)*$\")) of (it as string) ) of keys \"HKU\" of "\
            "(if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"
        namekey = "exists values \"{}\" of keys \"{}\" of keys whose (exists matches(regex(\"S-\d+-\d+-\d+(-\d+-\d+\-\d+\-\d+)*$\")) "\
            "of (it as string) ) of keys \"HKU\" of (if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"
        keyonly = "exists keys \"{}\" of keys whose (exists matches(regex(\"S-\d+-\d+-\d+(-\d+-\d+\-\d+\-\d+)*$\")) of (it as string) ) "\
            "of keys \"HKU\" of (if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"

        if not key.lower().startswith(("hkcu", "hkey_current_user")):
            namevaluekey = f"{namevaluekey[:47]}{namevaluekey[157:]}"
            namekey = f"{namekey[:34]}{namekey[144:]}"
            keyonly = f"{keyonly[:19]}{keyonly[129:]}"

        LOG.debug("get_bf_computer_by_registry_key_name_value triggered")

        if name and value:
            q_id = self.post_bfclientquery(namevaluekey.format(name, value, key))
        elif name:
            q_id = self.post_bfclientquery(namekey.format(name, key))
        else:
            q_id = self.post_bfclientquery(keyonly.format(key))

        return self.get_bfclientquery(q_id, self.retry_interval, self.retry_timeout)

    def check_exists_subkey(self, artifact_value, computer_id):
        """ Bigfix query - Determine if a registry key has subkeys.
        :param artifact_value: Name of artifact to query
        :param computer_id: BigFix Endpoint id
        :return resp: Response from action
        """
        subkey = "exists key of keys \"{}\" of keys whose (exists matches(regex(\"S-\d+-\d+-\d+(-\d+-\d+\-\d+\-\d+)*$\")) "\
                 "of (it as string) ) of keys \"HKU\" of (if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"

        # strip off the prefix if it exists for current user
        if artifact_value.lower().startswith(("hkcu", "hkey_current_user")):
            (hive, artifact_value) = artifact_value.split('\\', 1)
        else:
            subkey = f"{subkey[:26]}{subkey[137:]}"

        LOG.debug("check exists subkey triggered")

        return self.get_bfclientquery(self.post_bfclientquery(subkey.format(artifact_value), computer_id), self.retry_interval, self.retry_timeout)

    def check_is_folder(self, artifact_value, computer_id):
        """ Bigfix query - Determine if artifact value is a folder.
        :param artifact_value: Name of artifact to query
        :return resp: Response from action
        """
        LOG.debug("check is folder triggered")
        return self.get_bfclientquery(self.post_bfclientquery(f"exists folder \"{artifact_value}\""), self.retry_interval, self.retry_timeout)

    def send_delete_file_remediation_message(self, artifact_value, computer_id):
        """ Bigfix action - Delete file remediate action.
        :param artifact_value: Name of artifact to remediate
        :param computer_id: BigFix Endpoint id
        :return resp: Response from action
        """
        return self._post_bf_action_query(f"delete \"{artifact_value}\"", computer_id,
            f"Delete File '{artifact_value}'", f"exists file \"{artifact_value}\"")

    def send_kill_process_remediation_message(self, artifact_value, computer_id):
        """ Bigfix action - Kill process remediate action.
        :param artifact_value: Name of artifact to remediate
        :param computer_id: BigFix Endpoint id
        :return resp: Response from action
        """
        query = f"if {{windows of operating system}} \n waithidden cmd.exe /c taskkill /im {artifact_value} /f /t \nelse \n wait kill -9 "\
            f"{{concatenation \" \" of (ids of processes whose (name of it = \"{artifact_value}\") as string)}}\n endif"
        relevance = f"if (windows of operating system) then (exists process whose(name of it as lowercase = \"{artifact_value}\" as lowercase)) "\
            f"else if (name of it contains \"Linux\") of operating system then (exists process whose(name of it = \"{artifact_value}\")) else (false)"
        return self._post_bf_action_query(query, computer_id, f"Kill Process '{artifact_value}'", relevance)

    def send_stop_service_remediation_message(self, artifact_value, computer_id):
        """ Bigfix action - Stop service remediate action.
        :param artifact_value: Name of artifact to remediate
        :param computer_id: BigFix Endpoint id
        :return resp: Response from action
        """
        query = f"if {{windows of operating system}} \n waithidden cmd.exe /c net stop \"{artifact_value}\" \nelse\n wait stop service {artifact_value} \nendif"
        relevance = f"if (windows of operating system) then (disjunction of (exists matches(case insensitive regex(\"%22{artifact_value}%22.*%22running%22\")) "\
            "of it ) of (services as string as lowercase)) else (false)"
        return self._post_bf_action_query(query, computer_id, f"Stop service '{artifact_value}'", relevance)

    def send_delete_registry_key_remediation_message(self, artifact_value, computer_id):
        """ Bigfix action - Delete registry entry (MS Windows).
        :param artifact_value: Name of artifact to remediate
        :param computer_id: BigFix Endpoint id
        :return resp: Response from action
        """
        key_abs_path = artifact_value

        # strip off the prefix if it exists for current user
        if artifact_value.lower().startswith(("hkcu", "hkey_current_user")):
            # The hkcu hive maps to a corresponding entry in hku for each user.
            # For hkcu entries remediate instead in hku for corresponding key for all users.
            # The hku entries top-level keys are the sids for the users which can have an hkcu hive loaded.
            # e.g 'HKEY_USERS\S-1-5-18' or 'HKEY_USERS\S-1-5-21-0123456789-0123456789-0123456789-1000' for system or
            # standard account.
            # The regex pattern 'S-\d+-\d+-\d+(-\d+-\d+\-\d+\-\d+)*$' is used to match an sid in the hku hive.
            (hive, artifact_value) = artifact_value.split('\\', 1)
            query = dedent(f"""
                // set Powershell parameter
                if {{x64 of operating system}}
                    parameter "PowerShellexe"="{{value "Path" of key "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\\1\ShellIds\Microsoft.PowerShell" of x64 registry}}"
                else
                    parameter "PowerShellexe"="{{value "Path" of key "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\\1\ShellIds\Microsoft.PowerShell" of registry}}"
                endif

                //Create script
                delete __createfile
                delete remove_keys.ps1
                createfile until END_OF_FILE
                New-PSDrive -PSProvider Registry -Name HKU -Root HKEY_USERS
                $PatternSID = 'S-\d+-\d+-\d+(-\d+-\d+\-\d+\-\d+)*$'
                Get-ChildItem HKU:\* |where {{{{$_.name  -match $PatternSID}} | %{{{{$_.Name}} | % {{{{

                    if (Test-Path -Path HKU:\$_\{artifact_value}) {{{{
                        Remove-Item HKU:\$_\{artifact_value} -Confirm:$false
                    }}
                }}
                END_OF_FILE
                move __createfile remove_keys.ps1

                // Execute PowerShell script
                action uses wow64 redirection false
                waithidden "{{parameter "PowerShellexe"}}" -ExecutionPolicy Bypass -File remove_keys.ps1
                action uses wow64 redirection {{x64 of operating system}}
                delete remove_keys.ps1
            """)

            key_format = "exists keys \"{}\" of keys whose (exists matches(regex(\"S-\d+-\d+-\d+(-\d+-\d+\-\d+\-\d+)*$\")) of (it as string) ) "\
                "of keys \"HKU\" of (if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"
        else:
            query = f"action uses wow64 redirection false \nwaithidden cmd.exe /c reg delete \"{artifact_value}\" /f"
            key_format = "exists keys \"{}\" of(if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"

        return self._post_bf_action_query(query, computer_id, f"Delete Registry Key '{key_abs_path}'", key_format.format(artifact_value))

    def get_bfclientquery(self, query_id, wait=30, timeout=600):
        """ Get Bigfix query results.
        :param query_id: Bigfix query id from post request
        :param wait: Interval to wait while checking status - value in secs
        :param timeout: Timeout value in secs - give some time to BigFix to get all the data. Value of 0 means try once.
        :return result: Result (list of responses) for query id
        """
        # Let's give some time (5 secs) to BigFix to get all the data
        sleep(5)
        wait_for_endpoints = False
        response_timedout = True

        while timeout > 0:
            result = []
            r = self.rc.execute("get",
                    f"{self.base_url}/api/clientqueryresults/{query_id}?stats=1&output=json",
                    auth=(self.bf_user, self.bf_pass),
                    verify=self.verify)
            if r.status_code == 200:
                try:
                    response = loads(r.text)
                except Exception as e:
                    LOG.exception(f"XML processing, Got exception type: {e.__repr__()}, msg: {e.message}")
                    raise e

                total_results = response.get('totalResults')
                if total_results == 0:
                    LOG.debug("No results yet, retrying")
                elif total_results > 0:
                    response_timedout = False
                    LOG.debug(f"Received responses from {total_results} endpoints.")
                    for i in range(total_results):
                        rs = response['results'][i]
                        result.append({
                            "computer_id": rs.get('computerID'),
                            "computer_name": rs.get('computerName'),
                            "query_id": rs.get('subQueryID'),
                            "failure": rs.get('isFailure'),
                            "result": rs.get('result'),
                            "resp_time": rs.get('ResponseTime')
                        })
                    if hasattr(self, "endpoints_wait") and self.endpoints_wait:
                        # Set new timeout value to wait for all results.
                        if not wait_for_endpoints:
                            LOG.info(f"Waiting {self.endpoints_wait} seconds for all endpoints to report.")
                            # Reset timeout value to 'self.endpoints_wait' and add 'wait' value as it will
                            # be stripped off again below.
                            timeout = self.endpoints_wait + wait
                            wait_for_endpoints = True
                    else:
                        break
                else:
                    LOG.exception(f"Got unexpected number of results ({total_results})")
                    break
            else:
                LOG.exception(f"Unexpected HTTP status code: {r.status_code}")

            timeout -= wait
            if timeout > 0:
                sleep(timeout if timeout < wait else wait)

        if response_timedout:
            LOG.info("Timed out waiting for a result.")

        return result

    def post_bfclientquery(self, query, computer_id=None):
        """ Post Bigfix relevance query.
        :param query: Relevance query
        :return query_id: Query id generatd by request
        """
        post_xml = elementTree.Element('BESAPI')
        post_xml.attrib = {'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                           'xsi:noNamespaceSchemaLocation': 'BESAPI.xsd'}
        clientq_elem = elementTree.SubElement(post_xml, 'ClientQuery')
        app_elem = elementTree.SubElement(clientq_elem, 'ApplicabilityRelevance')
        app_elem.text = 'true'
        query_elem = elementTree.SubElement(clientq_elem, 'QueryText')
        query_elem.text = query
        target_elem = elementTree.SubElement(clientq_elem, 'Target')
        if computer_id:
            target_comp_elem = elementTree.SubElement(target_elem, 'ComputerID')
            target_comp_elem.text = str(computer_id)
        else:
            target_comp_elem = elementTree.SubElement(target_elem, 'CustomRelevance')
            target_comp_elem.text = 'true'

        r = self.rc.execute("post", f"{self.base_url}/api/clientquery", auth=(self.bf_user, self.bf_pass),
                 verify=self.verify, data=elementTree.tostring(post_xml))

        if r.status_code == 200:
            try:
                results = elementTree.fromstring(r.text).findall(".//ClientQuery/ID")
                return int(results[0].text)
            except Exception as e:
                LOG.exception(f"XML processing, Got exception type: {e.__repr__()}, msg: {e.message}")
                raise e
        else:
            LOG.exception(f"BigFix client query creation did not return expected value: {r}")

    def _post_bf_action_query(self, query, computer_id, action_name, relevance="true"):
        """ Post Bigfix action request.
        :param query: Remediation relevance query
        :param computer_id: BigFix Endpoint id
        :param action_name: BigFix Action name
        :param relevance: Action relevance - default to True
        :return action_id: Action id generatd by request
        """
        post_xml = elementTree.Element('BES')
        post_xml.attrib = {'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                           'xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'SkipUI': 'true'}
        clientq_elem = elementTree.SubElement(post_xml, 'SingleAction')
        title_elem = elementTree.SubElement(clientq_elem, 'Title')
        title_elem.text = action_name
        relevance_elem = elementTree.SubElement(clientq_elem, 'Relevance')
        relevance_elem.text = relevance
        script_elem = elementTree.SubElement(clientq_elem, 'ActionScript')
        script_elem.text = query
        criteria_elem = elementTree.SubElement(clientq_elem, 'SuccessCriteria')
        criteria_elem.attrib = {'Option': 'OriginalRelevance'}
        target_elem = elementTree.SubElement(clientq_elem, 'Target')
        target_comp_elem = elementTree.SubElement(target_elem, 'ComputerID')
        target_comp_elem.text = str(computer_id)

        r = self.rc.execute("post", f"{self.base_url}/api/actions", auth=(self.bf_user, self.bf_pass),
                 verify=self.verify, data=elementTree.tostring(post_xml))

        if r.status_code == 200:
            try:
                results = elementTree.fromstring(r.text).findall(".//Action/ID")
                if len(results) > 1:
                    LOG.error("size of results larger than 1, only the first one will be used.")
                #  Urg, hardcoded index...
                action_id = results[0].text
                LOG.info(f"BigFix action created successfully. Action ID: {action_id}")
                LOG.debug(f"BigFix action created successfully: {r.text}")
                return action_id
            except Exception as e:
                LOG.exception(f"XML processing, Got exception type: {e.__repr__()}, msg: {e.message}")
                raise e
        else:
            LOG.error(f"Received bad Status Code: {r.status_code}. Returned data: {r.text}")

    def _process_bf_computer_query_response_to_attachment(self, response_text, title, number_of_tuples=3):
        """Transform the response of get_bf_computer_fixlets and get_bf_computer_properties
                into a XML format for attachment
        :param response_text: Remediation relevance query
        :param title: Response title
        :param number_of_tuples: Tuple count in xml
        :return response: Response transformed to xml format
        """
        try:
            xmlroot = elementTree.fromstring(response_text.text.encode('utf8', 'ignore'))
            results = xmlroot.findall(".//Query/Result/Tuple/Answer")
            if len(results):
                response = f"<?xml version='1.0'?>\n<report> {title}: \n"
                insertion_count = 0
                for elt in results:
                    if insertion_count == 0:
                        response += f"\t<property> {elt.text} \n"
                    elif insertion_count == 1:
                        response += f"\t\t<name> {elt.text} </name> \n"
                    elif insertion_count == 2:
                        v = elt.text
                        # Convert "<none>" value to "None" else xml will be un-readable.
                        v = "None" if v == "<none>" else v
                        response += f"\t\t<value> {v} </value> \n"

                    insertion_count += 1
                    if insertion_count == number_of_tuples:
                        response += "\t</property>\n"
                        insertion_count = 0

                return f"{response}</report>"
        except elementTree.ParseError as e:
            LOG.error("There was an error trying to process XML. Returning RAW XML")
            LOG.exception(f"XML processing, Got exception type: {e.__repr__()}, msg: {e.message}")
            return response_text.text
        except Exception as e:
            LOG.exception(f"XML processing, Got exception type: {e.__repr__()}, msg: {e.message}")
            raise e

    def get_bf_action_status(self, action_id):
        """ Get Bigfix action status.
        :param action_id: BigFix actions id
        :return status: Return BigFix actions status
        """

        r = self.rc.execute("get", f"{self.base_url}/api/action/{action_id}/status",
                auth=(self.bf_user, self.bf_pass), verify=self.verify)

        if r.status_code == 200:
            try:
                results = elementTree.fromstring(r.text).findall(".//ActionResults/Computer/Status")
                status = results[0].text if len(results) > 0 else None
                LOG.debug(f"BigFix Action Status: {status} BigFix Action ID: {action_id}.")
            except Exception as e:
                LOG.exception(f"XML processing, Got exception type: {e.__repr__()}, msg: {e.message}")
                raise e
        else:
            status = r.text
            LOG.debug(f"Found an error trying to execution the action: {r.text}. Action: {action_id}")
        return status
