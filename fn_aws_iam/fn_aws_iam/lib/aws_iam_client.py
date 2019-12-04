# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" AWS IAM client support classes. """
from  datetime import datetime
import logging
import re
from botocore.exceptions import ClientError
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
    "LoginProfile"
]
FILTER_NAMES = [
    "UserName",
    "GroupName",
    "PolicyName"
]

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
        :param service_name: AWS service for which to create client.
        :return: AWS client.
        """
        # Create IAM client for iam or sts.
        try:

            client = Session(
                region_name=self.aws_iam_region,
                aws_access_key_id=self.aws_iam_access_key_id,
                aws_secret_access_key=self.aws_iam_secret_access_key
            ).client(service_name=service_name)

        except ClientError as cli_ex:
            LOG.error("ERROR instantiating AWS IAM client for service: %s, Got exception : %s",
                      service_name, cli_ex.__repr__())
            raise cli_ex

        return client

    def _get_type_from_response(self, response, type_list):
        """ The get type of data returned in an AWS IAM query.

        :param kwargs: Dictionary of AWS API parameters for function call .
        :param response: The response from AWS API query.
        :param type_list: List of valid types  in AWS IAM responses.
        result_type: The type of result e.g. 'Users'.
        """
        for key in response:
            if key in type_list:
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
            if self.result_get(self.iam.get_login_profile, UserName=result[i]["UserName"]):
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
        else:
            LOG.error("ERROR with unexpected result type %s for AWS IAM query", type(result))

        if any(n in result_type for n in ["User", "Users"]):
            result = self._add_user_properties(result)

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

    def result_paginator(self, method=None, filter=None, **kwargs):
        """ Get the result using get_paginator format for certain AWS IAM queries.
        Example calls include 'list_users' adn 'list_groups_for_user'.

        :param method: The method to pass to get_paginator e.g. 'list_users'.
        :param filter: Dict of filters by filter type.
        :param kwargs: Dictionary of AWS API parameters for function call .
        :return: Query result in a list.
        """
        result_type = None
        result = []

        try:
            paginator = self.iam.get_paginator(method)
            for response in paginator.paginate(**kwargs):
                if not result_type:
                    result_type = self._get_type_from_response(response, SUPPORTED_PAGINATE_TYPES)
                result.extend(response[result_type])

        except Exception as int_ex:
            LOG.error("ERROR in paginator with method: '%s' and args: '%s', Got exception: %s",
                      method, kwargs, int_ex.__repr__())
            LOG.info(int_ex)
            raise int_ex

        # Make updates to the raw result.
        if result:
            result = self._update_result(result, result_type)

        # Apply filter to results.
        if result and filter:
            return self._filter(result, filter)
        else:
            # Unfiltered result
            return result

    def result_get(self, aws_iam_op, **kwargs):
        """ Execute a 'query' type AWS IAM  operation.
        Example calls include 'get_user' and 'get_user_tags'.
        Note: That some the calls will translate to actual 'post' operations.

        :param aws_iam_op: The AWS IAM operation to execute e.g. 'get_user'.
        :param kwargs: Dictionary of AWS API parameters for function call .
        :return: Result in a list.
        """
        result = []
        result_type = None
        op_name = aws_iam_op.__name__
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
            else:
                raise no_such_entity_ex

        except Exception as int_ex:
            LOG.error("ERROR with %s and args: '%s', Got exception: %s",
                      aws_iam_op.__name__, kwargs, int_ex.__repr__())
            raise int_ex

        if result_type == "User":
            # Normalize and update result for 'User' to be same as that of list all users.
            result.append(response[result_type])
            return self._update_result(result, result_type)
        else:
            return response[result_type]


    def result_post(self, aws_iam_op, **kwargs):
        """ Execute a 'post' type AWS IAM  operation whihc results in an update or change to the AWS IAM environment.
        Example calls include 'delete_access_key' and 'attach_user_policy'.

        :param aws_iam_op: The AWS IAM operation to execute e.g. 'delete_access_key'.
        :param kwargs: Dictionary of AWS API parameters for function call .
        :return status: Return status string.
        """
        # Set default good status:
        status = "OK"

        try:
            aws_iam_op(**kwargs)

        except self.iam.exceptions.NoSuchEntityException:
            LOG.info("ERROR with %s and args: '%s', Got exception: %s", aws_iam_op.__name__, kwargs, "NoSuchEntityException")
            status = "NoSuchEntity"

        except self.iam.exceptions.PasswordPolicyViolation:
            LOG.info("ERROR with $s and args: '%s', Got exception %s", aws_iam_op.__name__, kwargs, "PasswordPolicyViolation")
            status = "PasswordPolicyViolation"

        except Exception as int_ex:
            LOG.error("ERROR with %s and args '%s', Got exception: %s", aws_iam_op.__name__, kwargs, int_ex.__repr__())
            raise int_ex

        return status


    def _filter(self, result, filter=None):
        """ Filter results returned from AWS IAM.

        :param result: Dict or list of dicts from AWS IAM response.
        :param filter: Dict of filters by filter type.
        :return: Result or Tuple of filtered result count and either full or filtered result depending on filter type.
        """
        # Set default good status:

        rtn = (len(result), result)

        for filter_name in FILTER_NAMES:
            if filter and filter_name in filter and filter_name in result[0]:
                regex = r'{}'.format(filter[filter_name])
                filtered_result = [r for r in result if re.search(regex, r[filter_name], re.IGNORECASE)]
                if filter_name in FILTER_NAMES[0]:
                    # If file is 'UserName' return filtered count and filtered result.
                    rtn = (len(filtered_result), filtered_result)
                else:
                    # For other filter types return filtered count and full result.
                    rtn = (len(filtered_result), result)
        return rtn