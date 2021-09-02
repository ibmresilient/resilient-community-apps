from datetime import datetime

mock_constants = {
    "DATE_TIME_MOCK_OBJ": datetime(2015, 1, 1)
}

def mocked_aws_step_function(*args, **kwargs):
    class MockAwsStepFunction:
        def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
            """Mock init; does nothing"""
            pass

        def get_execution_result(self, execution_arn):
            """Mock function that returns details about an ongoing execution description"""
            if execution_arn == "0000":
                startDate = mock_constants.get("DATE_TIME_MOCK_OBJ")
                stopDate = mock_constants.get("DATE_TIME_MOCK_OBJ")
            elif execution_arn == "1111":
                startDate = mock_constants.get("DATE_TIME_MOCK_OBJ")
                stopDate = None

            return {
                # response formatted from 
                # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.describe_execution
                'startDate': startDate,
                'stopDate': stopDate,
            }

        def invoke_step_function(self, step_function_name, async_bool, payload):
            return self.get_execution_result(step_function_name)

    return MockAwsStepFunction(*args, **kwargs)

def mocked_aws_lambda(*args, **kwargs):
    class MockAWSLambda:
        def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
            """Mock init; does nothing"""
            pass

        def invoke_lambda(self, function_name, payload):
            """Mock invocation of AWS lambda"""
            if function_name == "two_int_sum":
                val = int(payload.get("x")) + int(payload.get("y"))
            elif function_name == "concat_strings":
                val = payload.get("str1") + payload.get("str2")

            return {
                # response json formatted from 
                # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.invoke
                'StatusCode': 200,
                'FunctionError': 'MockedFunctionError',
                'LogResult': 'MockedLogResult',
                'Payload': _MockResponse(val),
                'ExecutedVersion': 'nan'
            }

    class _MockResponse:
        def __init__(self, val):
            self.val = val
        
        def read(self):
            return self.val

    return MockAWSLambda(*args, **kwargs)

def mocked_aws_sns(*args, **kwargs):
    class AwsSns:
        def __init__(self, aws_access_key_id, aws_secret_access_key, region_name, topic_name):
            pass

        def send_text_via_sns(self, message, cell_numbers):
            return {
                # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.publish
                'MessageId': '0000',
                'SequenceNumber': 'None'
            }
    
    return AwsSns(*args, **kwargs)
