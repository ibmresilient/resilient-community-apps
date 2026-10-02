# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.

""" Helper functions for Resilient circuits Functions supporting Cisco Umbrella Investigate """

from logging import getLogger
from datetime import datetime, timedelta, timezone
from time import mktime
from re import compile, error, split, match, IGNORECASE, search
from os import remove
from json import dump
from urllib.parse import urlparse, quote_plus, urljoin
from requests.auth import HTTPBasicAuth

PACKAGE_NAME = "fn_cisco_umbrella_inv"
LOG = getLogger(__name__)
IP_PATTERN = compile(r"^(\d{1,3}\.){3}\d{1,3}$")
DOMAIN_REGEX = "((?=[a-z0-9-]{1,63}\.)(xn--)?[a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,63}"
DOMAIN_PATTERN = compile(r"^\b{}\b$".format(DOMAIN_REGEX))
EMAIl_PATTERN = compile(r"(^[a-zA-Z0-9_.+-]+@{}$)".format(DOMAIN_REGEX))
UUID_PATTERN = compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
TIMEDELTA_PATTERN = compile(r"^-*(\d+)(seconds|minutes|hours|days|weeks)$")
MD5_PATTERN = compile(r"^[a-fA-F0-9]{32}$")
SHA1_PATTERN = compile(r"\b[a-fA-F0-9]{40}$")
SHA256_PATTERN = compile(r"\b[a-fA-F0-9]{64}$")
URIs = {
    "categorization":       "domains/categorization",
    "cooccurrences":        "recommendations/name/{}.json",
    "domain_rr_history":    "dnsdb/name/{}/{}.json", #
    "ip_rr_history":        "dnsdb/ip/{}/{}.json",
    "latest_domains":       "ips/{}/latest_domains",
    "related":              "links/name/{}",
    "security":             "security/name/{}",
    "whois_email":          "whois/emails/{}",
    "whois_ns":             "whois/nameservers/{}",
    "whois_domain_history": "whois/{}/history",
    "search":               "search/{}",
    "samples":              "samples/{}",
    "sample":               "sample/{}",
    "sample_artifacts":     "sample/{}/artifacts",
    "sample_connections":   "sample/{}/connections",
    "as_for_ip":            "bgp_routes/ip/{}/as_for_ip.json",
    "prefixes_for_asn":     "bgp_routes/asn/{}/prefixes_for_asn.json",
    "timeline":             "timeline/{}",
    "domain_volume":        "domains/volume/{}",
    "categories": "domains/categories/",
    "classifiers_classifiers": "url/{}/classifiers",
    "classifiers_info": "url/{}/info",
    "sample_behaviors": "sample/{}/behaviors"
}
SUPPORTED_DNS_TYPES = ["A", "NS", "MX", "TXT","CNAME"]
UNSUPPORTED_DNS_QUERY = ValueError(f"supported query types are: {SUPPORTED_DNS_TYPES}")
DOMAIN_ERR = ValueError("domains must be a string or a list of strings")
SEARCH_ERR = ValueError("Start argument must be a datetime or a timedelta")
IP_ERR = ValueError("invalid IP address")

class investigateClient():
    # Make API calls to Cisco Umbrella Investigate
    def __init__(self, options, rc):
        self.base_url = options.get("base_url", None)
        self.results_limit = options.get("results_limit", None)
        self.verify = rc.get_verify()
        self.proxies = rc.get_proxies()
        self.rc = rc
        self.header = {'Accept': 'application/json'}

        # Get or create access token
        token = None
        self.api_token = options.get("api_token", None)
        self.api_key = options.get("inv_api_key", None)
        self.api_secret = options.get("inv_api_secret", None)
        if self.api_token and self.api_token != "<api token>":
            # use given access token
            token = self.api_token
        elif self.api_key and self.api_secret and self.api_key != "<cisco_umbrella_investigate_api_key>" and self.api_secret != "<cisco_umbrella_investigate_api_secret>":
            # Create access token
            token = self.create_access_token(self.api_key, self.api_secret)
        else:
            raise ValueError("Either an inv_api_key and inv_api_secret have to be given or an api_token has to be given.")
        # Create authorization header
        self.header["Authorization"] = f"Bearer {token}"

    def create_access_token(self, api_key: str, api_secret: str):
        """Create an access token using the given api_key and api_secret.
        Args:
            api_key (str): Cisco Umbrella Investigate API key.
            api_secret (str): Umbrella Investigate API Secret

        Returns:
            str: Access token
        """
        resp = self.make_api_call("GET",
            urljoin(self.base_url.replace("investigate", "auth"), "token"),
            auth=HTTPBasicAuth(api_key, api_secret))
        return resp.get("access_token", None)

    def check_response(self, response):
        # Handle 400 error codes. If a 400 or a 403 error is returned then the access token could have expired.
        # If inv_api_key and inv_api_secret given in the app.config check response to determine if a new access token needs to be created.
        if response.status_code >= 400 and response.status_code < 500 and not self.api_token:
            # Return False, so the code knows to create a new access token and try the api call again.
            return False
        else:
            return response

    def make_api_call(self, method: str, uri: str, params: dict=None, data: dict=None, auth=None):
        """Make a REST API call to the Cisco Umbrella Investigate server

        Args:
            method (str): GET, POST, PUT, DELETE, etc...
            uri (str): API uri that can be found in the URIs variable
            params (dict, optional): Dictionary of params to pass to API call. Defaults to None.
            data (dict, optional): Dictionary of data to pass to API call. Defaults to None.
            auth: HTTPBasicAuth object. Defaults to None.

        Returns:
            json return from the API call
        """
        def api_call(callb: bool=True):
            if callb:
                return self.rc.execute(method,
                    urljoin(self.base_url, uri),
                    params=params if params else None,
                    data=data if data else None,
                    auth=auth,
                    proxies=self.proxies,
                    headers=self.header,
                    verify=self.verify,
                    callback=self.check_response)
            else:
                return self.rc.execute(method,
                    urljoin(self.base_url, uri),
                    params=params if params else None,
                    data=data if data else None,
                    auth=auth,
                    proxies=self.proxies,
                    headers=self.header,
                    verify=self.verify)
        # Make API call
        if not self.api_token:
            resp = api_call()
        else:
            resp = api_call(False)
        # If resp equals False then the status_code was a 400
        if not resp and not self.api_token:
            # Create new access token and set it in the header
            self.header = {"Authorization": f"Bearer {self.create_access_token(self.api_key, self.api_secret)}"}
            # Make API call again using new access token
            resp = api_call(False)
        return resp.json()

def get_time_input(time_input):
    """ Return the correct time """
    if not time_input:
        time_input = timedelta(days=30)
    if isinstance(time_input, timedelta):
        return int(mktime((datetime.now(timezone.utc) - time_input).timetuple()) * 1000)
    elif isinstance(time_input, datetime):
        return int(mktime(time_input.timetuple()) * 1000)
    elif isinstance(time_input, int) and (datetime.now()-datetime.fromtimestamp(time_input/1000)).days < 30:
        return int(time_input)
    else:
        raise SEARCH_ERR

def validate_url(url):
    """"Validate url string in a valid format and can be parsed ok.

    :param regex: url parameter value
    :return : boolean
    """
    try:
        result = urlparse(url)
        if all([result.scheme, result.netloc]):
            return True
        else:
            return False
    except:
        return False

def validate_regex(regex):
    """"Validate regex string in a valid format and can be parsed ok.

    :param regex: Regex parameter value
    :return : boolean
    """
    try:
        compile(regex)
        return True
    except error:
        LOG.debug("regex: %s", regex)
        return False

def validate_domains(doms):
    """"Validate domain string(s) are in a valid format.

    :param doms: Domain(s) parameter value
    :return : boolean
    """
    for d in split('\s+|,', doms):
        if not DOMAIN_PATTERN.match(d):
            return False
    return True

def validate_emails(emails):
    """"Validate email string(s) are a valid format.

    :param emails: Email(s) parameter value
    :return : boolean
    """
    for d in split('\s+|,', emails):
        if not EMAIl_PATTERN.match(d):
            return False
    return True

def validate_is_int(val):
    """"Validate value is in a valid int format.

    :param val: Value to test
    :return : boolean
    """
    try:
        int(val)
        return True
    except ValueError:
        return False

def validate_params(params):
    """"Check parameter fields for SOAR Function and validate that they are in correct format.

    :param params: Dictionary of SOAR Function parameters.
    """
    if not params:
        raise Exception("Error missing parameter 'params'")

    # If any entry has "None" string change to None value.
    for k, v in params.items():
        if isinstance(v, str) and v.lower() == 'none':
            params[k] = None

    # Now do some validation on input parameters.
    for (k, v) in params.copy().items():
        if match("^resource$", k) and v:
            if not IP_PATTERN.match(v) and not validate_url(v) \
                and not validate_domains(v) and not validate_emails(v) \
                    and not validate_is_int(v):
                raise ValueError("Invalid value for function parameter 'resource'.")
        # Domain name and name server should be in similar format use same validator.
        if match("^domain", k) and v and not validate_domains(v):
            raise ValueError(f"Invalid value for function parameter '{k}'.")
        if match("^ipaddr$", k) and v and not IP_PATTERN.match(v):
            raise ValueError("Invalid value for function parameter 'ipaddr'.")
        if match("^regex$", k) and v and not validate_regex(v):
            raise ValueError("Invalid value for function parameter 'regex'.")
        if match("^(limit|start_epoch|stop_epoch)$", k) and v and not isinstance(v, int):
            raise ValueError(f"Invalid value for function parameter '{k}'.")
        if match("^(start_relative|stop_relative)$", k) and v and not (TIMEDELTA_PATTERN.match(v) or \
            match("^Now$", v, IGNORECASE)):
            raise ValueError(f"Invalid value for function parameter '{k}'. ")
        if match("^(start|stop)", k) and not v:
            params.pop(k)
            # The regex pattern re.split('_', k)[0] splits [start|stop]_[epoch|relative] on '_' and selects 1st value
        elif match("^(start|stop)", k) and v and split('_', k)[0] not in params:
            params[split('_', k)[0]] = params.pop(k)
        elif match("^(start|stop)", k) and v and split('_', k)[0] in params:
            raise ValueError(f"Duplicate parameter {k} since the parameter {split('_', k)[0]} already set.")
        if match("^(showlabels|include_category)", k) and v and not isinstance(v, bool):
            raise ValueError(f"Invalid value for function parameter '{k}'")
        if match("^hash$", k) and v:
            if not MD5_PATTERN.match(v) and not SHA1_PATTERN.match(v) \
                and not SHA256_PATTERN.match(v):
                raise ValueError("Invalid value for function parameter 'hash'.")

def set_result(process_result, key_name, val):
    """"Setup string or list attribute for the SOAR Function for types:

        domain or domains,
        email or emails,
        nameserver or nameservers

    :param process_result: Processing result dict.
    :param key_name: Parameter Key name
    :param val: Value for parameter to be processed.
    """
    if (search('[\s+|,]', val)):
        # Assume multiple domains will be a list
        # Split on white spaces or commas e.g '"domain1.com" "domain2.com"' or '"domain1.com","domain2.com"'
        process_result["_"+key_name] = split('\s+|,', val)
    else:
        # Assume single domain  will be a string
        process_result["_"+key_name] = str(val)

def process_params(params, process_result):
    """"Process SOAR Function parameter fields doing any necessary transformations.

    :param params: Dictionary of SOAR Function parameters.
    :param process_result: Processing result dict.
    """
    if not params:
        raise Exception("Error missing parameter 'params'")

    # Validate the params
    validate_params(params)

    for (k, v) in params.items():
        if (match("^resource$", k)) and v:
            if IP_PATTERN.match(v) or validate_domains(v) or validate_emails(v) \
                    or validate_is_int(v):
                # Assume "resource" param is a domain name, nameserver, ip address, email address or asn.
                process_result["_res"] = str(v)
                if IP_PATTERN.match(v):
                    process_result["_res_type"] = "ip_address"
                elif validate_domains(v):
                    process_result["_res_type"] = "domain_name"
                elif validate_emails(v):
                    process_result["_res_type"] = "email_address"
                elif validate_is_int(v):
                    process_result["_res_type"] = "as_number"
            elif validate_url(v):
                # Assume "resource" param is a url.
                process_result["_res"] = quote_plus(v)
                process_result["_res_type"] = "url"
        if (match("^domain", k)) and v:
            set_result(process_result, k, v)
        if (match("^ipaddr$", k)) and v:
            process_result["_ipaddr"] = str(v)
        if (match("^regex$", k)) and v:
            process_result["_regex"] = str(v)
        if (match("^hash$", k)) and v:
            process_result["_hash"] = str(v)
        if match("^(start|stop)$", k) and v:
            if isinstance(v, int):
                params[k] = datetime.fromtimestamp(v / 1e3)
            else:
                if match("^Now$", v, IGNORECASE):
                    params[k] = datetime.now()
                else:
                    # Split value using regex e.g. -30days, m splits as m.group(1) = -30, m.group(2) = days
                    m = TIMEDELTA_PATTERN.search(v)
                    params[k] = timedelta(**{str(m.group(2)): int(m.group(1))})

def omit_params(params, omit_list):
    """"Filter out 'omit_list' list of parameters from the 'params' dict keys.

    :param params: SOAR Function parameters dictionary
    :param omit_list: List of parameter keys to remove
    :return: Updated parameter dictionary
    """
    if not params:
        raise Exception("Error missing parameter 'params'")
    if not omit_list:
        raise Exception("Error missing parameter 'omit_set'")
    if not isinstance(omit_list, str) and not isinstance(omit_list, list):
        raise ValueError("omit_list argument must be a string or list")
    return {k: v for (k, v) in params.items() if k not in omit_list}

def create_attachment(func_ref, func_name, artifact_value, params, rtn, query_execution_time):
    """"Create an attachment and post to SOAR platform.

    :param func_ref: SOAR Function instance reference
    :param func_name: SOAR Function name
    :param artifact_value: SOAR artifact value
    :param params: SOAR Function parameters dictionary
    :param rtn: Result returned from external source
    :param query_execution_time: External time of query
    :return att_report: Updated attachment report dictionary
    """
    file_name = f"{func_name} [{params.get('artifact_type')}: {artifact_value}].txt"

    try:
        rest_client = func_ref.rest_client()

        # Create the temporary file save results in json format.
        with open(file_name, 'w') as outfile:
            dump(rtn, outfile)

        # Post file to SOAR
        att_report = rest_client.post_attachment(f"/incidents/{params.get('incident_id')}/attachments",
            file_name, file_name, "text/plain", "")
        LOG.info("New attachment added to incident %s", params.get("incident_id"))

        # Delete the temporary file.
        remove(file_name)

    except Exception as ex:
        LOG.error(ex)
        raise ex

    return att_report
