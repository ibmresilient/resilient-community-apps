# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

""" Class for Resilient circuits Functions supporting REST API client for Cisco AMP for endpoints  """
import logging
import re
import json
from fn_sep.lib.helpers import setup_eoc_command
from fn_sep.lib.requests_sep import RequestsSep

try:
    from urllib.parse import urljoin
except:
    from urlparse import urljoin

LOG = logging.getLogger(__name__)
SEP_LIMIT_DEFAULT = 1000

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
        self.ws_base_path = options.get("ws_base_path")
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
            "auth":                     self.auth_path,
            "version":                  self.base_path+"/version",
            "domains":                  self.base_path+"/domains",
            "computers":                self.base_path+"/computers",
            "groups":                   self.base_path+"/groups",
            "upload_file":              self.base_path+"/command-queue/files",
            "file_details":             self.base_path+"/command-queue/file/{}/details",
            "quarantine_endpoints":     self.base_path+"command-queue/quarantine",
            "policies":                 self.base_path+"/policies/summary",
            "policies_by_type":         self.base_path+"/policies/summary/{}",
            "scan_endpoints":           self.base_path+"/command-queue/eoc",
            "fingerprints_list":        self.base_path+"/policy-objects/fingerprints",
            "fingerprints_list_by_id":  self.base_path+"/policy-objects/fingerprints/{}"
         }
        self._req = RequestsSep(options, function_params)
        self._headers = {"content-type": "application/json", "Authorization": "Bearer {0}".format(self._get_token())}

    def _get_token(self):
        """Get the authorization token to be used in subsequent requests.

        :return: Token
        """
        url = urljoin(self.base_url, self._endpoints["auth"])
        data = {"username": self.username, "password": self.password, "domain": self.domain}
        r = self._req.execute_call('post', url, verify_flag=False, payload=data)
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
                      pagesize=None, sort=None):
        """Get a list of computers. The paramaters are all optiional the default is to return results for all computers/
        endpoints.

        :param computername: The host name of computer. Wild card is supported as '*'.
        :param domain: The domain from which to get computer information.
        :param lastupdate: Indicates when a computer last updated its status. The default value of 0 gets all the results.
        :param order: Specifies whether the results are in ascending order (ASC) or descending order (DESC).
        :param os: The list of OS to filter.
        :param pageindex: The index page that is used for the returned results. The default page index is 1.
        :param pagesize: The number of results to include on each page. The default is 20.
        :param sort: The column by which the results are sorted.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["computers"])
        params = {"computerName": computername, "domain": domain, "lastUpdate": lastupdate, "order":order, "os":os,
                  "pageIndex": pageindex, "pageSize": pagesize, "sort": sort}
        r = self._req.execute_call('get', url, verify_flag=False, headers=self._headers, params=params)
        return r

    def get_groups(self, domain=None, fullpathname=None, mode=None, order=None, os=None, pageindex=None,
                      pagesize=None, sort=None):
        """Get a list of groups. The paramaters are all optional the default is to return results for all groups.

        :param domain: The file path of the suspicious file.
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

        :param policy_type: If present gets a summary for all the policies of this type..
        :param domainid: If present, get policies from this domain. Otherwise, get policies from the logged-on domain.
        :return Result in json format.
        """
        if policy_type is None:
            url = urljoin(self.base_url, self._endpoints["policies"])
        else:
            url = urljoin(self.base_url, self._endpoints["policies_by_type"]).format(policy_type["name"])
        params = {"policy_type": policy_type["name"], "domainId": domainid}
        r = self._req.execute_call('get', url, verify_flag=False, headers=self._headers, params=params)

        return r

    def get_fingerprint_list(self, id=None, domainid=None, name=None):
        """ Gets the file fingerprint list for a specified name as a set of hash values.

        :param id:
        :param domainid: If present, get policies from this domain. Otherwise, get policies from the logged-on domain.
        :param policy_type: If present gets a summary for all the policies of this type..
        :return Result in json format.
        """
        if id is None:
            url = urljoin(self.base_url, self._endpoints["fingerprints_list"])
        else:
            url = urljoin(self.base_url, self._endpoints["fingerprints_list_by_id"]).format(id)

        params = {"domainId": domainid, "name": name}
        r = self._req.execute_call('get', url, verify_flag=False, headers=self._headers, params=params)

        return r

    def add_fingerprint_list(self, data=None, description=None, domainid=None, hashtype=None, name=None):
        """ Add a blacklist as a file fingerprint list.

        :param data: The blacklist file’s data.
        :param description: The blacklist file’s description.
        :param domainid: If present, get policies from this domain. Otherwise, get policies from the logged-on domain.
        :param hashtype: The blacklist file’s hash type. Possible values are MD5 or SHA256.
        :param name: The blacklist file’s ID. This field is not required at the blacklist file’s creation, but when the blacklist file is updated, this field is required.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["fingerprints_list"])

        payload = json.dumps({"data": [{"name":"myEnterprise", "departments":"HR"}], "description": description, "domainId": domainid, "hashType": hashtype["name"]})
        r = self._req.execute_call('post', url, verify_flag=False, headers=self._headers, payload=payload)

    def update_fingerprint_list(self, id=None, data=None, description=None, domainid=None, hashtype=None, name=None):
        """ Update ingerprint list.

        :param data: The blacklist file’s data.
        :param description: The blacklist file’s description.
        :param domainid: If present, get policies from this domain. Otherwise, get policies from the logged-on domain.
        :param hashtype: The blacklist file’s hash type. Possible values are MD5 or SHA256.
        :param name: The blacklist file’s ID. This field is not required at the blacklist file’s creation, but when the blacklist file is updated, this field is required.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["fingerprints_list_byid"]).format(id)

        payload = {"data": data, "description": description, "domainId": domainid, "hashType": hashtype["name"],
                   "name": name}
        r = self._req.execute_call('get', url, verify_flag=False, headers=self._headers, payload=payload)

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
        params = {"file_path": file_path, "computer_ids": computer_ids, "sha256": sha256, "md5": md5, "sha1": sha1,
                  "source": source}
        r = self._req.execute_call('post', url, verify_flag=False, headers=self._headers, params=params)

        return r

    def get_file_details(self, file_id=None):
        """Get the details of a binary file, such as the checksum and the file size.

        :param file_id: The file ID from which to get detailed information.
        """
        url = urljoin(self.base_url, self._endpoints["file_details"]).format(file_id)

        r = self._req.execute_call('get', url, verify_flag=False, headers=self._headers)

        return r


    def quarantine_endpoints(self, group_ids=None, computer_ids=None, undo=None ):
        """Quarantine an endpoint in the SEP environment my moving to a quarantine group.

        :param group_ids: Id of quarntine group.
        :param computer_ids: List of computer ids.
        :param undo: Boolean value  set to unquarantine endpoint.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["quarantine_endpoints"])

        group_ids = re.split('\s+|,', group_ids)
        computer_ids = re.split('\s+|,', computer_ids)

        params = {"computer_ids": str(computer_ids), "group_ids": str(group_ids) }

        if undo is not None:
            params.update({"undo": undo})

        r = self._req.execute_call('post', url, verify_flag=False, headers=self._headers, params=params)

        return r

    def scan_endpoints(self, computer_ids=None, group_ids=None, scan_type=None, file_name=None, sha256=None,
                       description=None):
        """Run an 'Evidence of Compromise' scan on an endpoint.

        :param computer_ids: List of computer ids.
        :param group_ids: List of groups ids.
        :param scan_type: Select value for scan type e.g. "FULL_SCAN".
        :param file_name: File name to be scanned.
        :param sha_256: Sha256 of file.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["scan_endpoints"])
        if group_ids is not None:
            group_ids = re.split('\s+|,', group_ids)
        if computer_ids is not None:
            computer_ids = re.split('\s+|,', computer_ids)

        params = {"computer_ids": computer_ids, "group_ids": group_ids}
        payload = setup_eoc_command(scan_type["name"], file_name, sha256)

        r = self._req.execute_call('post', url, verify_flag=False, headers=self._headers, params=params, payload=payload)

        return r

    def move_client(self, group_id, hardwarekey):
        """ Move a clinet computer to a group

        :param group_id: Id of group to move.
        :param hardwarekey: The computer’s hardware key.
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["computers"])
        payload = json.dumps([{"group": {"id": group_id}, "hardwareKey": hardwarekey}])
        r = self._req.execute_call('patch', url, verify_flag=False, headers=self._headers, payload=payload)
        return r
