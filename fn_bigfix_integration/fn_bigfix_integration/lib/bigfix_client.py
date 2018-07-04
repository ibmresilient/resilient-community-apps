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
    def __init__(self, opts):
        """
        Class constructor
        """
        config = opts.get("fn_bigfix_integration", {})
        self.base_url = config.get("bigfix_url", "https://bigfix-url.com") + ":" + config.get("bigfix_port", "52311")
        self.bf_user = config.get("bigfix_user", "BigFixAdmin")
        self.bf_pass = config.get("bigfix_pass", "MyPassword")
        self.headers = {'content-type': 'application/json'}

        # Endpoints
        self.client_query_endpoint = '/api/clientquery'
        self.client_query_results_endpoint = '/api/clientqueryresults/'
        self.client_query_names_computers = '/api/query?relevance=names+of+bes+computers'
        self.computer_endpoint = '/api/computer/{id}'

        requests.packages.urllib3.disable_warnings()
    # end __init__

    def get_bf_computer_by_service_name(self, service_name):
        """ Class method - Bigfix query - Get endpoints by service name.

        :param service_name: Service name
        :return resp: Response from query

        """
        LOG.debug("get_bf_computer_by_service_name triggered")
        q_id = self.post_bfclientquery(
            "disjunction of (it contains \"{0}\" as lowercase AND it contains \"running\") "
            "of (services as string as lowercase)".format(service_name))
        resp = self.get_bfclientquery(q_id)
        return resp

    def get_bf_computer_by_process_name(self, process_name):
        """ Class method - Bigfix query - Get endpoints by process name.

        :param process_name: Process name
        :return resp: Response from query

        """
        LOG.debug("get_bf_computer_by_process_name triggered")
        q_id = self.post_bfclientquery(
            "exists process whose(name of it as lowercase = \"{0}\")".format(process_name))
        resp = self.get_bfclientquery(q_id)
        return resp

    def get_bf_computer_by_file_path(self, file_path):
        """ Class method - Bigfix query - Get endpoints by file path.

        :param file_path: File path
        :return resp: Response from query

        """
        head, tail = ntpath.split(file_path)
        query = "exists folder \"{0}\"".format(head)
        if tail:
            query = "exists file \"{0}\" of folder \"{1}\"".format(tail, head)
        LOG.debug("get_bf_computer_by_file_path triggered")
        q_id = self.post_bfclientquery(query)
        resp = self.get_bfclientquery(q_id)
        return resp

    def get_bf_computer_by_ip(self, ip):
        """ Class method - Bigfix query - Get endpoints by ip address.

        :param ip: ip address
        :return resp: Response from query

        """
        LOG.debug("get_bf_computer_by_ip triggered")
        q_id = self.post_bfclientquery(
            "exists remote addresses whose(it=\"{0}\") of sockets whose(established of tcp state of it) of network"
                .format(ip))
        resp = self.get_bfclientquery(q_id)
        return resp

    def get_bf_computer_by_registry_key_name_value(self, key, name, value):
        """ Class method - Bigfix query - Get endpoints by registry entry (MS Windows).

        :param key: Registry key
        :param name: Value name
        :param value: Value data
        :return resp: Response from query

        """
        LOG.debug("get_bf_computer_by_registry_key_name_value triggered")
        if name and value:
            q_id = self.post_bfclientquery(
                "exists values \"{0}\" whose (it=\"{1}\") of keys \"{2}\" "
                "of (if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"
                .format(name, value, key))
        elif name:
            q_id = self.post_bfclientquery(
                "exists values \"{0}\" of keys \"{1}\" "
                "of(if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"
                .format(name, key))
        else:
            q_id = self.post_bfclientquery(
                "exists keys \"{0}\" of(if(x64 of operating system) then(x64 registry;x32 registry) else(registry))"
                .format(name))

        resp = self.get_bfclientquery(q_id)
        return resp



    def get_bfclientquery(self, query_id, wait=5, timeout=5000):
        """ Class method - Get Bigfix query results.

        :param query_id: Bigfix query id from post request
        :param wait: Value name
        :param timeout: Timeout value - give some time to BigFix to get all the data
        :return result: Result (list of resposes) for query id

        """
        # Let's give some time to BigFix to get all the data
        time.sleep(wait)
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
                        LOG.debug("Got results: %s" % (response['totalResults']))
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
        """"Class method - Post Bigfix relevance query.

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