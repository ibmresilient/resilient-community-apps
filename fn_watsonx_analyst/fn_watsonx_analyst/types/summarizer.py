from typing import Callable, List, Tuple

from fn_watsonx_analyst.types.ai_response import AIResponse

Summarizer = Callable[[], Tuple[str, AIResponse]]
