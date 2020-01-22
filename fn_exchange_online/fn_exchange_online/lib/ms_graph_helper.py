# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
import datetime
from resilient_lib import OAuth2ClientCredentialsSession
from resilient_lib.components.integration_errors import IntegrationError

DEFAULT_SCOPE = 'https://graph.microsoft.com/.default'

class MSGraphHelper(object):
    """
    Helper object MSGraphHelper.
    """
    def __init__(self, ms_graph_token_url, ms_graph_url, tenant_id, client_id, client_secret, max_messages, max_users,
                 proxies=None):
        self.ms_graph_token_url = ms_graph_token_url.format(tenant=tenant_id)
        self.ms_graph_url = ms_graph_url
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.proxies = proxies
        self.ms_graph_session = self.authenticate()
        self.max_messages = int(max_messages)
        self.current_message_count = 0
        self.max_users = int(max_users)

    @staticmethod
    def check_ms_graph_response_code(status_code):
        """
        Check that the request status code: raise an integration error if great than 300 and code is "not found"
        :param status_code: request statues code
        :return:
        """
        if status_code >= 300 and status_code != 404:
            raise IntegrationError("Invalid response from Microsoft Graph API call.")

    def authenticate(self):
        """
        Authenticate and get oauth2 token for the session.
        """
        return OAuth2ClientCredentialsSession(url=self.ms_graph_token_url,
                                              client_id=self.client_id,
                                              client_secret=self.client_secret,
                                              scope=DEFAULT_SCOPE,
                                              proxies=self.proxies)

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

    def get_users(self):
        """
        Query MS Graph for all users endpoint.
        :return: requests response from the /users/ endpoint which is the list of all users.
        """
        user_list = []
        user_count = 0
        ms_graph_users_url = u'{0}/users'.format(self.ms_graph_url)

        while ms_graph_users_url and user_count <= self.max_users:
            response = self.ms_graph_session.get(ms_graph_users_url)
            json_response = response.json()
            for user in json_response['value']:
                # Add these users to the list
                user_list.append(user)

            # Keep track of the total users retrieved so far.
            user_count = user_count + len(json_response['value'])

            # Get URL for the next batch of results.
            ms_graph_users_url = json_response.get('@odata.nextLink')

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


    def send_message(self, sender_address, recipients, subject, body):
        """
        Call MS Graph to send message.
        :param sender_address: email address of the message sender
        :param recipients: comma separated list of users to send message to
        :param subject: message subject text
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
        response_json = response.json()
        time_zone = response_json["value"]

        # Calculate meeting start and end date/time.
        utc_start_time = datetime.datetime.fromtimestamp(start_time / 1000).strftime('%Y-%m-%dT%H:%M:%S')
        utc_end_time = datetime.datetime.fromtimestamp(end_time / 1000).strftime('%Y-%m-%dT%H:%M:%S')

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
                      "start": {"dateTime": utc_start_time,
                                "timeZone": time_zone},
                      "end": {"dateTime": utc_end_time,
                              "timeZone": time_zone},
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

    def query_messages_all_users(self, mail_folder, sender, start_date, end_date, has_attachments, message_subject,
                                 message_body):
        """
        This function iterates over all users and returns a list of emails that match the search criteria.
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
        user_list = self.get_users()

        # Iterate through all users
        for user in user_list:
            email_address = user['userPrincipalName']
            user_query = self.query_messages_by_address(email_address, mail_folder, sender, start_date, end_date,
                                                        has_attachments, message_subject, message_body)
            # Append results for this user
            results.append(user_query)

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

        input_choices = set(['all', 'all user', 'all users'])
        if email_address.lower() in input_choices:
            query_results = self.query_messages_all_users(mail_folder, sender, start_date, end_date,
                                                          has_attachments, message_subject, message_body)
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

        email_list = []
        # MS Graph will return message results back a certain number at a time, so we need to
        # append all of the results to a single list.  Because there can be a huge number of emails
        # returned, keep a count and limit the number returned to a variable set in the app.config.
        # MS Graph sends back the URL for the next batch of results in '@data.nextLink' field.
        while ms_graph_query_url and self.current_message_count <= self.max_messages:
            response = self.ms_graph_session.get(ms_graph_query_url)

            self.check_ms_graph_response_code(response.status_code)

            # Return empty list if the email address is not found.
            if response.status_code == 404:
                email_list = []
                break

            json_response = response.json()
            for email in json_response['value']:
                # Add these emails to the list
                email_list.append(email)

            # Keep track of the total emails retrieved so far.
            self.current_message_count = self.current_message_count + len(json_response['value'])

            # Get URL for the next batch of results.
            ms_graph_query_url = json_response.get('@odata.nextLink')

        results = {'email_address': email_address,
                   'status_code': response.status_code,
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
            return u'?$search="{0}"'.format(message_body)

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
            subject_query = u"(contains(subject,'{0}'))".format(message_subject)
            filter_query = self.append_query_to_query_url(filter_query, subject_query)

        # If nothing was added, then return the empty string.
        if len(filter_query) == filter_query_start_len:
            return ""

        return filter_query
