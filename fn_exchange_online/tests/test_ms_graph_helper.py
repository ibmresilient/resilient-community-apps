# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-

# (c) Copyright IBM Corp. 2020. All Rights Reserved.

import sys
from fn_exchange_online.lib.ms_graph_helper import MSGraphHelper
from resilient_lib.components.integration_errors import IntegrationError

if sys.version_info.major == 2:
    from mock import patch
else:
    from unittest.mock import patch

MOCKED_OPTS = {
    "microsoft_graph_token_url": "microsoft_graph_token_url",
    "microsoft_graph_url": u'microsoft_graph_url',
    "tenant_id": "tenant_id",
    "client_id": "client_id",
    "client_secret": "client_secret",
    "max_messages": "100",
    "max_users": "2000"
}

def generate_response(content, status):
    class simResponse:
        def __init__(self, content, status):
            self.status_code = status
            self.content = content

        def json(self):
            return self.content

    return simResponse(content, status)

class TestMSGraphHelper(object):
    """ Tests for the MSGraphHelper functions"""

    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.get')
    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.authenticate')
    def test_get_user_profile(self, authenticate_mock, get_mock):
        """ Test Get User Profile"""
        print("Test Get User Profile\n")

        try:
            authenticate_mock.return_value = True
            MS_graph_helper = MSGraphHelper(MOCKED_OPTS.get("microsoft_graph_token_url"),
                                            MOCKED_OPTS.get("microsoft_graph_url"),
                                            MOCKED_OPTS.get("tenant_id"),
                                            MOCKED_OPTS.get("client_id"),
                                            MOCKED_OPTS.get("client_secret"),
                                            MOCKED_OPTS.get("max_messages"),
                                            MOCKED_OPTS.get("max_users"),
                                            None)
            content = {"displayName": "Tester"}

            # Test
            get_mock.return_value = generate_response(content, 200)
            response = MS_graph_helper.get_user_profile("tester@example.com")
            assert response.status_code == 200
            assert response.content["displayName"] == "Tester"

            get_mock.return_value = generate_response(content, 404)
            response = MS_graph_helper.get_user_profile("tester@example.com")
            assert response.status_code == 404
            assert response.content["displayName"] == "Tester"

            get_mock.return_value = generate_response(content, 300)
            response = MS_graph_helper.get_user_profile("tester@example.com")

        except IntegrationError as err:
            assert True


    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.delete')
    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.authenticate')
    def test_delete_message(self, authenticate_mock, delete_mock):
        """ Test """
        print("Test Delete Message\n")
        content = {"displayName": "Tester"}

        try:
            authenticate_mock.return_value = True
            MS_graph_helper = MSGraphHelper(MOCKED_OPTS.get("microsoft_graph_token_url"),
                                            MOCKED_OPTS.get("microsoft_graph_url"),
                                            MOCKED_OPTS.get("tenant_id"),
                                            MOCKED_OPTS.get("client_id"),
                                            MOCKED_OPTS.get("client_secret"),
                                            MOCKED_OPTS.get("max_messages"),
                                            MOCKED_OPTS.get("max_users"),
                                            None)

            delete_mock.return_value = generate_response(content, 204)

            response = MS_graph_helper.delete_message("tester@example.com", None, "AAAA")
            assert response.status_code == 204

            delete_mock.return_value = generate_response(content, 300)
            response = MS_graph_helper.delete_message("tester@example.com", None, "AAAA")

        except IntegrationError as err:
            assert True

    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.get')
    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.authenticate')
    def test_get_message(self, authenticate_mock, get_mock):
        """ Test Get Message"""
        print("Test Get Message\n")
        content = {"displayName": "Tester"}

        try:
            authenticate_mock.return_value = True
            MS_graph_helper = MSGraphHelper(MOCKED_OPTS.get("microsoft_graph_token_url"),
                                            MOCKED_OPTS.get("microsoft_graph_url"),
                                            MOCKED_OPTS.get("tenant_id"),
                                            MOCKED_OPTS.get("client_id"),
                                            MOCKED_OPTS.get("client_secret"),
                                            MOCKED_OPTS.get("max_messages"),
                                            MOCKED_OPTS.get("max_users"),
                                            None)

            get_mock.return_value = generate_response(content, 200)

            response = MS_graph_helper.get_message("tester@example.com", "AAA")
            assert response.status_code == 200
            assert response.content["displayName"] == "Tester"

            get_mock.return_value = generate_response(content, 404)
            response = MS_graph_helper.get_message("tester@example.com", "AAA")
            assert response.status_code == 404
            assert response.content["displayName"] == "Tester"

            get_mock.return_value = generate_response(content, 300)
            response = MS_graph_helper.get_message("tester@example.com", "AAA")

        except IntegrationError as err:
            assert True

    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.get')
    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.authenticate')
    def test_get_message_mime(self, authenticate_mock, get_mock):
        """ Test Get Message Mime"""
        print("Test Get Message Mime\n")
        content = {"displayName": "Tester"}

        try:
            authenticate_mock.return_value = True
            MS_graph_helper = MSGraphHelper(MOCKED_OPTS.get("microsoft_graph_token_url"),
                                            MOCKED_OPTS.get("microsoft_graph_url"),
                                            MOCKED_OPTS.get("tenant_id"),
                                            MOCKED_OPTS.get("client_id"),
                                            MOCKED_OPTS.get("client_secret"),
                                            MOCKED_OPTS.get("max_messages"),
                                            MOCKED_OPTS.get("max_users"),
                                            None)

            get_mock.return_value = generate_response(content, 200)

            response = MS_graph_helper.get_message_mime("tester@example.com", "AAA")
            assert response.status_code == 200
            assert response.content["displayName"] == "Tester"

            get_mock.return_value = generate_response(content, 404)
            response = MS_graph_helper.get_message_mime("tester@example.com", "AAA")
            assert response.status_code == 404
            assert response.content["displayName"] == "Tester"

            get_mock.return_value = generate_response(content, 300)
            response = MS_graph_helper.get_message_mime("tester@example.com", "AAA")

        except IntegrationError as err:
            assert True

    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.post')
    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.authenticate')
    def test_move_message(self, authenticate_mock, post_mock):
        """ Test Move Message"""
        print("Test Move Message\n")
        content = {"displayName": "Tester"}

        try:
            authenticate_mock.return_value = True
            MS_graph_helper = MSGraphHelper(MOCKED_OPTS.get("microsoft_graph_token_url"),
                                            MOCKED_OPTS.get("microsoft_graph_url"),
                                            MOCKED_OPTS.get("tenant_id"),
                                            MOCKED_OPTS.get("client_id"),
                                            MOCKED_OPTS.get("client_secret"),
                                            MOCKED_OPTS.get("max_messages"),
                                            MOCKED_OPTS.get("max_users"),
                                            None)

            post_mock.return_value = generate_response(content, 201)

            response = MS_graph_helper.move_message("tester@example.com", None, "AAA", {'name': "recoverableitemsdeletions"})
            assert response.status_code == 201
            assert response.content["displayName"] == "Tester"

            post_mock.return_value = generate_response(content, 404)
            response = MS_graph_helper.move_message("tester@example.com", None, "AAA", {'name': "recoverableitemsdeletions"})
            assert response.status_code == 404
            assert response.content["displayName"] == "Tester"

            post_mock.return_value = generate_response(content, 300)
            response = MS_graph_helper.move_message("tester@example.com", None, "AAA", {'name': "recoverableitemsdeletions"})

        except IntegrationError as err:
            assert True

    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.get')
    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.authenticate')
    def test_get_users(self, authenticate_mock, get_mock):
        """ Test Get User"""
        print("Test Get Users\n")

        try:
            authenticate_mock.return_value = True
            MS_graph_helper = MSGraphHelper(MOCKED_OPTS.get("microsoft_graph_token_url"),
                                            MOCKED_OPTS.get("microsoft_graph_url"),
                                            MOCKED_OPTS.get("tenant_id"),
                                            MOCKED_OPTS.get("client_id"),
                                            MOCKED_OPTS.get("client_secret"),
                                            MOCKED_OPTS.get("max_messages"),
                                            MOCKED_OPTS.get("max_users"),
                                            None)
            content = {
                'value': [{'userPrincipalName': 'tester1@example.com'}, {'userPrincipalName': 'tester2@example.com'}]}
            get_mock.return_value = generate_response(content, 200)

            user_list = MS_graph_helper.get_users()
            assert len(user_list) == 2
            assert user_list[0]['userPrincipalName'] == 'tester1@example.com'
            assert user_list[1]['userPrincipalName'] == 'tester2@example.com'
        except IntegrationError as err:
            assert True

    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.get')
    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.authenticate')
    def test_query_messages_all_users(self, authenticate_mock, mocked_get):
        """ Test Get User"""
        print("Test Query Messages All Users\n")
        try:
            authenticate_mock.return_value = True
            MS_graph_helper = MSGraphHelper(MOCKED_OPTS.get("microsoft_graph_token_url"),
                                            MOCKED_OPTS.get("microsoft_graph_url"),
                                            MOCKED_OPTS.get("tenant_id"),
                                            MOCKED_OPTS.get("client_id"),
                                            MOCKED_OPTS.get("client_secret"),
                                            MOCKED_OPTS.get("max_messages"),
                                            MOCKED_OPTS.get("max_users"),
                                            None)

            # Mock the users
            content1 = {
                'value': [{'userPrincipalName': 'tester1@example.com'}, {'userPrincipalName': 'tester2@example.com'}]}

            # Mock the email lists for user 1
            content2 = {'value': [{'id': 'AAA'}, {'id': 'BBB'}]}

            # Mock the email lists for user 2
            content3 = {'value': [{'id': 'CCC'}]}

            mocked_get.side_effect = [generate_response(content1, 200),
                                      generate_response(content2, 200),
                                      generate_response(content3, 200)]

            email_list = MS_graph_helper.query_messages("all", None, None, None, None, None, "lunch", None)
            assert len(email_list) == 2
            assert email_list[0]['email_address'] == 'tester1@example.com'
            assert email_list[0]['status_code'] == 200
            assert email_list[0]['email_list'][0]['id'] == 'AAA'
            assert email_list[0]['email_list'][1]['id'] == 'BBB'
            assert email_list[1]['email_address'] == 'tester2@example.com'
            assert email_list[1]['status_code'] == 200
            assert email_list[1]['email_list'][0]['id'] == 'CCC'
        except IntegrationError as err:
            assert True

    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.get')
    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.authenticate')
    def test_query_messages(self, authenticate_mock, mocked_get):
        """ Test Get User"""
        print("Test Query Messages Single User\n")
        try:
            authenticate_mock.return_value = True
            MS_graph_helper = MSGraphHelper(MOCKED_OPTS.get("microsoft_graph_token_url"),
                                            MOCKED_OPTS.get("microsoft_graph_url"),
                                            MOCKED_OPTS.get("tenant_id"),
                                            MOCKED_OPTS.get("client_id"),
                                            MOCKED_OPTS.get("client_secret"),
                                            MOCKED_OPTS.get("max_messages"),
                                            MOCKED_OPTS.get("max_users"),
                                            None)

            # Mock the email lists for user 1
            content1 = {'value': [{'id': 'AAA'}, {'id': 'BBB'}]}

            mocked_get.side_effect = [generate_response(content1, 200)]

            result_list = MS_graph_helper.query_messages("tester1@example.com", None, "tester2@example.com", None,
                                                         None, None, "lunch", None)
            assert len(result_list) == 1
            assert result_list[0]['email_address'] == 'tester1@example.com'
            assert result_list[0]['status_code'] == 200
            assert result_list[0]['email_list'][0]['id'] == 'AAA'
            assert result_list[0]['email_list'][1]['id'] == 'BBB'

            mocked_get.side_effect = [generate_response(content1, 404)]
            result_list = MS_graph_helper.query_messages("tester1@example.com", None, None, None, None, None, "lunch",
                                                         None)
            assert len(result_list) == 1
            assert result_list[0]['status_code'] == 404
            assert len(result_list[0]['email_list']) == 0

            mocked_get.side_effect = [generate_response(content1, 300)]
            result_list = MS_graph_helper.query_messages("tester1@example.com", None, None, None, None, None, "lunch",
                                                         None)
        except IntegrationError as err:
            assert True

    @patch('fn_exchange_online.lib.ms_graph_helper.OAuth2ClientCredentialsSession.authenticate')
    def test_build_query_url(self, authenticate_mock):
        """ Test Build Query URL"""
        print("Test build MS Graph Query URL\n")
        try:
            authenticate_mock.return_value = True
            MS_graph_helper = MSGraphHelper(MOCKED_OPTS.get("microsoft_graph_token_url"),
                                            MOCKED_OPTS.get("microsoft_graph_url"),
                                            MOCKED_OPTS.get("tenant_id"),
                                            MOCKED_OPTS.get("client_id"),
                                            MOCKED_OPTS.get("client_secret"),
                                            MOCKED_OPTS.get("max_messages"),
                                            MOCKED_OPTS.get("max_users"),
                                            None)

            # Param list: email_address, mail_folder, sender, start_date, end_date, has_attachments, message_subject,
            # message_body
            # Test sender, hasAttachments, message subject
            url = MS_graph_helper.build_MS_graph_query_url("tester1@example.com", None, "tester2@example.com", None,
                                                           None, True, "lunch", None)
            assert url == u'microsoft_graph_url/users/tester1@example.com/messages?$filter=(from/emailAddress/address%20eq%20"tester2@example.com")%20and%20(hasAttachments%20eq%20true)%20and%20(contains(subject,\'lunch\'))'

            # Test $search in query (message body)
            url = MS_graph_helper.build_MS_graph_query_url("tester1@example.com", None, "tester2@example.com", None,
                                                           None, True, None, "lunch")
            assert url == u'microsoft_graph_url/users/tester1@example.com/messages?$search="lunch"&?$filter=(from/emailAddress/address%20eq%20"tester2@example.com")%20and%20(hasAttachments%20eq%20true)'

            # Test query: sender, start date, hasAttachments
            url = MS_graph_helper.build_MS_graph_query_url("tester1@example.com", None, "tester2@example.com",
                                                           1577854800000, None, True, None, None)
            assert url == u'microsoft_graph_url/users/tester1@example.com/messages?$filter=(receivedDateTime%20ge%202020-01-01T00:00:00Z)%20and%20(from/emailAddress/address%20eq%20"tester2@example.com")%20and%20(hasAttachments%20eq%20true)'

            # Test $search in query (sender, start date, hasAttachments)
            url = MS_graph_helper.build_MS_graph_query_url("tester1@example.com", None, "tester2@example.com",
                                                           1577854800000, None, None, None, "lunch")
            assert url == u'microsoft_graph_url/users/tester1@example.com/messages?$search="lunch"&?$filter=(receivedDateTime%20ge%202020-01-01T00:00:00Z)%20and%20(from/emailAddress/address%20eq%20"tester2@example.com")'

            # Test $search in query sender, start and end date
            url = MS_graph_helper.build_MS_graph_query_url("tester1@example.com", None, "tester2@example.com",
                                                           1577854800000, 1577895870000, None, None, "lunch")
            assert url == u'microsoft_graph_url/users/tester1@example.com/messages?$search="lunch"&?$filter=(receivedDateTime%20ge%202020-01-01T00:00:00Z)%20and%20(receivedDateTime%20le%202020-01-01T11:24:30Z)%20and%20(from/emailAddress/address%20eq%20"tester2@example.com")'

            # No query parameters will cause IntegrationError
            url = MS_graph_helper.build_MS_graph_query_url("tester1@example.com", None, None, None, None, None, None,
                                                           None)
        except IntegrationError as err:
            assert True
