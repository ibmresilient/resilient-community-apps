# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-
import logging
import sys
if sys.version_info.major >= 3:
    from urllib.parse import quote as url_encode
else:
    from urllib import quote as url_encode
import datetime
from pytz import timezone
import pytz
from tzlocal.windows_tz import win_tz
from resilient_lib import OAuth2ClientCredentialsSession
from requests.packages.urllib3.util import Retry
from requests.adapters import HTTPAdapter
from resilient_lib.components.integration_errors import IntegrationError
from resilient_lib import get_file_attachment_metadata
from fn_exchange_online.lib.resilient_helper import get_incident_file_attachment

LOG = logging.getLogger(__name__)
DEFAULT_SCOPE = 'https://graph.microsoft.com/.default'
TIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
MAX_RETRIES_TOTAL = 3
MAX_RETRIES_BACKOFF_FACTOR = 5
MAX_BATCHED_REQUESTS = 20

class MSGraphHelper(object):
    """
    Helper object MSGraphHelper.
    """
    def __init__(self, ms_graph_token_url, ms_graph_url, tenant_id, client_id, client_secret, max_messages, max_users,
                 max_retries_total, max_retries_backoff_factor, max_batched_requests, proxies=None):
        self.ms_graph_token_url = ms_graph_token_url.format(tenant=tenant_id)
        self.ms_graph_url = ms_graph_url
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.proxies = proxies
        self.max_retries_total = int(max_retries_total)
        self.max_retries_backoff_factor = int(max_retries_backoff_factor)
        self.max_messages = int(max_messages)
        self.current_message_count = 0
        self.max_users = int(max_users)
        self.max_batched_requests = int(max_batched_requests)
        self.ms_graph_session = self.authenticate()

    @staticmethod
    def check_ms_graph_response_code(status_code):
        """
        Check that the request status code: raise an integration error if great than 300 and code is "not found"
        :param status_code: request statues code
        :return:
        """
        if status_code >= 300 and status_code != 404:
            raise IntegrationError("Invalid response from Microsoft Graph API call: status_code = {0}".format(status_code))

    def authenticate(self):
        """
        Authenticate and get oauth2 token for the session.
        """
        session = OAuth2ClientCredentialsSession(url=self.ms_graph_token_url,
                                                 client_id=self.client_id,
                                                 client_secret=self.client_secret,
                                                 scope=DEFAULT_SCOPE,
                                                 proxies=self.proxies)
        session.mount('https://', HTTPAdapter(
            max_retries=Retry(
                total=self.max_retries_total,
                status_forcelist=[429, 500, 502, 503],
                backoff_factor=self.max_retries_backoff_factor,
                respect_retry_after_header=True
            )
        ))

        session.mount('http://', HTTPAdapter(
            max_retries=Retry(
                total=self.max_retries_total,
                status_forcelist=[429, 500, 502, 503],
                backoff_factor=self.max_retries_backoff_factor,
                respect_retry_after_header=True
            )
        ))

        return session

    def get_user_license_details(self, email_address):
        """
        Query MS Graph user profile endpoint using the MS graph session.
        :param email_address: email address of the user license details requested
        :return: requests response from the /users/profile endpoint
        """
        ms_graph_user_license_url = u'{0}/users/{1}/licenseDetails'.format(self.ms_graph_url, email_address)
        response = self.ms_graph_session.get(ms_graph_user_license_url)

        self.check_ms_graph_response_code(response.status_code)
        return response

    def get_user_profile(self, email_address):
        """
        Query MS Graph user profile endpoint using the MS graph session.
        :param email_address: email address of the user profile requested
        :return: requests response from the /users/profile endpoint
        """
        ms_graph_user_profile_url = u'{0}/users/{1}'.format(self.ms_graph_url, email_address)
        response = self.ms_graph_session.get(ms_graph_user_profile_url)

        self.check_ms_graph_response_code(response.status_code)

        return response

    def get_user_mail_folders(self, email_address):
        """
        Query MS Graph user mailFolders endpoint using the MS graph session.
        :param email_address: email address of the user profile requested
        :return: requests response from the /users/mailFolders endpoint
        """
        ms_graph_user_mail_folders = u'{0}/users/{1}/mailFolders'.format(self.ms_graph_url, email_address)
        response = self.ms_graph_session.get(ms_graph_user_mail_folders)

        self.check_ms_graph_response_code(response.status_code)

        return response

    def get_users(self, starts_with):
        """
        Query MS Graph for all users endpoint.
        :return: requests response from the /users/ endpoint which is the list of all users.
        """

        user_list = []
        user_count = 0

        # The maximum number of users that MS Graph will return in one API is 999.  Use $top to specify
        # return 999 users and $select to specify return just the userPrincipalName of the user.
        if starts_with:
            # Use the $filter parameter to get users with email address starting with specific characters.
            ms_graph_users_url = u"{0}/users?$filter=startswith(userPrincipalName,'{1}')&$top=999&$select=userPrincipalName".format(self.ms_graph_url, starts_with)
        else:
            ms_graph_users_url = u"{0}/users?$top=999&$select=userPrincipalName".format(self.ms_graph_url)

        while ms_graph_users_url and user_count <= self.max_users:

            response = self.ms_graph_session.get(ms_graph_users_url)
            self.check_ms_graph_response_code(response.status_code)
            json_response = response.json()

            for user in json_response['value']:
                email_address = user['userPrincipalName']
                user_list.append(email_address)

            # Keep track of the total users retrieved so far.
            user_count = len(user_list)

            # Get URL for the next batch of results.
            ms_graph_users_url = json_response.get('@odata.nextLink')

        LOG.info("get_users: Number of Exchange Online users to query: {}".format(user_count))
        LOG.debug(user_list)
        return user_list

    def get_message(self, email_address, message_id):
        """
        Call MS Graph to get message json.
        :param email_address: email address of the user's mailbox from which to get the message
        :param message_id: message id of the message to get
        :return: requests get response for the message to retrieve
        """
        ms_graph_users_url = u'{0}/users/{1}/messages/{2}'.format(self.ms_graph_url, email_address, message_id)

        response = self.ms_graph_session.get(ms_graph_users_url)

        self.check_ms_graph_response_code(response.status_code)

        return response

    def get_message_mime(self, email_address, message_id):
        """
        Call MS Graph to get message mime content.
        :param email_address: email address of the user's mailbox from which to get the message
        :param message_id: message id of the message to get
        :return: requests get response for the message to retrieve
        """
        ms_graph_users_url = u'{0}/users/{1}/messages/{2}/$value'.format(self.ms_graph_url, email_address, message_id)

        response = self.ms_graph_session.get(ms_graph_users_url)

        self.check_ms_graph_response_code(response.status_code)

        return response

    def delete_message(self, email_address, mail_folder, message_id):
        """
        Call MS Graph to delete message.
        :param email_address: email address of the user's mailbox from which to delete the message
        :param mail_folder: mailFolder id of the folder containing the message to be deleted
        :param message_id: message id of the message to be deleted
        :return: requests response from the /users/ endpoint which is the list of all users.
        """
        mail_folder_string = self.build_folder_string(mail_folder)

        ms_graph_users_url = u'{0}/users/{1}{2}/messages/{3}'.format(self.ms_graph_url, email_address,
                                                                     mail_folder_string, message_id)

        response = self.ms_graph_session.delete(ms_graph_users_url)

        self.check_ms_graph_response_code(response.status_code)

        return response

    def delete_messages_from_query_results(self, query_results):
        """
        :param query_results: query result list returned from Query Message function
        :return: list of messages for each email address search: list of deleted messages from the query results
        ;        and list of messages not deleted from query result
        """

        delete_results = []

        for user in query_results:
            email_address = user.get('email_address')
            deleted_list = []
            not_deleted_list = []
            for message in user.get('email_list'):

                # Call MS Graph API to delete the message
                response = self.delete_message(email_address, None, message["id"])

                # If message was deleted a 204 code is returned.
                if response.status_code == 204:
                    deleted_list.append(message)
                else:
                    not_deleted_list.append(message)

            user_delete_results = {'email_address': email_address,
                                   'deleted_list': deleted_list,
                                   'not_deleted_list': not_deleted_list}
            delete_results.append(user_delete_results)

        return delete_results

    def move_message(self, email_address, mail_folder, message_id, dest_folder):
        """
        Call MS Graph to move message.
        :param email_address: email address of the user's mailbox from which to delete the message
        :param message_id: message id of the message to be deleted
        :param mail_folder: mailFolder id of the folder containing the message to be deleted
        :return: requests response from the /users/ endpoint which is the list of all users.
        """
        mail_folder_string = self.build_folder_string(mail_folder)

        ms_graph_users_url = u'{0}/users/{1}{2}/messages/{3}/move'.format(self.ms_graph_url, email_address,
                                                                          mail_folder_string, message_id)

        response = self.ms_graph_session.post(ms_graph_users_url,
                                              headers={'Content-Type': 'application/json'},
                                              json={'destinationId': dest_folder['name']})

        self.check_ms_graph_response_code(response.status_code)

        return response

    def build_attachments(self, attachment_names, incident_id, resilient_client):
        """
        Get attachment data from Resilient and format it for Exchange Online.
        :param attachment_name: name of the attachment in Resilient
        :param incident_id: ID of Resilient incident
        :param resilient_client: Resilient REST API client
        :return: formatted attachment data
        """
        attachments = []
        attachment_names = [item.strip() for item in attachment_names.split(",")]
        for attachment_name in attachment_names:
            base64content, attachment_id = get_incident_file_attachment(resilient_client, incident_id, attachment_name)
            if not attachment_id:
                continue
            contentType = get_file_attachment_metadata(resilient_client, incident_id, attachment_id=attachment_id)["content_type"]
            attachment = {
                    "@odata.type": "#microsoft.graph.fileAttachment",
                    "name": attachment_name,
                    "contentType": contentType,
                    "contentBytes": base64content
                }

            attachments.append(attachment)
            LOG.info(u"Successfully attached %s", attachment_name)
        return attachments

    def send_message(self, sender_address, recipients, subject, body, attachment_names=None, incident_id=None, resilient_client=None):
        """
        Call MS Graph to send message.
        :param sender_address: email address of the message sender
        :param recipients: comma separated list of users to send message to
        :param subject: message subject text
        :param attachment_namse: comma seperated names of incident attachment to send with the message
        :param incident_id: ID of Resilient incident
        :param resilient_client: Resilient REST API client
        :param body: message body text
        :return: requests response from post.
        """

        ms_graph_create_message_url = u'{0}/users/{1}/sendMail'.format(self.ms_graph_url, sender_address)

        # Create recipient list in required format.
        recipient_list = [{'emailAddress': {'address': address.strip()}}
                          for address in recipients.split(',')]

        # Create the message in the required json format
        message_json = {"message": {"subject": subject,
                                    "body": {"contentType": "HTML", "content": body},
                                    "toRecipients": recipient_list},
                        "saveToSentItems": "true"}

        # Build attachment data
        if attachment_names:
            attachments = self.build_attachments(attachment_names, incident_id, resilient_client)
            message_json["message"]["attachments"] = attachments

        response = self.ms_graph_session.post(ms_graph_create_message_url,
                                              headers={'Content-Type': 'application/json'},
                                              json=message_json)

        self.check_ms_graph_response_code(response.status_code)

        return response


    def create_meeting(self, email_address, start_time, end_time, subject, body, required_attendees, optional_attendees,
                       location):
        """
         create_meeting will create an event in the specified email_address user's calandar and send email to the
         required and optional attendee email addresses.
        :param email_address: meeting organizer
        :param start_time: start time of the meeting
        :param end_time: end time of the meeting
        :param subject: subject of the meeting/email
        :param body: body email meeting invitation
        :param required_attendees: list of required attendee email addresses
        :param location: list of optional attendee email addresses
        :return: response from MS Graph API post to calendar/events endpoint
        """
        ms_graph_calender_event_url = u'{0}/users/{1}/calendar/events'.format(self.ms_graph_url, email_address)

        # Get the time zone of the organizer.
        ms_graph_timezone_url = u'{0}/users/{1}/mailboxSettings/timeZone'.format(self.ms_graph_url, email_address)
        response = self.ms_graph_session.get(ms_graph_timezone_url)

        self.check_ms_graph_response_code(response.status_code)

        if response.status_code == 200:
            response_json = response.json()
            windows_time_zone = response_json["value"]
        else:
            # If the timezone is not found (not set) then default to UTC time
            windows_time_zone = "UTC"

        # Convert the Windows time zone to IANA format.
        iana_time_zone = win_tz.get(windows_time_zone)

        # Use pytz with IANA time zone.
        to_zone = timezone(iana_time_zone)

        # Convert the start time to the time zone of the user mailbox
        start = datetime.datetime.utcfromtimestamp(start_time / 1000)
        start_tz = start.replace(tzinfo=pytz.utc).astimezone(to_zone).strftime(TIME_FORMAT)

        # Convert the end time to the time zone of the user mailbox
        end = datetime.datetime.utcfromtimestamp(end_time / 1000)
        end_tz = end.replace(tzinfo=pytz.utc).astimezone(to_zone).strftime(TIME_FORMAT)

        LOG.debug("Windows time zone = %s", windows_time_zone)
        LOG.debug("IANA time zone = %s", iana_time_zone)
        LOG.debug("meeting start = %s", start_tz)
        LOG.debug("meeting end = %s", end_tz)

        # Create attendee list in required format.  If no required/optional attendees are specified set to empty string.
        if not required_attendees:
            required_attendees = ""
        if not optional_attendees:
            optional_attendees = ""

        required_list = [{'emailAddress': {'address': address.strip()}, 'type': "required"}
                         for address in required_attendees.split(',')]
        optional_list = [{'emailAddress': {'address': address.strip()}, 'type': "optional"}
                         for address in optional_attendees.split(',')]
        attendees = required_list + optional_list

        # Format the calendar event json.
        event_json = {"subject": subject,
                      "body": {"contentType": "HTML",
                                "content": body},
                      "start": {"dateTime": start_tz,
                                "timeZone": windows_time_zone},
                      "end": {"dateTime": end_tz,
                              "timeZone": windows_time_zone},
                      "location": {"displayName": location},
                      "attendees": attendees}

        response = self.ms_graph_session.post(ms_graph_calender_event_url,
                                              headers={'Content-Type': 'application/json'},
                                              json=event_json)

        self.check_ms_graph_response_code(response.status_code)

        return response

    def get_message_attachments(self, email_address, message_id):
        """
        Get the attachments of a messages
        :param email_address: Email address of mailbox containing the message
        :param message_id: Message to get the attachments from.
        :return:
        """
        ms_graph_users_url = u'{0}/users/{1}/messages/{2}/attachments'.format(self.ms_graph_url, email_address,
                                                                              message_id)
        response = self.ms_graph_session.get(ms_graph_users_url)

        self.check_ms_graph_response_code(response.status_code)

        return response

    def query_messages_all_users(self, starts_with, mail_folder, sender, start_date, end_date, has_attachments,
                                 message_subject, message_body):
        """
        This function iterates over all users and returns a list of emails that match the search criteria.
        :param starts_with: get all users starting with this character(s)
        :param mail_folder: mailFolder id of the folder to search
        :param sender: email address of sender to search for
        :param start_date: date/time string of email received dated to start search
        :param end_date: date/time string of email received dated to end search
        :param has_attachments: boolean flag indicating to search for emails with or without attachments
        :param message_subject: search for emails containing this string in the "subject" of email
        :param message_body: search for emails containing this string in the "body" of email
        :return: list of emails in all user email account that match the search criteria.
        """

        # Start with an empty list of results.
        results = []

        # Get the users
        user_list = self.get_users(starts_with)

        # Iterate through all users
        LOG.debug("=====================Query All Users==========================\n")
        for email_address in user_list:

            user_query = self.query_messages_by_address(email_address, mail_folder, sender, start_date, end_date,
                                                        has_attachments, message_subject, message_body)
            # Append results for this user
            status_code = user_query.get('status_code')
            email_list = user_query.get('email_list')
            if status_code >= 200 and status_code < 300:
                results.append(user_query)
            LOG.debug(u"***************** status = {0} **************************\n".format(status_code))

            LOG.debug(u"email_address = {0} status_code = {1} number email = {2}".format(email_address, status_code, len(email_list)))
        return results

    def query_messages_all_users_batched(self, starts_with, mail_folder, sender, start_date, end_date, has_attachments,
                                         message_subject, message_body):
        """
        This function iterates over all users and returns a list of emails that match the search criteria.
        The $batch endpoint is used to send a list of query requests in one API call.  A list of requests (queries)
        is built and then sent to the endpoint when MAX_BATCHED_REQUESTS queries have been queued. After the
        responses are returned, the messages are appended into a list of email results.
        :param starts_with: get all users starting with this character(s)
        :param mail_folder: mailFolder id of the folder to search
        :param sender: email address of sender to search for
        :param start_date: date/time string of email received dated to start search
        :param end_date: date/time string of email received dated to end search
        :param has_attachments: boolean flag indicating to search for emails with or without attachments
        :param message_subject: search for emails containing this string in the "subject" of email
        :param message_body: search for emails containing this string in the "body" of email
        :return: list of emails in all user email account that match the search criteria.
        """

        # Start with an empty list of results.
        results = []

        # Get the users
        user_list = self.get_users(starts_with)

        # Iterate through all users
        LOG.debug("===================== Query All Users Batched ==========================\n")
        index = 1
        requests_list = []
        for email_address in user_list:
            url = self.build_MS_graph_query_url(email_address, mail_folder, sender, start_date, end_date,
                                                has_attachments, message_subject, message_body)
            # Append to the request url just the json fields we view in the data table.
            url = u"{0}&$select=id,subject,sender,hasAttachments,receivedDateTime,webLink".format(url)

            # The batch endpoint is different from single GET message API requests in that it takes
            # a relative url not the full url, so remove the base url from the string.
            url_relative = url.replace(self.ms_graph_url, "")

            request = {"id": str(index),
                       "method": "GET",
                       "url": url_relative
                        }
            requests_list.append(request)

            # When the requests list is equal to the maximum requests MS allows in a $batch request,
            # then process the batch of query requests.
            if index >= self.max_batched_requests:
                query_results = self.process_batched_query_requests(requests_list)
                for result in query_results:
                    results.append(result)
                # Reinitialize the requests list and start filling it again.
                index = 1
                requests_list = []
            else:
                index = index + 1

        # Send out any requests that are still queued.
        if len(requests_list):
            query_results = self.process_batched_query_requests(requests_list)
            for result in query_results:
               results.append(result)
        return results

    def process_batched_query_requests(self, requests_list):
        """
        Send a list of requests to the $batch endpoint and then process the responses and place query results
        into a list of json query result objects.
        :param requests_list: list of MAX_BATCHED_REQUESTS
        :return: list of json results with one entry per email address queried. Each json object contains
        the list of emails found matching the search criteria.  Results are only returned for email addresses have
        200 status code (not 404: mailbox not found).
        """
        results = []
        ms_graph_batch = u"{0}/$batch".format(self.ms_graph_url)
        LOG.debug(u"POST these query requests to MS Graph $batch endpoint:")
        LOG.debug(requests_list)
        responses = self.ms_graph_session.post(ms_graph_batch,
                                               headers={'Content-Type': 'application/json'},
                                               json={'requests': requests_list})
        status_code = responses.status_code
        if status_code >= 200 and status_code < 300:
            json_response = responses.json()
            responses_list = json_response.get("responses")
        else:
            # If invalid json then print the requests that failed and try to continue.
            LOG.error(u"Error: Invalid response from MS Graph $batch endpoint: %s", responses)
            LOG.error(u"Requests list:")
            LOG.error(requests_list)
            responses_list = []

        # Each response is a query result.
        for response in responses_list:
            status_code = response.get('status')
            # Only add to the email results list if the query was found.
            # 404 mailbox not found is status code when the mailbox is not found or it has no license.
            if status_code >= 200 and status_code < 300:
                email_list = []
                # The id is a string starting at 1, so subtract 1 when using as an integer index.
                response_id = int(response.get('id')) - 1
                url = requests_list[response_id]['url']

                # Parse out the mailbox being queried the from the url.
                url_list = url.split('/')
                email_address = url_list[2]

                # value contains the list of message results and next_link is the url for next set of messages
                # to retrieve Graph API.  If status is 200, there should be a body and value in the response.
                # '@odata.nextLink' may not be a defined field.
                body = response.get("body")
                value = body.get('value')
                next_link = body.get('@odata.nextLink', None)
                while len(value) > 0 and self.current_message_count <= self.max_messages:
                    for email in value:
                        # Add these emails to the list
                        LOG.debug(u"adding email_address = {0} email subject = {1} id = {2}".format(email_address,
                                                                                                email.get('subject'),
                                                                                                email.get('id')))
                        email_list.append(email)

                    # Keep track of the total emails retrieved so far.
                    self.current_message_count = self.current_message_count + len(value)

                    # Get the pointer to the next set of messages to retrieve from Graph API endpoint.
                    if next_link:
                        response_next = self.ms_graph_session.get(next_link)
                        json_response_next = response_next.json()
                        next_link = json_response_next.get('@odata.nextLink', None)
                        value = json_response_next.get('value')
                    else:
                        value = []

                if len(email_list) > 0:
                    # Put this query result in a json object and add to the list or results.
                    query_result = {'email_address': email_address,
                                    'status_code': status_code,
                                    'email_list': email_list
                                    }
                    results.append(query_result)
        return results

    def query_messages_by_list(self, email_address_string, mail_folder, sender, start_date, end_date, has_attachments,
                               message_subject, message_body):
        """
        query_messages_by_list iterates over a list of email addresses and returns a list of emails that match the
        search criteria.
        :param email_address_string: a comma separated string that that is converted to a list of email addresses to
        query.
        :param mail_folder: mailFolder id of the folder to search
        :param sender: email address of sender to search for
        :param start_date: date/time string of email received dated to start search
        :param end_date: date/time string of email received dated to end search
        :param has_attachments: boolean flag indicating to search for emails with or without attachments
        :param message_subject: search for emails containing this string in the "subject" of email
        :param message_body: search for emails containing this string in the "body" of email
        :return: list of emails in all user email account that match the search criteria.
        """
        results = []

        # Iterator through list of email addresses
        for email_address in email_address_string.split(','):
            user_query = self.query_messages_by_address(email_address.strip(), mail_folder, sender, start_date,
                                                        end_date, has_attachments, message_subject, message_body)
            # Append results for this user
            status_code = user_query.get('status_code')
            if status_code >= 200 and status_code < 300:
                results.append(user_query)
        return results

    def query_messages(self, email_address, mail_folder, sender, start_date, end_date, has_attachments, message_subject,
                       message_body):
        """
        query_messages is the top level routine for querying message.  If the email_address to search contains the
        string "ALL" or "all", then all of the users of the tenant are searched.
        :param email_address: A string indicating which emails to query.  email_address will be either:
                a single email address
                a comma separated string of email addresses
                a string "ALL" indicating that all user emails should be queried.
        :param mail_folder: mailFolder id of the folder to search
        :param sender: email address of sender to search for
        :param start_date: date/time string of email received dated to start search
        :param end_date: date/time string of email received dated to end search
        :param has_attachments: boolean flag indicating to search for emails with or without attachments
        :param message_subject: search for emails containing this string in the "subject" of email
        :param message_body: search for emails containing this string in the "body" of email
        :return: list of emails in all user email account that match the search criteria.
        """
        # Initialize message count at the top-level query function.
        self.current_message_count = 0
        user_startswith = None
        input_choices = set(['all', 'all user', 'all users'])
        if email_address.lower() in input_choices:
            query_results = self.query_messages_all_users_batched(user_startswith, mail_folder, sender, start_date,
                                                                  end_date, has_attachments, message_subject,
                                                                  message_body)
        elif email_address.lower().startswith('all:'):
            user_startswith = email_address.lstrip('all:')
            query_results = self.query_messages_all_users_batched(user_startswith, mail_folder, sender, start_date,
                                                                  end_date, has_attachments, message_subject,
                                                                  message_body)
        else:
            query_results = self.query_messages_by_list(email_address, mail_folder, sender, start_date, end_date,
                                                        has_attachments, message_subject, message_body)
        return query_results

    def query_messages_by_address(self, email_address, mail_folder, sender, start_date, end_date, has_attachments,
                                  message_subject, message_body):
        """
         query_messages_by_address returns the results of a query on a single email address (mailbox).
         :param email_address: a single email address to be queried.
         :param mail_folder: mailFolder id of the folder to search
         :param sender: email address of sender to search for
         :param start_date: date/time string of email received dated to start search
         :param end_date: date/time string of email received dated to end search
         :param has_attachments: boolean flag indicating to search for emails with or without attachments
         :param message_subject: search for emails containing this string in the "subject" of email
         :param message_body: search for emails containing this string in the "body" of email
         :return: list of emails in all user email account that match the search criteria.
         """

        ms_graph_query_url = self.build_MS_graph_query_url(email_address, mail_folder, sender, start_date, end_date,
                                                           has_attachments, message_subject, message_body)
        # Append to the request url just the json fields we view in the data table.
        ms_graph_query_url = u"{0}&$select=id,subject,sender,hasAttachments,receivedDateTime,webLink".format(ms_graph_query_url)

        email_list = []
        # MS Graph will return message results back a certain number at a time, so we need to
        # append all of the results to a single list.  Because there can be a huge number of emails
        # returned, keep a count and limit the number returned to a variable set in the app.config.
        # MS Graph sends back the URL for the next batch of results in '@data.nextLink' field.
        response_status = 404
        while ms_graph_query_url and self.current_message_count <= self.max_messages:
            LOG.debug("ms_graph_query_url = {0}".format(ms_graph_query_url))
            response = self.ms_graph_session.get(ms_graph_query_url)

            response_status = response.status_code
            self.check_ms_graph_response_code(response_status)

            # Return empty list if the email address is not found.
            if response_status == 404:
                email_list = []
                LOG.debug(u"============== 404 ==================== current_message_count = {0}".format(self.current_message_count))
                break

            json_response = response.json()
            for email in json_response['value']:
                # Add these emails to the list
                LOG.debug(u"adding email_address = {0} email subject = {1} id = {2}".format(email_address, email.get('subject'), email.get('id')))
                email_list.append(email)

            # Keep track of the total emails retrieved so far.
            self.current_message_count = self.current_message_count + len(json_response['value'])

            # Get URL for the next batch of results.
            ms_graph_query_url = json_response.get('@odata.nextLink')

        results = {'email_address': email_address,
                   'status_code': response_status,
                   'email_list': email_list
                   }
        return results

    def build_MS_graph_query_url(self, email_address, mail_folder, sender, start_date, end_date, has_attachments,
                                 message_subject, message_body):
        """
          build_MS_graph_query_url returns the MS Graph URL to query messages with this specified parameters.
          :param email_address: a single email address to be queried.
          :param mail_folder: mailFolder id of the folder to search
          :param sender: email address of sender to search for
          :param start_date: date/time string of email received dated to start search
          :param end_date: date/time string of email received dated to end search
          :param has_attachments: boolean flag indicating to search for emails with or without attachments
          :param message_subject: search for emails containing this string in the "subject" of email
          :param message_body: search for emails containing this string in the "body" of email
          :return: list of emails in all user email account that match the search criteria.
          """
        # Compute the mail folder if it is specified.
        folder_string = self.build_folder_string(mail_folder)

        # Create $search string query for search on message body string.
        search_query = self.build_search_query(message_body)

        # Create $filter query string for query on messages.
        filter_query = self.build_filter_query(start_date, end_date, sender, message_subject, has_attachments)

        # Assemble the MS Graph API query string.
        if search_query:
            if filter_query:
                ms_graph_query_url = u'{0}/users/{1}{2}/messages{3}&{4}'.format(self.ms_graph_url,
                                                                                email_address,
                                                                                folder_string,
                                                                                search_query,
                                                                                filter_query)
            else:
                ms_graph_query_url = u'{0}/users/{1}{2}/messages{3}'.format(self.ms_graph_url,
                                                                            email_address,
                                                                            folder_string,
                                                                            search_query)
        elif filter_query:
            ms_graph_query_url = u'{0}/users/{1}{2}/messages{3}'.format(self.ms_graph_url,
                                                                        email_address,
                                                                        folder_string,
                                                                        filter_query)
        else:
            raise IntegrationError("Exchange Online: Query Messages: no query parameters specified.")

        return ms_graph_query_url

    @staticmethod
    def build_folder_string(mail_folder):
        """
        build_folder_string function creates the string used on MS Graph API calls to specify the mail folder
        location of the message.  (Mail Folder is not always used or needed if you have the actual message ID.)
        :param mail_folder: mailFolder id
        :return: the mailFolder string to be used in MS Graph API calls where a mail folder is used.
        """
        if not mail_folder:
            return ""

        folder_string = u"/mailFolders/{}".format(mail_folder)
        return folder_string

    @staticmethod
    def append_query_to_query_url(filter_query, new_query):
        """
        :param filter_query: query filter string
        :param new_query: new query to add to the filter query string
        :return: the new query filter string
        # Each $filter query will be enclosed in parentheses.
        # If there is already a query appended on the query filter string it will end with a close parentheses ')'
        # otherwise it will end "=" when it is the first query parameter.  When adding a new query, url-encoded
        # ' and ' string should be be placed between the two queries.
        """
        if filter_query.endswith(')'):
            join_string = u'%20and%20'
        else:
            join_string = ""
        return u'{0}{1}{2}'.format(filter_query, join_string, new_query)

    @staticmethod
    def build_search_query(message_body):
        """
         Build the "$search" query portion of the string to search the body of the message.
         :param message_body: string to find in the message body.
         :return: $search query portion of the string if there is a message_body string to search for.
         """
        if message_body:
            url_encoded_body = url_encode(message_body.encode('utf8'))
            return u'?$search="{0}"'.format(url_encoded_body)

        return ""

    def build_filter_query(self, start_date, end_date, sender, message_subject, has_attachments):
        """
           Build the "$search" query portion of the string to search the body of the message.
           :param start_date: date/time string of email received dated to start search
           :param end_date: date/time string of email received dated to end search
           :param sender: email address of sender to search for
           :param message_subject: search for emails containing this string in the "subject" of email
           :param has_attachments: boolean flag indicating to search for emails with or without attachments
           :return: $filter portion of the query string containing parameter
           """
        # Initialize $filter query string
        filter_query = u'?$filter='
        filter_query_start_len = len(filter_query)

        if start_date:
            # convert from epoch to utc time.
            utc_time = datetime.datetime.fromtimestamp(start_date/1000).strftime('%Y-%m-%dT%H:%M:%SZ')
            start_date_query = u'(receivedDateTime%20ge%20{0})'.format(utc_time)
            filter_query = self.append_query_to_query_url(filter_query, start_date_query)

        if end_date:
            # convert from epoch to utc time.
            utc_time = datetime.datetime.fromtimestamp(end_date/1000).strftime('%Y-%m-%dT%H:%M:%SZ')
            end_date_query = u'(receivedDateTime%20le%20{0})'.format(utc_time)
            filter_query = self.append_query_to_query_url(filter_query, end_date_query)

        if sender:
            sender_query = u"(from/emailAddress/address%20eq%20'{0}')".format(sender)
            filter_query = self.append_query_to_query_url(filter_query, sender_query)

        if has_attachments is not None:
            has_attachments_query = u'(hasAttachments%20eq%20{0})'.format(str(has_attachments).lower())
            filter_query = self.append_query_to_query_url(filter_query, has_attachments_query)

        if message_subject:
            # OData query requires single quotes be replaced by 2 single quotes when using $filter (not $search)!
            # First url encode the subject and then substitutes one single quote (%27)
            # with 2 single quotes (not url encoded).
            url_encoded_subject = url_encode(message_subject.encode('utf8'))
            url_encoded_subject = url_encoded_subject.replace("%27", "''")
            subject_query = u"(contains(subject,'{0}'))".format(url_encoded_subject)
            filter_query = self.append_query_to_query_url(filter_query, subject_query)

        # If nothing was added, then return the empty string.
        if len(filter_query) == filter_query_start_len:
            return ""

        return filter_query
