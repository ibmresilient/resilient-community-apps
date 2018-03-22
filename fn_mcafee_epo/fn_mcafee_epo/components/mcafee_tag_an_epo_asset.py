# -*- coding: utf-8 -*-
# Copyright IBM Corp. - Confidential Information
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests
from urlparse import urljoin
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

LOG = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_tag_an_epo_asset"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        try:
            self.options = opts.get("fn_mcafee_epo", {})
            url = self.options.get("epo_url")
            username = self.options.get("epo_username")
            password = self.options.get("epo_password")
            cert_trust = self.options.get("epo_trust_cert")
            if url is None:
                LOG.error("epo_url is not set. You must set this path to run this threat service")
                raise ValueError("epo_url is not set. You must set this path to run this threat service")

            if username is None:
                LOG.error("epo_username is not set. You must set this path to run this threat service")
                raise ValueError("epo_username is not set. You must set this path to run this threat service")

            if password is None:
                LOG.error("epo_password is not set. You must set this path to run this threat service")
                raise ValueError("epo_password is not set. You must set this path to run this threat service")

            if cert_trust is None:
                LOG.error("epo_trust_cert is not set. You must set this path to run this threat service")
                raise ValueError("epo_trust_cert is not set. You must set this path to run this threat service")

        except AttributeError:
            LOG.error("There is no [fn_mcafee_epo] section in the config file, "
                      "please set that by running resilient-circuits config -u")
            raise AttributeError("[fn_mcafee_epo] section is not set in the config file")

        # Create client
        self.client = Client(url, username, password, cert_trust)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_mcafee_epo", {})

    @function("mcafee_tag_an_epo_asset")
    def _mcafee_tag_an_epo_asset_function(self, event, *args, **kwargs):
        """Function: A function which takes two inputs:

mcafee_epo_system: Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO.
mcafee_epo_tag: A Tag managed on ePO.

Applies tag to the systems in ePO."""
        try:
            yield StatusMessage("Starting...")

            # Get the function parameters:
            mcafee_epo_systems = kwargs.get("mcafee_epo_systems")  # text
            mcafee_epo_tag = kwargs.get("mcafee_epo_tag")  # text

            LOG.info("mcafee_epo_systems: %s", mcafee_epo_systems)
            LOG.info("mcafee_epo_tag: %s", mcafee_epo_tag)
            params = {}
            params["names"] = mcafee_epo_systems
            params["tagName"] = mcafee_epo_tag

            response = self.client("system.applyTag", params)
            status_code = response.status_code
            content = response.text

            if not status_code < 300 and content.startswith('OK'):
                yield FunctionError

            yield StatusMessage("Tag Applied...")

            # Produce a FunctionResult with the results
            yield FunctionResult(content)
        except Exception:
            yield FunctionError()


class Client:

    def __init__(self, url, username, password, trust_cert):
        self.url = url
        self.username = username
        self.password = password
        self.trust_cert = trust_cert
        self._session = requests.Session()

    def _request(self, command_name, **kwargs):
        kwargs.setdefault('auth', (self.username, self.password))
        params = kwargs.setdefault('params', {})
        # Set output default to be json
        params.setdefault(':output', 'json')
        url = urljoin(self.url, 'remote/{}'.format(command_name))

        # Default to trusting cert
        trust_cert = True
        if self.trust_cert == "true":
            trust_cert = True
        elif self.trust_cert == "false":
            trust_cert = False

        # Make request
        r = self._session.get(url, verify=trust_cert, **kwargs)
        return r

    def __call__(self, command_name, params, *args, **kwargs):

        return self._request(command_name, params=params)
