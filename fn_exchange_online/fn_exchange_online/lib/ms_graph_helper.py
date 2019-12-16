# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
import datetime
import logging
from resilient_lib import OAuth2ClientCredentialsSession
from resilient_lib.components.integration_errors import IntegrationError

LOG = logging.getLogger(__name__)
class MSGraphHelper(object):
    """
    Helper object MSGraphHelper.
    """
    def __init__(self, ms_graph_token_url, ms_graph_url, tenant_id, client_id, client_secret, max_emails, proxies=None):
        self.__ms_graph_token_url = ms_graph_token_url.format(tenant=tenant_id)
        self.__ms_graph_url = ms_graph_url
        self.__tenant_id = tenant_id
        self.__client_id = client_id,
        self.__client_secret = client_secret
        self.__proxies = proxies
        self.__ms_graph_session = self.authenticate()
        self.__max_emails = max_emails

    def authenticate(self):
        """
        Authenticate and get oauth2 token for the session.
        """
        return OAuth2ClientCredentialsSession(url=self.__ms_graph_token_url,
                                              client_id=self.__client_id,
                                              client_secret=self.__client_secret,
                                              scope=['.default'],
                                              proxies=self.__proxies)

    def get_user_profile(self, email_address):
        """
        Query MS Graph user profile endpoint using the MS graph session.
        :param email_address: email address of the user profile requested
        :return: requests response from the users/profile endpoint
        """
        ms_graph_user_profile_url = u'{0}users/{1}'.format(self.__ms_graph_url, email_address)
        response = self.__ms_graph_session.get(ms_graph_user_profile_url)

        # User not found (404) is a valid "error" so don't return error for that.
        if response.status_code >= 300 and response.status_code != 404:
            raise IntegrationError("Invalid response from Microsoft Graph when trying to get user profile.")

        return response

    def get_users(self):
        """
        Query MS Graph for all users endpoint using .
        :return: requests response from the /users/ endpoint
        """
        ms_graph_users_url = u'{0}users?$count=true'.format(self.__ms_graph_url)
        response = self.__ms_graph_session.get(ms_graph_users_url)

        # User not found (404) is a valid "error" so don't return error for that.
        if response.status_code >= 300 and response.status_code != 404:
            raise IntegrationError("Invalid response from Microsoft Graph when trying to get list of users.")

        return response

    def query_emails_all_users(self, sender, start_date, end_date, has_attachments, message_subject, message_body):

        response = self.get_users()
        response_user_json = response.json()
        user_list = response_user_json['value']
        results = []
        for user in user_list:
            email_address = user['userPrincipalName']
            user_query = self.query_emails(email_address, sender, start_date, end_date, has_attachments,
                                           message_subject, message_body)
            results.append(user_query)
        return results

    def append_query_to_query_url(self, filter_query, new_query):
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

    def build_search_query(self, message_body):
        """
         Build the "$search" query portion of the string to search the body of the message.
         :param message_body: string to find in the message body.
         :return: $search query portion of the string if there is a message_body string to search for.
         """
        if message_body:
            return u'?$search="{0}"'.format(message_body)
        else:
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
            sender_query = u'(from/emailAddress/address%20eq%20"{0}")'.format(sender)
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

    def query_emails(self, email_address, sender, start_date, end_date, has_attachments, message_subject, message_body):
        """
        Query MS Graph user profile endpoint using the MS graph session.
        :param email_address: email address of the user whose mailbox is being searched.
        :return: requests response from the email query
        """

        # Create $search string query for search on message body string.
        search_query = self.build_search_query(message_body)

        # Create $filter query string for query on messages.
        filter_query = self.build_filter_query(start_date, end_date, sender, message_subject, has_attachments)

        # Assemble the MS Graph API query string.
        if len(search_query) > 0:
            if len(filter_query) > 0:
                ms_graph_query_messages_url = u'{0}users/{1}/messages{2}&{3}'.format(self.__ms_graph_url, email_address,
                                                                                     search_query, filter_query)
            else:
                ms_graph_query_messages_url = u'{0}users/{1}/messages{2}'.format(self.__ms_graph_url, email_address,
                                                                                 search_query)
        elif len(filter_query) > 0:
                ms_graph_query_messages_url = u'{0}users/{1}/messages{2}'.format(self.__ms_graph_url, email_address,
                                                                                     filter_query)
        else:
            raise IntegrationError("Exchange Online: Query Emails: no query parameters specified.")

        LOG.info(u'Exchange Online query string {0}', ms_graph_query_messages_url)
        response = self.__ms_graph_session.get(ms_graph_query_messages_url)

        # User not found (404) is a valid "error" so don't return error for that.
        if response.status_code >= 300 and response.status_code != 404:
            raise IntegrationError("Invalid response from Microsoft Graph when trying to query emails.")
        response_json = response.json()
        results = {'email_address': email_address,
                   'email_list': response_json['value']
                   }
        return results

