# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
# Generated with resilient-sdk v51.0.1.0.695

import logging
from urllib.parse import urljoin
from cachetools import cached, TTLCache

from resilient_lib import IntegrationError, validate_fields, readable_datetime, str_to_bool, clean_html

from fn_wiz.lib.wiz_graphql_queries import GRAPHQL_PULL_ISSUES, GRAPHQL_PULL_VULNERABILITIES, GRAPHQL_UPDATE_ISSUE

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_wiz"

HEADER = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

# Max results that can be returned from a given query
MAX_RESULTS = 500

# Max results that can be returned from the vulnerabilities query.
# Can be up to 500, but script to add vulnerabilities
# to a data table might fail due to a large volume of operations
MAX_VULN_RESULTS = 50

CACHE_TTL = 60*60*24    # 86400 seconds = 1 day

class AppCommon():
    def __init__(self, rc, package_name, app_configs):
        """
        Initialize the parameters needed to communicate to the endpoint solution

        :param rc: object to resilient_lib.requests_common for making API calls
        :type rc: ``resilient_lib.RequestsCommon``
        :param package_name: name of the package to be created
        :type package_name: str
        :param app_configs: app.config parameters in order to authenticate and access the endpoint
        :type app_configs: dict
        """
        self.package_name = package_name
        self.rc = rc
        self.verify = _get_verify_ssl(app_configs)

        # Check required configs
        validate_fields(["client_id", "client_secret", "api_url", "endpoint_url", "token_url"], app_configs)
        # Key and secret used to generate Bearer token
        self.client_id = app_configs.get('client_id')
        self.client_secret = app_configs.get('client_secret')
        # GraphQL API url
        self.graphql_api_url = app_configs.get('api_url')
        # Wiz App url
        self.endpoint_url = app_configs.get('endpoint_url')
        # Wiz authentication url to generate bearer token
        self.auth_url = app_configs.get('token_url')

        # Get optional configs
        self.get_vulnerabilities_filter = app_configs.get('get_vulnerabilities_filter', None)
        if self.get_vulnerabilities_filter:
            LOG.debug("get_vulnerabilities_filter set to %s", self.get_vulnerabilities_filter)

    def _get_uri(self, cmd: str):
        """
        Build API url

        :param cmd: portion of API: alerts, endpoints, policies
        :type cmd: str
        :return: complete URL
        :rtype: str
        """
        return urljoin(self.graphql_api_url, cmd)

    def _make_headers(self, token: str):
        """Build API header using authorization token

        :param token: authorization token
        :type token: str
        :return: complete header
        :rtype: dict
        """
        header = HEADER.copy()

        header['Authorization'] = f"Bearer {token}"

        return header
    
    def _generate_auth_token(self):
        """
        An Bearer token is required to make API calls. These tokens expire daily, so it is recommended to generate a token
        for every API call.

        :returns token: access_token to make API calls to graphql endpoints
        :rtype token: str
        """

        payload = {
            "grant_type": "client_credentials",
            "audience": "wiz-api",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded"
        }

        response = self.rc.execute("POST",
                               self.auth_url,
                               data=payload,
                               headers=headers,
                               verify=self.verify)
        
        response_json = response.json()

        return response_json.get('access_token')

    @staticmethod
    def check_error(response: dict):
        """ Since Wiz returns 200 status codes even if there is an error, we have to manually check if the 
                response that came back from the API contains an error

        :param response: response that we have to check from API
        :type response: JSON
        :raises: Integration error if there is an error (or multiple errors) returned by Wiz API.
        """
        errors = response.get('errors', [])
        if len(errors) == 1:
            msg = errors[0].get('message', "")
            LOG.error("Received an error from Wiz API: %s", msg)
            
            # Raise an error that can be caught in the function code
            raise IntegrationError(msg)
        
        if len(errors) > 1:
            raise IntegrationError(f"Unexpected number of errors returned {len(errors)}")


    def _api_call(self, method: str, url: str, payload: dict=None):
        """
        Make an API call to the endpoint solution and get back the response

        :param method: REST method to execute (GET, POST, PUT, ...)
        :type method: str
        :param url: URL to send request to
        :type url: str
        :param payload: JSON payload to send if a POST, defaults to None
        :type payload: dict|None
        :return: requests.Response object returned from the endpoint call
        :rtype: ``requests.Response``
        """    

        # Generate Bearer token with
        token = self._generate_auth_token()

        response = self.rc.execute(method,
                               url,
                               json=payload,
                               headers=self._make_headers(token),
                               verify=self.verify)
        
        resp_json = response.json()

        self.check_error(resp_json)

        return resp_json

    
    def _api_call_paged_issues(self, variables: dict):
        """
        Make API calls to the endpoint solution and paginate if necessary.
         Accumulate results into a list and return
         This function is specific to querying issues

        :param variables: dictionary variables to send as a filter for results from query
        :type variables: dict
        :return: list of entities
        :rtype: list[dict]
        """
        has_next_page = True  # Indicates if we need to continue querying for the next page
        end_cursor = None   # Indicates where to continue pagination
        entities = []       # list of all our issue objects

        while has_next_page:
            if end_cursor:
                # Use the end cursor to get the next page, add it to the variables (end_cursor = "" if there is a next page)
                variables["after"] = end_cursor

            query = {
                "query": GRAPHQL_PULL_ISSUES,
                "variables": variables
            }

            LOG.debug("_api_call_paged_issues: Querying for issues with variables: %s", variables)

            response = self._api_call("POST", self.graphql_api_url, query)

            # If we have nodes (which represents a list of issues), add it to our final list of issues (entities) to be returned
            nodes = response.get('data', {}).get('issues', {}).get('nodes', [])
            if nodes:
                entities.extend(nodes)

            # Get information about whether we need to continue to the next page
            page_info = response.get('data', {}).get('issues', {}).get('pageInfo', {})
            has_next_page = page_info.get('hasNextPage', False)
            end_cursor = page_info.get('endCursor', None)
        
        return entities

    
    def query_changed_entities_since_ts(self, timestamp: int):
        """
        Get issues since last poller run where the statusChangedAt date has been updated since the last poll. This 
        will include any newly created issues.

        :param timestamp: datetime when the last poller ran
        :type timestamp: datetime
        :param *args: additional positional parameters needed for endpoint queries
        :param **kwargs: additional key/value pairs needed for endpoint queries
        :return: changed entity list
        :rtype: list
        """

        entities = []       # list of all our issue objects

        variables = {
                "first": MAX_RESULTS,
                "filterBy": {
                    "statusChangedAt": {
                        "after": readable_datetime(timestamp) # utc datetime format
                    }
                }
            }
    
        entities = self._api_call_paged_issues(variables)

        LOG.debug("Found %s issues where statusChangedAt has been updated since %s", len(entities), timestamp)
        
        return entities

    def make_linkback_url(self, entity_id: str, linkback_url: str):
        """
        Create a url to link back to the endpoint entity

        :param entity_id: id representing the entity
        :type entity_id: str
        :param linkback_url: string to in which one can format the entity ID to join to the base url
        :type linkback_url: str
        :return: completed url for linkback
        :rtype: str
        """
        return urljoin(self.endpoint_url, linkback_url.format(entity_id))

    def get_issue(self, wiz_issue_id: str):
        """
        Get issue data

        :param wiz_issue_id: Issue ID
        :type wiz_issue_id: str

        :return: JSON object with issue data
        :rtype: JSON
        """
        LOG.debug("Querying for issue ID %s from Wiz", wiz_issue_id)

        variables = {
            "first": 1,
            "filterBy": {
                "id": [
                    wiz_issue_id
                ]
            }
        }

        query = {
                "query": GRAPHQL_PULL_ISSUES,
                "variables": variables
            }

        LOG.debug("get_issue: Querying for Wiz issue with variables: %s", variables)

        response = self._api_call("POST", self.graphql_api_url, query)

        # pull out the issue which is stored by Wiz as a "node"
        issues = response.get('data', {}).get('issues', {}).get('nodes', [])
        if len(issues) != 1:
            raise IntegrationError(f"Unexpected number of issues returned {len(issues)} for issue ID {wiz_issue_id}. Expected 1 issue.")

        return issues[0]

    @cached(TTLCache(maxsize=1024, ttl=CACHE_TTL), key=lambda _, num_results=MAX_RESULTS: num_results)
    def get_vulnerabilities(self, num_results = MAX_RESULTS):
        """
        Get all recent vulnerabilities -- top MAX_RESULTS of High and Critical Severity, in order of most recent
        """
        
        # get all vulnerabilities (max 500)
        variables = {
            "first": num_results,
            "filterBy": {
                "vendorSeverity": ["HIGH", "CRITICAL"],
                "status": ["OPEN"]
            },
            "orderBy": {
                "direction": "DESC"     # descending by firstDetectedAt value; most recent at the beginning
            }
        }
        query = {
                "query": GRAPHQL_PULL_VULNERABILITIES,
                "variables": variables
            }
        
        vulnerabilities = []

        LOG.info("Querying for vulnerabilities from Wiz with variables: %s", variables)

        response = self._api_call("POST", self.graphql_api_url, query)

        # Vulnerabilities are stored as "nodes"
        vulnerabilities = response.get('data', {}).get('vulnerabilityFindings', {}).get('nodes', [])

        LOG.debug("Found %s vulnerabilities.", len(vulnerabilities))
        
        return vulnerabilities

    @cached(TTLCache(maxsize=1024, ttl=CACHE_TTL), key=lambda _, project_ids, num_results: f'{",".join(project_ids)}:{num_results}' )
    def get_vulnerabilities_by_project(self, project_ids, num_results):
        """
        Filter vulnerabilities by the project ids (can be 1 or multiple in a list)
        Cache key is the alphabetized list of project ids joined together as a comma separated string and concatenated with ":num_results"

        :param project_ids: SORTED list of project IDs
        :type project_ids: list[str]
        :param num_results: Number of vulnerabilities to return
        :type num_results: int

        :returns: num_results # of vulnerabilities
        :rtype: JSON
        """

        LOG.debug("Querying for vulnerabilities with get_vulnerabilities_by_project()")

        if num_results > MAX_RESULTS:
            raise IntegrationError(f"Requested number of results exceeds maximum ({MAX_RESULTS}) as allowed by Wiz API. \
                                   Please update function input 'wiz_num_results' to a lower value.")
        
        vulnerabilities = self.get_vulnerabilities()    # should be cached
        associated_vulns = []       # vulnerabilities to be returned back to the playbook

        if num_results and not project_ids:
            # If project ids list is empty, just return the top num_results (this is what the Wiz API does)
            associated_vulns = vulnerabilities[:num_results]

            LOG.debug("Collected most recent %s vulnerabilities since last vulnerabilities refresh: %s seconds.", len(associated_vulns), CACHE_TTL)

        else:
            # Convert project_ids into a set so that we can use intersection for comparison
            project_ids = set(project_ids)

            # Pull out vulnerabilities that have project ids that match the project_ids passed in
            for vuln in vulnerabilities:
                vuln_projects = {p.get("id","") for p in vuln.get("projects", [])}  # set comprehension to get project IDs for this vulnerability
                if vuln_projects & project_ids:
                    # If any of the project Ids provided via the function inputs are found in the vulnerability, then add the vulnerability to our running list
                    associated_vulns.append(vuln)

                # if we only want the first "num_results", when we hit this number, return
                if len(associated_vulns) == num_results:
                    break
        
            LOG.debug("Found %s vulnerabilities associated with projects %s.", len(associated_vulns), project_ids)
            
        return associated_vulns

    def get_vulnerabilities_custom(self, custom_filter: dict):
        """
        Get vulnerabilities with a custom filter provided by user via function inputs.

        We should not paginate vulnerabilities results because there can be thousands of results for a given query. This can overwhelm SOAR and
        would not be meaningful in a data table

        :param custom_filter: custom "variables" object which can be used to filter results from Wiz API
        :type custom_filter: dict

        :return vulnerabilities: all vulnerabilities returned from query
        :rtype: list of dictionaries
        """

        # But first check if the required 'first' parameter is there, otherwise Wiz will reject the query
        if not custom_filter.get('first'):
            raise IntegrationError(f"Required 'first' parameter for Wiz query is not provided in \
                                    wiz_filter_query input: {custom_filter}. Please revise the filter \
                                    input to include the 'first' parameter with a value < {MAX_RESULTS} to indicate max number \
                                    of results to retrieve from Wiz.")
        
        # If the `first` parameter is provided, we can pass the filter to Wiz as the `variables`
        query = {
                "query": GRAPHQL_PULL_VULNERABILITIES,
                "variables": custom_filter
            }
        
        vulnerabilities = []

        LOG.info("Querying for vulnerabilities from Wiz with custom filter for variables: %s", custom_filter)

        response = self._api_call("POST", self.graphql_api_url, query)

        # Vulnerabilities are stored as "nodes"
        vulnerabilities = response.get('data', {}).get('vulnerabilityFindings', {}).get('nodes', [])

        LOG.debug("Found %s vulnerabilities for wiz_query_filter %s", len(vulnerabilities), custom_filter)
        
        return vulnerabilities

    def update_issue(self, query, issue_id: str):
        """Posts an update query to Wiz - is used in case of updating issue status or adding notes to an issue
        
        :param query: GraphQL query with variables based on update action
        :type query: dict
        :param issue_id: Wiz issue id to update
        :type issue_id: str

        :return: the received issue data (dictionary)
        """
        LOG.debug("update_issue: Querying to update Wiz issue %s with variables: %s", issue_id, query.get('variables'))

        response = self._api_call("POST", self.graphql_api_url, query)
        
        issue = response.get('data', {}).get('updateIssue', {}).get('issue', {})
        return issue

    def add_note_to_issue(self, issue_id: str, note_text: str):
        """ Add a note to the Wiz issue, without the HTML

        :param issue_id: Wiz Issue ID
        :type issue_id: str
        :param note_text: SOAR note content to get added to the Issue as a comment 
        :type note_text: str
        """

        LOG.debug("Adding following note to Wiz issue %s: %s", issue_id, note_text)

        variables = {
            "issueId": issue_id,
            "patch": {
                "note": f"Note from SOAR: {clean_html(note_text)}"
            }
        }

        query = {
                "query": GRAPHQL_UPDATE_ISSUE,
                "variables": variables
            }

        return self.update_issue(query, issue_id)

    def sync_status_with_wiz(self, issue_id: str, reason: str, summary: str = None):
        """ Update the issue if the SOAR case got closed.
        * Wiz issue status can be set to OPEN, IN_PROGRESS, or REJECTED; cannot manually be set to RESOLVED. So if a SOAR case
            gets Resolved, then we will skip updating Wiz issue status. Other resolution ids will be translated as "REJECTED"
            with a "WONT_FIX" reason to Wiz
        * An issue resolution reason and a note is required if a Wiz issue gets set to REJECTED
            * The issue resolution reason can be one of - FALSE_POSITIVE, EXCEPTION, WONT_FIX; for this app we will set to "WONT_FIX"

        :param issue_id: Wiz Issue ID
        :type issue_id: str
        :param reason: reason why SOAR case was closed, one of: ["Unresolved", "Duplicate", "Not an Issue", "Resolved"]
        :type reason: str

        :return: issue
        """

        if reason == "Resolved":
            LOG.warning("Cannot update Wiz issue to be 'Resolved'. Wiz issue can only be closed if case is closed for reason: \
                        'Unresolved', 'Duplicate', 'Not an Issue'.")
            
            raise IntegrationError("Cannot update Wiz issue to be 'Resolved'")

        LOG.debug("Updating status of Wiz issue %s to be 'REJECTED'", issue_id)

        variables = {
            "issueId": issue_id,
            "patch": {
                "status": "REJECTED",
                "resolutionReason": "WONT_FIX",
                "note": f"Corresponding SOAR case has been closed with reason {reason} and resolution summary {summary}"
            }
        }

        query = {
                "query": GRAPHQL_UPDATE_ISSUE,
                "variables": variables
            }

        return self.update_issue(query, issue_id)


def _get_verify_ssl(app_configs):
    """
    Get ``verify`` parameter from app config.
    Value can be set in the [fn_my_app] section

    :param opts: All of the app.config file as a dict
    :type opts: dict
    :param app_options: App specific configs
    :type app_options: dict
    :return: Value to set ``requests.request.verify`` to. Either a path or a boolean. Defaults to ``True``
    :rtype: bool|str(path)
    """
    # start checking the app specific settings
    verify = app_configs.get("verify")

    # because verify can be either a boolean or a path,
    # we need to check if it is a string with a boolean 
    # value first then, and only then, we convert it to a bool
    # NOTE: that this will then only support "true" or "false"
    # (case-insensitive) rather than the normal "true", "yes", etc...
    if isinstance(verify, str) and verify.lower() in ["false", "true"]:
        verify = str_to_bool(verify)

    return verify