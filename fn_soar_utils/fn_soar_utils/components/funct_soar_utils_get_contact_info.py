# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'fn_get_contact_info'.
        Returns contact info for an incident or task owner, and incident or task members.
      
        
        Example Returns:
        1. Individual owner:
        {
            "owner": {"owner_type": "individual", "owner_info": {"display_name": "admin example", "email": "admin@example.com"}},
            "members": [{"display_name": "admin2 example", "email": "admin2@example.com"}, {"display_name": "admin3 example", "email": "admin3@example.com"}]
        }

        2. Group owner:
        {
            "owner": {"owner_type": "group", "group_name": "Developer", "members": ["admin2 example", "admin3 example", "admin example"]},
            "members": [...]
        }
        """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super().__init__(opts)

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
            "owner": self.get_owner_contact_info(res_client, incident_info.get("owner_id")),
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
            "owner": self.get_owner_contact_info(res_client, task_info.get("owner_id"))
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

    def get_owner_contact_info(self, res_client, owner_id):

        """
        Returns detailed contact info for an owner (individual or group).

        Args:
            res_client: Client to fetch user/group info.
            owner_id: ID of the owner.

        Returns:
            dict: {
                "owner_type": "individual" | "group" | "unknown",
                "owner_id": str,
                "owner_info": dict | None,
                "group_name": str (if group),
                "members": list of str (if group),
                }
        """

        try:
            owner_contact_info = self.get_contact_info_for_uid(res_client, owner_id)
            if owner_contact_info:
                return {
                    "owner_type": "individual",
                    "owner_info": owner_contact_info
                }
            group_info = self.get_group_info_for_uid(res_client, owner_id)
            if not group_info:
                return {
                    "owner_type": "unknown",
                    "owner_info": None
                }
            group_name = group_info.get("display_name", "Unknown Group")
            member_ids = group_info.get("members", [])
            members_info = []
            for member_id in member_ids:
                member_contact_info = self.get_contact_info_for_uid(res_client, member_id)
                if member_contact_info:
                    members_info.append(member_contact_info.get("display_name", "Unknown User"))

            return {
                "owner_type": "group",
                "group_name": group_name,
                "members": members_info
            }

        except Exception:
            return

    def get_members_contact_info(self, res_client, member_list):
        """
        For a member list, return contact information for all
        :param member_list:
        :return: list of member contact information
        """

        result = []

        for member in member_list:
            contact_info = self.get_contact_info_for_uid(res_client, member)

            if contact_info:
                result.append(contact_info)
            else:
                # If not a user, checking as a group
                group_info = self.get_group_info_for_uid(res_client, member)
                if group_info:
                    group_members = group_info.get("members", [])
                    for group_member_id in group_members:
                        member_contact = self.get_contact_info_for_uid(res_client, group_member_id)
                        if member_contact:
                            result.append(member_contact)

        return result

    def get_contact_info_for_uid(self, res_client, uid):
        """
            return contact information for a user
            :param uid:
            :return: JSON contact information
        """
        try:
            NOT_A_USER = 403
            user_data = res_client.get(f'/users/{uid}', skip_retry=NOT_A_USER)
            return {"fname": user_data.get("fname", None),
                "lname": user_data.get("lname", None),
                "title": user_data.get("title", None),
                "display_name": user_data.get("display_name", None),
                "email": user_data.get("email", None),
                "phone": user_data.get("phone", None),
                "cell": user_data.get("cell", None)}
        except Exception as e:
            log = getLogger(__name__)
            if "Forbidden" in str(e):
                log.info("UID %s is likely a group, not a user. Checking for a group.", uid)
            else:
                log.info("Error retrieving user info for UID %s: %s",uid, e)
            return None


    def get_group_info_for_uid(self, res_client, uid):
        """
        return information for a group
        :param uid:
        :return: JSON group information
        """
        try:
            user_data = res_client.get(f'/groups/{uid}')
            return {
                "members": user_data.get("members", []),
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
