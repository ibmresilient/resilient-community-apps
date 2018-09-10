# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Helper module containing REST API client for BigFix  """
import logging
import requests
import xml.etree.ElementTree as elementTree
import ntpath
import json
import time

# TODO: Check how should be defined this logger
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
                    LOG.info("No properties returned for computer_id : %s" % (computer_id))

                return qr_to_attachment

            except Exception as e:
                LOG.exception("XML processing, Got exception type: %s, msg: %s" % (e.__repr__(), e.message))
                raise e
        else:
            LOG.exception("Unexpected HTTP status code: %d" % (response.status_code))
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
        query = "exists folder \"{0}\"".format(head)
        if tail:
            query = "exists file \"{0}\" of folder \"{1}\"".format(tail, head)
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

        # strip off the prefix if it exists for current user or users
        if key.lower().startswith(("hkcu", "hkey_current_user", "hku", "hkey_users")):
            key = key.split('/', 1)[1]

        LOG.debug("get_bf_computer_by_registry_key_name_value triggered")
        if name and value:
            q_id = self.post_bfclientquery(
                "exists values \"{0}\" whose (it=\"{1}\") of keys \"{2}\" "
                "of current user keys (logged on users) "
                "of (if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"
                .format(name, value, key))
        elif name:
            q_id = self.post_bfclientquery(
                "exists values \"{0}\" of keys \"{1}\" "
                "of current user keys (logged on users) "
                "of(if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"
                .format(name, key))
        else:
            q_id = self.post_bfclientquery(
                "exists keys \"{0}\" "
                "of current user keys (logged on users) "
                "of(if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"
                .format(key))

        resp = self.get_bfclientquery(q_id, self.retry_interval, self.retry_timeout)
        return resp

    def send_delete_file_remediation_message(self, artifact_value, computer_id):
        """ Bigfix action - Delete file remediate action.

        :param artifact_value: Name of artifact to remediate
        :param computer_id: BigFix Endpoint id
        :return resp: Response from action

        """
        query = "delete \"{0}\"".format(artifact_value)
        relevance = "exists file \"{0}\"".format(artifact_value)
        return self._post_bf_action_query(query, computer_id, "Delete File {0}".format(artifact_value), relevance)

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
        return self._post_bf_action_query(query, computer_id, "Kill Process {0}".format(artifact_value), relevance)

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
        return self._post_bf_action_query(query, computer_id, "Stop service {0}".format(artifact_value),
                                          relevance)

    def send_delete_registry_key_remediation_message(self, artifact_value, computer_id):
        """ Bigfix action - Delete registry entry (MS Windows).

        :param artifact_value: Name of artifact to remediate
        :param computer_id: BigFix Endpoint id
        :return resp: Response from action

        """
        query = "action uses wow64 redirection false \n" \
                "waithidden cmd.exe /c reg delete " \
                "\"{0}\" /f".format(artifact_value)

        relevance = "exists keys \"{0}\" of(if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"\
            .format(artifact_value)

        return self._post_bf_action_query(query, computer_id, "Delete Registry Key {0}".format(artifact_value),
                                               relevance)

    def get_bfclientquery(self, query_id, wait=30, timeout=600):
        """ Get Bigfix query results.

        :param query_id: Bigfix query id from post request
        :param wait: Value name
        :param timeout: Timeout value - give some time to BigFix to get all the data
        :return result: Result (list of resposes) for query id

        """
        # Let's give some time (5 secs) to BigFix to get all the data
        time.sleep(5)
        """
            timeout is in ms. 0 means try once
        """
        clientq_restapi = 'api/clientqueryresults'
        req_url = "%s/%s/%d?stats=1&output=json" % (self.base_url, clientq_restapi, query_id)

        result = []
        while timeout >= 0:
            r = requests.get(req_url, auth=(self.bf_user, self.bf_pass), verify=False)
            if r.status_code == 200:
                try:
                    response = json.loads(r.text)
                    if response['totalResults'] == 0:
                        LOG.debug("No results yet, retrying")
                    elif response['totalResults'] > 0:
                        LOG.debug("Received responses from %s endpoints." % (response['totalResults']))
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
                        break
                    else:
                        LOG.exception("Got unexpected number of results (%d)" % (response['totalResults']))
                        break

                except Exception as e:
                    LOG.exception("XML processing, Got exception type: %s, msg: %s" % (e.__repr__(), e.message))
                    raise e
            else:
                LOG.exception("Unexpected HTTP status code: %d" % (r.status_code))

            timeout = timeout - 1000
            if timeout > 0:
                time.sleep(1)
        return result

    def post_bfclientquery(self, query):
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
                LOG.debug("** Client Query ID: %d" % (query_id))
                return query_id
            except Exception as e:
                # TODO - return error so that msg parser can handle it
                LOG.exception("XML processing, Got exception type: %s, msg: %s" % (e.__repr__(), e.message))
                raise e
        else:
            LOG.exception("BigFix client query creation did not return expected value: %s".format(r))

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
        settings_elem = elementTree.SubElement(clientq_elem, 'Settings')
        settingsLocks_elem = elementTree.SubElement(clientq_elem, 'SettingsLocks')
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
                LOG.info("BigFix action created successfully. Action ID: {0}".format(action_id))
                LOG.debug("BigFix action created successfully: {0}".format(r.text))
                return action_id
            except Exception as e:
                LOG.exception("XML processing, Got exception type: %s, msg: %s" % (e.__repr__(), e.message))
                raise e
        else:
            LOG.error("Received bad Status Code: {0}. Returned data: {1}".format(r.status_code, r.text))
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
                response = "<?xml version='1.0' ?>\n<report> %s: \n" % title
                insertion_count = 0
                for elt in results:
                    if insertion_count == 0:
                        response += "\t<property> %s \n" % elt.text
                    elif insertion_count == 1:
                        response += "\t\t<name> %s </name> \n" % elt.text
                    elif insertion_count == 2:
                        response += "\t\t<value> %s </value> \n" % elt.text

                    insertion_count += 1
                    if insertion_count == number_of_tuples:
                        response += "\t</property>\n"
                        insertion_count = 0

                response += "</report>"
                return response
        except elementTree.ParseError as e:
            LOG.error("There was an error trying to process XML. Returning RAW XML")
            LOG.exception("XML processing, Got exception type: %s, msg: %s" % (e.__repr__(), e.message))
            return response_text.text
        except Exception as e:
            LOG.exception("XML processing, Got exception type: %s, msg: %s" % (e.__repr__(), e.message))
            raise e

    def get_bf_action_status(self, action_id):
        """" Get Bigfix action status.

        :param action_id: BigFix actions id
        :return status: Return BigFix actions status

         """
        query_url = "{0}/api/action/{1}/status".format(self.base_url, action_id)
        r = requests.get(query_url, auth=(self.bf_user, self.bf_pass), verify=False)
        if r.status_code == 200:
            try:
                status = None
                xmlroot = elementTree.fromstring(r.text)
                results = xmlroot.findall(".//ActionResults/Computer/Status")
                if len(results) > 0:
                    status = results[0].text
                LOG.debug("BigFix Action Status: {0} BigFix Action ID: {1}."
                          .format(status, action_id))
            except Exception as e:
                LOG.exception("XML processing, Got exception type: %s, msg: %s" % (e.__repr__(), e.message))
                raise e
        else:
            status = r.text
            LOG.debug("Found an error trying to execution the action: {0}. Action: {1}".format(r.text, action_id))
        return status