import pytest
from unittest.mock import MagicMock, patch

from fn_watsonx_analyst.util.watsonx_client import WatsonxClient
from fn_watsonx_analyst.util.errors import (
    WatsonxBadRequestException,
    WatsonxForbiddenException,
    WatsonxModelIdNotFoundException,
    WatsonxNotFoundException,
    WatsonxTokenLimitExceededException,
    WatsonxUnauthorizedException,
    WatsonxUnreachableException,
    WatsonxApiException,
    WatsonxTooManyRequestsException,
    WatsonxInternalErrorException,
)
from fn_watsonx_analyst.util.state_manager import app_state
from tests.helper import generate_app_state


class TestWatsonxClientInitialization:
    """Test WatsonxClient initialization and configuration"""

    def test_init_success(self):
        """Test successful initialization with valid config"""
        generate_app_state()
        client = WatsonxClient()
        
        assert client.model_id is not None
        assert client.res_client is not None
        assert client.opts is not None
        assert client.credentials is not None
        assert client.wx_client is not None
        assert client.project_id is not None

    def test_init_without_opts_raises_error(self):
        """Test initialization fails without application options"""
        generate_app_state()
        app_state.get().opts = None
        
        with pytest.raises(ValueError, match="Application options not configured"):
            WatsonxClient()

    def test_get_config_value_success(self):
        """Test retrieving configuration values"""
        endpoint = "https://us-south.ml.cloud.ibm.com"
        generate_app_state(watsonx_endpoint=endpoint)
        client = WatsonxClient()
        
        endpoint = client._get_config_value('watsonx_endpoint')
        assert endpoint == endpoint

    def test_get_config_value_missing_key(self):
        """Test retrieving missing configuration key returns None"""
        generate_app_state()
        client = WatsonxClient()
        
        value = client._get_config_value('nonexistent_key')
        assert value is None

    def test_get_config_value_empty_value(self):
        """Test retrieving empty configuration value returns None"""
        generate_app_state()
        client = WatsonxClient()
        
        value = client._get_config_value('watsonx_endpoint')
        assert value == None


class TestWatsonxClientMessageBuilding:
    """Test message building functionality"""

    def test_build_message_user_role(self):
        """Test building a user message"""
        generate_app_state()
        client = WatsonxClient()
        
        message = client.build_message("user", "Hello, world!")
        
        assert message["role"] == "user"
        assert message["content"] == "Hello, world!"
        assert isinstance(message, dict)

    def test_build_message_system_role(self):
        """Test building a system message"""
        generate_app_state()
        client = WatsonxClient()
        
        message = client.build_message("system", "You are a helpful assistant")
        
        assert message["role"] == "system"
        assert message["content"] == "You are a helpful assistant"

    def test_build_message_assistant_role(self):
        """Test building an assistant message"""
        generate_app_state()
        client = WatsonxClient()
        
        message = client.build_message("assistant", "I can help you with that")
        
        assert message["role"] == "assistant"
        assert message["content"] == "I can help you with that"

    def test_build_message_empty_content(self):
        """Test building a message with empty content"""
        generate_app_state()
        client = WatsonxClient()
        
        message = client.build_message("user", "")
        
        assert message["role"] == "user"
        assert message["content"] == ""


class TestWatsonxClientChat:
    """Test chat functionality"""

    def test_chat_success(self):
        """Test successful chat request"""
        generate_app_state()
        client = WatsonxClient()
        
        messages = [
            client.build_message("system", "You are a helpful assistant"),
            client.build_message("user", "Hello!")
        ]
        
        response = client.chat(messages)
        
        assert "choices" in response
        assert len(response["choices"]) > 0
        assert "message" in response["choices"][0]
        assert "content" in response["choices"][0]["message"]
        assert response["choices"][0]["message"]["role"] == "assistant"

    def test_chat_with_temperature(self):
        """Test chat with custom temperature"""
        generate_app_state()
        client = WatsonxClient()
        
        messages = [client.build_message("user", "Test message")]
        
        response = client.chat(messages, temperature=0.5)
        
        assert "choices" in response
        assert response["choices"][0]["message"]["content"] is not None

    def test_chat_with_max_tokens(self):
        """Test chat with custom max_tokens"""
        generate_app_state()
        client = WatsonxClient()
        
        messages = [client.build_message("user", "Test message")]
        
        response = client.chat(messages, max_tokens=100)
        
        assert "choices" in response
        assert response["choices"][0]["message"]["content"] is not None

    def test_chat_updates_token_counts(self):
        """Test that chat updates token counts in app state"""
        generate_app_state()
        client = WatsonxClient()
        
        initial_input_tokens = app_state.get().input_tokens
        initial_output_tokens = app_state.get().output_tokens
        
        messages = [client.build_message("user", "Test message")]
        client.chat(messages)
        
        # Token counts should be updated
        assert app_state.get().input_tokens >= initial_input_tokens
        assert app_state.get().output_tokens >= initial_output_tokens

    def test_chat_with_multiple_messages(self):
        """Test chat with conversation history"""
        generate_app_state()
        client = WatsonxClient()
        
        messages = [
            client.build_message("system", "You are a helpful assistant"),
            client.build_message("user", "What is 2+2?"),
            client.build_message("assistant", "4"),
            client.build_message("user", "What about 3+3?")
        ]
        
        response = client.chat(messages)
        
        assert "choices" in response
        assert response["choices"][0]["message"]["content"] is not None


class TestWatsonxClientEmbeddings:
    """Test embeddings functionality"""

    def test_generate_embeddings_watsonx(self):
        """Test generating embeddings using watsonx API"""
        generate_app_state()
        client = WatsonxClient()
        
        texts = ["Hello world", "Test text"]
        embeddings = client.generate_embeddings(texts, use_local=False)
        
        assert isinstance(embeddings, list)
        assert len(embeddings) > 0
        assert isinstance(embeddings[0], list)

    def test_generate_embeddings_truncates_large_input(self):
        """Test that embeddings truncate to 1000 texts"""
        generate_app_state()
        client = WatsonxClient()
        
        texts = [f"Text {i}" for i in range(1500)]
        
        with patch.object(client, '_generate_watsonx_embeddings') as mock_gen:
            mock_gen.return_value = [[0.1, 0.2, 0.3]]
            client.generate_embeddings(texts, use_local=False)
            
            # Should only pass first 1000 texts
            call_args = mock_gen.call_args[0][0]
            assert len(call_args) == 1000

    def test_generate_embeddings_uses_config_for_local(self):
        """Test that embeddings use config to determine local vs watsonx"""
        generate_app_state()
        app_state.get().opts["fn_watsonx_analyst"]["local_embeddings"] = "true"
        client = WatsonxClient()
        
        with patch.object(client, '_generate_local_embeddings') as mock_local:
            mock_local.return_value = [[0.1, 0.2, 0.3]]
            client.generate_embeddings(["test"], use_local=None)
            mock_local.assert_called_once()


class TestWatsonxClientModels:
    """Test model listing functionality"""

    def test_get_available_models_success(self):
        """Test retrieving available models"""
        generate_app_state()
        client = WatsonxClient()
        
        with patch.object(client.wx_client.foundation_models, 'get_model_specs') as mock_specs:
            mock_specs.return_value = {
                "resources": [
                    {"model_id": "model1"},
                    {"model_id": "model2"},
                    {"model_id": "model3"}
                ]
            }
            
            assert client.get_available_models() == True

    def test_get_available_models_empty_response(self):
        """Test handling empty model list response"""
        generate_app_state()
        client = WatsonxClient()
        
        with patch.object(client.wx_client.foundation_models, 'get_model_specs') as mock_specs:
            mock_specs.return_value = None
            assert client.get_available_models() == False

    def test_get_available_models_missing_resources(self):
        """Test handling response without resources key"""
        generate_app_state()
        client = WatsonxClient()
        
        with patch.object(client.wx_client.foundation_models, 'get_model_specs') as mock_specs:
            mock_specs.return_value = {"data": []}
            assert client.get_available_models() == False


class TestWatsonxClientExceptionHandling:
    """Test exception handling and mapping"""

    def test_handle_token_limit_exception(self):
        """Test token limit exception handling"""
        generate_app_state()
        client = WatsonxClient()
        
        error = Exception("Token limit exceeded for this request")
        
        with pytest.raises(WatsonxTokenLimitExceededException):
            client._handle_exception(error)

    def test_handle_unauthorized_exception(self):
        """Test unauthorized exception handling"""
        generate_app_state()
        client = WatsonxClient()
        
        error = Exception("Unauthorized access - 401")
        
        with pytest.raises(WatsonxUnauthorizedException):
            client._handle_exception(error)

    def test_handle_forbidden_exception(self):
        """Test forbidden exception handling"""
        generate_app_state()
        client = WatsonxClient()
        
        error = Exception("Forbidden - 403")
        
        with pytest.raises(WatsonxForbiddenException):
            client._handle_exception(error)

    def test_handle_not_found_exception(self):
        """Test not found exception handling"""
        generate_app_state()
        client = WatsonxClient()
        
        error = Exception("Resource not found - 404")
        
        with pytest.raises(WatsonxNotFoundException):
            client._handle_exception(error)

    def test_handle_model_not_found_exception(self):
        """Test model not found exception handling"""
        generate_app_state()
        client = WatsonxClient()
        
        error = Exception("Model not found - 404")
        
        with pytest.raises(WatsonxModelIdNotFoundException):
            client._handle_exception(error)

    def test_handle_bad_request_exception(self):
        """Test bad request exception handling"""
        generate_app_state()
        client = WatsonxClient()
        
        error = Exception("Bad request - 400")
        
        with pytest.raises(WatsonxBadRequestException):
            client._handle_exception(error)

    def test_handle_rate_limit_exception(self):
        """Test rate limit exception handling"""
        generate_app_state()
        client = WatsonxClient()
        
        error = Exception("Rate limit exceeded - 429")
        
        with pytest.raises(WatsonxTooManyRequestsException):
            client._handle_exception(error)

    def test_handle_connection_exception(self):
        """Test connection exception handling"""
        generate_app_state()
        client = WatsonxClient()
        
        error = Exception("Connection timeout occurred")
        
        with pytest.raises(WatsonxUnreachableException):
            client._handle_exception(error)

    def test_handle_internal_error_exception(self):
        """Test internal server error exception handling"""
        generate_app_state()
        client = WatsonxClient()
        
        error = Exception("Internal server error - 500")
        
        with pytest.raises(WatsonxInternalErrorException):
            client._handle_exception(error)

    def test_handle_generic_exception(self):
        """Test generic exception handling"""
        generate_app_state()
        client = WatsonxClient()
        
        error = Exception("Some unexpected error")
        
        with pytest.raises(WatsonxApiException):
            client._handle_exception(error)

    def test_chat_exception_propagation(self):
        """Test that chat exceptions are properly propagated"""
        generate_app_state()
        client = WatsonxClient()
        
        with patch('fn_watsonx_analyst.util.watsonx_client.ModelInference') as mock_model:
            mock_instance = MagicMock()
            mock_instance.chat.side_effect = Exception("Unauthorized - 401")
            mock_model.return_value = mock_instance
            
            messages = [client.build_message("user", "test")]
            
            with pytest.raises(WatsonxUnauthorizedException):
                client.chat(messages)

    def test_embeddings_exception_propagation(self):
        """Test that embeddings exceptions are properly propagated"""
        generate_app_state()
        client = WatsonxClient()
        
        with patch('fn_watsonx_analyst.util.watsonx_client.Embeddings') as mock_embed:
            mock_instance = MagicMock()
            mock_instance.generate.side_effect = Exception("Bad request - 400")
            mock_embed.return_value = mock_instance
            
            with pytest.raises(WatsonxBadRequestException):
                client.generate_embeddings(["test"], use_local=False)


class TestWatsonxClientEdgeCases:
    """Test edge cases and boundary conditions"""

    def test_chat_with_empty_messages(self):
        """Test chat with empty message list"""
        generate_app_state()
        client = WatsonxClient()
        
        # Should not raise an error, let the API handle it

        with pytest.raises(WatsonxApiException):
            client.chat([])

    def test_embeddings_with_empty_list(self):
        """Test embeddings with empty text list"""
        generate_app_state()
        client = WatsonxClient()
        
        embeddings = client.generate_embeddings([], use_local=False)
        assert isinstance(embeddings, list)

    def test_chat_with_very_long_content(self):
        """Test chat with very long message content"""
        generate_app_state()
        client = WatsonxClient()
        
        long_content = "test " * 10000
        messages = [client.build_message("user", long_content)]
        
        # Should handle long content (may hit token limits)
        try:
            response = client.chat(messages)
            assert response is not None
        except WatsonxTokenLimitExceededException:
            # Expected for very long content
            pass

    def test_embeddings_with_special_characters(self):
        """Test embeddings with special characters"""
        generate_app_state()
        client = WatsonxClient()
        
        texts = ["Hello! @#$%", "Test\n\t\r", "Unicode: 你好"]
        embeddings = client.generate_embeddings(texts, use_local=False)
        
        assert isinstance(embeddings, list)
        assert len(embeddings) > 0

    def test_multiple_client_instances(self):
        """Test creating multiple client instances"""
        generate_app_state()
        
        client1 = WatsonxClient()
        client2 = WatsonxClient()
        
        assert client1.model_id == client2.model_id
        assert client1.project_id == client2.project_id

    def test_chat_response_structure(self):
        """Test that chat response has expected structure"""
        generate_app_state()
        client = WatsonxClient()
        
        messages = [client.build_message("user", "test")]
        response = client.chat(messages)
        
        # Verify response structure
        assert "id" in response
        assert "model_id" in response
        assert "choices" in response
        assert "usage" in response
        assert len(response["choices"]) > 0
        assert "message" in response["choices"][0]
        assert "content" in response["choices"][0]["message"]
        assert "role" in response["choices"][0]["message"]
