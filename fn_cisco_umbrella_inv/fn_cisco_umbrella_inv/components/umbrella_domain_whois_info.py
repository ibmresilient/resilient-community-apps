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
import re

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import validate_opts, validate_params, process_params, omit_params, \
    is_none


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_domain_whois_info' of package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup and takes the following parameters:
            umbinv_resource, umbinv_limit, umbinv_sortby, umbinv_offset
    An example of a set of query parameter might look like the following:

            umbinv_resource = "domain.com" or umbinv_resource = "ns1.google.com" or umbinv_resource = "test@example.com"
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
            umbinv_resource = kwargs.get("umbinv_resource")  # text
            umbinv_limit = kwargs.get("umbinv_limit")  # number
            umbinv_sortby = kwargs.get("umbinv_sortby")  # text
            umbinv_offset = kwargs.get("umbinv_offset")  # number

            log = logging.getLogger(__name__)
            log.info("umbinv_resource: %s", umbinv_resource)
            log.info("umbinv_limit: %s", umbinv_limit)
            log.info("umbinv_sortby: %s", umbinv_sortby)
            log.info("umbinv_offset: %s", umbinv_offset)

            if is_none(umbinv_resource):
                raise ValueError("Required parameter 'umbinv_resource' not set")

            yield StatusMessage("Starting...")
            res = None
            res_type = None
            process_result = {}
            params = {"resource": umbinv_resource.strip(), "limit": umbinv_limit, "sort_field": umbinv_sortby,
                      "offset": umbinv_offset}

            validate_params(params)
            process_params(params, process_result)

            if "_res" not in process_result or "_res_type" not in process_result:
                raise ValueError("Parameter 'umbinv_resource' was not processed correctly")
            else:
                res = process_result.pop("_res")
                res_type = process_result.pop("_res_type")

            if res_type != "domain_name" and res_type != "email_address":
                    raise ValueError(
                        "Parameter 'umbinv_resource' was an incorrect type '{}', should be a 'domain name', "
                        "an 'email address' or a 'nameserver'.".format(res_type))

            api_token = self.options.get("api_token")
            base_url = self.options.get("base_url")
            rinv = ResilientInv(api_token, base_url)

            yield StatusMessage("Running Cisco Investigate query...")

            if res_type == "domain_name":
                # Can be either domain name or name server.
                # Execute wois query for domain history.
                rtn_dom = rinv.domain_whois_history(res, params["limit"])
                # Execute whois query for nameserver.
                rtn_ns = rinv.ns_whois(res, **omit_params(params, ["resource"]))
                query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                if len(rtn_dom) != 0:
                    # Test if resource is a name server.
                    for entry in rtn_dom:
                        for ns in entry["nameServers"]:
                            if res == ns:
                                res_type = "nameserver"
                                log.debug("Resource '{}' is a nameserver.".format(res))
                                break

                # Add "query_execution_time", 'resource' and 'resource_type' key to result to facilitate post-processing.
                results = {"domain_whois": json.loads(json.dumps(rtn_dom)), "ns_whois": json.loads(json.dumps(rtn_ns)),
                           "resource": res, "resource_type": res_type, "query_execution_time": query_execution_time}
                yield StatusMessage("Returning 'whois' results for resource '{}' of resource type '{}'."
                                    .format(res, res_type))
            elif res_type == "email_address":
                rtn = rinv.email_whois(res, **omit_params(params, ["resource"]))
                query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # Add "query_execution_time" and "emails" key to result to facilitate post-processing.
                results = {"email_whois": json.loads(json.dumps(rtn)), "emails": res,
                           "query_execution_time": query_execution_time}
                yield StatusMessage("Returning 'email_whois' results for resource '{}'.".format(res))
            else:
                raise ValueError("Parameter 'umbinv_resource' was an incorrect type '{}', should be a 'domain name', "
                                 "an 'email address' or a 'nameserver'.".format(res_type))

            yield StatusMessage("Done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function.")
            yield FunctionError()