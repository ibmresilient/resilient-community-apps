from typing import List, TypedDict

from fn_watsonx_analyst.types.message_payload import MessagePayload

class GeneratedTextResult(TypedDict):
    """Infer text result from watsonx"""
    generated_text: str
    generated_token_count: int
    input_token_count: int
    stop_reason: str

class EmbeddingResult(TypedDict):
    """Embed text result from watsonx"""

    embedding: List[float]

class WatsonxTextGenerationResponse(TypedDict):
    """Full watsonx response for infer text"""
    model_id: str
    created_at: str
    results: List[GeneratedTextResult]

class WatsonxEmbeddingResponse(TypedDict):
    """Full watsonx response for embedding text"""
    model_id: str
    created_at: str
    results: List[EmbeddingResult]
    input_token_count: int

class ChatResult(TypedDict):
    """Embedded chat response"""
    index: int
    message: MessagePayload
    finish_reason: str

class SystemMessage(TypedDict):
    warnings: dict

class WatsonxChatResponse(TypedDict):
    """Full watsonx response for text chat"""
    id: str
    object: str
    
    model_id: str
    model: str

    choices: List[ChatResult]
    
    created: int
    created_at: str

    usage: dict
    system: SystemMessage