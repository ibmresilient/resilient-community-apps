# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'fn_get_contact_info'.
        Returns contact info for an incident or task owner, and incident or task members.
        Ex:
        {'owner': {'fname': 'SOAR', 'lname': 'Sysadmin', 'title': '', 'display_name': 'SOAR Sysadmin', 'email': 'b@a.com', 'phone': '781 838 4848', 'cell': '978 373 2839'}, 'members': []}
        {'owner': None, 'members': [{'fname': 'SOAR', 'lname': 'Sysadmin', 'title': '', 'display_name': 'SOAR Sysadmin', 'email': 'b@a.com', 'phone': '781 838 4848', 'cell': '978 373 2839'}]}
    """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

    @function("soar_utils_get_contact_info")
    def _fn_get_contact_info_function(self, event, *args, **kwargs):
        """Function: Retrieve contact information for an incidents owner and members or those from a task"""
        try:
            validate_fields(["incident_id"], kwargs)
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number

            log = getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)

            yield StatusMessage("starting...")
            res_client = self.rest_client()
            if incident_id and not task_id:
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
        incident_info = res_client.get(f'/incidents/{incident_id}')

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
        task_info = res_client.get(f'/tasks/{task_id}')

        result = {
            "owner": self.get_contact_info_for_uid(res_client, task_info.get("owner_id"))
        }

        # private tasks have at least "members": []
        if task_info.get("members"):
            members = self.get_members_contact_info(res_client, task_info.get("members"))
        else:
            # get the incident's members
            incident_info = res_client.get(f'/incidents/{incident_id}')
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
            contact_info = self.get_contact_info_for_uid(res_client, member)
            if not contact_info:
                contact_info = self.get_group_info_for_uid(res_client, member)

            if contact_info:
                result.append(contact_info)

        return result

    def get_contact_info_for_uid(self, res_client, uid):
        """
            return contact information for a user
            :param uid:
            :return: JSON contact information
        """
        try:
            user_data = res_client.get(f'/users/{uid}')
            return {"fname": user_data.get("fname", None),
                "lname": user_data.get("lname", None),
                "title": user_data.get("title", None),
                "display_name": user_data.get("display_name", None),
                "email": user_data.get("email", None),
                "phone": user_data.get("phone", None),
                "cell": user_data.get("cell", None)}
        except Exception:
            return

    def get_group_info_for_uid(self, res_client, uid):
        """
        return information for a group
        :param uid:
        :return: JSON group information
        """
        try:
            user_data = res_client.get(f'/groups/{uid}')
            return {
                "fname": None,
                "lname": None,
                "title": None,
                "display_name": user_data.get("name"),
                "email": None,
                "phone": None,
                "cell": None
            }
        except Exception:
            return
