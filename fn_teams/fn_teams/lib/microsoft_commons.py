# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction Common utilities"""
import json
from urllib import parse

from resilient_lib import IntegrationError
from fn_teams.lib import constants

class ResponseHandler:
    """
    Handles the responses received from the Webex endpoint.
    Used as a callback function for request_common.execute

    The behaviour of the response received can be customized by allowing
    certain response codes to pass through and not raise an exception.

    Input:
    ------
        Response  (<response>) : A response from rc.execute

    Defaults:
    ---------
        msg                    : Message in accordance with the error code
        default_exempt_codes   : default list of codes that are to be
                                 exempted from raising an exception
        exempt_codes           : list of codes that are to be exempted
                                 from raising an exception

    Returns:
    --------
            (<dict>) : Response with appropriate status code and message
    """
    def __init__(self):
        self.msg, self.response = None, None
        self.return_raw = False
        self.default_exempt_codes = []
        self.empty_response_codes = [204]
        self.exempt_codes = self.default_exempt_codes.copy()


    def set_return_raw(self, value: bool=False):
        self.return_raw = value


    def _monitor_status(self):
        """
        Monitors the response recieved from the endpoint and generates a custom message
        for the webex application.

        Raises:
        -------
            IntegrationError : If the recieved response is None, raises this error. This
                               could be due to an invalid call methord being passed.
        """
        if self.response is None:
            raise IntegrationError(constants.MSG_RESPONSE_NONE)
        if self.response.status_code in self.empty_response_codes:
            self.msg = constants.MSG_RESPONSE_204
        elif "error" in self.response.json():
            response = self.response.json()
            error = " ".join([
                response.get('error').get('message'),
                response.get('error_description', '')])
            if self.response.status_code == 400:
                self.msg = constants.MSG_RESPONSE_400.format(error)
            elif self.response.status_code == 401:
                self.msg = constants.MSG_RESPONSE_404.format(error)
            elif self.response.status_code == 404:
                self.msg = constants.MSG_RESPONSE_404.format(error)
            elif self.response.status_code == 405:
                self.msg = constants.MSG_RESPONSE_405.format(error)


    def _raise_or_return_erros(self):
        """
        Filters through the response to either raise or return the request.
            * If the status code matches with the exempt list, the method
              will allow it to pass and returns the message body.
            * If the status_code is not > 204 and not in exempt list, the method
              raises an exception.
            * If the status code is 204 and in exempt list, creates a message
              body and returns it with a custom message

        Raises:
        -------
            IntegrationError: When an exception occurs and not exempted.

        Returns:
        --------
            (<dict>): If the methord doesnot raise an error, it the returns the response
                      in the form of a dictionary.
        """
        if self.return_raw:
            return self.response

        if not self.msg:
            res = self.response.json()
            res["status_code"] = self.response.status_code
            return res

        if self.response.status_code not in self.exempt_codes and (
            self.response.status_code not in self.empty_response_codes):
            raise IntegrationError(self.msg)

        if self.response.status_code in self.empty_response_codes:
            res = {}
        else:
            res = self.response.json()
        res["status_code"] = self.response.status_code
        if self.msg:
            res["message"] = self.msg
        return res



    def clear_exempt_codes(self, default=False):
        """
        Clears the exempt code list or resets it back to the
        default value.

        Arguments:
        ----------
            default (<bool>) : Resets the code to default list of codes
                               else, clears all codes
        """
        if default:
            self.exempt_codes = self.default_exempt_codes.copy()
        else:
            self.exempt_codes = []


    def add_exempt_codes(self, codes):
        """
        Allows for adding codes to the exempt list

        Args:
        -----
            codes (<int>) or (<list>): A code or a list of codes to be added
                                       to the exempt code list

        Raises:
        -------
            TypeError: When unsupported type supplied for codes.
            Supported type <list> or <int>
        """
        if isinstance(codes, int):
            self.exempt_codes.append(codes)
        elif isinstance(codes, list):
            self.exempt_codes.extend(codes)
        else:
            raise IntegrationError(constants.MSG_UNSUPPORTED_TYPE.format(codes))

    def clear_empty_response_codes(self, default=False):
        """
        Clears the exempt code list or resets it back to the
        default value.

        Arguments:
        ----------
            default (<bool>) : Resets the code to default list of codes
                               else, clears all codes
        """
        if default:
            self.empty_response_codes = [204]
        else:
            self.empty_response_codes = []


    def add_empty_response_code(self, codes):
        """
        Allows for adding codes to the exempt list

        Args:
        -----
            codes (<int>) or (<list>): A code or a list of codes to be added
                                       to the exempt code list

        Raises:
        -------
            TypeError: When unsupported type supplied for codes.
            Supported type <list> or <int>
        """
        if isinstance(codes, int):
            self.empty_response_codes.append(codes)
        elif isinstance(codes, list):
            self.empty_response_codes.extend(codes)
        else:
            raise IntegrationError(constants.MSG_UNSUPPORTED_TYPE.format(codes))


    def check_response(self, response):
        """
        Wrapper to run the object

        Args:
        -----
            response (<response>): Response from the rc object

        Returns:
        --------
            (<dict>) : Response body with status code.
        """
        self.msg = None
        self.response = response
        self._monitor_status()
        return self._raise_or_return_erros()


def get_user_info(user_id, **kwargs):
    """
    Fetches information using the email address of the SOAR user and assigns
    a role (member or owner) depending upon the information that was provided
    in the function, and saves this information in self.user_db for later use.

    Arguments:
    ----------
        user_id          <str>  : Email address used for information retrieval
        request_common   <obj>  : rc object that allows for making external requests
        response_handler <obj>  : response handler that monitors responses
        logger           <obj>  : Logger object
        headers          <dict> : Authorization headers for MS endpoint

    Updates:
    --------
         response <dict> : User information retrieved from the MS Endpoint
    """

    rc  = kwargs.get("request_common")
    rh  = kwargs.get("response_handler")
    log = kwargs.get("logger")
    headers = kwargs.get("headers")

    url = parse.urljoin(
        constants.BASE_URL,
        constants.URL_USERS.format(user_id))

    response = rc.execute(
        method="get",
        url=url,
        headers=headers,
        callback=rh.check_response)

    if "mail" in response:
        return response
    else:
        log.warn(constants.WARN_DIDNOT_FIND_USER.format(user_id))


def find_group(**kwargs):
    """
    Allows for locating a group based on its displayName or mailNickname attribute
    This function at least required either the group_name or the group_mail_nickname
    keyword argument.

    Kwargs:
    -------
        request_common      <obj>  : rc object that allows for making external requests
        response_handler    <obj>  : response handler that monitors responses
        logger              <obj>  : Logger object
        headers             <dict> : Authorization headers for MS endpoint
        group_name          <str>  : Display name of the group
        group_mail_nickname <str>  : Mail nickname of the group

    Raises:
    -------
        IntegrationError: Unable to locate the group

    Returns:
    --------
        <dict> : Details of the detected group
    """
    rc  = kwargs.get("request_common")
    rh  = kwargs.get("response_handler")
    log = kwargs.get("logger")
    headers = kwargs.get("headers")

    if "group_name" in kwargs:
        log.info(constants.INFO_FIND_GROUP_BY_NAME)
        _name = kwargs.get("group_name")
        error_msg = constants.ERROR_DIDNOT_FIND_GROUP.format("Group Name", _name)
        _query = constants.QUERY_GROUP_FIND_BY_NAME.format(_name)

    if "group_mail_nickname" in kwargs:
        log.info(constants.INFO_FIND_GROUP_BY_MAIL)
        _name = kwargs.get("group_mail_nickname")
        if "@" in _name:
            _name = _name.split("@")[0]
        error_msg = constants.ERROR_DIDNOT_FIND_GROUP.format("Mail Nickname", _name)
        _query = constants.QUERY_GROUP_FIND_BY_MAIL.format(_name)

    url = parse.urljoin(
        constants.BASE_URL,
        constants.URL_GROUPS_QUERY.format(_query))

    response = rc.execute(
        method="get",
        url=url,
        headers=headers,
        callback=rh.check_response)

    log.debug(json.dumps(response, indent=2))

    if len(response.get("value")) > 0 :
        log.info(constants.INFO_FOUND_GROUP)
        return response.get("value")

    log.error(error_msg)
    raise IntegrationError(error_msg)


def is_direct_member(incident_member_id, org_member_list):
    """
    Checks to see if the member Id acquired from the incident or task belongs to the
    list of users from the organization. Upon a match, it then extracts the email
    address for that particular user.

    Args:
    -----
        incident_member_id <str>  : The user Id acquired from the incident
        org_member_list    <list> : The list of member Ids of all organization members

    Returns:
    --------
        <str>: Email address of the incident member
    """
    for user in org_member_list:
        if incident_member_id == user.get("id"):
            return user.get(constants.EMAIL)


def is_group_member(incident_member_id, org_member_list, org_group_list):
    """
    Checks to see if the member Id acquired from the incident or task belongs to
    the list of all groups from the organization. Upon a match, it then queries a list
    of Ids associated with that group and matches with a user using the
    >>is_direct_member<< function

    Args:
    -----
        incident_member_id  <str> : The user Id acquired from the incident
        org_member_list    <list> : The list of member Ids of all organization members
        org_group_list     <list> : The list of group Ids of all organization members

    Returns:
    --------
        <list>: list of all email addresses of incident members
    """
    ret = []
    for group in org_group_list:
        if incident_member_id == group.get("id"):
            for member in group.get("members"):
                ret.append(is_direct_member(member, org_member_list))
    return ret


def generate_member_list(**kwargs):
    """
    Generates a list of email addresses of the members of a SOAR instance. The main 
    goal is to extract user email addresses from the SOAR instance for specific users.
    While querying an incident or a task for members, user ids are returned as appose to
    entire user data. These ids are then converted to useful information (in this case
    user email address) by fetching user information based on the retrieved ids.

    kwargs:
    -------
        logger             <obj> : Logger object
        resclient          <obj> : Client object to interface with Resilient SOAR
        task_id            <str> : Task ID number
        incident_id        <str> : Incident ID number
        add_members_from   <str> : Read members from task or incident level
        additional_members <str> : Add additional member email addresses to be added

    Returns:
    --------
        email_ids <list> : a list of all participant email addresses to be added
    """

    log = kwargs.get("logger")
    resclient = kwargs.get("resclient")

    task_id = kwargs.get("task_id")
    incident_id = kwargs.get("incident_id")
    add_members_from = kwargs.get("add_members_from")
    additional_members = kwargs.get("additional_members")

    org_member_list  = resclient.post(constants.RES_USERS, payload={}).get("data")
    org_group_list   = resclient.get(constants.RES_GROUPS)
    add_members_from = add_members_from.lower().strip()
    add_members_from = None if add_members_from == "none" else add_members_from

    log.debug(f"task_id            : {task_id}")
    log.debug(f"incident_id        : {incident_id}")
    log.debug(f"add_members_from   : {add_members_from}")
    log.debug(f"additional_members : {additional_members}")

    email_ids = []
    if add_members_from:
        if add_members_from.strip().lower() == "task":
            incident_members = resclient.get(parse.urljoin(constants.RES_TASK,
                constants.MEMBERS_URL.format(task_id)))
        else:
            incident_members = resclient.get(parse.urljoin(constants.RES_INCIDENT,
                constants.MEMBERS_URL.format(incident_id)))
        if not incident_members.get("members") or len(incident_members.get("members")) == 0:
            log.warn(constants.WARN_INCIDENT_NO_MEMBERS)
        else:
            for incident_member in incident_members.get("members"):
                if is_direct_member(incident_member, org_member_list):
                    email_ids.append(
                        is_direct_member(incident_member, org_member_list))
                elif is_group_member(incident_member, org_member_list, org_group_list):
                    email_ids.extend(
                        is_group_member(
                            incident_member, org_member_list, org_group_list))
        log.debug(email_ids)
    elif not additional_members:
        log.warn(constants.WARN_NO_ADDITIONAL_PARTICIPANTS)

    if additional_members:
        email_ids += (additional_members
        .lower()
        .replace(" ", "")
        .split(","))
    email_ids = list(set(email_ids))
    log.info(constants.INFO_ADD_MEMEBERS.format(email_ids))
    return email_ids
