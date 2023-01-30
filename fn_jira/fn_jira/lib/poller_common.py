# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

import functools
from datetime import datetime
from logging import getLogger
from threading import Event
from traceback import format_exc
from resilient import SimpleHTTPException
from fn_jira.util.helper import get_id_from_jira_issue_description, check_jira_issue_linked_to_task

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

    def get_open_soar_cases(opts, search_fields, rest_client, data_to_get_from_case, open_cases=True):
        """
        Find all IBM SOAR cases which are associated with the endpoint platform
        :param search_fields: (dict) List of field(s) used to track the relationship with a SOAR case
                                    field values can be True/False for 'has_a_value' or 'does_not_have_a_value'
                                    Otherwise a field will use 'equals' for the value
        NOTE: search_fields only supports custom fields
        :param data_to_get_from_case: Dictionary of dicts that say what info to get from each SOAR case
        :return soar_cases: (list) Returned list of cases
        :return error_msg: (str) Any error during the query or None
        """
        fields_to_remove = ["perms", "creator", "creator_principal", "exposure_type_id", "workspace", "assessment", "pii",
                            "gdpr", "creator_id", "crimestatus_id", "sequence_code", "owner_id", "plan_status", "phase_id",
                            "org_handle", "task_changes"]

        query = SOARCommon._build_search_query(search_fields, open_cases=open_cases)

        # List of all returned SOAR case dictionaries
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

            # Get the date that needs to be added to the current SOAR case
            data_to_get = data_to_get_from_case.get(cases_list[num].get("jira_issue_id"))
            if data_to_get:

                if data_to_get.get("comments"): # If comments were on the linked Jira ticket
                    # Add comment/notes to case
                    SOARCommon.add_to_case(rest_client, cases_list, num, "comments")

                if data_to_get.get("attachments"): # If attachments were on the linked Jira ticket
                    # Add attachments to cases
                    SOARCommon.add_to_case(rest_client, cases_list, num, "attachments")

            tasks = data_to_get_from_case.get("tasks")
            if tasks:
                for task in tasks:
                    if task.get("incident_id") == cases_list[num].get("id"):
                        task_data_to_get = data_to_get_from_case.get(task.get("task_key"))
                        if task_data_to_get:
                            SOARCommon.add_task_to_case(rest_client,
                                                        cases_list,
                                                        num,
                                                        task.get("task_id"),
                                                        comments=task_data_to_get.get("comments"),
                                                        attachments=task_data_to_get.get("attachments")
                                                       )

        return cases_list, err_msg

    def add_task_to_case(rest_client, cases_list, num, id, comments=False, attachments=False):
        """
        Adds task data to the SOAR case
        :param rest_client: Client connection to SOAR
        :param cases_list: List of SOAR cases
        :param num: The index of the case in case_list
        :param id: Task ID
        :param comments: Boolean if to add comments
        :param attachments: Boolean if to add attachments
        :return: None
        """
        case_id = cases_list[num].get('id')

        # Add Tasks to cases
        case_tasks = rest_client.get(f"/incidents/{case_id}/tasks?want_notes=true")
        if case_tasks:
            # Add tasks field to the case if the field does not exist
            task = cases_list[num].get("tasks")
            cases_list[num]["tasks"] = task if task else []
            del task # Delete variable that is no longer needed

            for task_num in range(len(case_tasks)):
                task_id = case_tasks[task_num].get("id")
                if id == task_id:
                    cases_list[num]["tasks"].append(
                        {k: v for k, v in case_tasks[task_num].items()\
                            if v is not None and \
                                k not in ["perms", "actions", "playbooks", "creator_principal", "regs", "notes_count", "attachments_count", "inc_owner_id", "user_notes", "auto_deactivate", "phase_id"]}
                    )
                    case_task_num = len(cases_list[num]["tasks"])-1

                    # Get notes
                    if comments:
                        task_notes = case_tasks[task_num].get("notes")
                        cases_list[num]["tasks"][case_task_num]["notes"] = []
                        for note_num in range(len(task_notes)):
                            cases_list[num]["tasks"][case_task_num]["notes"].append(
                                task_notes[note_num].get("text")
                            )
                    else:
                        cases_list[num]["tasks"][case_task_num]["notes"] = []

                    del comments

                    # Get attachments
                    if attachments:
                        task_attachments = rest_client.get(f"/tasks/{task_id}/attachments")
                        cases_list[num]["tasks"][case_task_num]["attachments"] = []
                        for attach_num in range(len(task_attachments)):
                            cases_list[num]["tasks"][case_task_num]["attachments"].append({
                                "id": task_attachments[attach_num].get("id"),
                                "name": task_attachments[attach_num].get("name")
                            })
                    else:
                        cases_list[num]["tasks"][case_task_num]["attachments"] = []

                    # Add the data table that contains the task info to the task
                    case_datatables = rest_client.get(f"/incidents/{case_id}/table_data?handle_format=names")
                    if case_datatables:
                        found = False
                        for datatable in case_datatables:
                            if found:
                                break
                            for row in case_datatables[datatable].get("rows"):
                                if str(id) == row["cells"].get("task_id").get("value"):
                                    found = True
                                    for field in ["actions", "playbooks", "inc_owner", "inc_name"]:
                                        row.pop(field)
                                    cases_list[num]["tasks"][case_task_num]["datatable"] = row
                                    cases_list[num]["tasks"][case_task_num]["datatable"]["table_id"] = case_datatables[datatable].get("id")
                                    break
                    break

    def add_to_case(rest_client, cases_list, num, field_name):
        """
        Function adds comments and attachments on the SOAR incident to the case in the list
        :param rest_client: Client connection to SOAR
        :param cases_list: List of SOAR cases
        :param num: The index of the case in case_list
        :param field_name: Name of the field to add. Either 'attachments' or 'comments'
        :return: None
        """
        url_end = '?want_notes=true' if field_name == 'tasks' else ''
        case_field = rest_client.get(f"/incidents/{cases_list[num].get('id')}/{field_name}{url_end}")
        if case_field:
            cases_list[num][field_name] = []
            for field_num in range(len(case_field)):
                field_dict = {"id": case_field[field_num].get("id")}
                if field_name == "comments":
                    field_dict["content"] = case_field[field_num].get("text").replace("<div>","").replace("</div>","")
                if field_name == "attachments":
                    field_dict["name"] = case_field[field_num].get("name")
                cases_list[num][field_name].append(field_dict)

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

    def search_jira_issues(opts, jira_client, search_filters, last_poller_time=None, max_results=50, data_to_get_from_case=None):
        """
        Search for Jira issues with given filters
        :param jira_client: Client connection to Jira
        :param search_filters: Search filters for Jira
        :param last_poller_time: Last time the poller ran
        :param max_results: Max number of issues that can be returned from Jira issue search
        """

        if last_poller_time:
            search_filters = f"{search_filters} and updated > '{last_poller_time.strftime('%Y/%m/%d %H:%M')}'"

        issues_list = jira_client.search_issues(
            search_filters,
            maxResults=max_results,
            fields=["issuetype", "project", "priority", "updated", "status", "description", "attachment", "summary", "comment", "created", "resolutiondate"],
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

            if not data_to_get_from_case.get(issue.get("key")):
                data_to_get_from_case[issue.get("key")] = {}

            data_to_get_from_case[issue.get("key")]["comments"] = False
            data_to_get_from_case[issue.get("key")]["attachments"] = False

            # Create a list of just comment string
            comments = issue.get("comment")
            if comments:
                data_to_get_from_case[issue.get("key")]["comments"] = True
                for comment_num in range(len(comments)):
                    comments[comment_num] = comments[comment_num].get("body")

            # Convert the string times to integer epoch time
            issue["created"] = JiraCommon.str_time_to_int_time(issue.get("created"))
            issue["updated"] = JiraCommon.str_time_to_int_time(issue.get("updated"))

            # Create a list of just attachment filenames
            attachments = issue.get("attachment")
            if attachments:
                data_to_get_from_case[issue.get("key")]["attachments"] = True
                for attach_num in range(len(attachments)):
                    attachments[attach_num] = {
                        "filename": attachments[attach_num].get("filename"),
                        "content": jira_client._session.get(attachments[attach_num].get("content")).content
                    }

            issue_description = issue.get("description")
            if check_jira_issue_linked_to_task(issue_description):
                task_id = get_id_from_jira_issue_description(issue_description)
                data_to_get_from_case["tasks"].append({
                    "incident_id": int(issue_description[issue_description.index("incidents/")+10:issue_description.index("?task_id")]),
                    "task_id": task_id,
                    "task_key": issue.get("key")
                })

        return issues_list, data_to_get_from_case
