# pylint: disable=line-too-long
class WatsonxApiException(Exception):
    """Generic API exception when interfacing with watsonx.ai"""

    status_code: int
    msg: str = "Unkown error"
    code: str = ""

    err_message: str

    def __init__(self, message: str = ""):
        self.err_message = message

    def __repr__(self):
        return f"""{self.__class__.__name__}: {self.status_code} - {self.msg} ({self.code}): {str(self.err_message or 'null')}"""


class WatsonxUnreachableException(WatsonxApiException):
    msg: str = (
        "Unable to reach watsonx.ai API. Ensure the WATSONX_ENDPOINT is configured correctly, and that the App Host can reach the internet."
    )


class WatsonxBadRequestException(WatsonxApiException):
    status_code = 400
    msg = "Bad request to watsonx.ai API. Please review the logs, and ensure watsonx_project_id, and watsonx_endpoint are configured properly in app.config."


class WatsonxUnauthorizedException(WatsonxApiException):
    status_code = 401
    msg = "Not authorized to use watsonx.ai. Check the watsonx_api_key, watsonx_project_id and watsonx_endpoint settings in the app.config for the watsonx.ai app. If using a trial account, ensure token usage has not been exceeded."


class WatsonxForbiddenException(WatsonxUnauthorizedException):
    status_code = 403


class WatsonxNotFoundException(WatsonxApiException):
    status_code = 404
    msg = "Not found"


class WatsonxTooManyRequestsException(WatsonxApiException):
    status_code = 429
    msg = "Rate limit exceeded. Upgrade your watsonx.ai subscription to increase rate limit, or try again when there are fewer concurrent requests."


class WatsonxModelIdNotFoundException(WatsonxNotFoundException):
    msg = "Model ID '{model_id}' not found. If this model is not available in the region endpoint set in the App config, you can change the model in the 'fn_watsonx_analyst_model_id' function input."
    code = "model_not_supported"

    def __init__(self, model_id: str):
        self.msg = self.msg.format(model_id=model_id)


class WatsonxTokenLimitExceededException(WatsonxBadRequestException):
    msg = """Number of tokens provided as input exceeds the limit allowed by the model.
Retry chunking with a lower input token threshold for the top chunks.
    """
    code = "invalid_input_argument"


class WatsonxUnparseableResponseException(WatsonxApiException):
    msg = "Unparseable response from watsonx.ai. Ensure that the watsonx_endpoint is set correctly, and that DNS records are resolved correctly."


class WatsonxInternalErrorException(WatsonxApiException):
    status_code = 500
    msg = "Unhandled error from watsonx.ai"
