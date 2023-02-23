# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Poller Helper"""

from resilient_lib import SOARCommon
from fn_jira.util.helper import remove_html_tags

# Helper functions for processing SOAR cases
class SOAR():

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
        case_tasks = SOARCommon(rest_client)._get_case_info(case_id, "tasks?want_notes=true")
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
                    case_datatables = SOARCommon(rest_client)._get_case_info(case_id, "table_data?handle_format=names")
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
        case_field = SOARCommon(rest_client)._get_case_info(cases_list[num].get('id'), f"{field_name}{url_end}")
        if case_field:
            cases_list[num][field_name] = []
            for field_num in range(len(case_field)):
                field_dict = {"id": case_field[field_num].get("id")}
                if field_name == "comments":
                    field_dict["content"] = case_field[field_num].get("text").replace("<div>","").replace("</div>","")
                if field_name == "attachments":
                    field_dict["name"] = case_field[field_num].get("name")
                cases_list[num][field_name].append(field_dict)

def update_task_comments(res_client, task, jira):
    """
    Update the task comments
    :param task: Dictionary of data from the SOAR task
    :param jira: Dictionary of data from the Jira issue
    :param res_client: Connection to SOAR
    :return: None
    """
    # Remove all html tags from the task notes
    for num in range(len(task.get("notes"))):
        task["notes"][num] = remove_html_tags(task["notes"][num].replace("<br/>Added from Jira", ""))

    # Update comments/notes
    comments = jira.get("fields").get("comment")
    if comments:
        for comment in comments:
            if comment not in task.get("notes"):
                comment_payload = {
                    "text": {
                        "format": "text",
                        "content": f"{comment}\nAdded from Jira"
                    },
                    "is_deleted": False
                }
                res_client.post(f"/tasks/{task.get('id')}/comments", comment_payload)

def update_task_attachments(jira, task, res_client):
    """
    Update task attachments
    :param task: Dictionary of data from the SOAR task
    :param jira: Dictionary of data from the Jira issue
    :param res_client: Connection to SOAR
    :return: None
    """
    attachments = jira.get("fields").get("attachment")
    if attachments:
        task_attachments = [att.get("name") for att in task.get("attachments")]
        for attach in attachments:
            filename = attach.get("filename")
            if filename not in task_attachments:
                res_client.post_attachment(f"/tasks/{task.get('id')}/attachments", filepath=None, filename=filename, bytes_handle=attach.get("content"))

def update_task_datatable(task, jira, res_client):
    """
    Update data table on SOAR with new information from the updated task
    :param task: Dictionary of data from the SOAR task
    :param jira: Dictionary of data from the Jira issue
    :param res_client: Connection to SOAR
    :return: None
    """
    datatable = task.get('datatable')
    datatable_cells = datatable.get("cells")

    d_payload = {
        "id": datatable.get("id"),
        "version": datatable.get("version")
    }
    d_payload["cells"] = {cell: { "value": datatable_cells[cell].get("value")} for cell in datatable_cells}
    d_payload["cells"]["last_updated"]["value"] = jira.get("fields").get("updated")
    d_payload["cells"]["status"]["value"] = jira.get("fields").get("status").get("name")

    res_client.put(f"/incidents/{task.get('inc_id')}/table_data/{datatable.get('table_id')}/row_data/{datatable.get('id')}", d_payload)
