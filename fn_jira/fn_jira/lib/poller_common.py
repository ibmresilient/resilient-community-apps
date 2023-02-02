# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

import functools
from datetime import datetime
from logging import getLogger
from threading import Event
from traceback import format_exc
from fn_jira.util.helper import get_id_from_jira_issue_description, check_jira_issue_linked_to_task, PACKAGE_NAME

LOG = getLogger(__name__)

# P O L L E R   L O G I C
def poller(named_poller_interval, named_last_poller_time):
    """
    :param named_poller_interval: name of instance variable containing the poller interval in seconds
    :type named_poller_interval: str
    :param named_last_poller_time: name of instance variable containing the lookback value in mseconds
    :type named_last_poller_time: datetime
    """
    def poller_wrapper(func):
        # Decorator for running a function forever, passing the ms timestamp of
        # when the last poller run to the function it's calling
        @functools.wraps(func)
        def wrapped(self, *args):
            last_poller_time = getattr(self, named_last_poller_time)
            exit_event = Event()

            while not exit_event.is_set():
                try:
                    LOG.info("%s polling start.", PACKAGE_NAME)
                    poller_start = datetime.now()
                    # Function execution with the last poller time in ms
                    func(self, *args, last_poller_time=int(last_poller_time.timestamp()*1000))

                except Exception as err:
                    LOG.error(str(err))
                    LOG.error(format_exc())
                finally:
                    LOG.info(f"{PACKAGE_NAME} polling complete.")
                    # Set the last poller time for next cycle
                    last_poller_time = poller_start

                    # Sleep before the next poller execution
                    exit_event.wait(getattr(self, named_poller_interval))
            exit_event.set() # Loop complete

        return wrapped
    return poller_wrapper

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
