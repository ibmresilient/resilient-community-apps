# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long

""" Class for SOAR Functions supporting REST API client for Symantec SEP  """
from logging import getLogger
from re import split
from json import dumps
from textwrap import dedent
from ast import literal_eval

from fn_sep.lib.requests_sep import RequestsSep
from urllib.parse import urljoin

LOG = getLogger(__name__)

HASH_LENGTH_TO_TYPE = {
    64: "SHA256",
    40: "SHA-1",
    32: "MD5"
}
PACKAGE_NAME = "fn_sep"

DEFAULT_COMPUTERS = 10000 # arbitrary large value for number of endpoints to return

class Sepclient(object):
    """ Client class used to expose Symantec SEP Rest API. """
    def __init__(self, options, function_params=None):
        """ Class constructor"""
        self.host = options.get("sep_host")
        self.port = options.get("sep_port")
        self.base_path = options.get("sep_base_path")
        self.auth_path = options.get("sep_auth_path")
        self.username = options.get("sep_username")
        self.password = options.get("sep_password")
        self.domain = options.get("sep_domain")
        self.base_url = f"https://{self.host}:{self.port}"
        self.auth_url = self.base_url + self.auth_path
        if options.get("sep_query_limit") is not None:
            self.query_limit = int(options.get("sep_query_limit"))
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
            "fingerprints_list":                        self.base_path+"/policy-objects/fingerprints",
            "fingerprints_list_by_id":                  self.base_path+"/policy-objects/fingerprints/{}",
            "assign_fingerprint_list_to_group":         self.base_path+"/groups/{0}/system-lockdown/fingerprints/{1}"
        }
        self._req = RequestsSep(options, function_params)
        self._headers = {"content-type": "application/json", "Authorization": f"Bearer {self._get_token()}"}

    @staticmethod
    def get_hash_type(hash):
        """ Find hash type from size for sha256, sha-1 and md5.
        :param hash: The hash value.
        :return: Hash type info.
        """
        if len(hash) in HASH_LENGTH_TO_TYPE:
            return HASH_LENGTH_TO_TYPE[len(hash)]
        else:
            raise ValueError(f'Unknown hash type for value: {hash}')

    @staticmethod
    def setup_scan_xml(scan_type, file_path, sha256, sha1, md5, description, scan_action):
        """ Set up xml payload for an eoc or remediation scan.

        :param scan_type: Type of scan e.g. 'QUICK_SCAN', 'FULL_SCAN'.
        :param file_path: Can be a file path or name or None value. (Optional parameter)
        :param sha256: Sha256 hash value. (Optional parameter)
        :param sha1: Sha1 hash value. (Optional parameter)
        :param md5: Sha1 hash value. (Optional parameter)
        :param description: Description of scan.
        :param scan_action: Used to set action for remediation scans.
        :return An xml payload string.
        """
        action = ''
        if scan_action and scan_action.lower() == "remediate":
            action = "<RemediationAction>REMEDIATE</RemediationAction>"

        # Reset 'None' values to blanks'
        file_path = '' if not file_path else file_path
        hvs = ['' if not hv else hv for hv in [sha256, sha1, md5]]

        scan_xml = dedent(f"""
            <EOC creator="SOAR" version="" id="">
                <DataSource name="" id="" version="" />
                <ScanType>{scan_type.upper()}</ScanType>
                {action}
                <Threat category="" type="" severity="" time="">
                    <Description>{description}</Description>
                    <Attacker></Attacker>
                </Threat>
                <Activity>
                    <OS id="1" name="" version="" patch="">
                        <Process></Process>
                        <Files>
                            <File name="{file_path or 'SHA256'}" action="create">
                                <Hash name="SHA256" value="{hvs[0]}" />
                            </File>
                            <File name="{file_path or 'SHA1'}" action="create">
                                <Hash name="SHA1" value="{hvs[1]}" />
                            </File>
                            <File name="{file_path or 'MD5'}" action="create">
                                <Hash name="MD5" value="{hvs[2]}" />
                            </File>
                        </Files>
                        <Registry></Registry>
                        <Network></Network>
                    </OS>
                </Activity>
            </EOC>""")

        return scan_xml.encode('utf-8')

    def _get_token(self):
        """Get the authorization token to be used in subsequent requests.
        :return: Token
        """
        r = self._req.execute_call("POST",
                                   urljoin(self.base_url, self._endpoints.get("auth")),
                                   verify=False,
                                   json={"username": self.username, "password": self.password, "domain": self.domain})

        return r.get("token")

    def get_version(self):
        """Get version of SEPM.
        :return: Result in json format
        """
        return self._req.execute_call("GET",
                                      urljoin(self.base_url, self._endpoints.get("version")),
                                      verify=False,
                                      headers=self._headers)

    def get_domains(self):
        """Get a list of domains.
        :return Result in json format.
        """
        return self._req.execute_call("GET", urljoin(self.base_url,
                                                     self._endpoints.get("domains")),
                                                     verify=False,
                                                     headers=self._headers)

    def get_computers(self, computername=None, domain=None, lastupdate=None, order=None, os=None, pageindex=None,
                      pagesize=DEFAULT_COMPUTERS, sort=None, status=None, status_details=None, matching_endpoint_ids=None):
        """Get a list of computers. The parameters are all optional the default is to return results for all computers/
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
        :param matching_endpoint_ids: Return matching endpoint ids in scan. Used by the integration, Not in REST call signature.
        :return Result in json format.
        """
        params = {"computerName": computername, "domain": domain, "lastUpdate": lastupdate, "order": order, "os": os,
                  "pageIndex": pageindex, "pageSize": pagesize, "sort": sort}

        return self._req.execute_call("GET",
                                      urljoin(self.base_url, self._endpoints.get("computers")),
                                      verify=False,
                                      headers=self._headers,
                                      params=params)

    def get_clients_online_status(self):
        """Gets a list and count of the online and offline clients.
        :return Result in json format.
        """
        return self._req.execute_call("GET",
                                      urljoin(self.base_url, self._endpoints.get("clients_online_status")),
                                      verify=False,
                                      headers=self._headers)

    def get_groups(self, domain=None, fullpathname=None, mode=None, order=None, os=None, pageindex=None,
                   pagesize=None, sort=None):
        """Get a list of groups. The parameters are all optional the default is to return results for all groups.

        :param domain: The SEP domain name.
        :param fullpathname: The full path name of the group.
        :param mode: The presentation mode for the results, as a list (default) or as a tree.
        :param order: Specifies whether the results are in ascending order (ASC) or descending order (DESC).
        :param pageindex: The index page that is used for the returned results. The default page index is 1.
        :param pagesize: The number of results to include on each page. The default is 20.
        :param sort: The column by which the results are sorted.
        :return Result in json format.
        """
        params = {"domain": domain, "fullPathName": fullpathname, "order": order, "pageIndex": pageindex,
                  "pageSize": pagesize, "sort": sort}
        return self._req.execute_call("GET",
                                      urljoin(self.base_url, self._endpoints.get("groups")),
                                      verify=False,
                                      headers=self._headers,
                                      params=params)

    def get_fingerprint_list(self, fingerprintlist_id=None, domainid=None, fingerprintlist_name=None):
        """ Gets the fingerprint list for a specified name as a set of hash values. Either parameter fingerprintlist_id
        or fingerprintlist_name can be used but not at the same time.

        :param fingerprintlist_id: Id of fingerprint list.
        :param domainid: If present, get policies from this domain. Otherwise, get policies from the logged-on domain.
        :param fingerprintlist_name: Name of a fingerprint list.
        :return Result in json format.
        """
        if not fingerprintlist_id:
            url = urljoin(self.base_url, self._endpoints.get("fingerprints_list"))
        else:
            url = urljoin(self.base_url, self._endpoints.get("fingerprints_list_by_id")).format(fingerprintlist_id)

        params = {"domainId": domainid, "name": fingerprintlist_name}
        result = self._req.execute_call('get', url, verify=False, headers=self._headers, params=params)
        # Check if error message for using V2 api was returned.
        if isinstance(result, dict) and result.get("errorMessage") and 'This FingerprintList is not supported by V1, please try V2!' in result.get("errorMessage"):
            # Edit url to use v2 api call
            result = self._req.execute_call('get', url.replace("/v1/", "/v2/"), verify=False, headers=self._headers, params=params)
        return result

    def delete_fingerprint_list(self, fingerprintlist_id=None):
        """ Delete a file fingerprint list.

        :param fingerprintlist_id: The fingerprint list id.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints.get("fingerprints_list_by_id")).format(fingerprintlist_id)

        result = self._req.execute_call('delete', url, verify=False, headers=self._headers)
        # Check if error message for using V2 api was returned.
        if isinstance(result, dict) and result.get("errorMessage") and 'This FingerprintList is not supported by V1, please try V2!' in result.get("errorMessage"):
            # Edit url to use v2 api call
            result = self._req.execute_call('delete', url.replace("/v1/", "/v2/"), verify=False, headers=self._headers)
        return result

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
        url = urljoin(self.base_url, self._endpoints.get("fingerprints_list"))

        hash_type = "MD5" if not hash_value else self.get_hash_type(hash_value)

        if not hash_value:
            hash_value = ''

        if hash_type not in ["MD5", "SHA256"]:
            raise ValueError(f"Unsupported hash type for value: {hash_value}")

        payload = dumps({"name": fingerprintlist_name, "description": description, "domainId": domainid, "hashType": hash_type,
                              "data": [hash_value]})

        result =  self._req.execute_call('post', url, verify=False, headers=self._headers, data=payload)
        # Check if error message for using V2 api was returned.
        if isinstance(result, dict) and result.get("errorMessage") and 'This FingerprintList is not supported by V1, please try V2!' in result.get("errorMessage"):
            # Edit url to use v2 api call
            result = self._req.execute_call('post', url.replace("/v1/", "/v2/"), verify=False, headers=self._headers, data=payload)
        return result

    def update_fingerprint_list(self, fingerprintlist_id=None, fingerprintlist_name=None, description=None, domainid=None, hash_value=None):
        """ Update fingerprint list.

        :param fingerprintlist_id: The fingerprint list id.
        :param fingerprintlist_name: The name of the fingerprint list.
        :param description: The fingerprint file’s description.
        :param domainid: If present, get policies from this domain. Otherwise, get policies from the logged-on domain.
        :param hash_value: The hash or hashes to update the given fingerprint list. Either MD5 or SHA256 hash type.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints.get("fingerprints_list_by_id")).format(fingerprintlist_id)

        hash_values = []
        if hash_value:
            # Check if using the new format. A list of dictionaries.
            if isinstance(literal_eval(hash_value)[0], dict):
                payload = dumps({"name": fingerprintlist_name, "description": description, "domainId": domainid,
                            "data": literal_eval(hash_value)})
                # Edit url to use v2 api call
                result = self._req.execute_call('post', url.replace("/v1/", "/v2/"), verify=False, headers=self._headers, data=payload)
            else:
                hash_values = split('\s+|,', hash_value)

                hash_type = self.get_hash_type(hash_values[0])

                if hash_type not in ["MD5", "SHA256"]:
                    raise ValueError(f"Unsupported hash type for value: {hash_value}")

                payload = dumps({"name": fingerprintlist_name, "description": description, "domainId": domainid,
                                    "hashType": hash_type, "data": hash_values})
                result = self._req.execute_call('post', url, verify=False, headers=self._headers, data=payload)
        return result

    def assign_fingerprint_list_to_group(self, groupid, fingerprintlist_id=None):
        """ Assign a fingerprint list to a group for lockdown purposes.

        :param group_id: The group id to assign fingerprint id.
        :param fingerprintlist_id: The fingerprint list id.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints.get("assign_fingerprint_list_to_group"))\
            .format(groupid, fingerprintlist_id)

        payload = dumps({"group_id": groupid, "fingerprint_id": fingerprintlist_id})

        return self._req.execute_call('PUT', url, verify=False, headers=self._headers, data=payload)

    def upload_file(self, file_path=None, computer_ids=None, sha256=None, md5=None, sha1=None, source=None):
        """Upload a suspicious file to the SEPM server.

        :param file_path: The file path of the suspicious file.
        :param computer_ids: List of computer ids.
        :param sha256: The SHA256 hash value of the suspicious file.
        :param md5: The MD5 hash value of the suspicious file (optional).
        :param sha1: The SHA1 hash value of the suspicious file (optional).
        :param source: Source of file to upload can be FILESYSTEM (default), QUARANTINE, or BOTH.
        :return Result in json format.
        """
        if computer_ids:
            computer_ids = split('\s+|,', computer_ids)

        params = {"file_path": file_path, "computer_ids": computer_ids, "source": source}
        if sha256:
            params["sha256"] = sha256
        if md5:
            params["md5"] = md5
        if sha1:
            params["sha1"] = sha1

        return self._req.execute_call('POST',
                                      urljoin(self.base_url, self._endpoints.get("upload_file")),
                                      verify=False, headers=self._headers, params=params)

    def get_command_status(self, commandid=None, order=None, pageindex=None, pagesize=None, sort=None, status_type=None,
                           matching_endpoint_ids=None, incident_id=None, scan_date=None):
        """Get command status from command id.

        :param commandid: The command id.
        :param order: Specifies whether the results are in ascending order (ASC) or descending order (DESC).
        :param pageindex: The index page that is used for the returned results. The default page index is 1.
        :param pagesize: The number of results to include on each page. The default is 20.
        :param sort: The column by which the results are sorted.
        :param status_type: The type of command status requested. Used by the integration, Not in REST call signature.
        :param incident_id: SOAR incident id. Used by the integration, Not in REST call signature.
        :param scan_date: The datetime when scan was initiated. Used by the integration, Not in REST call signature.
        :param matching_endpoint_ids: Return matching endpoint ids in scan. Used by the integration, Not in REST call signature.
        :return Result in json format.
        """
        return self._req.execute_call('get',
                                      urljoin(self.base_url, self._endpoints.get("command_status")).format(commandid),
                                      verify=False,
                                      headers=self._headers,
                                      params={"order": order, "pageIndex": pageindex, "pageSize": pagesize, "sort": sort})

    def get_file_content(self, file_id=None):
        """Get the details of a binary file, such as the checksum and the file size.
        :param file_id: The file ID from which to get detailed information.
        """
        headers = self._headers
        headers.update({"content-type":"application/json; charset=UTF-8", "Accept-Encoding": "gzip, deflate, compress"})
        return self._req.execute_call('GET',
                                      urljoin(self.base_url, self._endpoints.get("file_content")).format(file_id),
                                      verify=False,
                                      headers=headers,
                                      stream=True)

    def quarantine_endpoints(self, group_ids=None, computer_ids=None, undo=None, hardware_keys=None):
        """Quarantine an endpoint in the SEP environment my moving to a quarantine group.

        :param group_ids: Id of quarantine group.
        :param computer_ids: List of computer ids.
        :param undo: Boolean value set to unquarantine endpoint.
        :return Result in json format.
        """
        if group_ids:
            group_ids = split('\s+|,', group_ids)
        if computer_ids:
            computer_ids = split('\s+|,', computer_ids)
        if hardware_keys:
            hardware_keys = split('\s+|,', hardware_keys)

        params = {"computer_ids": computer_ids, "group_ids": group_ids, "hardware_ids": hardware_keys}

        if undo:
            params.update({"undo": undo})

        return self._req.execute_call('POST',
                                      urljoin(self.base_url, self._endpoints.get("quarantine_endpoints")),
                                      verify=False, headers=self._headers, params=params)

    def scan_endpoints(self, computer_ids=None, group_ids=None, scan_type=None, file_path=None, sha256=None,
                       sha1=None, md5=None, description=None, scan_action=None):
        """Run an 'eoc' or "Remediation" scan on endpoint(s).

        :param computer_ids: List of computer ids.
        :param group_ids: List of groups ids.
        :param scan_type: Select value for scan type e.g. "FULL_SCAN".
        :param file_path: File name or path to be scanned.
        :param sha256: Sha256 hash value.
        :param sha1: Sha1 hash value.
        :param md5: Sha1 hash value.
        :param description: Description for scan.
        :param scan_action: Perform an action e.g 'remediation' with the scan.
        :return Result in json format.
        """
        if group_ids:
            group_ids = split('\s+|,', group_ids)

        if computer_ids:
            computer_ids = split('\s+|,', computer_ids)

        payload = self.setup_scan_xml(scan_type, file_path, sha256, sha1, md5, description, scan_action)

        return self._req.execute_call('POST',
                                      urljoin(self.base_url, self._endpoints.get("scan_endpoints")),
                                      verify=False, headers=self._headers,
                                      params={"computer_ids": computer_ids, "group_ids": group_ids},
                                      data=payload)

    def move_endpoint(self, groupid, hardwarekey):
        """ Move an endpoint computer to a group.

        :param groupid: Id of group to move.
        :param hardwarekey: The computer’s hardware key.
        :return Result in json format.
        """
        return self._req.execute_call('PATCH',
                                      urljoin(self.base_url, self._endpoints.get("computers")),
                                      verify=False, headers=self._headers,
                                      data=dumps([{"group": {"id": groupid}, "hardwareKey": hardwarekey}]))

    def get_paginated_results(self, get_method, **params):
        """Get multiple pages of paginated data to get cumulative result.

        :param: get_method: Reference to instance get method e.g. self.get_groups etc.
        :return Result in json format.
        """
        rtn = get_method(**params)
        if "content" in rtn and rtn.get("content"):
            # Set page index to 1 if parameter not set in their action.
            page_index = params.get("pageindex") or 1
            items_per_page = rtn.get("size")
            total_pages = rtn.get("totalPages")
            max_count = rtn.get("totalElements")

            # Get initial cumulative item count.
            current_item_count = rtn.get("numberOfElements")

            if current_item_count >= items_per_page:
                while (max_count > current_item_count and total_pages > page_index):
                    page_index += 1
                    params["pageindex"] = page_index

                    # Re-run request and filter results with new page index set.
                    rtn_sub = get_method(**params)
                    rtn["content"].extend(rtn_sub.get("content"))
                    for v in ["firstPage", "lastPage", "numberOfElements"]:
                        rtn[v] = rtn_sub.get(v)
                    # Update initial cumulative item count.
                    current_item_count += rtn.get("numberOfElements")

        return rtn
