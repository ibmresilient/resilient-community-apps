# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" AWS GuardDuty client class. """
import logging

from botocore.exceptions import ClientError
from botocore.config import Config
from boto3 import Session
from resilient_lib import RequestsCommon

LOG = logging.getLogger(__name__)
# List of get types supported for the integration.
SUPPORTED_GET_TYPES = [
    "Findings",
    "Regions"
]
# List of get paginated types supported for the integration.
SUPPORTED_PAGINATE_TYPES = [
    "DetectorIds",
    "FindingIds"
]


class AwsGdClient():
    """
    Client class for AWS GuardDuty.
    """
    def __init__(self, opts, function_options=None, service_name=None, region=None):
        """
        Class constructor.
        """
        if not isinstance(opts, dict) and not opts:
            raise ValueError("The 'opts' parameter is not set correctly.")
        if not isinstance(function_options, dict) and not function_options:
            raise ValueError("The 'function_options' parameter is not set correctly.")
        if not region:
            raise ValueError("The 'region' parameter is not set correctly.")

        self.aws_gd_access_key_id = function_options.get("aws_gd_access_key_id")
        self.aws_gd_secret_access_key = function_options.get("aws_gd_secret_access_key")
        self.aws_gd_region = region
        self.proxies = RequestsCommon(opts, function_options).get_proxies()
        if not service_name:
            service_name = "guardduty"
        self.gd = self._get_client(service_name)

    def _get_client(self, service_name):
        """ Create an AWS GuardDuty client.

        :param service_name: AWS service for which to create client.
        :param aws_gd_region: (Optional): AWS Region default is the integration default.
        :return: AWS client.
        """
        # Create an AWS boto3 client instance for AWS GuardDuty.

        try:
            client = Session(
                region_name=self.aws_gd_region,
                aws_access_key_id=self.aws_gd_access_key_id,
                aws_secret_access_key=self.aws_gd_secret_access_key,
            ).client(service_name=service_name, config=Config(proxies=self.proxies))

        except ClientError as cli_ex:
            LOG.error("ERROR instantiating AWS GuardDuty client for service: %s, Got exception : %s",
                      service_name, str(cli_ex))
            raise cli_ex

        return client


    def paginate(self, op=None, **kwargs):
        """ Get the result using get_paginator format for certain AWS GuardDuty queries.

        :param op: The AWS GuardDuty operation to execute.
        :param kwargs: Dictionary of AWS API parameters for function call .
        :return: Query result in a list.
        """
        result_type = None
        result = []

        try:
            paginator = self.gd.get_paginator(op)
            for response in paginator.paginate(**kwargs):
                if not result_type:
                    result_type = self._get_type_from_response(response, SUPPORTED_PAGINATE_TYPES)

                result.extend(response[result_type])

        except self.gd.exceptions.InternalServerErrorException as intserv_ex:
            LOG.info("ERROR with %s and args: '%s', Got exception: %s",
                     op, kwargs, "InternalServerErrorException")
            raise intserv_ex

        except self.gd.exceptions.BadRequestException as badreq_ex:
            LOG.info("ERROR with %s and args: '%s', Got exception: %s",
                     op, kwargs, "BadRequestException")
            raise badreq_ex

        except self.gd.exceptions.ClientError as invalid_ex:

            if "ValidationError" in str(invalid_ex):

                LOG.info("ERROR with %s and args: '%s', Got exception: %s",
                         op, kwargs, "ValidationErrorException")

            raise invalid_ex

        except Exception as int_ex:
            LOG.error("ERROR in paginator with operation: '%s' and args: '%s', Got exception: %s",
                      op, kwargs, str(int_ex))
            LOG.info(int_ex)
            raise int_ex

        return result

    def get(self, op=None, paginate=False, **kwargs):
        """ Execute a "query" type AWS GuardDuty  operation.
        The calls will translate to actual "get" or query operations. The operation will return
        standard or paginated result since not all query operations support pagination.

        :param op: The AWS GuardDuty operation to execute.
        :param paginate: Boolean to indicate operation will return paginated result.
        :param kwargs: Dictionary of AWS API parameters for function call .
        :return: Result in a list.
        """
        if self.gd.can_paginate(op):
            return self.paginate(op, **kwargs)

        result = []
        result_type = None
        try:
            # Get the AWS GuardDuty object corresponding to the operation "op".
            aws_gd_op = getattr(self.gd, op)
        except AttributeError as attr_ex:
            LOG.error("Unknown AWS GuardDuty operation %s, Got exception: %s",
                      op, str(attr_ex))
            raise attr_ex

        try:
            response = aws_gd_op(**kwargs)

            if not result_type:
                result_type = self._get_type_from_response(response, SUPPORTED_GET_TYPES)

        except self.gd.exceptions.InternalServerErrorException as intserv_ex:
            LOG.info("ERROR with %s and args: '%s', Got exception: %s",
                     aws_gd_op.__name__, kwargs, "InternalServerErrorException")
            raise intserv_ex

        except self.gd.exceptions.BadRequestException as badreq_ex:
            LOG.info("ERROR with %s and args: '%s', Got exception: %s",
                     aws_gd_op.__name__, kwargs, "BadRequestException")
            raise badreq_ex

        except self.gd.exceptions.ClientError as invalid_ex:

            if "ValidationError" in str(invalid_ex):

                LOG.info("ERROR with %s and args: '%s', Got exception: %s",
                         aws_gd_op.__name__, kwargs, "ValidationErrorException")

            raise invalid_ex

        except Exception as int_ex:

            LOG.error("ERROR with %s and args: '%s', Got exception: %s",
                      aws_gd_op.__name__, kwargs, str(int_ex))
            raise int_ex

        result = response[result_type]

        return result

    def post(self, op, **kwargs):
        """ Execute a "post" type AWS GuardDuty  operation which results in an update or change
        to the AWS GuardDuty environment.

        :param op: The AWS GuardDuty operation to execute.
        :param kwargs: Dictionary of AWS API parameters for function call .
        :return status: Return status string.
        """
        # Set default good status:
        status = {"status": "ok"}
        try:
            # Get the AWS GuardDuty object corresponding to the operation "op".
            aws_gd_op = getattr(self.gd, op)
        except AttributeError as attr_ex:
            LOG.error("Unknown AWS GuardDuty operation %s, Got exception: %s",
                      op, str(attr_ex))
            raise attr_ex
        try:
            res = aws_gd_op(**kwargs)

        except self.gd.exceptions.ClientError as invalid_ex:
            for excp in ["ValidationError", "BadRequestException", "InternalServerErrorException"
                         "EndpointConnectionError"]:
                if excp in str(invalid_ex):
                    return {"status": "error", "msg": str(invalid_ex)}

            LOG.info("ERROR with %s and args: '%s', Got exception: %s",
                     aws_gd_op.__name__, kwargs, "ValidationErrorException")
            raise invalid_ex

        except Exception as int_ex:
            LOG.error("ERROR with %s and args '%s', Got exception: %s", aws_gd_op.__name__, kwargs, str(int_ex))
            raise int_ex

        return status


    @staticmethod
    def _get_type_from_response(response, type_list):
        """ The get type of data returned in an AWS GuardDuty response.

        :param response: The response from AWS API query.
        :param type_list: List of valid types  in AWS GuardDuty responses.
        result_type: The type of result e.g. "Findings".
        """
        result_type = None
        for key in response:
            if key in type_list:
                result_type = key

        if not result_type:
            raise ValueError("No supported type for integration found in AWS GuardDuty response")

        return result_type
