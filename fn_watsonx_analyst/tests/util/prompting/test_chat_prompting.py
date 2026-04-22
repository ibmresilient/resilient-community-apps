"""Unit Tests for ChatPrompting"""


import pytest
from unittest.mock import patch

from fn_watsonx_analyst.util.chat_prompting import ChatPrompting
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.state_manager import app_state
from tests import helper
from tests.helper import generate_app_state

class TestChatPrompting:
    """Unit tests for ChatPrompting class."""

    def setup_method(self):
        """Setup method to initialize app state before each test."""
        generate_app_state()
        app_state.get().opts["fn_watsonx_analyst"]["default_language"] = "en"
        app_state.get().opts["fn_watsonx_analyst"]["watsonx_endpoint"] = "https://us-south.ml.cloud.ibm.com"

    # Initialization Tests
    def test_initialization_success(self):
        """Test successful initialization of ChatPrompting class."""
        chat_prompting = ChatPrompting()
        assert chat_prompting is not None
        assert hasattr(chat_prompting, 'default_language')
        assert hasattr(chat_prompting, 'prompting_config')
        assert chat_prompting.default_language in ChatPrompting.supported_languages

    def test_supported_languages(self):
        """Test that supported languages are correctly defined."""
        assert ChatPrompting.supported_languages == ["en", "es", "fr", "de", "pt", "ja"]

    def test_get_default_language(self):
        """Test getting default language from app state."""
        lang = "pt"
        app_state.get().opts["fn_watsonx_analyst"]["default_language"] = lang
        chat_prompting = ChatPrompting()
        assert chat_prompting._get_default_language() == lang

    def test_get_default_language_fallback(self):
        """Test fallback to 'en' when default language is not configured."""
        opts = app_state.get().opts.copy()
        if "fn_watsonx_analyst" in opts and "default_language" in opts["fn_watsonx_analyst"]:
            del opts["fn_watsonx_analyst"]["default_language"]
        app_state.get().opts = opts
        assert ChatPrompting._get_default_language() == "en"

    # Language Detection Tests
    def test_detect_language_english(self):
        """Test language detection for English text."""
        chat_prompting = ChatPrompting()
        text = "This is a test query in English language"
        detected = chat_prompting.detect_language(text)
        assert detected == "en"

    def test_detect_language_spanish(self):
        """Test language detection for Spanish text."""
        chat_prompting = ChatPrompting()
        text = "Esta es una consulta de prueba en español"
        detected = chat_prompting.detect_language(text)
        assert detected == "es"

    def test_detect_language_french(self):
        """Test language detection for French text."""
        chat_prompting = ChatPrompting()
        text = "Ceci est une requête de test en français"
        detected = chat_prompting.detect_language(text)
        assert detected == "fr"

    def test_detect_language_low_confidence(self):
        """Test language detection with low confidence falls back to default."""
        chat_prompting = ChatPrompting()
        text = "abc"
        detected = chat_prompting.detect_language(text, confidence_threshold=0.99)
        assert detected in ChatPrompting.supported_languages

    def test_detect_language_custom_threshold(self):
        """Test language detection with custom confidence threshold."""
        chat_prompting = ChatPrompting()
        text = "This is English text"
        detected = chat_prompting.detect_language(text, confidence_threshold=0.5)
        assert detected == "en"

    # Prompt Text Retrieval Tests
    def test_get_prompt_text_system(self):
        """Test retrieving system prompt text."""
        chat_prompting = ChatPrompting()
        prompt = chat_prompting._get_prompt_text("system_prompts", "default_prompt", "en")
        assert isinstance(prompt, str)
        assert len(prompt) > 0

    def test_get_prompt_text_user(self):
        """Test retrieving user prompt text."""
        chat_prompting = ChatPrompting()
        prompt = chat_prompting._get_prompt_text("user_prompts", "contents_summary", "en")
        assert isinstance(prompt, str)

    def test_get_prompt_text_missing(self):
        """Test retrieving non-existent prompt returns empty string."""
        chat_prompting = ChatPrompting()
        prompt = chat_prompting._get_prompt_text("system_prompts", "nonexistent_key", "en")
        assert prompt == ""

    def test_get_prompt_text_with_date_substitution(self):
        """Test that {current_date} placeholder is substituted."""
        chat_prompting = ChatPrompting()
        prompt = chat_prompting._get_prompt_text("system_prompts", "default_prompt", "en")
        assert "{current_date}" not in prompt

    # System Prompt Tests
    def test_get_system_prompt_artifact_conversation(self):
        """Test getting system prompt for artifact conversation."""
        chat_prompting = ChatPrompting()
        prompt = chat_prompting.get_system_prompt(AiResponsePurpose.ARTIFACT_CONVERSATION, "en")
        assert isinstance(prompt, str)
        assert len(prompt) > 0

    def test_get_system_prompt_artifact_summary(self):
        """Test getting system prompt for artifact summary."""
        chat_prompting = ChatPrompting()
        prompt = chat_prompting.get_system_prompt(AiResponsePurpose.ARTIFACT_SUMMARY, "en")
        assert isinstance(prompt, str)
        assert len(prompt) > 0

    def test_get_system_prompt_metadata_summary(self):
        """Test getting system prompt for metadata summary."""
        chat_prompting = ChatPrompting()
        prompt = chat_prompting.get_system_prompt(AiResponsePurpose.ARITFACT_META_SUMMARY, "en")
        assert isinstance(prompt, str)
        assert len(prompt) > 0

    def test_get_system_prompt_default(self):
        """Test getting default system prompt."""
        chat_prompting = ChatPrompting()
        prompt = chat_prompting.get_system_prompt(AiResponsePurpose.NOTE_CONVERSATION, "en")
        assert isinstance(prompt, str)
        assert len(prompt) > 0

    def test_get_system_prompt_with_kwargs(self):
        """Test getting system prompt with format kwargs."""
        chat_prompting = ChatPrompting()
        prompt = chat_prompting.get_system_prompt(
            AiResponsePurpose.ARTIFACT_SUMMARY,
            "en",
            content_type="application/json"
        )
        assert isinstance(prompt, str)

    # User Prompt Tests
    def test_get_user_prompt_artifact_summary(self):
        """Test getting user prompt for artifact summary."""
        chat_prompting = ChatPrompting()
        prompt = chat_prompting.get_user_prompt(AiResponsePurpose.ARTIFACT_SUMMARY, "en")
        assert isinstance(prompt, str)

    def test_get_user_prompt_metadata_summary(self):
        """Test getting user prompt for metadata summary."""
        chat_prompting = ChatPrompting()
        prompt = chat_prompting.get_user_prompt(AiResponsePurpose.ARITFACT_META_SUMMARY, "en")
        assert isinstance(prompt, str)

    def test_get_user_prompt_returns_empty_for_conversation(self):
        """Test that user prompt returns empty for conversation purposes."""
        chat_prompting = ChatPrompting()
        prompt = chat_prompting.get_user_prompt(AiResponsePurpose.NOTE_CONVERSATION, "en")
        assert prompt == ""

    def test_get_user_prompt_with_kwargs(self):
        """Test getting user prompt with format kwargs."""
        chat_prompting = ChatPrompting()
        prompt = chat_prompting.get_user_prompt(
            AiResponsePurpose.ARTIFACT_SUMMARY,
            "en",
            file_contents="Sample content"
        )
        assert isinstance(prompt, str)

    # Helper Text Tests
    def test_get_help_text(self):
        """Test retrieving help text for a locale."""
        chat_prompting = ChatPrompting()
        help_text = chat_prompting.get_help_text("en")
        assert isinstance(help_text, str)

    def test_get_grounding_text(self):
        """Test retrieving grounding text."""
        chat_prompting = ChatPrompting()
        grounding = chat_prompting.get_grounding_text("incident", "en")
        assert isinstance(grounding, str)

    # Build Chat Messages Tests
    def test_build_chat_messages_basic(self):
        """Test building basic chat messages."""
        app_state.get().purpose = AiResponsePurpose.NOTE_CONVERSATION
        chat_prompting = ChatPrompting()
        
        messages = chat_prompting.build_chat_messages(
            purpose=AiResponsePurpose.NOTE_CONVERSATION,
            query="What is this incident about?",
            context="Security breach detected"
        )
        
        assert isinstance(messages, list)
        assert len(messages) > 0
        assert all(isinstance(msg, dict) for msg in messages)
        assert all("role" in msg and "content" in msg for msg in messages)

    def test_build_chat_messages_with_system_message(self):
        """Test that chat messages include system message."""
        app_state.get().purpose = AiResponsePurpose.NOTE_CONVERSATION
        chat_prompting = ChatPrompting()
        
        messages = chat_prompting.build_chat_messages(
            purpose=AiResponsePurpose.NOTE_CONVERSATION,
            query="Test query for watsonx.ai", context='', previous_messages=None, include_relevant_prompts=True
        )

        print(messages)
        
        system_messages = [msg for msg in messages if msg["role"] == "system"]
        assert len(system_messages) > 0

    def test_build_chat_messages_with_user_message(self):
        """Test that chat messages include user message."""
        app_state.get().purpose = AiResponsePurpose.NOTE_CONVERSATION
        chat_prompting = ChatPrompting()
        query = "What is the root cause?"
        
        messages = chat_prompting.build_chat_messages(
            purpose=AiResponsePurpose.NOTE_CONVERSATION,
            query=query
        )
        
        user_messages = [msg for msg in messages if msg["role"] == "user"]
        assert len(user_messages) > 0
        assert query in user_messages[0]["content"]

    def test_build_chat_messages_with_previous_messages(self):
        """Test building chat messages with conversation history."""
        app_state.get().purpose = AiResponsePurpose.NOTE_CONVERSATION
        chat_prompting = ChatPrompting()
        
        previous = [
            {"role": "user", "content": "Previous question"},
            {"role": "assistant", "content": "Previous answer"}
        ]
        
        messages = chat_prompting.build_chat_messages(
            purpose=AiResponsePurpose.NOTE_CONVERSATION,
            query="Follow-up question",
            previous_messages=previous
        )
        
        assert isinstance(messages, list)
        assert len(messages) > 0

    def test_build_chat_messages_artifact_summary(self):
        """Test building chat messages for artifact summary."""
        app_state.get().purpose = AiResponsePurpose.ARTIFACT_SUMMARY
        chat_prompting = ChatPrompting()
        
        messages = chat_prompting.build_chat_messages(
            purpose=AiResponsePurpose.ARTIFACT_SUMMARY,
            query=None,
            context="Artifact content",
            file_contents="Sample file content",
            content_type="application/json"
        )
        
        assert isinstance(messages, list)
        assert len(messages) > 0

    def test_build_chat_messages_with_locale(self):
        """Test building chat messages with explicit locale."""
        app_state.get().purpose = AiResponsePurpose.NOTE_CONVERSATION
        chat_prompting = ChatPrompting()
        
        messages = chat_prompting.build_chat_messages(
            purpose=AiResponsePurpose.NOTE_CONVERSATION,
            query="Test query",
            locale="es"
        )
        
        assert isinstance(messages, list)
        assert len(messages) > 0

    def test_build_chat_messages_without_relevant_prompts(self):
        """Test building chat messages without relevant prompts."""
        app_state.get().purpose = AiResponsePurpose.NOTE_CONVERSATION
        chat_prompting = ChatPrompting()
        
        messages = chat_prompting.build_chat_messages(
            purpose=AiResponsePurpose.NOTE_CONVERSATION,
            query="Test query",
            include_relevant_prompts=False
        )
        
        assert isinstance(messages, list)
        assert len(messages) > 0

    def test_build_chat_messages_with_format_kwargs(self):
        """Test building chat messages with format kwargs."""
        app_state.get().purpose = AiResponsePurpose.ARTIFACT_SUMMARY
        chat_prompting = ChatPrompting()
        
        messages = chat_prompting.build_chat_messages(
            purpose=AiResponsePurpose.ARTIFACT_SUMMARY,
            query=None,
            file_contents="Sample content",
            content_type="text/plain"
        )
        
        assert isinstance(messages, list)
        assert len(messages) > 0

    def test_build_chat_messages_incident_summary(self):
        """Test building chat messages for incident summary."""
        app_state.get().purpose = AiResponsePurpose.INCIDENT_SUMMARY
        chat_prompting = ChatPrompting()
        
        messages = chat_prompting.build_chat_messages(
            purpose=AiResponsePurpose.INCIDENT_SUMMARY,
            query="Summarize this incident",
            context="Incident data"
        )
        
        assert isinstance(messages, list)
        assert len(messages) > 0

    # Build Simple Chat Tests
    def test_build_simple_chat_basic(self):
        """Test building simple chat messages."""
        chat_prompting = ChatPrompting()
        
        messages = chat_prompting.build_simple_chat(
            system_prompt="You are a helpful assistant",
            user_message="Hello, how are you?"
        )
        
        assert isinstance(messages, list)
        assert len(messages) == 2
        assert messages[0]["role"] == "system"
        assert messages[1]["role"] == "user"

    def test_build_simple_chat_with_previous_messages(self):
        """Test building simple chat with previous messages."""
        chat_prompting = ChatPrompting()
        
        previous = [
            {"role": "user", "content": "First question"},
            {"role": "assistant", "content": "First answer"}
        ]
        
        messages = chat_prompting.build_simple_chat(
            system_prompt="You are helpful",
            user_message="Second question",
            previous_messages=previous
        )
        
        assert isinstance(messages, list)
        assert len(messages) == 4  # system + 2 previous + user
        assert messages[0]["role"] == "system"
        assert messages[-1]["role"] == "user"

    def test_build_simple_chat_empty_system_prompt(self):
        """Test building simple chat with empty system prompt."""
        chat_prompting = ChatPrompting()
        
        messages = chat_prompting.build_simple_chat(
            system_prompt="",
            user_message="Test message"
        )
        
        assert isinstance(messages, list)
        assert len(messages) == 1
        assert messages[0]["role"] == "user"

    def test_build_simple_chat_empty_user_message(self):
        """Test building simple chat with empty user message."""
        chat_prompting = ChatPrompting()
        
        messages = chat_prompting.build_simple_chat(
            system_prompt="System prompt",
            user_message=""
        )
        
        assert isinstance(messages, list)
        assert len(messages) == 1
        assert messages[0]["role"] == "system"

    # Edge Cases and Error Handling Tests
    def test_build_chat_messages_empty_query(self):
        """Test building chat messages with empty query."""
        app_state.get().purpose = AiResponsePurpose.NOTE_CONVERSATION
        chat_prompting = ChatPrompting()
        
        messages = chat_prompting.build_chat_messages(
            purpose=AiResponsePurpose.NOTE_CONVERSATION,
            query=""
        )
        
        assert isinstance(messages, list)

    def test_build_chat_messages_none_query(self):
        """Test building chat messages with None query."""
        app_state.get().purpose = AiResponsePurpose.ARTIFACT_SUMMARY
        chat_prompting = ChatPrompting()
        
        messages = chat_prompting.build_chat_messages(
            purpose=AiResponsePurpose.ARTIFACT_SUMMARY,
            query=None,
            file_contents="Content"
        )
        
        assert isinstance(messages, list)

    def test_build_chat_messages_empty_context(self):
        """Test building chat messages with empty context."""
        app_state.get().purpose = AiResponsePurpose.NOTE_CONVERSATION
        chat_prompting = ChatPrompting()
        
        messages = chat_prompting.build_chat_messages(
            purpose=AiResponsePurpose.NOTE_CONVERSATION,
            query="Test query",
            context=""
        )
        
        assert isinstance(messages, list)
        assert len(messages) > 0

    def test_build_chat_messages_special_characters(self):
        """Test building chat messages with special characters."""
        app_state.get().purpose = AiResponsePurpose.NOTE_CONVERSATION
        chat_prompting = ChatPrompting()
        query = "What about <script>alert('test')</script> and {format} strings?"
        
        messages = chat_prompting.build_chat_messages(
            purpose=AiResponsePurpose.NOTE_CONVERSATION,
            query=query
        )
        
        assert isinstance(messages, list)
        assert len(messages) > 0

    def test_build_chat_messages_unicode(self):
        """Test building chat messages with unicode characters."""
        app_state.get().purpose = AiResponsePurpose.NOTE_CONVERSATION
        chat_prompting = ChatPrompting()
        query = "What about émojis 🔥 and spëcial çharacters?"
        
        messages = chat_prompting.build_chat_messages(
            purpose=AiResponsePurpose.NOTE_CONVERSATION,
            query=query
        )
        
        assert isinstance(messages, list)
        assert len(messages) > 0

    def test_build_chat_messages_multiple_purposes(self):
        """Test building chat messages for all purpose types."""
        purposes = [
            AiResponsePurpose.NOTE_CONVERSATION,
            AiResponsePurpose.ARTIFACT_CONVERSATION,
            AiResponsePurpose.ARTIFACT_SUMMARY,
            AiResponsePurpose.ARITFACT_META_SUMMARY,
            AiResponsePurpose.INCIDENT_SUMMARY
        ]
        
        chat_prompting = ChatPrompting()
        
        for purpose in purposes:
            app_state.get().purpose = purpose
            
            if purpose == AiResponsePurpose.INCIDENT_SUMMARY:
                messages = chat_prompting.build_chat_messages(
                    purpose=purpose,
                    query="Test query",
                    context="Context"
                )
            elif purpose in [AiResponsePurpose.ARTIFACT_SUMMARY, AiResponsePurpose.ARITFACT_META_SUMMARY]:
                messages = chat_prompting.build_chat_messages(
                    purpose=purpose,
                    query=None,
                    file_contents="Sample content",
                    content_type="text/plain"
                )
            elif purpose == AiResponsePurpose.ARTIFACT_CONVERSATION:
                messages = chat_prompting.build_chat_messages(
                    purpose=purpose,
                    query="Test query",
                    file_contents="Sample content"
                )
            else:
                messages = chat_prompting.build_chat_messages(
                    purpose=purpose,
                    query="Test query"
                )
            
            assert isinstance(messages, list)
            assert len(messages) > 0
            assert all(isinstance(msg, dict) for msg in messages)