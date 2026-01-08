from typing import List, TypedDict

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
