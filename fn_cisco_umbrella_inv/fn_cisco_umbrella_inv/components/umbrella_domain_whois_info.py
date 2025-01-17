# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.

""" SOAR functions component to run an Umbrella investigate Query - WHOIS information for a Domain against a
Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
from datetime import datetime

from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from fn_cisco_umbrella_inv.util.helpers import process_params, PACKAGE_NAME,\
    investigateClient, URIs
from resilient_lib import validate_fields

FN_NAME = "umbrella_domain_whois_info"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'umbrella_domain_whois_info' of package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup and takes the following parameters:
        umbinv_resource, umbinv_limit, umbinv_sortby, umbinv_offset

    An example of a set of query parameter might look like the following:
        umbinv_resource = "domain.com" or umbinv_resource = "ns1.google.com" or umbinv_resource = "test@example.com"
        umbinv_limit = 2
        umbinv_sortby = "created"
        umbinv_offset = 0

    The Investigate Query will execute a REST call against the Cisco Umbrella Investigate server and returns a result in
    JSON format similar to the following.

    The Investigate Query will execute a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.

        {'domain': 'cisco.com',
         'query_execution_time': '2018-04-27 10:01:23',
         'domain_whois': {'registrantFaxExt': None, 'administrativeContactPostalCode': '95134',
                          'zoneContactCity': None, 'addresses': ['170 w. tasman drive', '170 west tasman drive'],
                          'billingContactState': None, 'technicalContactStreet': ['170 w. tasman drive'],
                          'auditUpdatedDate': '2018-04-22 20:55:22.000 UTC', 'administrativeContactCity': 'San Jose',
                          'administrativeContactEmail': 'infosec@cisco.com', 'technicalContactFax': '14085267373',
                          'technicalContactTelephone': '14085279223', 'billingContactEmail': None,
                          'technicalContactPostalCode': '95134', 'registrantOrganization': 'Cisco Technoself.LOGy Inc.',
                          'zoneContactPostalCode': None, 'registrantState': 'CA',
                          'administrativeContactName': 'Info Sec', 'billingContactFaxExt': None,
                          'billingContactCity': None, 'technicalContactEmail': 'dns-info@CISCO.COM',
                          'registrantCountry': 'UNITED STATES', 'technicalContactFaxExt': None,
                          'registrantName': 'Info Sec', 'registrantEmail': 'infosec@cisco.com',
                          'billingContactCountry': None, 'billingContactName': None,
                          'registrarName': 'CSC CORPORATE DOMAINS, INC.', 'technicalContactTelephoneExt': None,
                          'administrativeContactFax': None, 'zoneContactFax': None, 'zoneContactFaxExt': None,
                          'registrantCity': 'San Jose', 'administrativeContactTelephoneExt': None,
                          'status': ['clientTransferProhibited serverDeleteProhibited serverTransferProhibited serverUpdateProhibited'],
                          'updated': '2017-05-11', 'expires': '2018-05-15', 'whoisServers': 'whois.corporatedomains.com',
                          'zoneContactEmail': None, 'technicalContactState': 'CA',
                          'nameServers': ['ns1.cisco.com', 'ns2.cisco.com', 'ns3.cisco.com'], 'timestamp': None,
                          'recordExpired': False, 'registrantFax': '14085264575',
                          'administrativeContactStreet': ['170 west tasman drive'],
                          'registrantTelephoneExt': None, 'billingContactFax': None,
                          'technicalContactOrganization': 'Cisco Technoself.LOGy Inc.',
                          'administrativeContactState': 'CA', 'zoneContactOrganization': None,
                          'billingContactPostalCode': None, 'zoneContactStreet': [],
                          'zoneContactName': None, 'registrantPostalCode': '95134',
                          'billingContactTelephone': None, 'emails': ['dns-info@cisco.com', 'infosec@cisco.com'],
                          'registrantTelephone': '14085273842', 'administrativeContactCountry': 'UNITED STATES',
                          'technicalContactCity': 'San Jose', 'administrativeContactTelephone': '14085273842',
                          'created': '1987-05-14', 'registrantStreet': ['170 west tasman drive'],
                          'domainName': 'cisco.com', 'technicalContactCountry': 'UNITED STATES',
                          'billingContactStreet': [], 'timeOfLatestRealtimeCheck': 1524501072693, 'zoneContactState': None,
                          'administrativeContactOrganization': 'Cisco Technoself.LOGy Inc.', 'administrativeContactFaxExt': None,
                          'billingContactTelephoneExt': None, 'zoneContactTelephone': None, 'technicalContactName':
                          'Network Services', 'zoneContactTelephoneExt': None, 'billingContactOrganization': None,
                          'registrarIANAID': '299', 'zoneContactCountry': None, 'hasRawText': True},
        }
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: SOAR Function: Cisco Umbrella Investigate for Domain Whois info."""
        try:
            # Validate required input fields
            validate_fields(["umbinv_resource"], fn_inputs)
            # Get the function parameters:
            umbinv_resource = fn_inputs.umbinv_resource  # text
            umbinv_limit = getattr(fn_inputs, "umbinv_limit", None)  # number
            umbinv_sortby = getattr(fn_inputs, "umbinv_sortby", None)  # text
            umbinv_offset = getattr(fn_inputs, "umbinv_offset", None)  # number

            self.LOG.info("umbinv_resource: %s", umbinv_resource)
            self.LOG.info("umbinv_limit: %s", umbinv_limit)
            self.LOG.info("umbinv_sortby: %s", umbinv_sortby)
            self.LOG.info("umbinv_offset: %s", umbinv_offset)

            yield self.status_message(f"Starting App Function: '{FN_NAME}'")
            res, res_type = None, None
            process_result = {}
            process_params({"resource": umbinv_resource.strip(), "limit": umbinv_limit,
                            "sort_field": umbinv_sortby, "offset": umbinv_offset},
                           process_result)

            if "_res" not in process_result or "_res_type" not in process_result:
                raise ValueError("Parameter 'umbinv_resource' was not processed correctly")
            else:
                res = process_result.pop("_res")
                res_type = process_result.pop("_res_type")

            if res_type not in ["domain_name", "email_address"]:
                    raise ValueError(
                        f"Parameter 'umbinv_resource' was an incorrect type '{res_type}', should be a 'domain name', "
                        "an 'email address' or a 'nameserver'.")

            invClient = investigateClient(self.options, self.rc)
            yield self.status_message("Running Cisco Investigate query...")

            if res_type == "domain_name":
                # Can be either domain name or name server.
                # Execute whois query for domain history.
                rtn_dom = invClient.make_api_call("GET",
                                                  URIs.get("whois_domain_history").format(res),
                                                  params={"limit": umbinv_limit} if umbinv_limit else None)
                # Execute whois query for nameserver.
                rtn_ns = invClient.make_api_call("GET",
                                                 URIs.get("whois_ns").format("" if isinstance(res, list) else res),
                                                 params={"limit": umbinv_limit,
                                                         "offset": umbinv_offset,
                                                         "sortField": umbinv_sortby,
                                                         "nameServerList": ",".join(res) if isinstance(res, list) else None})
                query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                if len(rtn_dom) != 0:
                    # Test if resource is a name server.
                    for entry in rtn_dom:
                        for ns in entry.get("nameServers"):
                            if res == ns:
                                res_type = "nameserver"
                                self.LOG.debug(f"Resource '{res}' is a nameserver.")
                                break

                # Add "query_execution_time", 'resource' and 'resource_type' key to result to facilitate post-processing.
                results = {"domain_whois": rtn_dom, "ns_whois": rtn_ns,
                           "resource": res, "resource_type": res_type, "query_execution_time": query_execution_time}
                yield self.status_message(f"Returning 'whois' results for resource '{res}' of resource type '{res_type}'.")
            elif res_type == "email_address":
                rtn = invClient.make_api_call("GET",
                                              URIs.get("whois_email").format("" if isinstance(res, list) else res),
                                              params={"limit": umbinv_limit,
                                                      "offset": umbinv_offset,
                                                      "sortField": umbinv_sortby,
                                                      "emailList": ",".join(res) if isinstance(res, list) else None})
                query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # Add "query_execution_time" and "emails" key to result to facilitate post-processing.
                results = {"email_whois": rtn, "emails": res,
                           "query_execution_time": query_execution_time}
                yield self.status_message(f"Returning 'email_whois' results for resource '{res}'.")
            else:
                raise ValueError(f"Parameter 'umbinv_resource' was an incorrect type '{res_type}', should be a 'domain name', "
                                 "an 'email address' or a 'nameserver'.")

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
