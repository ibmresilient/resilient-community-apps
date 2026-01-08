import json
from unittest.mock import patch

import pytest
from fn_watsonx_analyst.util.errors import (
    WatsonxApiException,
    WatsonxBadRequestException,
    WatsonxForbiddenException,
    WatsonxModelIdNotFoundException,
    WatsonxNotFoundException,
    WatsonxTokenLimitExceededException,
    WatsonxUnauthorizedException,
)

from tests import helper
from tests.helper import FakeResponse, generate_app_state

from fn_watsonx_analyst.util.persistent_org_cache import CacheObj
from fn_watsonx_analyst.util.QueryHelper import QueryHelper
from fn_watsonx_analyst.util.state_manager import app_state

def mock_fetch_data(_self, _res_client, cache_obj: CacheObj, watsonx_api_key):
    match cache_obj:
        case "watsonx_key":
            return {"access_token": watsonx_api_key}
        case _:
            return {}  # TODO sample org JSON


watsonx_endpoint_url = "https://us-south.ml.cloud.ibm.com"

embedding_response = json.loads(
    """
{
  "model_id": "slate",
  "results": [
    {
      "embedding": [
        -0.006929283,
        -0.005336422,
        -0.024047505
      ]
    }
  ],
  "created_at": "2024-02-21T17:32:28Z",
  "input_token_count": 10
}
"""
)

models_response = json.loads(
    """
{
  "total_count": 1,
  "limit": 100,
  "first": {
    "href": "https://us-south.ml.cloud.ibm.com/ml/v1/foundation_model_specs?version=2023-05-02"
  },
  "resources": [
    {
      "model_id": "bigcode/starcoder",
      "label": "starcoder-15.5b",
      "provider": "BigCode",
      "source": "Hugging Face",
      "short_description": "The StarCoder models are 15.5B parameter models that can generate code from natural language descriptions",
      "tasks": [
        {
          "id": "code",
          "ratings": {
            "quality": 3
          }
        }
      ],
      "min_shot_size": 0,
      "input_tier": "class_2",
      "output_tier": "class_2",
      "number_params": "15.5b"
    }
  ]
}"""
)

sample_response = json.loads(
    """
{
  "model_id": "google/flan-t5-xl",
  "created_at": "2023-07-21T16:52:32.190Z",
  "results": [
    {
      "generated_text": "Test **output** goes here",
      "generated_token_count": 118,
      "input_token_count": 11,
      "stop_reason": "eos_token",
      "moderations": {
        "pii": [
          {
            "score": 0.8,
            "input": false,
            "position": {
              "start": 74,
              "end": 88
            },
            "entity": "PhoneNumber"
          },
          {
            "score": 0.8,
            "input": false,
            "position": {
              "start": 200,
              "end": 212
            },
            "entity": "PhoneNumber"
          },
          {
            "score": 0.8,
            "input": false,
            "position": {
              "start": 244,
              "end": 259
            },
            "entity": "EmailAddress"
          }
        ]
      }
    }
  ]
}"""
)


def make_body(errCode: str) -> dict:
    return {"errors": [{"code": errCode}]}


def mock_req_get(url: str, headers=None, timeout=30):
    return FakeResponse(200, models_response)

def mock_req_post(url: str, data, json=None, timeout=None, headers=None):

    if watsonx_endpoint_url in url:
        if url.endswith("/ml/v1/text/embeddings?version=2023-10-25"):
            return FakeResponse(200, embedding_response)


        return FakeResponse(200, sample_response)

    body = make_body(url)
    match url:
        case "bad_req":
            return FakeResponse(400, body)
        case WatsonxTokenLimitExceededException.code:
            return FakeResponse(400, body)
        case "unauthorized":
            return FakeResponse(401, body)
        case "forbidden":
            return FakeResponse(403, body)
        case "not_found":
            return FakeResponse(404, body)
        case "model_not_supported":
            return FakeResponse(404, body)


@patch("requests.post", mock_req_post)
@patch(
    "fn_watsonx_analyst.util.persistent_org_cache.PersistentCache.get_data",
    mock_fetch_data,
)
class TestQueryHelper:

    def test_text_generation(self):

        generate_app_state(watsonx_endpoint=watsonx_endpoint_url)
        query_helper = QueryHelper()
        x = query_helper.text_generation("test_prompt")
        assert x["results"][0]["generated_text"] == sample_response["results"][0]["generated_text"]

    def test_ensure_correct_excs(self):
        def expect_exc(qh: QueryHelper, url: str, exc: WatsonxApiException):
            def mock_get_endpoint(_self):
                return url

            with patch(
                "fn_watsonx_analyst.util.QueryHelper.QueryHelper._get_api_endpoint",
                mock_get_endpoint,
            ):
                with pytest.raises(exc):
                    qh.text_generation("test prompt")

        query_helper = QueryHelper()

        expect_exc(query_helper, "bad_req", WatsonxBadRequestException)
        expect_exc(
            query_helper,
            WatsonxTokenLimitExceededException.code,
            WatsonxTokenLimitExceededException,
        )
        expect_exc(query_helper, "unauthorized", WatsonxUnauthorizedException)
        expect_exc(query_helper, "forbidden", WatsonxForbiddenException)
        expect_exc(query_helper, "not_found", WatsonxNotFoundException)
        expect_exc(query_helper, "model_not_supported", WatsonxModelIdNotFoundException)

    def test_get_embeddings(self):

        generate_app_state(watsonx_endpoint=watsonx_endpoint_url)
        query_helper = QueryHelper()

        assert query_helper.generate_embeddings("test_prompt") == [
            embedding_response["results"][0]["embedding"]
        ]

    @patch("requests.get", mock_req_get)
    def test_get_models(self):
        generate_app_state(watsonx_endpoint=watsonx_endpoint_url)
        query_helper = QueryHelper()

        assert query_helper.get_generation_models() == ["bigcode/starcoder"]

    def test_get_api_key(self):
        api_key = "api_key_123"
        opts = {
            "fn_watsonx_analyst": {
                "watsonx_api_key": api_key,
                "watsonx_project_id": "",
                "watsonx_endpoint": "",
            }
        }

        generate_app_state()
        app_state.get().opts = opts

        query_helper = QueryHelper()

        assert (
            query_helper.get_api_key(None)
            == opts["fn_watsonx_analyst"]["watsonx_api_key"]
        )

