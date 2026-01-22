from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose

class RequestContext:
    """
    Data class to store Function invocation state
    """
    model_id: str
    purpose: AiResponsePurpose

    input_tokens: int = 0
    output_tokens: int = 0
    embedding_tokens: int = 0
