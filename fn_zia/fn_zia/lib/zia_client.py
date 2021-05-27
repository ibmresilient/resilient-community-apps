# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Zia client class class for SOAR app supporting Zscalar Internet Access """
import logging
import json
import re
from .auth import Auth

LOG = logging.getLogger(__name__)


class ZiaClient(Auth):
    """ Class to support Zscaler Internet Access (Zia) api.

    """
    def __init__(self, opts, fn_opts):
        """ Class constructor.

        :param opts: Resilient options dict.
        :param fn_opts: Function specific options dict.

        """
        if not isinstance(opts, dict) and not opts:
            raise ValueError("The 'opts' parameter is not set correctly.")
        if not isinstance(fn_opts, dict) and not fn_opts:
            raise ValueError("The 'fn_opts' parameter is not set correctly.")
        self.api_base_url = fn_opts.get("zia_api_base_url")
        # Define api endpoints
        self._endpoints = {
            # Block lists
            "blocklist":        "/".join([self.api_base_url, "security/advanced"]),
            "blocklist_action": "/".join([self.api_base_url, "security/advanced/blacklistUrls?action={}"]),            # Allow lists
            # Allow lists
            "allowlist":        "/".join([self.api_base_url, "security"]),
            # Custom lists/URL categories
            "categories":       "/".join([self.api_base_url, "urlCategories{}"]),
            "url_lookup":       "/".join([self.api_base_url, "urlLookup"]),
            # Sandbox
            "sandbox_report":       "/".join([self.api_base_url, "sandbox/report/{}"]),
            # Activation
            "activate":         "/".join([self.api_base_url, "status/activate"]),
        }
        super(ZiaClient, self).__init__(opts, fn_opts)

    def _perform_method(self, method, uri, **kwargs):
        """Handle requests to zia endpoints .

        :param method: Request method such as "get","post", "put"
        :param uri: The uri of the request.
        :param kwargs: Can include request parameter dicts such as headers, data etc.
        :return res: Parsed response
        """
        result = None

        res = self._req.execute_call_v2(method, uri, proxies=self.proxies, **kwargs)

        if res.content:
            try:
                result = res.json()
            except ValueError:
                # Default response likely not in json format just return content as is.
                #return res.content
                result = res.content
        else:
            result = {"status": "OK"}

        return result

    def get_blocklist_urls(self):
        """Get a list of blocklisted URLs.

        The URLs can be either a url or ip address.

        See following for url guidelines
        https://help.zscaler.com/zia/url-format-guidelines

        return res: Parsed response
        """
        uri = self._endpoints["blocklist"]
        res = self._perform_method("get", uri, headers=self._headers)

        return res

    def get_allowlist_urls(self):
        """Get a list of allowlisted URLs.

        The URLs can be either a url or ip address.

        See following for url guidelines
        https://help.zscaler.com/zia/url-format-guidelines

        return res: Parsed response
        """
        uri = self._endpoints["allowlist"]
        res = self._perform_method("get", uri, headers=self._headers)

        return res

    def blocklist_action(self, blocklisturls=None, action=None):
        """ Perform an add or remove action on a list of URLs to the blocklist.

        The URLs can be either urls or ip addresses.
        Valid actions are "ADD_TO_LIST" and "REMOVE_FROM_LIST".
        See following for url guidelines
        https://help.zscaler.com/zia/url-format-guidelines

        :param blocklist_urls: List of urls and/or ipaddresses
        return res: Parsed response
        """
        if blocklisturls:
            blacklisturls = list(filter(None, re.split("\s+|,", blocklisturls)))

        payload = {
            "blacklistUrls": blacklisturls
        }

        uri = self._endpoints["blocklist_action"].format(action)
        res = self._perform_method("post", uri, data=json.dumps(payload), headers=self._headers)

        return res

    def allowlist_action(self, allowlisturls=None, action=None):
        """ Perform an add or remove action on a list of URLs to the allowlist.

        The URLs can be either urls or ip addresses.
        Valid actions are "ADD_TO_LIST" and "REMOVE_FROM_LIST".
        See following for url guidelines
        https://help.zscaler.com/zia/url-format-guidelines

        :param blocklist_urls: List of urls and/or ipaddresses
        return res: Parsed response
        """
        if allowlisturls:
            # Convert urls in comma-seperated string to a list.
            allowlisturls = list(filter(None, re.split("\s+|,", allowlisturls)))

        # Get result for current allowlist query.
        curr_allowlist_res = self.get_allowlist_urls()
        # Set current allow list.
        curr_allowlist = curr_allowlist_res["whitelistUrls"] if curr_allowlist_res else []

        if action == "ADD_TO_LIST":
            new_allowlist = curr_allowlist.copy()
            new_allowlist += [a for a in allowlisturls if a not in new_allowlist]
        elif action == "REMOVE_FROM_LIST":
            new_allowlist = [a for a in curr_allowlist if a not in allowlisturls]

        payload = {
            "whitelistUrls": new_allowlist
        }

        uri = self._endpoints["allowlist"]
        res = self._perform_method("put", uri, data=json.dumps(payload), headers=self._headers)

        return res

    def get_url_categories(self, custom_only, category_id):
        """Get a list of URL categories.

        :param custom_only: Custom categories only = 'true', all = 'false'
        :param category_id: Custom category ID
        return res: Normalized response
        """
        # Set default uri
        uri = self._endpoints["categories"].format('')
        params = {}

        if category_id:
            uri = "/".join([uri, category_id])

        elif custom_only:
            params = {"customOnly": custom_only}

        res = self._perform_method("get", uri, headers=self._headers, params=params)

        # Normalize response dict to a list.
        return [res] if isinstance(res, dict) else res

    def add_url_category(self, urls=None, configured_name=None, custom_category=True,
                         super_category=None, keywords=None):
        """Add a new URL category with a list of urls.

        The URLs can be either a url or ip address.

        :param urls: Comma or newline seperated urls in string to add to new category
        :param configured_name: Name of new category
        :param custom_category: Custom categories = 'true'
        :param super_category: Name of super category
        :param keywords: Comma or newline seperated keywords in string to add to new category
        return res: Response
        """
        if urls:
            # Convert urls in comma or newline seperated string to a list.
            urls = list(filter(None, re.split(r"\s+|,|\n", urls)))

        if keywords:
            # Convert keywords in comma or newline seperated string to a list.
            keywords = list(filter(None, re.split(r"\s+|,|\n", keywords)))

        payload = {
            "configuredName": configured_name,
            "customCategory": custom_category,
            "superCategory": super_category,
            "keywords": keywords,
            "urls": urls
        }

        uri = self._endpoints["categories"].format('')
        res = self._perform_method("post", uri, data=json.dumps(payload), headers=self._headers)

        return res

    def category_action(self, category_id=None, configured_name=None, urls=None, action=None):
        """ Perform an add or remove action on a list of URLs to a custom category.

        The URLs can be either urls or ip addresses.
        Valid actions are "ADD_TO_LIST" and "REMOVE_FROM_LIST".
        See following for url guidelines
        https://help.zscaler.com/zia/url-format-guidelines

        :param category_id: Custom category ID
        :param configured_name: Name of category
        :param urls: List of urls and/or ipaddresses
        :param action: Action name "ADD_TO_LIST" and "REMOVE_FROM_LIST"
        return res: Response
        """
        if urls:
            # Convert urls in comma-seperated string to a list.
            urls = list(filter(None, re.split(r"\s+|,|\n", urls)))

        params = {
            "action": action
        }

        payload = {
            "urls": urls,
            "configuredName": configured_name
        }

        uri = "/".join([self._endpoints["categories"].format(''), category_id])
        res = self._perform_method("put", uri, params=params, data=json.dumps(payload), headers=self._headers)

        return res

    def url_lookup(self, urls=None):
        """ Lookup categorization  on a list of URLs.

        The URLs can be either urls or ip addresses.
        See following for url guidelines
        https://help.zscaler.com/zia/url-format-guidelines

        :param urls: Comma or newline seperated string of urls and/or ipaddresses
        return res: Response
        """
        if urls:
            # Convert urls in comma or newline seperated string to a list.
            urls = list(filter(None, re.split(r"\s+|,|\n", urls)))

        payload = urls

        uri = self._endpoints["url_lookup"]
        res = self._perform_method("post", uri, headers=self._headers, data=json.dumps(payload))

        # Normalize response dict to a list.
        return res

    def activate(self):
        """Activate configuration.

        return res: Response
        """
        uri = self._endpoints["activate"]
        res = self._perform_method("post", uri, headers=self._headers)

        return res

    def get_sandbox_report(self, md5, full=False):
        """ Get a full (i.e., complete) or summary detail report for an MD5 hash of a
        file that was analyzed by the Sandbox.

        :param md5: MD5 hash value
        :param full: Boolean true if a full report required
        return res: Response
        """
        params = {}
        if full:
            params.update({
                "details": "full"
            })

        uri = self._endpoints["sandbox_report"].format(md5)
        res = self._perform_method("get", uri, params=params, headers=self._headers)

        return res
