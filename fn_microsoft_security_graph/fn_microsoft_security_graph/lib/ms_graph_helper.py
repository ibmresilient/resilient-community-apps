# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
from logging import getLogger
from resilient_lib import OAuth2ClientCredentialsSession
from resilient_lib.components.integration_errors import IntegrationError
from resilient_lib import validate_fields, RequestsCommon

LOG = getLogger(__name__)
DEFAULT_SCOPE = 'https://graph.microsoft.com/.default'

class MSGraphHelper(object):
    """
    Helper object MSGraphHelper.
    """
    def __init__(self, ms_graph_token_url, ms_graph_url, tenant_id, client_id, client_secret, scope=DEFAULT_SCOPE, proxies=None):
        self.ms_graph_token_url = ms_graph_token_url.format(tenant=tenant_id)
        self.ms_graph_url = ms_graph_url
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.proxies = proxies
        self.scope = scope
        self.ms_graph_session = self.authenticate()

    @staticmethod
    def check_ms_graph_response_code(status_code):
        """
        Check that the request status code: raise an integration error if great than 300 and code is "not found"
        :param status_code: request statues code
        :return:
        """
        if status_code >= 300 and status_code != 404:
            raise IntegrationError("Invalid response from Microsoft Graph API call.")

    def authenticate(self):
        """
        Authenticate and get oauth2 token for the session.
        """
        return OAuth2ClientCredentialsSession(url=self.ms_graph_token_url,
                                              client_id=self.client_id,
                                              client_secret=self.client_secret,
                                              scope=self.scope,
                                              proxies=self.proxies)

def connect_MSGraph(opts, reload=False):
    options = opts.get("fn_microsoft_security_graph", {})

    if reload:
        return MSGraphHelper(options.get("tenant_id"),
                             options.get("client_id"),
                             options.get("client_secret"),
                             options.get("scope", DEFAULT_SCOPE))
    else:
        # Validate required fields in app.config are set
        validate_fields(["microsoft_graph_token_url", "microsoft_graph_url", "tenant_id", "client_id", "client_secret"], options)

        return MSGraphHelper(options.get("microsoft_graph_token_url"),
                             options.get("microsoft_graph_url"),
                             options.get("tenant_id"),
                             options.get("client_id"),
                             options.get("client_secret"),
                             options.get("scope", DEFAULT_SCOPE),
                             RequestsCommon(opts, options).get_proxies())
