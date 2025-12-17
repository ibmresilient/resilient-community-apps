from functools import cache
from typing import Tuple
from fn_watsonx_analyst.config import ModelConfig, load_model_config


class ModelHelper:

    EMBEDDING_MODEL_COST = 0.1

    @staticmethod
    @cache
    def get_model_config(model_id: str) -> ModelConfig:
        config = load_model_config()
        for model in config:
            if model["name"] == model_id:
                return model
        raise ValueError("model not found")

    @staticmethod
    def context_length_for_model(model_id: str) -> int:
        return ModelHelper.get_model_config(model_id)["context_length"]

    @staticmethod
    def max_output_tokens_for_model(model_id: str) -> int:
        return ModelHelper.get_model_config(model_id)["max_output_tokens"]

    def get_model_cost(self, model_id: str) -> Tuple[float, float, float]:
        """
        Returns the input cost, output cost, and embedding model cost per 1M tokens
        """
        model_conf = ModelHelper.get_model_config(model_id)
        return (model_conf["input_cost"], model_conf["output_cost"], self.EMBEDDING_MODEL_COST)

