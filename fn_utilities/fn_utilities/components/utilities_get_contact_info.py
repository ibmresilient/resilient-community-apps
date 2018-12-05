# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_get_contact_info'.
        Returns contact info for an incident or task owner, and incident or task members.
        Ex:
        {'owner': {'fname': 'Resilient', 'lname': 'Sysadmin', 'title': '', 'display_name': 'Resilient Sysadmin', 'email': 'b@a.com', 'phone': '781 838 4848', 'cell': '978 373 2839'}, 'members': []}
        {'owner': None, 'members': [{'fname': 'Resilient', 'lname': 'Sysadmin', 'title': '', 'display_name': 'Resilient Sysadmin', 'email': 'b@a.com', 'phone': '781 838 4848', 'cell': '978 373 2839'}]}
    """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

    @function("utilities_get_contact_info")
    def _fn_get_contact_info_function(self, event, *args, **kwargs):
        """Function: Retrieve contact information for an incidents owner and members or those from a task"""
        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)

            if incident_id is None:
                raise ValueError("incident_id is required")

            yield StatusMessage("starting...")
            res_client = self.rest_client()
            if incident_id and task_id is None:
                results = self.get_contact_info_by_incident(res_client, incident_id)
            else:
                results = self.get_contact_info_by_task(res_client, incident_id, task_id)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()

    def get_contact_info_by_incident(self, res_client, incident_id):
        """
        get owner and member contact information for an incident
        :param res_client:
        :param incident_id:
        :return: json owner and member information
        """

        # get the incident's members
        incident_info = res_client.get('/incidents/{}'.format(incident_id))

        result = {
            "owner": self.get_contact_info_for_uid(res_client, incident_info.get("owner_id")),
            "members": self.get_members_contact_info(res_client, incident_info.get("members"))
        }

        return result

    def get_contact_info_by_task(self, res_client, incident_id, task_id):
        """
        get owner and member contact information for a task. If the task is a public task, all the incident
        members are returned. If a private task, the task members are returned.
        :param res_client:
        :param incident_id:
        :param task_id:
        :return: json owner and member information
        """

        # get task information
        task_info = res_client.get('/tasks/{}'.format(task_id))

        result = {
            "owner": self.get_contact_info_for_uid(res_client, task_info.get("owner_id"))
        }

        # private tasks have at least "members": []
        if task_info.get("members"):
            members = self.get_members_contact_info(res_client, task_info.get("members"))
        else:
            # get the incident's members
            incident_info = res_client.get('/incidents/{}'.format(incident_id))
            members = self.get_members_contact_info(res_client, incident_info.get("members"))

        result['members'] = members
        return result

    def get_members_contact_info(self, res_client, member_list):
        """
        For a member list, return contact information for all
        :param member_list:
        :return: list of member contact information
        """
        result = []

        for member in member_list:
            result.append(self.get_contact_info_for_uid(res_client, member))

        return result


    def get_contact_info_for_uid(self, res_client, uid):
        """
        return contact information for a user
        :param uid:
        :return: JSON contact information
        """
        result = {}
        try:
            user_data = res_client.get('/users/{}'.format(uid))
            result = {  "fname": user_data.get("fname"),
                        "lname": user_data.get("lname"),
                        "title": user_data.get("title"),
                        "display_name": user_data.get("display_name"),
                        "email": user_data.get("email"),
                        "phone": user_data.get("phone"),
                        "cell": user_data.get("cell")
                        }
        except Exception:
            return None

        return result