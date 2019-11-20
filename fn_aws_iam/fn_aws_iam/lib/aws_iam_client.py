# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
from boto3 import Session
from botocore.exceptions import ClientError
from  datetime import datetime
import logging

LOG = logging.getLogger(__name__)
# List of paginated types supported for the integration.
SUPPORTED_PAGINATE_TYPES = ["Users", "Groups"]

class AwsIamClient():
    """
    Client class for AWS IAM.
    """
    def __init__(self, options, function_options=None, sts_client=False):
        """
        Class constructor.
        """
        self.aws_iam_access_key_id = function_options.get("aws_iam_access_key_id")
        self.aws_iam_secret_access_key = function_options.get("aws_iam_secret_access_key")
        if function_options.get("aws_iam_region") is not None:
            self.aws_iam_region = options.get("aws_iam_region")
        else:
            self.aws_iam_region = None

        self.iam = self._get_client("iam")

        if sts_client:
            self.sts = self._get_client("sts")

    def _get_client(self, service_name):
        """ Create an AWS IAM client.

        :param kwargs: Dictionary of AWS API parameters for function call .
        :return: Converted  string.

        """
        # Create IAM client for iam or sts.
        try:

            client = Session(
                region_name=self.aws_iam_region,
                aws_access_key_id=self.aws_iam_access_key_id,
                aws_secret_access_key=self.aws_iam_secret_access_key
            ).client(service_name=service_name)

        except ClientError as e:
            LOG.error("ERROR instantiating AWS IAM client for service: {0}, Got exception type: {1}, msg: {2}"
                      .format(service_name, e.__repr__(), e.message))
            raise e

        return client

    def _get_type_from_response(self, response):
        for key in response:
            if key in SUPPORTED_PAGINATE_TYPES:
                result_type = key

        return result_type

    def _add_user_properties(self, result):
        """ Add metadata entries for login profile, default user.

        :param result: List of dicts from AWS IAM response.
        :return: Updated result.

        """
        # Add a flag for the default user in result.
        default_index = None
        default_identity = self._get_default_identity()
        for i in range(len(result)):
            if self.get_login_profile(UserName=result[i]["UserName"]):
                result[i].update({"LoginProfileExists": "Yes"})
            else:
                result[i].update({"LoginProfileExists": "No"})
            if result[i]["UserId"] == default_identity["UserId"]:
                default_index = i
                result[i].update({"DefaultUser": "Yes"})

        # Insert the default user at the top of the result.
        if len(result) > 1:
            result.insert(0, result.pop(default_index))

        return result

    def _update_result(self, result, result_type):
        """ Make any necessary conversions and additions to AWS IAM result.

        :param result: Dict or list of dicts from AWS IAM response.
        :param result_type: The type of result e.g. 'Users'.
        :return: Updated result.

        """
        if isinstance(result, list):
            for entry in result:
                entry = self._datetime_to_str(entry)
        else:
            LOG.error("ERROR with unexpected result type {0} for AWS IAM query".format(type(result)))

        if any(n in result_type for n in ["User", "Users"]):
            result = self._add_user_properties(result)

        return result

    def _get_default_identity(self):
        """ Get the identity of the current AWS IAM user.

        :param kwargs: Dictionary of AWS API parameters for function call .
        :return: Converted  string.

        """
        try:
            # Create IAM client for sts

            default_identity = self.sts.get_caller_identity()
        except Exception as e:
            LOG.error("ERROR with 'get_caller_identity' Got exception type: {0}, msg: {1}"
                      .format(e.__repr__(), e.message))
            raise e

        return default_identity

    @staticmethod
    def _datetime_to_str(result_entry):
        """ Convert datetime objects returned in result e.g. 'CreateDate' to a string.

        :param result_entry: Result entry dict from AWS IAM response.
        :return: Converted result.

        """
        for key in result_entry:
            if isinstance(result_entry[key], datetime):
                result_entry[key] = result_entry[key].strftime("%Y-%m-%d %H:%M:%S")
        return result_entry

    def result_paginator(self, method, **kwargs):
        """ Get the result in using get_paginator format for certain AWS IAM queries.
        Example calls include 'list_users' adn 'list_groups_for_user'.

        :param method: The method to pass to get_paginator e.g. 'list_users'.
        :param kwargs: Dictionary of AWS API parameters for function call .
        :return: Query result in a list.
        """
        result_type = None
        result = []
        try:
            paginator = self.iam.get_paginator(method)
            for response in paginator.paginate(**kwargs):
                if not result_type:
                    result_type = self._get_type_from_response(response)
                result.extend(response[result_type])

        except Exception as e:
            LOG.error("ERROR with method: '{0}' and args: '{1}, Got exception type: {2}, msg: {3}"
                      .format(method, kwargs, e.__repr__(), e.message))
            LOG.info(e)
            raise e

        return  self._update_result(result, result_type)

    def get_user(self, **kwargs):
        """ Get AWS IAM user properties.

        :param kwargs: Dictionary of AWS API parameters for function call .
        :return: Boolean.
        """
        result = []
        try:
            user = self.iam.get_user(**kwargs)["User"]
        except Exception as e:
            LOG.error("ERROR with 'get_user' and args: '{0}, Got exception type: {1}, msg: {2}"
                      .format(kwargs, e.__repr__(), e.message))
            raise e

        # Normalize result to be same as that of list all users.
        result.append(user)

        return  self._update_result(result, "User")

    def list_user_tags(self, **kwargs):
        # Get user tags:
        tags = []
        # Get user tags:
        try:
            tags = self.iam.list_user_tags(**kwargs)["Tags"]
        except Exception as e:
            LOG.error("ERROR with 'list_user_tags' and args: '{0}, Got exception type: {1}, msg: {2}"
                      .format(kwargs, e.__repr__(), e.message))
            LOG.info(e)
            raise e

        return tags

    def get_login_profile(self, **kwargs):
        """ Get AWS IAM user Profile.

        :param kwargs: Dictionary of AWS API parameters for function call .
        :return: Boolean.
        """
        # Set default good status:
        profile = {}

        try:

            response = self.iam.get_login_profile(**kwargs)
            profile = response["LoginProfile"]

        except self.iam.exceptions.NoSuchEntityException:
            LOG.info('ERROR get_login_profile {0} :{1} exception'.format(kwargs, "NoSuchEntity"))

            profile = {}

        except Exception as e:
            LOG.error("ERROR with 'get_login_profile' and args {0}, Got exception type: {1}, msg: {2}"
                      .format(kwargs, e.__repr__(), e.message))
            raise e

        return profile

    def delete_login_profile(self, **kwargs):
        """ Delete AWS IAM user Profile.

        :param kwargs: Dictionary of AWS API parameters for function call .
        :return: Converted  string.

        """
        # Set default good status:
        status = "OK"

        try:

            response = self.iam.delete_login_profile(**kwargs)

        except self.iam.exceptions.NoSuchEntityException:
            LOG.info('ERROR delete_login_profile {0} :{1} exception'.format(kwargs, "NoSuchEntity"))
            status = "NoSuchEntity"

        except Exception as e:
            LOG.error("ERROR with 'delete_login_profile' and args {0}, Got exception type: {1}, msg: {2}"
                      .format(kwargs, e.__repr__(), e.message))
            LOG.info(e)
            raise e

        return status

    def update_login_profile(self, **kwargs):

        # Get user tags:
        status = "OK"

        try:
            response = self.iam.update_login_profile(**kwargs)

        except self.iam.exceptions.PasswordPolicyViolation:
            LOG.info('ERROR update_login_profile {0} :{1} exception'.format(kwargs, "PasswordPolicyViolation"))
            status = "PasswordPolicyViolation"

        except Exception as e:
            LOG.error("ERROR with 'update_login_profile' and args {0}, Got exception type: {1}, msg: {2}"
                      .format(kwargs, e.__repr__(), e.message))
            raise e

        return status