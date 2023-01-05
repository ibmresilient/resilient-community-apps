# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import functools
from datetime import datetime
from logging import getLogger
from threading import Event
from traceback import format_exc
from resilient import SimpleHTTPException

LOG = getLogger(__name__)

# P O L L E R   L O G I C
def poller(named_poller_interval, named_last_poller_time, package_name):
    """
    Decorator for poller, manage poller time, calling the customized method for getting the next entities
    :param named_poller_interval: (str) Name of instance variable containing the poller interval in seconds
    :param named_last_poller_time: (datetime) Name of instance variable containing the lookback value in mseconds
    :param package_name: (str) Name of package for loggging
    """
    def poller_wrapper(func):
        # Decorator for running a function forever, passing the ms timestamp of
        # when the last poller run to the function it's calling
        @functools.wraps(func)
        def wrapped(self):
            last_poller_time = getattr(self, named_last_poller_time)
            exit_event = Event()

            while not exit_event.is_set():
                try:
                    LOG.info(f"{package_name} polling start.")
                    poller_start = datetime.now()
                    # Function execution with the last poller time in ms
                    func(self, last_poller_time = int(last_poller_time.timestamp()*1000))

                except Exception as err:
                    LOG.error(str(err))
                    LOG.error(format_exc())
                finally:
                    LOG.info(f"{package_name} polling complete.")
                    # Set the last poller time for next cycle
                    last_poller_time = poller_start

                    # Sleep before the next poller execution
                    exit_event.wait(getattr(self, named_poller_interval))
            exit_event.set() # Loop complete

        return wrapped
    return poller_wrapper

class SOARCommon():
    """ Common methods for accessing IBM SOAR cases and their entities: comment, attachments, etc. """

    def get_open_soar_cases(search_fields, rest_client, open_cases=True):
        """
        Find all IBM SOAR cases which are associated with the endpoint platform
        :param search_fields: (dict) List of field(s) used to track the relationship with a SOAR case
                                    field values can be True/False for 'has_a_value' or 'does_not_have_a_value'
                                    Otherwise a field will use 'equals' for the value
        NOTE: search_fields only supports custom fields
        :return soar_cases: (list) Returned list of cases
        :return error_msg: (str) Any error during the query or None
        """
        fields_to_remove = ["perms", "creator", "creator_principal", "exposure_type_id", "workspace", "assessment", "pii",
                            "gdpr", "creator_id", "crimestatus_id", "sequence_code", "owner_id", "plan_status", "phase_id",
                            "org_handle", "task_changes"]


        query = SOARCommon._build_search_query(search_fields, open_cases = open_cases)
        cases_list = []

        try:
            cases_list, err_msg = rest_client.post('/incidents/query?return_level=normal&handle_format=names', query), None
        except SimpleHTTPException as err:
            LOG.error(str(err))
            LOG.error(query)
            return None, str(err)

        # Remove case keys that are empty and unused keys
        for num in range(len(cases_list)):
            cases_list[num] = dict([(key,value) for key,value in cases_list[num].items() if value])
            for field in fields_to_remove:
                cases_list[num].pop(field)

            # Change the value of the dict key to the one value that is used in that dict
            for key, value in cases_list[num].get("properties").items():
                cases_list[num][key] = value
            cases_list[num].pop("properties")

            # Add comment/notes to case
            case_comments = rest_client.get(f"/incidents/{cases_list[num].get('id')}/comments")
            if case_comments:
                cases_list[num]["comments"] = []
                for comment_num in range(len(case_comments)):
                    cases_list[num]["comments"].append({
                        "id": case_comments[comment_num].get("id"),
                        "content": case_comments[comment_num].get("text").replace("<div>","").replace("</div>","")
                    })

        return cases_list, err_msg

    def _build_search_query(search_fields, open_cases=True):
        """
        Build the json structure needed to search for cases
        :param search_fields: (dict/list) Key/value pairs to search custom fields with specific values.
                                        If a value contains "*" then a search is used with 'has_a_value'
        NOTE: search_fields works on custom fields
        :return query_string: (dict) json stucture used for cases searching
        """
        query = {
            "filters": [{ "conditions": [] }],
            "sorts": [{
                "field_name": "create_date",
                "type": "desc"
            }]
        }

        if open_cases:
            field_search = {"field_name": "plan_status",
                            "method": "equals",
                            "value": "A"}
            query['filters'][0]['conditions'].append(field_search)

        if isinstance(search_fields, dict):
            for search_field, search_value in search_fields.items():
                field_search = {"field_name": f"properties.{search_field}"}
                if isinstance(search_value, bool):
                    field_search['method'] = "has_a_value" if search_value else "does_not_have_a_value"
                else:
                    field_search['method'] = "equals"
                    field_search['value'] = search_value

                query['filters'][0]['conditions'].append(field_search)

        return query

class JiraCommon():
    """ Common methods for accessing Jira issues """

    def str_time_to_int_time(str_time):
        """
        Convert time string to integer epoch time
        :param str_time: Time in string
        :return: Epoch time as integer
        """
        str_time = str_time[:str_time.rindex(".")]
        return int(datetime.strptime(str_time, "%Y-%m-%dT%H:%M:%S").timestamp() * 1e3)

    def search_jira_issues(jira_client, search_filters, max_results=50):
        """
        Search for Jira issues with given filters
        :param jira_client: Client connection to Jira
        :param search_filters: Search filters for Jira
        :param max_results: Max number of issues that can be returned from Jira issue search
        """

        issues_list = jira_client.search_issues(search_filters,
            maxResults=max_results,
            fields=["issuetype", "project", "priority", "updated", "status", "description", "attachment", "summary", "comment", "created"],
            json_result=True).get("issues")

        # Format each dictionary
        for issue in issues_list:
            issue.pop("expand")

            for key, value in issue.get("fields").items():
                issue[key] = value
            issue.pop("fields")

            # Change the value of the dict key to the one value that is used in that dict
            for key, value in {"issuetype": "name", "project": "key", "priority": "name", "status": "name", "comment": "comments"}.items():
                if issue.get(key):
                    issue[key] = issue[key].get(value)

            # Create a list of just comment string
            comments = issue.get("comment")
            if comments:
                for num in range(len(comments)):
                    comments[num] = comments[num].get("body")

            # Convert the string times to integer epoch time
            issue["created"] = JiraCommon.str_time_to_int_time(issue.get("created"))
            issue["updated"] = JiraCommon.str_time_to_int_time(issue.get("updated"))

        return issues_list
