# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import logging
import uuid
from fn_aws_utilities.util.aws_common import AWSCommon
import time


class AwsStepFunction(AWSCommon):
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        """Initializes boto3 client"""
        AWSCommon.__init__(self, "stepfunctions", aws_access_key_id, aws_secret_access_key, region_name)

    def get_execution_result(self, execution_arn):
        """Returns details about an ongoing description"""
        log = logging.getLogger(__name__)

        try:
            execution_description = self.aws_client.describe_execution(executionArn=execution_arn)
        except Exception as e:
            log.error(e)  # Python 3.6 compatible exception info
            raise Exception("Failed to retrieve execution description (is the ARN valid?).")

        return execution_description

    def invoke_step_function(self, step_function_name, async, payload):
        """Invoke a step function aka a state machine"""
        next_token = None
        state_machine_arn = None
        while True:
            if next_token is None:  # If there are any more state machines we're missing
                state_machine_query = self.aws_client.list_state_machines(maxResults=100)  # can't do more than 100
            else:
                state_machine_query = self.aws_client.list_state_machines(maxResults=100, nextToken=next_token)

            state_machines = state_machine_query.get("stateMachines")

            for state_machine in state_machines:
                if state_machine.get("name") == step_function_name:
                    state_machine_arn = state_machine.get("stateMachineArn")
                    break

            if state_machine_arn is not None:  # if we found the arn
                break

            next_token = state_machine_query.get("nextToken")

            if next_token is None:  # If we reached the end of the step functions list, and still haven't found it
                raise Exception("Unable to find the step function by that name")

        if state_machine_arn is None:
            raise ValueError("Could not find state machine")

        log = logging.getLogger(__name__)

        try:
            execution_information = self.aws_client.start_execution(stateMachineArn=state_machine_arn, input=payload)
        except Exception as e:
            log.error(e)  # Python 3.6 compatible exception info
            raise Exception("Failed to start execution")

        execution_arn = execution_information.get("executionArn")

        try:
            execution_description = self.aws_client.describe_execution(executionArn=execution_arn)
        except Exception as e:
            log.error(e)  # Python 3.6 compatible exception info
            raise Exception("Failed to get execution information")

        execution_status = execution_description.get("status")

        if async is False:
            while execution_description.get("output") is None:
                execution_description = self.aws_client.describe_execution(executionArn=execution_arn)
                execution_status = execution_description.get("status")
                if execution_status != "RUNNING" and execution_status != "SUCCEEDED":
                    raise Exception("Function did not complete successfully, status: {}.".format(execution_status))

                log.info('Execution not complete, sleeping for 10 seconds')
                time.sleep(10)  # Free up the CPU and don't spam API calls

            return execution_description

        # There is no default state "STARTING", only running, so no need to loop to make sure it has started
        if execution_status != "RUNNING" and execution_status != "SUCCEEDED":
            raise Exception("Function did not complete successfully, status: {}.".format(execution_status))

        return execution_description
