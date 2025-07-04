"""Unit tests for ContextHelper"""

import pytest
from bs4 import BeautifulSoup
import re
from tika import parser


from fn_watsonx_analyst.util.ContextHelper import ContextHelper


@pytest.fixture(name = "context_helper")
def fixture_context_helper():
    """Fixture to create an instance of ContextHelper"""
    return ContextHelper()

def test_valid_plain_text(context_helper):
    """Checks for the vlaid input"""
    input_text = "This is a simple text document."
    expected_output = input_text  # No formatting needed
    assert context_helper.multi_format_parser(input_text) == expected_output

def test_valid_html(context_helper):
    """Checks if the HTML is correctly formatted"""
    input_text = "<html><body><h1>Title</h1><p>Some content.</p></body></html>"
    expected_output = "Title\nSome content."  # HTML should be converted to text
    assert context_helper.multi_format_parser(input_text) == expected_output

def test_empty_input(context_helper):
    """Raises value error when the empty data is passed"""
    with pytest.raises(ValueError, match="Input data is empty or contains only whitespace."):
        context_helper.multi_format_parser("")

def test_whitespace_input(context_helper):
    """Raises value error when the empty data contains whitespaces"""
    with pytest.raises(ValueError, match="Input data is empty or contains only whitespace."):
        context_helper.multi_format_parser("    \n  ")

def test_non_text_input(context_helper):
    """Raises value error when the parsed content is wrong or corrupted"""
    binary_data = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"
    with pytest.raises(ValueError, match="Parsed content is empty or could not be extracted."):
        context_helper.multi_format_parser(binary_data.decode(errors="ignore"))  # Force conversion

def test_tika_fails(context_helper):
    """Provide non-text binary data to force a parsing failure"""
    binary_data = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"  # Corrupted PNG file header
    with pytest.raises(ValueError, match="Parsed content is empty or could not be extracted."):
        context_helper.multi_format_parser(binary_data.decode(errors="ignore"))  # Force decode


def test_tika_missing_metadata(context_helper):
    """Provide an input that results in missing metadata"""
    input_text = "Plain text without metadata"

    # If no exception is raised, print output for debugging
    parsed_output = context_helper.multi_format_parser(input_text)
    print(f"Parsed Output: {parsed_output}")

    # Check if parsed_output matches expected behavior
    assert parsed_output == input_text  # Since there's no metadata, it should return the text itself


def test_tika_returns_none_content_parser(context_helper):
    """Provide unreadable binary data to force tika to return None"""
    binary_data = b"\x00\x01\x02\x03\x04"  # Random binary data
    with pytest.raises(ValueError, match="Parsed content is empty or could not be extracted."):
        context_helper.multi_format_parser(binary_data.decode(errors="ignore"))  # Force decode

@pytest.mark.parametrize("input_data, target, replacement, expected_output", [
    # Test case 1: Simple string replacement inside dictionary
    ({"key": "Email Attachment"}, "Email Attachment", "File", {"key": "File"}),

    # Test case 2: Case-insensitive replacement
    ({"key": "email attachment"}, "Email Attachment", "File", {"key": "File"}),

    # Test case 3: String inside a nested dictionary
    ({"incident": {"type": "Email Attachment"}}, "Email Attachment", "File", {"incident": {"type": "File"}}),

    # Test case 4: String inside a list of dictionaries
    ({"incident": {"artifacts": [{"type": "Email Attachment"}, {"type": "Not Relevant"}]}},
     "Email Attachment", "File",
     {"incident": {"artifacts": [{"type": "File"}, {"type": "Not Relevant"}]}}),

    # Test case 5: String in a deep nested structure
    ({"level1": {"level2": {"level3": "Email Attachment"}}},
     "Email Attachment", "File",
     {"level1": {"level2": {"level3": "File"}}}),

    # Test case 6: No replacement needed
    ({"incident": {"artifacts": [{"type": "File"}]}}, "Email Attachment", "File", {"incident": {"artifacts": [{"type": "File"}]}}),

    # Test case 7: String inside a list
    (["Email Attachment", "Another String"], "Email Attachment", "File", ["File", "Another String"]),

    # Test case 8: Mixed types (should be ignored)
    ({"key": 123, "list": [None, True, 4.5, "Email Attachment"]},
     "Email Attachment", "File",
     {"key": 123, "list": [None, True, 4.5, "File"]}),

    # Test case 9: Multiple occurrences in different places
    ({"incident": {"artifacts": [{"type": "Email Attachment", "desc": "Email Attachment"}, {"type": "Not Relevant"}]}},
     "Email Attachment", "File",
     {"incident": {"artifacts": [{"type": "File", "desc": "File"}, {"type": "Not Relevant"}]}}),

    # Test case 10: Empty dictionary (edge case)
    ({}, "Email Attachment", "File", {}),

    # Test case 11: Empty list (edge case)
    ([], "Email Attachment", "File", []),

])

def test_replace_string_in_values(context_helper, input_data, target, replacement, expected_output):
    result = ContextHelper.replace_string_in_values(context_helper, input_data, target, replacement)
    assert result == expected_output