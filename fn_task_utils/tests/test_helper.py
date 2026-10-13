# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019

from __future__ import unicode_literals
from pytest_resilient_circuits import BasicResilientMock, resilient_endpoint

import requests_mock
import logging
from tasks_mock import TasksMockHolder
LOG = logging.getLogger(__name__)


class TasksResilientMock(BasicResilientMock):
    data_mocker = TasksMockHolder()
    mock_tasks_list = data_mocker.get_tasks_list()
    LOG.info("Mock tasks before %s", mock_tasks_list)

    LOG.info("Mock tasks after %s", mock_tasks_list)
    task_mock = data_mocker.get_single_task_mock()

    # A list of mock comments
    task_notes_mock = data_mocker.get_mock_notes_for_task()

    # Task Endpoints for the TaskREST Resourcee related to CRUD operations on tasks.

    @resilient_endpoint("GET", "/tasks/[0-9]+$")
    def task_get(self, request):
        """ Callback for GET to /orgs/<org_id>/tasks/<task_id>/ """
        LOG.debug("task_get")

        if "9999" in request.url: # Sentinel Task ID used for when we want to fail task get
            return requests_mock.create_response(request,
                                                 status_code=404,
                                                 json={
                                                  "success": False,
                                                  "title": None,
                                                  "message": "Unable to find object with ID 9,999",
                                                  "hints": [],
                                                  "error_code": "generic"
                                                })
        else:
            return requests_mock.create_response(request,
                                                 status_code=200,
                                                 json=self.task_mock)

    @resilient_endpoint("PUT", "/tasks/[0-9]+$")
    def task_put(self, request):
        """ Callback for GET to /orgs/<org_id>/tasks/<task_id>/ """
        LOG.debug("task_put")
        return requests_mock.create_response(request,
                                             status_code=200,
                                             json=self.task_mock)

    @resilient_endpoint("GET", "/tasks/[0-9]+/instructions")
    def tasks_get_instructions(self, request):
        """ Callback for GET to /orgs/<org_id>/tasks/<task_id>/instructions """
        LOG.debug("tasks_get_instructions")
        data = b"""Test task instructions <br> Test task instructions<br><br>"""

        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=data)

    # Task Endpoints for the IncidentRest Resource

    @resilient_endpoint("POST", "incidents/[0-9]+/tasks")
    def task_create(self, request):
        """ Callback for GET to /orgs/<org_id>/tasks/<inc_id> """
        LOG.debug("task_post")
        self.task_mock["name"] = request.json()["name"]

        return requests_mock.create_response(request,
                                             status_code=200,
                                             json=self.task_mock)

    @resilient_endpoint("GET", "/incidents/[0-9]+/tasks\?want_layouts=false\&want_notes=false$")
    def incident_get_tasks(self, request):
        """ GET tasks instructions /orgs/<org_id>/incidents/tasks/"""
        LOG.debug("incident_get_tasks")

        return requests_mock.create_response(request,
                                             status_code=200,
                                             json=self.mock_tasks_list)

    # Task Note Mock Endpoints for the TaskRest Resource

    @resilient_endpoint("GET", "/tasks/[0-9]+/comments")
    def task_note_get(self, request):
        """ Callback for GET to /orgs/<org_id>/tasks/<task_id>/comments"""
        LOG.debug("task_note_get")

        return requests_mock.create_response(request,
                                                 status_code=200,
                                                 json=self.task_notes_mock)

    @resilient_endpoint("POST", "/tasks/[0-9]+/comments")
    def task_note_post(self, request):
        """ Callback for POST to /orgs/<org_id>/tasks/<task_id>/comments"""
        LOG.debug("task_note_put")

        # A new note is added to the task. Append it to our common TaskNoteMock
        self.task_notes_mock.append(request.json())
        LOG.info(self.task_notes_mock)

        return requests_mock.create_response(request,
                                             status_code=200,
                                             json=self.task_notes_mock)

    @resilient_endpoint("POST", "/rest/session")
    def session_post(self, request):
        """ Callback for POST to /rest/session """
        LOG.debug("session_post")
        session_data = {
            "saml_alias": None,
            "csrf_token": "79945884c2e6f2339cbffbbaba01f17b",
            "user_lname": "Doe",
            "user_id": 1,
            "is_ldap": False,
            "is_saml": False,
            "orgs": [
                {
                    "city": "AnyCity",
                    "addr": None,
                    "zip": None,
                    "has_available_twofactor": False,
                    "perms": {
                        "create_shared_layout": True,
                        "administrator": False,
                        "create_incs": True,
                        "master_administrator": True,
                        "observer": False
                    },
                    "supports_ldap": False,
                    "enabled": True,
                    "twofactor_auth_domain": None,
                    "attachments_enabled": True,
                    "has_saml": False,
                    "state": None,
                    "addr2": None,
                    "twofactor_cookie_lifetime_secs": 0,
                    "require_saml": False,
                    "tasks_private": False,
                    "authorized_ldap_group": None,
                    "id": 201,
                    "name": self.org_name
                },
                {
                    "city": None,
                    "addr": None,
                    "zip": None,
                    "has_available_twofactor": False,
                    "perms": {
                        "create_shared_layout": True,
                        "administrator": False,
                        "create_incs": True,
                        "master_administrator": True,
                        "observer": False
                    },
                    "supports_ldap": False,
                    "enabled": True,
                    "twofactor_auth_domain": None,
                    "attachments_enabled": True,
                    "has_saml": False,
                    "state": None,
                    "addr2": None,
                    "twofactor_cookie_lifetime_secs": 0,
                    "require_saml": False,
                    "tasks_private": False,
                    "authorized_ldap_group": None,
                    "id": 202,
                    "name": "Mock Org"
                }
            ],
            "session_ip": "192.168.56.1",
            "user_fname": "John",
            "user_email": self.email
        }
        cookies = {'JSESSIONID': 'FakeSessionId'}
        import requests
        return requests_mock.create_response(request,
                                             status_code=200,
                                             cookies=requests.cookies.cookiejar_from_dict(cookies),
                                             json=session_data)



