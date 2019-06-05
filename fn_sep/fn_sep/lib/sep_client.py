# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

""" Class for Resilient circuits Functions supporting REST API client for Symantec SEP  """
import logging
import re
import json
from textwrap import dedent

from fn_sep.lib.requests_sep import RequestsSep

try:
    from urllib.parse import urljoin
except:
    from urlparse import urljoin

LOG = logging.getLogger(__name__)

HASH_LENGTH_TO_TYPE = {
    64: "SHA256",
    40: "SHA-1",
    32: "MD5",
}

class Sepclient(object):
    """
    Client class used to expose Symantec SEP Rest API.
    """
    def __init__(self, options, function_params=None):
        """
        Class constructor
        """
        self.host = options.get("host")
        self.port = options.get("port")
        self.base_path = options.get("base_path")
        self.auth_path = options.get("auth_path")
        self.username = options.get("username")
        self.password = options.get("password")
        self.domain = options.get("domain")
        self.base_url = "https://{0}:{1}".format(self.host, self.port)
        self.auth_url = self.base_url + self.auth_path
        if options.get("query_limit") is not None:
            self.query_limit = int(options.get("query_limit"))
        # Rest request endpoints
        self._endpoints = {
            # Admin endpoints
            "auth":                                     self.auth_path,
            "version":                                  self.base_path+"/version",
            "domains":                                  self.base_path+"/domains",
            "computers":                                self.base_path+"/computers",
            "groups":                                   self.base_path+"/groups",
            "clients_online_status":                    self.base_path+"/stats/client/onlinestatus",
            "scan_endpoints":                           self.base_path+"/command-queue/eoc",
            "upload_file":                              self.base_path+"/command-queue/files",
            "command_status":                           self.base_path+"/command-queue/{}",
            "file_content":                             self.base_path+"/command-queue/file/{}/content",
            "quarantine_endpoints":                     self.base_path+"/command-queue/quarantine",
            "policies":                                 self.base_path+"/policies/summary",
            "policies_by_type":                         self.base_path+"/policies/summary/{}",
            "fingerprints_list":                        self.base_path+"/policy-objects/fingerprints",
            "fingerprints_list_by_id":                  self.base_path+"/policy-objects/fingerprints/{}",
            "assign_fingerprint_list_to_group":         self.base_path+"/groups/{0}/system-lockdown/fingerprints/{1}"
         }
        self._req = RequestsSep(options, function_params)
        self._headers = {"content-type": "application/json", "Authorization": "Bearer {0}".format(self._get_token())}

    @staticmethod
    def get_hash_type(hash):
        """ Find hash type from size for sha256, sha-1 and md5.
        :param hash: The hash value.
        :return: Hash type info.
        """
        if len(hash) in HASH_LENGTH_TO_TYPE:
            return HASH_LENGTH_TO_TYPE[len(hash)]
        else:
            raise ValueError('Unknown hash type for value: ' + hash)

    @staticmethod
    def setup_scan_xml(scan_type, file_path, sha256, sha1, md5, description, scan_action):
        """ Set up xml payload for an eoc or remediation scan.

        :param scan_type: Type of scan e.g. 'QUICK_SCAN', 'FULL_SCAN'.
        :param file_path: Can be a file path or name or None value. (Optional parameter)
        :param sha256: Sha256 hash value. (Optional parameter)
        :param sha1: Sha1 hash value.(Optional parameter)
        :param md5: Sha1 hash value. (Optional parameter)
        :param description: Description of scan.
        :param scan_action: Used to set action for remediation scans.
        :return An xml payload string.
        """
        if scan_action is not None and scan_action.lower() == "remediate":
            action = "<RemediationAction>REMEDIATE</RemediationAction>"
        else:
            action = ''

        # Reset 'None' values to blanks'
        file_path = '' if file_path is None else file_path
        hvs = ['' if hv is None else hv for hv in [sha256, sha1, md5]]

        scan_xml = dedent(u"""\
            <?xml version="1.0" encoding="UTF-8"?>
            <EOC creator="Resilient" version="1.0" id="id">
              <DataSource name="name" id="id" version="version"/>
              <ScanType>{0}</ScanType>
              {6}
              <Threat category="" type="" severity="" time="">
                <Description>{5}</Description>
                <Attacker/>
              </Threat>
              <Activity>
                <OS id="0" name="name" version="version">
                  <Process/>
                  <Files>
                    <File name="{1}" action="create">
                      <Hash name="SHA256" value="{2}"/>
                    </File>
                    <File name="{1}" action="create">
                      <Hash name="SHA1" value="{3}"/>
                    </File>
                    <File name="{1}" action="create">
                      <Hash name="MD5" value="{4}"/>
                    </File>
                  </Files>
                  <Registry/>
                  <Network/>
                </OS>
              </Activity>
            </EOC>""").format(scan_type, file_path, hvs[0], hvs[1], hvs[2], description.encode('utf-8'), action)

        return scan_xml


    def _get_token(self):
        """Get the authorization token to be used in subsequent requests.

        :return: Token
        """
        url = urljoin(self.base_url, self._endpoints["auth"])
        json = {"username": self.username, "password": self.password, "domain": self.domain}
        r = self._req.execute_call('post', url, verify_flag=False, json=json)

        return r["token"]

    def get_version(self):
        """Get version of SEPM.

        :return: Result in json format
        """
        url = urljoin(self.base_url, self._endpoints["version"])

        r =  self._req.execute_call('get', url, verify_flag=False, headers=self._headers)

        return r

    def test_connectivity(self):
        """Connectivity Test which is used by resilient_circuits selftest.

        Calls http 'head' request against 'computers' endpoint.

        :return: Result in json format
        """
        url = urljoin(self.base_url, self._endpoints["computers"])

        r = self._req.execute_call('head', url, verify_flag=False, resp_type='bytes', headers=self._headers)

        return r

    def get_domains(self):
        """Get a list of domains.

        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["domains"])

        r = self._req.execute_call('get', url, verify_flag=False, headers=self._headers)

        return r

    def get_computers(self, computername=None, domain=None, lastupdate=None, order=None, os=None, pageindex=None,
                      pagesize=None, sort=None, status=None, status_details=None):
        """Get a list of computers. The paramaters are all optional the default is to return results for all computers/
        endpoints.

        :param computername: The host name of computer. Wild card is supported as '*'.
        :param domain: The domain from which to get computer information.
        :param lastupdate: Indicates when a computer last updated its status. The default value of 0 gets all the results.
        :param order: Specifies whether the results are in ascending order (ASC) or descending order (DESC).
        :param os: The list of OS to filter.
        :param pageindex: The index page that is used for the returned results. The default page index is 1.
        :param pagesize: The number of results to include on each page. The default is 20.
        :param sort: The column by which the results are sorted.
        :param status: Overall endpoints status. Used by the integration, Not in REST call signature.
        :param status_details: Endpoints status details. Used by the integration, Not in REST call signature.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["computers"])
        params = {"computerName": computername, "domain": domain, "lastUpdate": lastupdate, "order":order, "os":os,
                  "pageIndex": pageindex, "pageSize": pagesize, "sort": sort}

        r = self._req.execute_call('get', url, verify_flag=False, headers=self._headers, params=params)

        return r

    def get_clients_online_status(self):
        """Gets a list and count of the online and offline clients.

        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["clients_online_status"])

        r = self._req.execute_call('get', url, verify_flag=False, headers=self._headers)

        return r

    def get_groups(self, domain=None, fullpathname=None, mode=None, order=None, os=None, pageindex=None,
                      pagesize=None, sort=None):
        """Get a list of groups. The paramaters are all optional the default is to return results for all groups.

        :param domain: The SEP domain name.
        :param fullpathname: The full path name of the group.
        :param mode: The presentation mode for the results, as a list (default) or as a tree.
        :param order: Specifies whether the results are in ascending order (ASC) or descending order (DESC).
        :param pageindex: The index page that is used for the returned results. The default page index is 1.
        :param pagesize: The number of results to include on each page. The default is 20.
        :param sort: The column by which the results are sorted.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["groups"])

        params = {"domain": domain, "fullPathName": fullpathname, "order":order,
                  "pageIndex": pageindex , "pageSize": pagesize, "sort": sort}

        r = self._req.execute_call('get', url, verify_flag=False, headers=self._headers, params=params)

        return r

    def get_policies_summary(self, policy_type=None, domainid=None):
        """ Get list of policies.
        Supported types are: av, fw, lu, hi, hid adc, ips, or exceptions.
        :param policy_type: If present gets a summary for all the policies of this type.
        :param domainid: If present, get policies from this domain. Otherwise, get policies from the logged-on domain.
        :return Result in json format.
        """
        if policy_type is None:
            url = urljoin(self.base_url, self._endpoints["policies"])
        else:
            url = urljoin(self.base_url, self._endpoints["policies_by_type"]).format(policy_type)

        params = {"domainId": domainid}

        r = self._req.execute_call('get', url, verify_flag=False, headers=self._headers, params=params)

        return r

    def get_fingerprint_list(self, fingerprintlist_id=None, domainid=None, fingerprintlist_name=None):
        """ Gets the fingerprint list for a specified name as a set of hash values. Either parameter fingerprintlist_id
        or fingerprintlist_name can be used but not at the same time.

        :param fingerprintlist_id: Id of fingerprint list.
        :param domainid: If present, get policies from this domain. Otherwise, get policies from the logged-on domain.
        :param fingerprintlist_name: Name of a fingerprint list.
        :return Result in json format.
        """
        if fingerprintlist_id is None:
            url = urljoin(self.base_url, self._endpoints["fingerprints_list"])
        else:
            url = urljoin(self.base_url, self._endpoints["fingerprints_list_by_id"]).format(fingerprintlist_id)

        params = {"domainId": domainid, "name": fingerprintlist_name}

        r = self._req.execute_call('get', url, verify_flag=False, headers=self._headers, params=params)

        return r

    def delete_fingerprint_list(self, fingerprintlist_id=None):
        """ Delete a file fingerprint list.

        :param fingerprintlist_id: The fingerprint list  id.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["fingerprints_list_by_id"]).format(fingerprintlist_id)

        r = self._req.execute_call('delete', url, verify_flag=False, headers=self._headers)

        return r

    def add_fingerprint_list(self, fingerprintlist_name=None, description=None, domainid=None, hash_value=None):
        """ Add a blacklist as a file fingerprint list with hash value.

        :param name: The blacklist file’s ID. This field is not required at the blacklist file’s creation,
                    but when the blacklist file is updated, this field is required.
        :param description: The blacklist file’s description.
        :param domainid: If present, get policies from this domain. Otherwise, get policies from the logged-on domain.
        :param hash_type: The blacklist file’s hash type. Possible values are MD5 or SHA256.
        :param hash_value: The blacklist file’s hash type. Possible values are MD5 or SHA256.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["fingerprints_list"])

        hash_type = "MD5" if hash_value in [None, ''] else self.get_hash_type(hash_value)

        if hash_value is None:
            hash_value = ''

        if hash_type not in ["MD5"]:
            raise ValueError("Unsupported hash type for value: " + hash_value)

        payload = json.dumps({"name": fingerprintlist_name, "description": description, "domainId": domainid, "hashType": hash_type,
                              "data": [hash_value]})

        r = self._req.execute_call('post', url, verify_flag=False, headers=self._headers, data=payload)

        return r

    def update_fingerprint_list(self, fingerprintlist_id=None, fingerprintlist_name=None, description=None, domainid=None, hash_value=None):
        """ Update fingerprint list.

        :param fingerprint_id: The fingerprint list id.
        :param description: The blacklist file’s description.
        :param domainid: If present, get policies from this domain. Otherwise, get policies from the logged-on domain.
        :param hash_type: The blacklist file’s hash type. Possible values are MD5 or SHA256.
        :param name: The blacklist file’s ID. This field is not required at the blacklist file’s creation, but when the blacklist file is updated, this field is required.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["fingerprints_list_by_id"]).format(fingerprintlist_id)

        if hash_value is not None:
            hash_values =  re.split('\s+|,', hash_value)

        hash_type = self.get_hash_type(hash_values[0])

        if hash_type not in ["MD5"]:
            raise ValueError("Unsupported hash type for value: " + hash_value)

        payload = json.dumps({"name": fingerprintlist_name,"description": description, "domainId": domainid,
                              "hashType": hash_type, "data": hash_values})
        r = self._req.execute_call('post', url, verify_flag=False, headers=self._headers, data=payload)

        return r

    def assign_fingerprint_list_to_group(self, groupid, fingerprintlist_id=None):
        """ Assign a fingerprint list to a group for lockdown purposes.

        :param group_id: The group id to assign fingerprint iud.
        :param fingerprintlist_id: The fingerprint list id.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["assign_fingerprint_list_to_group"])\
            .format(groupid, fingerprintlist_id)

        payload = json.dumps({"group_id": groupid, "fingerprint_id": fingerprintlist_id})

        r = self._req.execute_call('put', url, verify_flag=False, headers=self._headers, data=payload)

        return r

    def upload_file(self, file_path=None, computer_ids=None, sha256=None, md5=None, sha1=None, source=None ):
        """Upload a suspicious file to the SEPM server.

        :param file_path: The file path of the suspicious file.
        :param computer_ids: List of computer ids.
        :param sha256: The SHA256 hash value of the suspicious file.
        :param md5: The MD5 hash value of the suspicious file (optional).
        :param sha1: The SHA1 hash value of the suspicious file (optional).
        :param source: Source of file to upload can be FILESYSTEM (default), QUARANTINE, or BOTH.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["upload_file"])

        if computer_ids is not None:
            computer_ids =  re.split('\s+|,', computer_ids)

        params = {"file_path": file_path, "computer_ids": computer_ids, "sha256": sha256, "md5": md5, "sha1": sha1,
                  "source": source}

        r = self._req.execute_call('post', url, verify_flag=False, headers=self._headers, params=params)

        return r

    def get_command_status(self, commandid=None, order=None, pageindex=None, pagesize=None, sort=None, status_type=None,
                           matching_endpoint_ids=None, incident_id=None):
        """Get command status from command id.

        :param commandid: The command id.
        :param order: Specifies whether the results are in ascending order (ASC) or descending order (DESC).
        :param pageindex: The index page that is used for the returned results. The default page index is 1.
        :param pagesize: The number of results to include on each page. The default is 20.
        :param sort: The column by which the results are sorted.
        :param status_type: The type of command status requested. Used by the integration, Not in REST call signature.
        :param incident_id: Resilient incident id. Used by the integration, Not in REST call signature.
        :param matching_endpoint_ids: Return matching endpoint ids in scan. Used by the integration, Not in REST call signature.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["command_status"]).format(commandid)

        params = {"order": order, "pageIndex": pageindex, "pageSize": pagesize, "sort": sort}

        r = self._req.execute_call('get', url, verify_flag=False, headers=self._headers)

        return r

    def get_file_content(self, file_id=None):
        """Get the details of a binary file, such as the checksum and the file size.

        :param file_id: The file ID from which to get detailed information.
        """
        url = urljoin(self.base_url, self._endpoints["file_content"]).format(file_id)
        headers = self._headers
        headers.update({"content-type":"application/json; charset=UTF-8", "Accept-Encoding": "gzip, deflate, compress"})
        r = self._req.execute_call('get', url, verify_flag=False, headers=headers, stream=True)

        return r

    def quarantine_endpoints(self, group_ids=None, computer_ids=None, undo=None ):
        """Quarantine an endpoint in the SEP environment my moving to a quarantine group.

        :param group_ids: Id of quarantine group.
        :param computer_ids: List of computer ids.
        :param undo: Boolean value  set to unquarantine endpoint.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["quarantine_endpoints"])

        if group_ids is not None:
            group_ids = re.split('\s+|,', group_ids)
        if computer_ids is not None:
            computer_ids =  re.split('\s+|,', computer_ids)

        params = {"computer_ids": computer_ids, "group_ids": group_ids,  }

        if undo is not None:
            params.update({"undo": undo})

        r = self._req.execute_call('post', url, verify_flag=False, headers=self._headers, params=params)

        return r

    def scan_endpoints(self, computer_ids=None, group_ids=None, scan_type=None, file_path=None, sha256=None,sha1=None,
                       md5=None, description=None, scan_action=None):
        """Run an 'eoc' or "Remediation" scan on endpoint(s).

        :param computer_ids: List of computer ids.
        :param group_ids: List of groups ids.
        :param scan_type: Select value for scan type e.g. "FULL_SCAN".
        :param file_path: File name or path to be scanned.
        :param sha256: Sha256 hash value.
        :param sha1: Sha1 hash value.
        :param md5: Sha1 hash value.
        :param remediate: Perform a remediation scan.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["scan_endpoints"])

        if group_ids is not None:
            group_ids = re.split('\s+|,', group_ids)

        if computer_ids is not None:
            computer_ids =  re.split('\s+|,', computer_ids)

        params = {"computer_ids": computer_ids, "group_ids": group_ids}

        payload = self.setup_scan_xml(scan_type, file_path, sha256, sha1, md5, description, scan_action)

        r = self._req.execute_call('post', url, verify_flag=False, headers=self._headers, params=params, data=payload)

        return r

    def move_endpoint(self, groupid, hardwarekey):
        """ Move an endpoint computer to a group.

        :param groupid: Id of group to move.
        :param hardwarekey: The computer’s hardware key.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["computers"])

        payload = json.dumps([{"group": {"id": groupid}, "hardwareKey": hardwarekey}])

        r = self._req.execute_call('patch', url, verify_flag=False, headers=self._headers, data=payload)

        return r

    def get_paginated_results(self, get_method, **params):
        """Get multiple pages of paginated data to get cumulmative result.

        :param: get_method: Reference to instance get method e.g. self.get_groups etc.
        :param: params: Parameters for get method .

        :return Result in json format.

        """

        rtn = get_method(**params)
        if "content" in rtn and len(rtn["content"]) > 0:
            # Set page index to 1 if parameter not set in ther action.
            page_index = params.get('pageindex', 1)
            items_per_page = rtn["size"]
            total_pages = rtn["totalPages"]
            max_count = rtn["totalElements"]


            # Get initial cumulative item count.
            current_item_count = rtn["numberOfElements"]

            if not current_item_count < items_per_page:
                while (max_count > current_item_count and total_pages > page_index):

                    remaining_count = max_count - current_item_count

                    page_index += 1
                    params["pageindex"] = page_index

                    # Re-run request and filter results with new offset set.
                    rtn_sub = get_method(**params)
                    rtn["content"].extend(rtn_sub["content"])
                    for v in ["firstPage", "lastPage", "numberOfElements"]:
                        rtn[v] = rtn_sub[v]
                    # Update initial cumulative item count.
                    current_item_count += rtn["numberOfElements"]

        return rtn