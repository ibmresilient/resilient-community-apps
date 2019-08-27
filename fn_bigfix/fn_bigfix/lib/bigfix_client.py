# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

""" Helper module containing REST API client for BigFix  """
import logging
from textwrap import dedent
import requests
import xml.etree.ElementTree as elementTree
import ntpath
import json
import time
from sys import version_info

LOG = logging.getLogger(__name__)

__author__ = 'Resilient'


class BigFixClient(object):
    """
    Client class used to expose BigFix Rest API for BigFix Query
    """
    def __init__(self, options):
        """
        Class constructor
        """
        self.base_url = options.get("bigfix_url") + ":" + options.get("bigfix_port")
        self.bf_user = options.get("bigfix_user")
        self.bf_pass = options.get("bigfix_pass")
        self.headers = {'content-type': 'application/json'}
        self.retry_interval = int(options.get("bigfix_polling_interval"))
        self.retry_timeout = int(options.get("bigfix_polling_timeout"))
        if options.get("bigfix_endpoints_wait") is not None:
            self.endpoints_wait = int(options.get("bigfix_endpoints_wait"))
        # Endpoints
        self.client_query_endpoint = '/api/clientquery'
        self.client_query_results_endpoint = '/api/clientqueryresults/'
        self.client_query_names_computers = '/api/query?relevance=names+of+bes+computers'
        self.computer_endpoint = '/api/computer/{id}'

        requests.packages.urllib3.disable_warnings()
    # end __init__

    def get_bf_computer_properties(self, computer_id):
        """ Bigfix query - Get endpoint properties.

        :param computer_id: BigFix Endpoint id
        :return : Return response in XML format

        """
        query_str = 'api/query?relevance=if(number of property results of bes computers ' \
                    'whose (id of it = {0}) < 10000) ' \
                    'then((name of source analysis of property of it|"Retrieved Property",name of property of it,values of it) ' \
                    'of property results of bes computers whose(id of it = {0})) else error "Too Many Results"' \
                    .format(computer_id)

        req_str = "{0}/{1}".format(self.base_url, query_str)

        response = requests.get(req_str, auth=(self.bf_user, self.bf_pass), verify=False, timeout=None)
        if response.status_code == 200:
            try:
                qr_to_attachment = self._process_bf_computer_query_response_to_attachment(response,
                                                                                          "Computer ID {0} Properties"
                                                                                          .format(computer_id), 3)
                if not qr_to_attachment:
                    LOG.info("No properties returned for computer_id : %s", computer_id)

                return qr_to_attachment

            except Exception as e:
                LOG.exception("XML processing, Got exception type: %s, msg: %s", e.__repr__(), e.message)
                raise e
        else:
            LOG.exception("Unexpected HTTP status code: %d", response.status_code)
            return None

    def get_bf_computer_by_service_name(self, service_name):
        """ Bigfix query - Get endpoints by service name.

        :param service_name: Service name
        :return resp: Response from query

        """
        LOG.debug("get_bf_computer_by_service_name triggered")

        q_id = self.post_bfclientquery(
            "if (windows of operating system) "
            "then (disjunction of (exists matches(case insensitive regex(\"%22{0}%22.*%22running%22\")) of it ) "
            "of (services as string as lowercase)) else (false)".format(service_name))
        resp = self.get_bfclientquery(q_id, self.retry_interval, self.retry_timeout)
        return resp

    def get_bf_computer_by_process_name(self, process_name):
        """ Bigfix query - Get endpoints by process name.

        :param process_name: Process name
        :return resp: Response from query

        """
        LOG.debug("get_bf_computer_by_process_name triggered")

        q_id = self.post_bfclientquery(
            "if (windows of operating system) "
            "then (exists process whose(name of it as lowercase = \"{0}\" as lowercase)) "
            "else if (name of it contains \"Linux\") of operating system "
            "then (exists process whose(name of it = \"{0}\")) else (false)".format(process_name))
        resp = self.get_bfclientquery(q_id, self.retry_interval, self.retry_timeout)
        return resp

    def get_bf_computer_by_file_path(self, file_path):
        """ Bigfix query - Get endpoints by file path.

        :param file_path: File path
        :return resp: Response from query

        """
        head, tail = ntpath.split(file_path)
        query = u"exists file \"{0}\"".format(head)
        if tail:
            query = u"exists file \"{0}\" of folder \"{1}\"".format(tail, head)
        LOG.debug("get_bf_computer_by_file_path triggered")
        q_id = self.post_bfclientquery(query)
        resp = self.get_bfclientquery(q_id, self.retry_interval, self.retry_timeout)
        return resp

    def get_bf_computer_by_ip(self, ip):
        """ Bigfix query - Get endpoints by ip address.

        :param ip: ip address
        :return resp: Response from query

        """
        LOG.debug("get_bf_computer_by_ip triggered")
        q_id = self.post_bfclientquery(
            "exists remote addresses whose(it=\"{0}\") of sockets whose(established of tcp state of it) of network"
                .format(ip))
        resp = self.get_bfclientquery(q_id, self.retry_interval, self.retry_timeout)
        return resp

    def get_bf_computer_by_registry_key_name_value(self, key, name, value):
        """ Bigfix query - Get endpoints by registry entry (MS Windows).

        :param key: Registry key
        :param name: Value name
        :param value: Value data
        :return resp: Response from query

        """

        # strip off the prefix if it exists for current user
        if key.lower().startswith(("hkcu", "hkey_current_user")):
            # The hkcu hive maps to a corresponding entry in hku for each user.
            # For hkcu search instead in hku for existence of key for each actual user.
            # The hku entries top-level keys are the sids for the users which can have an hkcu hive loaded.
            # e.g 'HKEY_USERS\S-1-5-18' or 'HKEY_USERS\S-1-5-21-0123456789-0123456789-0123456789-1000' for a system or
            # standard account.
            # The regex pattern 'S-\d+-\d+-\d+(-\d+-\d+\-\d+\-\d+)*$' is used to match an sid in the hku hive.
            key = key.split('\\', 1)[1]
            namevaluekey = "exists values \"{0}\" whose (it=\"{1}\") of " \
                           "keys \"{2}\" of keys whose (exists matches(regex(\"S-\d+-\d+-\d+(-\d+-\d+\-\d+\-\d+)*$\")) " \
                           "of (it as string) ) of keys \"HKU\" of " \
                           "(if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"
            namekey = "exists values \"{0}\" of keys \"{1}\" of keys whose " \
                      "(exists matches(regex(\"S-\d+-\d+-\d+(-\d+-\d+\-\d+\-\d+)*$\")) of (it as string) ) of " \
                      "keys \"HKU\" of (if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"
            keyonly = "exists keys \"{0}\" of keys whose (exists matches(regex(\"S-\d+-\d+-\d+(-\d+-\d+\-\d+\-\d+)*$\")) " \
                      "of (it as string) ) of keys \"HKU\" of " \
                      "(if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"
        else:
            namevaluekey = "exists values \"{0}\" whose (it=\"{1}\") of keys \"{2}\" " \
                "of (if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"
            namekey = "exists values \"{0}\" of keys \"{1}\" " \
                "of(if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"
            keyonly = "exists keys \"{0}\" " \
                "of(if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"

        LOG.debug("get_bf_computer_by_registry_key_name_value triggered")
        if name and value:
            q_id = self.post_bfclientquery(namevaluekey.format(name, value, key))
        elif name:
            q_id = self.post_bfclientquery(namekey.format(name, key))
        else:
            q_id = self.post_bfclientquery(keyonly.format(key))

        resp = self.get_bfclientquery(q_id, self.retry_interval, self.retry_timeout)
        return resp

    def check_exists_subkey(self, artifact_value, computer_id):
        """ Bigfix query - Determine if a registry key has subkeys.

        :param artifact_value: Name of artifact to query
        :param computer_id: BigFix Endpoint id
        :return resp: Response from action

        """
        # strip off the prefix if it exists for current user
        if artifact_value.lower().startswith(("hkcu", "hkey_current_user")):
            (hive, artifact_value) = artifact_value.split('\\', 1)
            # The hkcu hive maps to a corresponding entry in hku for each user.
            # For hkcu get subkey instead in hku for existence of key for each actual user.
            # The hku entries top-level keys are the sids for the users which can have an hkcu hive loaded.
            # e.g 'HKEY_USERS\S-1-5-18' or 'HKEY_USERS\S-1-5-21-0123456789-0123456789-0123456789-1000' for a system or
            # standard account.
            # The regex pattern 'S-\d+-\d+-\d+(-\d+-\d+\-\d+\-\d+)*$' is used to match an sid in the hku hive.
            subkey = "exists key of keys \"{0}\" of keys whose (exists matches(regex(\"S-\d+-\d+-\d+(-\d+-\d+\-\d+\-\d+)*$\")) " \
                      "of (it as string) ) of keys \"HKU\" of " \
                      "(if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"
        else:
            subkey = "exists key of keys \"{0}\" " \
                "of(if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"

        LOG.debug("check exists subkey triggered")
        q_id = self.post_bfclientquery(subkey.format(artifact_value), computer_id)

        resp = self.get_bfclientquery(q_id, self.retry_interval, self.retry_timeout)
        return resp

    def check_is_folder(self, artifact_value, computer_id):
        """ Bigfix query - Determine if artifact value is a folder.

        :param artifact_value: Name of artifact to query
        :param computer_id: BigFix Endpoint id
        :return resp: Response from action

        """
        LOG.debug("check is folder triggered")
        q_id = self.post_bfclientquery(u"exists folder \"{0}\"".format(artifact_value))
        resp = self.get_bfclientquery(q_id, self.retry_interval, self.retry_timeout)
        return resp

    def send_delete_file_remediation_message(self, artifact_value, computer_id):
        """ Bigfix action - Delete file remediate action.

        :param artifact_value: Name of artifact to remediate
        :param computer_id: BigFix Endpoint id
        :return resp: Response from action

        """
        query = u"delete \"{0}\"".format(artifact_value)
        relevance = u"exists file \"{0}\"".format(artifact_value)
        return self._post_bf_action_query(query, computer_id, u"Delete File '{0}'".format(artifact_value), relevance)

    def send_kill_process_remediation_message(self, artifact_value, computer_id):
        """ Bigfix action - Kill process remediate action.

        :param artifact_value: Name of artifact to remediate
        :param computer_id: BigFix Endpoint id
        :return resp: Response from action

        """
        query = "if {{windows of operating system}} \n waithidden cmd.exe /c taskkill /im {0} /f /t \n" \
                "else \n wait kill -9  {{concatenation \" \" of (ids of processes whose (name of it = \"{0}\") as string)}}\n " \
                "endif".format(artifact_value)
        relevance = "if (windows of operating system) " \
                    "then (exists process whose(name of it as lowercase = \"{0}\" as lowercase)) " \
                    "else if (name of it contains \"Linux\") of operating system " \
                    "then (exists process whose(name of it = \"{0}\")) else (false)".format(artifact_value)
        return self._post_bf_action_query(query, computer_id, "Kill Process '{0}'".format(artifact_value), relevance)

    def send_stop_service_remediation_message(self, artifact_value, computer_id):
        """ Bigfix action - Stop service remediate action.

        :param artifact_value: Name of artifact to remediate
        :param computer_id: BigFix Endpoint id
        :return resp: Response from action

        """
        query = "if {{windows of operating system}} \n waithidden cmd.exe /c net stop \"{0}\" \n" \
                "else\n wait stop service {0} \n" \
                "endif".format(artifact_value)
        relevance = "if (windows of operating system) " \
                    "then (disjunction of (exists matches(case insensitive regex(\"%22{0}%22.*%22running%22\")) of it ) " \
                    "of (services as string as lowercase)) else (false)".format(artifact_value)
        return self._post_bf_action_query(query, computer_id, "Stop service '{0}'".format(artifact_value),
                                          relevance)

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
            query = dedent("""
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

                    if (Test-Path -Path HKU:\$_\{0}) {{{{
                        Remove-Item HKU:\$_\{0} -Confirm:$false
                    }}
                }}
                END_OF_FILE
                move __createfile remove_keys.ps1

                // Execute PowerShell script
                action uses wow64 redirection false
                waithidden "{{parameter "PowerShellexe"}}" -ExecutionPolicy Bypass -File remove_keys.ps1
                action uses wow64 redirection {{x64 of operating system}}
                delete remove_keys.ps1
            """.format(artifact_value))

            key_format = "exists keys \"{0}\" of keys whose " \
                         "(exists matches(regex(\"S-\d+-\d+-\d+(-\d+-\d+\-\d+\-\d+)*$\")) of (it as string) ) of " \
                         "keys \"HKU\" of (if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"
        else:
            query = "action uses wow64 redirection false \n" \
                    "waithidden cmd.exe /c reg delete " \
                    "\"{0}\" /f".format(artifact_value)

            key_format = "exists keys \"{0}\" " \
                         "of(if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"

        relevance = key_format.format(artifact_value)

        return self._post_bf_action_query(query, computer_id, "Delete Registry Key '{0}'".format(key_abs_path),
                                               relevance)

    def get_bfclientquery(self, query_id, wait=30, timeout=600):
        """ Get Bigfix query results.

        :param query_id: Bigfix query id from post request
        :param wait: Interval to wait while checking status - value in secs
        :param timeout: Timeout value in secs - give some time to BigFix to get all the data. Value of 0 means try once.
        :return result: Result (list of responses) for query id

        """
        # Let's give some time (5 secs) to BigFix to get all the data
        time.sleep(5)
        clientq_restapi = 'api/clientqueryresults'
        req_url = "%s/%s/%d?stats=1&output=json" % (self.base_url, clientq_restapi, query_id)
        wait_for_endpoints = False
        response_timedout = True

        while timeout > 0:
            result = []
            r = requests.get(req_url, auth=(self.bf_user, self.bf_pass), verify=False)
            if r.status_code == 200:
                try:
                    response = json.loads(r.text)
                    if response['totalResults'] == 0:
                        LOG.debug("No results yet, retrying")
                    elif response['totalResults'] > 0:
                        response_timedout = False
                        LOG.debug("Received responses from %s endpoints.", response['totalResults'])
                        for i in range(response['totalResults']):
                            result.append({
                                "computer_id": response['results'][i]['computerID'],
                                "computer_name": response['results'][i]['computerName'],
                                "query_id": response['results'][i]['subQueryID'],
                                "failure": response['results'][i]['isFailure'],
                                "result": response['results'][i]['result'],
                                "resp_time": response['results'][i]['ResponseTime']
                                }
                            )
                        if hasattr(self, "endpoints_wait") and self.endpoints_wait is not None:
                            # Set new timeout value to wait for all results.
                            if not wait_for_endpoints:
                                LOG.info("Waiting %s seconds for all endpoints to report.", self.endpoints_wait)
                                # Reset timeout value to 'self.endpoints_wait' and add 'wait' value as it will
                                # be stripped off again below.
                                timeout = self.endpoints_wait + wait
                                wait_for_endpoints = True
                        else:
                            break
                    else:
                        LOG.exception("Got unexpected number of results (%d)", response['totalResults'])
                        break

                except Exception as e:
                    LOG.exception("XML processing, Got exception type: %s, msg: %s", e.__repr__(), e.message)
                    raise e
            else:
                LOG.exception("Unexpected HTTP status code: %d", r.status_code)

            timeout = timeout - wait
            if timeout > 0:
                if timeout < wait:
                    time.sleep(timeout)
                else:
                    time.sleep(wait)

        if response_timedout:
            LOG.info("Timed out waiting for a result.")

        return result

    def post_bfclientquery(self, query, computer_id=None):
        """" Post Bigfix relevance query.

        :param query: Relevance query
        :return query_id: Query id generatd by request

         """
        query_str = 'api/clientquery'
        query_url = "%s/%s" % (self.base_url, query_str)
        post_xml = elementTree.Element('BESAPI')
        post_xml.attrib = {'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                           'xsi:noNamespaceSchemaLocation': 'BESAPI.xsd'}
        clientq_elem = elementTree.SubElement(post_xml, 'ClientQuery')
        app_elem = elementTree.SubElement(clientq_elem, 'ApplicabilityRelevance')
        app_elem.text = 'true'
        query_elem = elementTree.SubElement(clientq_elem, 'QueryText')
        query_elem.text = query
        target_elem = elementTree.SubElement(clientq_elem, 'Target')
        if computer_id is not None:
            target_comp_elem = elementTree.SubElement(target_elem, 'ComputerID')
            target_comp_elem.text = str(computer_id)
        else:
            target_comp_elem = elementTree.SubElement(target_elem, 'CustomRelevance')
            target_comp_elem.text = 'true'
        r = requests.post(query_url, auth=(self.bf_user, self.bf_pass), verify=False, data=elementTree.tostring(post_xml))
        if r.status_code == 200:
            try:
                # TODO! count the number of Tuples - should only be 1
                xmlroot = elementTree.fromstring(r.text)
                # TODO - should just be one ID, change XML path string
                results = xmlroot.findall(".//ClientQuery/ID")
                #  Urg, hardcoded index...
                query_id = int(results[0].text)
                LOG.debug("** Client Query ID: %d", query_id)
                return query_id
            except Exception as e:
                # TODO - return error so that msg parser can handle it
                LOG.exception("XML processing, Got exception type: %s, msg: %s", e.__repr__(), e.message)
                raise e
        else:
            LOG.exception("BigFix client query creation did not return expected value: %s", r)

    def _post_bf_action_query(self, query, computer_id, action_name, relevance="true"):
        """" Post Bigfix action request.

        :param query: Remediation relevance query
        :param computer_id: BigFix Endpoint id
        :param action_name: BigFix Action name
        :param relevance: Action relevance - default to True
        :return action_id: Action id generatd by request

         """
        query_str = 'api/actions'
        query_url = "%s/%s" % (self.base_url, query_str)
        post_xml = elementTree.Element('BES')
        post_xml.attrib = {'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                           'xmlns:xsd': 'http://www.w3.org/2001/XMLSchema',
                           'SkipUI': 'true'}
        clientq_elem = elementTree.SubElement(post_xml, 'SingleAction')
        title_elem = elementTree.SubElement(clientq_elem, 'Title')
        title_elem.text = action_name
        relevance_elem = elementTree.SubElement(clientq_elem, 'Relevance')
        relevance_elem.text = relevance
        script_elem = elementTree.SubElement(clientq_elem, 'ActionScript')
        script_elem.text = query
        criteria_elem = elementTree.SubElement(clientq_elem, 'SuccessCriteria')
        criteria_elem.attrib = {'Option': 'OriginalRelevance'}
        #settings_elem = elementTree.SubElement(clientq_elem, 'Settings')
        #settingsLocks_elem = elementTree.SubElement(clientq_elem, 'SettingsLocks')
        target_elem = elementTree.SubElement(clientq_elem, 'Target')
        target_comp_elem = elementTree.SubElement(target_elem, 'ComputerID')
        target_comp_elem.text = str(computer_id)
        r = requests.post(query_url, auth=(self.bf_user, self.bf_pass), verify=False,
                          data=elementTree.tostring(post_xml))
        if r.status_code == 200:
            try:
                # TODO! count the number of Tuples - should only be 1
                xmlroot = elementTree.fromstring(r.text)
                # TODO - should just be one ID, change XML path string
                results = xmlroot.findall(".//Action/ID")
                if len(results) > 1:
                    LOG.error("size of results larger than 1, only the first one will be used.")
                #  Urg, hardcoded index...
                action_id = results[0].text
                LOG.info("BigFix action created successfully. Action ID: %s", action_id)
                LOG.debug("BigFix action created successfully: %s", r.text)
                return action_id
            except Exception as e:
                LOG.exception("XML processing, Got exception type: %s, msg: %s", e.__repr__(), e.message)
                raise e
        else:
            LOG.error("Received bad Status Code: %s. Returned data: %s", r.status_code, r.text)
            return None

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
            if len(results) == 0:
                return None
            else:
                response = "<?xml version='1.0'?>\n<report> %s: \n" % title
                insertion_count = 0
                for elt in results:
                    if insertion_count == 0:
                        response += "\t<property> %s \n" % elt.text
                    elif insertion_count == 1:
                        response += "\t\t<name> %s </name> \n" % elt.text
                    elif insertion_count == 2:
                        v = elt.text
                        # Convert "<none>" value to "None" else xml will be un-readable.
                        if v == "<none>":
                            v = v.replace("<none>", "None")
                        response += "\t\t<value> %s </value> \n" % v

                    insertion_count += 1
                    if insertion_count == number_of_tuples:
                        response += "\t</property>\n"
                        insertion_count = 0

                response += "</report>"
                return response
        except elementTree.ParseError as e:
            LOG.error("There was an error trying to process XML. Returning RAW XML")
            LOG.exception("XML processing, Got exception type: %s, msg: %s", e.__repr__(), e.message)
            return response_text.text
        except Exception as e:
            LOG.exception("XML processing, Got exception type: %s, msg: %s", e.__repr__(), e.message)
            raise e

    def get_bf_action_status(self, action_id):
        """" Get Bigfix action status.

        :param action_id: BigFix actions id
        :return status: Return BigFix actions status

         """
        query_url = u"{0}/api/action/{1}/status".format(self.base_url, action_id)
        r = requests.get(query_url, auth=(self.bf_user, self.bf_pass), verify=False)
        if r.status_code == 200:
            try:
                status = None
                if version_info.major < 3:
                    xmlroot = elementTree.fromstring(r.text.encode('utf8'))
                else:
                    xmlroot = elementTree.fromstring(r.text)
                results = xmlroot.findall(".//ActionResults/Computer/Status")
                if len(results) > 0:
                    status = results[0].text
                LOG.debug("BigFix Action Status: %s BigFix Action ID: %s.", status, action_id)
            except Exception as e:
                LOG.exception("XML processing, Got exception type: %s, msg: %s", e.__repr__(), e.message)
                raise e
        else:
            status = r.text
            LOG.debug("Found an error trying to execution the action: %s. Action: %s", r.text, action_id)
        return status