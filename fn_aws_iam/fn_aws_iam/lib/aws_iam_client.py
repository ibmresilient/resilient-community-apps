# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" AWS IAM client support classes. """
from  datetime import datetime
import logging
import re
from botocore.exceptions import ClientError
from botocore.config import Config
from boto3 import Session

LOG = logging.getLogger(__name__)
# List of paginated types supported for the integration.
SUPPORTED_PAGINATE_TYPES = [
    "Users",
    "Groups",
    "AccessKeyMetadata",
    "Policies",
    "PolicyNames",
    "AttachedPolicies"
]
SUPPORTED_GET_TYPES = [
    "User",
    "Tags",
    "LoginProfile",
    "AccessKeyLastUsed"
]
FILTER_NAMES = [
    "UserName",
    "GroupName",
    "PolicyName",
    "AccessKeyId"
]

class AwsIamClient():
    """
    Client class for AWS IAM.
    """
    def __init__(self, function_options={}, sts_client=False):
        """
        Class constructor.
        """
        if not isinstance(function_options, dict) and not function_options:
            raise ValueError("The 'function_options' parameter is not set correctly.")
        self.aws_iam_access_key_id = function_options.get("aws_iam_access_key_id", None)
        if not self.aws_iam_access_key_id:
            raise ValueError("The '{}' config setting is not set for the '{}' parameter."
                             .format("aws_iam_access_key_id", "function_options"))
        self.aws_iam_secret_access_key = function_options.get("aws_iam_secret_access_key", None)
        if not self.aws_iam_secret_access_key:
            raise ValueError("The '{}' config setting is not set for the '{}' parameter."
                             .format("aws_iam_secret_access_key", "function_options"))
        self.aws_iam_region = function_options.get("aws_iam_region", None)

        self.proxies = {}
        if "https_proxy" in function_options and function_options["https_proxy"] is not None:
            self.proxies.update({"https": function_options.get("https_proxy")})
        if "http_proxy" in function_options and function_options["http_proxy"] is not None:
            self.proxies.update({"http": function_options.get("http_proxy")})

        self.iam = self._get_client("iam")

        if sts_client:
            self.sts = self._get_client("sts")
            self.default_identity = self._get_default_identity()

    def _get_client(self, service_name):
        """ Create an AWS IAM client.

        :param service_name: AWS service for which to create client.
        :return: AWS client.
        """
        # Create an AWS boto3 client instance for the specified AWS service name. Supported AWS service names
        # for the integration are 'aws' and 'sts'.
        try:
            client = Session(
                region_name=self.aws_iam_region,
                aws_access_key_id=self.aws_iam_access_key_id,
                aws_secret_access_key=self.aws_iam_secret_access_key,
            ).client(service_name=service_name, config=Config(proxies=self.proxies))

        except ClientError as cli_ex:
            LOG.error("ERROR instantiating AWS IAM client for service: %s, Got exception : %s",
                      service_name, cli_ex.__repr__())
            raise cli_ex

        return client

    def _add_user_properties(self, result):
        """ Add metadata entries for login profile, default user.

        :param result: List of dicts from AWS IAM response.
        :return: Updated result.

        """
        # Add a flag for the default user in result.
        default_index = None
        default_identity = self._get_default_identity()
        for i in range(len(result)):
            if self.get("get_login_profile", UserName=result[i]["UserName"]):
                result[i].update({"LoginProfileExists": "Yes"})
            else:
                result[i].update({"LoginProfileExists": "No"})
            if result[i]["UserId"] == default_identity["UserId"]:
                default_index = i
                result[i].update({"DefaultUser": "Yes"})

        # Insert the default user at the top of the result.
        if default_index and len(result) > 1:
            result.insert(0, result.pop(default_index))

        return result

    def _add_access_key_properties(self, result):
        """ Add metadata entries for access keys.

        :param result: List of dicts from AWS IAM response.
        :return: Updated result.

        """
        # Add a flag for the default access key in result.
        for i in range(len(result)):
            if result[i]["AccessKeyId"] == self.aws_iam_access_key_id:
                result[i].update({"DefaultKey": "Yes"})
        return result

    def _update_result(self, result, result_type):
        """ Make any necessary conversions and additions to AWS IAM result.

        :param result: Dict or list of dicts from AWS IAM response.
        :param result_type: The type of result e.g. 'Users'.
        :return: Updated result.

        """
        if isinstance(result, list):
            for entry in result:
                if isinstance(entry, dict):
                    entry = self._datetime_to_str(entry)
        elif isinstance(result, dict):
            result = self._datetime_to_str(result)
        else:
            LOG.error("ERROR with unexpected result type %s for AWS IAM query", type(result))
        # If the result is for a user or list of users add some additional user properties.
        if any(n in result_type for n in ["User", "Users"]):
            result = self._add_user_properties(result)
        elif "AccessKeyMetadata" in result_type:
            result = self._add_access_key_properties(result)
        return result

    def _get_default_identity(self):
        """ Get the identity of the current AWS IAM user.

        :return default_identity: Called identity dict.
        """
        try:
            default_identity = self.sts.get_caller_identity()

        except Exception as int_ex:
            LOG.error("ERROR with 'get_caller_identity' Got exception: %s",
                      int_ex.__repr__())
            raise int_ex

        return default_identity

    def paginate(self, op=None, results_filter=None, return_filtered=False, **kwargs):
        """ Get the result using get_paginator format for certain AWS IAM queries.
        Example calls include 'list_users' adn 'list_groups_for_user'.

        :param op: The AWS IAM operation to execute e.g. 'list_users'.
        :param results_filter: Dict of filters by filter type.
        :param kwargs: Dictionary of AWS API parameters for function call .
        :return: Query result in a list.
        """
        result_type = None
        result = []
        try:
            paginator = self.iam.get_paginator(op)
            for response in paginator.paginate(**kwargs):
                if not result_type:
                    result_type = self._get_type_from_response(response, SUPPORTED_PAGINATE_TYPES)
                result.extend(response[result_type])

        except Exception as int_ex:
            LOG.error("ERROR in paginator with operation: '%s' and args: '%s', Got exception: %s",
                      op, kwargs, int_ex.__repr__())
            LOG.info(int_ex)
            raise int_ex

        # Make updates to the raw result.
        if result:
            result = self._update_result(result, result_type)

        # Apply filter to results.
        if result and results_filter:
            return self._filter(result, results_filter, return_filtered)

        # Return unfiltered result
        return result

    def get(self, op=None, paginate=False, return_filtered=False, **kwargs):
        """ Execute a 'query' type AWS IAM  operation.
        Example calls include 'get_user' and 'get_user_tags', 'list_users'.
        The calls will translate to actual 'get' or query operations. The operation will return
        standard or paginated result since not all query operations support pagination.

        :param op: The AWS IAM operation to execute e.g. 'get_user' or 'list_users'.
        :param paginate: Boolean to indicate operation will return paginated result e.g. 'list_users'.
        :param kwargs: Dictionary of AWS API parameters for function call .
        :return: Result in a list.
        """
        if paginate:
            return self.paginate(op, return_filtered=return_filtered, **kwargs)

        result = []
        result_type = None
        try:
            # Get the AWS IAM object corresponding to the operation 'op'.
            aws_iam_op = getattr(self.iam, op)
        except AttributeError as attr_ex:
            LOG.error("Unknown AWS IAM operation %s, Got exception: %s",
                      op, attr_ex.__repr__())
            raise attr_ex

        try:
            response = aws_iam_op(**kwargs)

            if not result_type:
                result_type = self._get_type_from_response(response, SUPPORTED_GET_TYPES)

        except self.iam.exceptions.NoSuchEntityException as no_such_entity_ex:
            LOG.info("ERROR with %s and args: '%s', Got exception: %s",
                     aws_iam_op.__name__, kwargs, "NoSuchEntityException")
            # If Return empty dict if the object doesn't exist.
            if aws_iam_op.__name__ == "get_login_profile":
                # If result is of type 'get_login_profile' return empty dict if the object doesn't exist.
                return {}

            raise no_such_entity_ex

        except Exception as int_ex:
            LOG.error("ERROR with %s and args: '%s', Got exception: %s",
                      aws_iam_op.__name__, kwargs, int_ex.__repr__())
            raise int_ex

        if result_type == "User":
            # Normalize and update result for 'User' to be same as that of list all users.
            result.append(response[result_type])
        else:
            result = response[result_type]

        return self._update_result(result, result_type)


    def post(self, op, **kwargs):
        """ Execute a 'post' type AWS IAM  operation which results in an update or change to the AWS IAM environment.
        Example calls include 'delete_access_key' and 'attach_user_policy'.

        :param op: The AWS IAM operation to execute e.g. 'delete_access_key'.
        :param kwargs: Dictionary of AWS API parameters for function call .
        :return status: Return status string.
        """
        # Set default good status:
        status = "OK"
        try:
            # Get the AWS IAM object corresponding to the operation 'op'.
            aws_iam_op = getattr(self.iam, op)
        except AttributeError as attr_ex:
            LOG.error("Unknown AWS IAM operation %s, Got exception: %s",
                      op, attr_ex.__repr__())
            raise attr_ex
        try:
            aws_iam_op(**kwargs)

        except self.iam.exceptions.NoSuchEntityException:
            LOG.info("ERROR with %s and args: '%s', Got exception: %s", aws_iam_op.__name__, kwargs, "NoSuchEntityException")
            status = "NoSuchEntity"

        except self.iam.exceptions.PasswordPolicyViolation:
            LOG.info("ERROR with %s and args: '%s', Got exception %s", aws_iam_op.__name__, kwargs, "PasswordPolicyViolation")
            status = "PasswordPolicyViolation"

        except Exception as int_ex:
            LOG.error("ERROR with %s and args '%s', Got exception: %s", aws_iam_op.__name__, kwargs, int_ex.__repr__())
            raise int_ex

        return status


    def _filter(self, result, results_filter=None, return_filtered=False):
        """ Filter results returned from AWS IAM.

        :param result: Dict or list of dicts from AWS IAM response.
        :param results_filter: Dict of filters by filter type.
        :param return_filtered: Boolean to determine whether the filtered result is returned in result tuple.
        :return: Result or Tuple of filtered result count and either full or filtered result depending on filter type.
        """
        # Set default good result:
        rtn = (len(result), result)

        for filter_name in FILTER_NAMES:
            if results_filter and filter_name in results_filter and filter_name in result[0]:
                regex = r'{}'.format(results_filter[filter_name])
                filtered_result = [r for r in result if re.search(regex, r[filter_name], re.IGNORECASE)]
                if return_filtered:
                    # Return filtered count and filtered result.
                    rtn = (len(filtered_result), filtered_result)
                else:
                    # If Boolean not set return filtered count and full result.
                    rtn = (len(filtered_result), result)
        return rtn

    @staticmethod
    def _get_type_from_response(response, type_list):
        """ The get type of data returned in an AWS IAM response.

        :param response: The response from AWS API query.
        :param type_list: List of valid types  in AWS IAM responses.
        result_type: The type of result e.g. 'Users'.
        """
        result_type = None
        for key in response:
            if key in type_list:
                result_type = key

        if not result_type:
            raise ValueError("No supported type for integration found in AWS IAM response")

        return result_type

    @staticmethod
    def _datetime_to_str(result_entry):
        """ Convert datetime objects returned in result e.g. 'CreateDate' to a string.

        :param result_entry: Result entry dict from AWS IAM response.
        :return result_entry: Converted result entry.
        """
        for key in result_entry:
            if isinstance(result_entry[key], datetime):
                result_entry[key] = result_entry[key].strftime("%Y-%m-%d %H:%M:%S")
        return result_entry
