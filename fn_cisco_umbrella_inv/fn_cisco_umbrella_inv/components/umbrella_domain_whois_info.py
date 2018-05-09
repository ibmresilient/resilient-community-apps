# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run an Umbrella investigate Query - WHOIS information for a Domain against a
Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
import json
import logging
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import init_env, validate_opts, validate_params, process_params, omit_params, \
    is_none


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_domain_whois_info' of package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup and takes the following parameters:
            umbinv_emails, umbinv_nameservers, umbinv_domain, umbinv_limit, umbinv_sortby, umbinv_offset
    An example of a set of query parameter might look like the following:

            umbinv_emails = None
            umbinv_nameservers = None
            umbinv_domain = artifact.value
            umbinv_limit = 2
            umbinv_sortby = "created"
            umbinv_offset = 0

    The Investigate Query will executs a REST call agaist the Cisco Umbrell Investigate server and returns a result in
    JSON format similar to the following.


    The Investigate Query will executs a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.

        {'domain': 'cisco.com',
         'query_execution_time': '2018-04-27 10:01:23',
         'domain_whois': {u'registrantFaxExt': None, u'administrativeContactPostalCode': u'95134',
                          u'zoneContactCity': None, u'addresses': [u'170 w. tasman drive', u'170 west tasman drive'],
                          u'billingContactState': None, u'technicalContactStreet': [u'170 w. tasman drive'],
                          u'auditUpdatedDate': u'2018-04-22 20:55:22.000 UTC', u'administrativeContactCity': u'San Jose',
                          u'administrativeContactEmail': u'infosec@cisco.com', u'technicalContactFax': u'14085267373',
                          u'technicalContactTelephone': u'14085279223', u'billingContactEmail': None,
                          u'technicalContactPostalCode': u'95134', u'registrantOrganization': u'Cisco Technology Inc.',
                          u'zoneContactPostalCode': None, u'registrantState': u'CA',
                          u'administrativeContactName': u'Info Sec', u'billingContactFaxExt': None,
                          u'billingContactCity': None, u'technicalContactEmail': u'dns-info@CISCO.COM',
                          u'registrantCountry': u'UNITED STATES', u'technicalContactFaxExt': None,
                          u'registrantName': u'Info Sec', u'registrantEmail': u'infosec@cisco.com',
                          u'billingContactCountry': None, u'billingContactName': None,
                          u'registrarName': u'CSC CORPORATE DOMAINS, INC.', u'technicalContactTelephoneExt': None,
                          u'administrativeContactFax': None, u'zoneContactFax': None, u'zoneContactFaxExt': None,
                          u'registrantCity': u'San Jose', u'administrativeContactTelephoneExt': None,
                          u'status': [u'clientTransferProhibited serverDeleteProhibited serverTransferProhibited serverUpdateProhibited'],
                          u'updated': u'2017-05-11', u'expires': u'2018-05-15', u'whoisServers': u'whois.corporatedomains.com',
                          u'zoneContactEmail': None, u'technicalContactState': u'CA',
                          u'nameServers': [u'ns1.cisco.com', u'ns2.cisco.com', u'ns3.cisco.com'], u'timestamp': None,
                          u'recordExpired': False, u'registrantFax': u'14085264575',
                          u'administrativeContactStreet': [u'170 west tasman drive'],
                          u'registrantTelephoneExt': None, u'billingContactFax': None,
                          u'technicalContactOrganization': u'Cisco Technology Inc.',
                          u'administrativeContactState': u'CA', u'zoneContactOrganization': None,
                          u'billingContactPostalCode': None, u'zoneContactStreet': [],
                          u'zoneContactName': None, u'registrantPostalCode': u'95134',
                          u'billingContactTelephone': None, u'emails': [u'dns-info@cisco.com', u'infosec@cisco.com'],
                          u'registrantTelephone': u'14085273842', u'administrativeContactCountry': u'UNITED STATES',
                          u'technicalContactCity': u'San Jose', u'administrativeContactTelephone': u'14085273842',
                          u'created': u'1987-05-14', u'registrantStreet': [u'170 west tasman drive'],
                          u'domainName': u'cisco.com', u'technicalContactCountry': u'UNITED STATES',
                          u'billingContactStreet': [], u'timeOfLatestRealtimeCheck': 1524501072693, u'zoneContactState': None,
                          u'administrativeContactOrganization': u'Cisco Technology Inc.', u'administrativeContactFaxExt': None,
                          u'billingContactTelephoneExt': None, u'zoneContactTelephone': None, u'technicalContactName':
                          u'Network Services', u'zoneContactTelephoneExt': None, u'billingContactOrganization': None,
                          u'registrarIANAID': u'299', u'zoneContactCountry': None, u'hasRawText': True},
        }
    """
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cisco_umbrella_inv", {})
        validate_opts(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_umbrella_inv", {})
        validate_opts(self)

    @function("umbrella_domain_whois_info")
    def _umbrella_domain_whois_info_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate for Domain Whois info."""
        try:
            # Get the function parameters:
            umbinv_emails = kwargs.get("umbinv_emails")  # text
            umbinv_nameservers = kwargs.get("umbinv_nameservers")  # text
            umbinv_domain = kwargs.get("umbinv_domain")  # text
            umbinv_limit = kwargs.get("umbinv_limit")  # number
            umbinv_sortby = kwargs.get("umbinv_sortby")  # text
            umbinv_offset = kwargs.get("umbinv_offset")  # number

            log = logging.getLogger(__name__)
            log.info("umbinv_emails: %s", umbinv_emails)
            log.info("umbinv_nameservers: %s", umbinv_nameservers)
            log.info("umbinv_domain: %s", umbinv_domain)
            log.info("umbinv_limit: %s", umbinv_limit)
            log.info("umbinv_sortby: %s", umbinv_sortby)
            log.info("umbinv_offset: %s", umbinv_offset)

            if is_none(umbinv_emails) and is_none(umbinv_nameservers) and is_none(umbinv_domain):
                raise ValueError("One of parameters 'umbinv_emails', 'umbinv_nameservers 'or 'umbinv_domain' "
                                 "must be set.")

            yield StatusMessage("Starting...")
            init_env(self)

            self._params = {"emails": umbinv_emails, "nameservers": umbinv_nameservers,
                            "domain": umbinv_domain, "limit": umbinv_limit, "sort_field": umbinv_sortby,
                            "offset": umbinv_offset}

            # Reset 'emails' and 'domain' or 'nameserver param if inmput paramater set.
            if not is_none(umbinv_domain):
                self._params.setdefault("domains", umbinv_domain.strip())

            if not is_none(umbinv_nameservers):
                self._params.setdefault("nameservers", umbinv_nameservers.strip())

            if not is_none(umbinv_emails):
                self._params.setdefault("emails", umbinv_emails.strip())

            validate_params(self)
            process_params(self)

            if not hasattr(self, '_domain') and not hasattr(self, '_emails') and not hasattr(self, '_nameservers'):
               raise ValueError("One of parameters 'umbinv_domain', 'umbinv_emails' or 'umbinv_nameservers' was "
                                "not processed correctly")

            api_token = self.options.get("api_token")
            base_url = self.options.get("base_url")
            rinv = ResilientInv(api_token,base_url)

            yield StatusMessage("Running Cisco Investigate query...")
            if hasattr(self, '_domain'):
                if self._params["limit"] is None:
                # Add metadata of "query_execution_time", "min_id" and "max_id" keys to make it easier in post-processing.
                    rtn = rinv.domain_whois(self._domain)
                else:
                    rtn = rinv.domain_whois_history(self._domain, self._params["limit"])
                query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # Add "query_execution_time" and "domain" key to result to facilitate post-processing.
                results = {"domain_whois": json.loads(json.dumps(rtn)), "domain": self._domain,
                           "query_execution_time": query_execution_time}
            elif hasattr(self, '_emails'):
                rtn = rinv.email_whois(self._emails, **omit_params(self._params, ["emails","nameservers","domain"]))
                query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # Add "query_execution_time" and "emails" key to result to facilitate post-processing.
                results = {"email_whois": json.loads(json.dumps(rtn)), "emails": self._emails,
                           "query_execution_time": query_execution_time}
            elif hasattr(self, '_nameservers'):
                rtn = rinv.ns_whois(self._nameservers, **omit_params(self._params, ["emails","nameservers","domain"]))
                query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # Add "query_execution_time" and "nameservers" key to result to facilitate post-processing.
                results = {"ns_whois": json.loads(json.dumps(rtn)), "nameservers": self._nameservers,
                           "query_execution_time": query_execution_time}
            yield StatusMessage("Done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()