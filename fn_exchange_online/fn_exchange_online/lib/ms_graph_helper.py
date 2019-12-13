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
    def __init__(self, ms_graph_token_url, ms_graph_url, tenant_id, client_id, client_secret, proxies=None):
        self.__ms_graph_token_url = ms_graph_token_url.format(tenant=tenant_id)
        self.__ms_graph_url = ms_graph_url
        self.__tenant_id = tenant_id
        self.__client_id = client_id,
        self.__client_secret = client_secret
        self.__proxies = proxies
        self.__ms_graph_session = self.authenticate()

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

    def append_query_to_query_url(self, filter_query, new_query):
        """
        :param filter_query: query filter string
        :param new_query: new query to add to the filter query string
        :return: the new query filter string
        # If there is already a query appended on the query filter string it will end with a close parentheses ')'
        # otherwise it will end "=".  When adding a new query, url-encoded ' and ' string should be be placed between
        # between the two queries.
        """
        if filter_query.endswith(')'):
            join_string = u"%20and%20"
        else:
            join_string = ""
        return u"{0}{1}{2}".format(filter_query, join_string, new_query)

    def query_emails(self, email_address, sender, start_date, end_date, has_attachments, message_subject, message_body, order_by_recency):
        """
        Query MS Graph user profile endpoint using the MS graph session.
        :param email_address: email address of the user whose mailboz is being searched.
        :return: requests response from the email query
        """
        filter_query = u"?$filter="
        filter_start_length = len(filter_query)
        search_query = u"?$search="
        search_start_length = len(search_query)
        order_query = u"?$orderby="
        order_start_length = len(order_query)
        if order_by_recency is not None:
            if order_by_recency:
                order_query = u"{0}(receivedDateTime%20desc)".format(order_query)
            else:
                order_query = u"{0}(receivedDateTime%20asc)".format(order_query)
            # When using $orderby in query you must also use the same parameter in $filter clause
            # So, if a start date is note specified set one.
            if start_date is None:
                start_date_query = u"(receivedDateTime%20ge%20{0})".format('1900-01-01T00:00:00Z')
                filter_query = self.append_query_to_query_url(filter_query, start_date_query)

        if start_date:
            # convert from epoch to utc time.
            utc_time = datetime.datetime.fromtimestamp(start_date/1000).strftime('%Y-%m-%dT%H:%M:%SZ')
            start_date_query = u"(receivedDateTime%20ge%20{0})".format(utc_time)
            filter_query = self.append_query_to_query_url(filter_query, start_date_query)

        if end_date:
            # convert from epoch to utc time.
            utc_time = datetime.datetime.fromtimestamp(end_date/1000).strftime('%Y-%m-%dT%H:%M:%SZ')
            end_date_query = u"(receivedDateTime%20le%20{0})".format(utc_time)
            filter_query = self.append_query_to_query_url(filter_query, end_date_query)

        if sender:
            sender_query = u"(from/emailAddress/address%20eq%20'{0}')".format(sender)
            filter_query = self.append_query_to_query_url(filter_query, sender_query)

        if has_attachments is not None:
            has_attachments_query = u"(hasAttachments%20eq%20{0})".format(str(has_attachments).lower())
            filter_query = self.append_query_to_query_url(filter_query, has_attachments_query)

        if message_subject:
            subject_query = u"(contains(subject,'{0}'))".format(message_subject)
            filter_query = self.append_query_to_query_url(filter_query, subject_query)

        # body does not work yet.
        if message_body:
            body_query = u"{0}".format(message_body)
            search_query = self.append_query_to_query_url(search_query, message_body)

        if len(filter_query) > filter_start_length or len(search_query) > search_start_length:
            # Assemble the MS Graph API query string.
            if len(search_query) > search_start_length:
                ms_graph_query_messages_url = u'{0}users/{1}/messages{2}&{3}'.format(self.__ms_graph_url, email_address,
                                                                                     search_query, filter_query)
            else:
                ms_graph_query_messages_url = u'{0}users/{1}/messages{2}'.format(self.__ms_graph_url, email_address,
                                                                                 filter_query)
        else:
            raise IntegrationError("Exchange Online: Query Emails: no query parameters specified.")

        LOG.info(u"Exchange Online query string {0}", ms_graph_query_messages_url)
        response = self.__ms_graph_session.get(ms_graph_query_messages_url)

        # User not found (404) is a valid "error" so don't return error for that.
        if response.status_code >= 300 and response.status_code != 404:
            raise IntegrationError("Invalid response from Microsoft Graph when trying to query emails.")

        return response

