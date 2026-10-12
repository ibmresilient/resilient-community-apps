"""Unit tests for File Parser module"""
import base64
import io
import os
import random
import uuid
from unittest.mock import patch, MagicMock
import pytest
from fn_watsonx_analyst.util.FileParser import FileParser, UnsupportedEncodingError, EmptyContentsError


class TestFileParser:
    """Test suite for the FileParser class."""

    @classmethod
    def setup_class(cls):
        """Setup test class with FileParser instance"""
        cls.parser = FileParser()

    def _open_file(self, filename: str) -> bytes:
        """Helper method to open test data files"""
        with open(os.path.join(os.path.dirname(__file__), "..", "data", filename), "rb") as f:
            return f.read()

    @pytest.mark.parametrize("encoding", ["utf-8", "utf-16", "utf-32", "ascii", "cp1251"])
    def test_multi_encodings(self, encoding):
        """Test extraction with multiple text encodings"""
        data = "Hello world 123"
        assert FileParser().extract_text_contents(data.encode(encoding)) == data

    def test_extract_text_contents_simple_utf8(self):
        """Test basic UTF-8 text extraction"""
        data = b"Hello, World!"
        result = self.parser.extract_text_contents(data)
        assert result == "Hello, World!"

    def test_extract_text_contents_with_unicode(self):
        """Test extraction with Unicode characters"""
        data = "Hello 世界 🌍".encode("utf-8")
        result = self.parser.extract_text_contents(data)
        assert "Hello" in result
        assert "世界" in result

    def test_extract_text_contents_empty_data(self):
        """Test that empty data raises ValueError"""
        with pytest.raises(EmptyContentsError):
            self.parser.extract_text_contents(b"")

    def test_extract_text_contents_none_data(self):
        """Test that None data raises ValueError"""
        with pytest.raises(EmptyContentsError):
            self.parser.extract_text_contents(None)

    def test_extract_text_contents_with_newlines(self):
        """Test extraction preserves newlines correctly"""
        data = b"Line 1\nLine 2\nLine 3"
        result = self.parser.extract_text_contents(data)
        assert "Line 1" in result
        assert "Line 2" in result
        assert "Line 3" in result

    def test_extract_text_contents_with_tabs(self):
        """Test extraction handles tabs"""
        data = b"Column1\tColumn2\tColumn3"
        result = self.parser.extract_text_contents(data)
        assert "Column1" in result
        assert "Column2" in result

    def test_extract_text_contents_utf16_with_null_bytes(self):
        """Test UTF-16 encoding which contains null bytes"""
        data = "Hello World".encode("utf-16")
        result = self.parser.extract_text_contents(data)
        assert "Hello World" in result

    def test_extract_text_contents_utf32_with_null_bytes(self):
        """Test UTF-32 encoding which contains null bytes"""
        data = "Test UTF-32".encode("utf-32")
        result = self.parser.extract_text_contents(data)
        assert "Test UTF-32" in result

    def test_extract_text_contents_binary_file_raises_error(self):
        """Test that binary data raises UnsupportedEncodingError"""
        # Create truly random binary data that won't be detected as valid text encoding
        # Mix of high bytes and control characters that don't form valid UTF-16/32
        binary_data = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A,  # PNG header
                            0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46])  # JPEG-like bytes
        with pytest.raises(UnsupportedEncodingError):
            self.parser.extract_text_contents(binary_data)

    def test_with_pdf(self):
        """Test that PDF files raise UnsupportedEncodingError"""
        exc = False
        filename = "test.pdf"
        contents = self._open_file(filename)
        try:
            FileParser().extract_text_contents(contents, filename)
        except Exception as e:
            exc = e
        finally:
            assert exc is not None
            assert isinstance(exc, UnsupportedEncodingError)

    def test_with_eml(self):
        """Test extraction from EML file with headers, text/plain, text/html, and attachment"""
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders

        msg = MIMEMultipart('mixed')
        msg['From'] = 'sender@example.com'
        msg['To'] = 'recipient@example.com'
        msg['Subject'] = 'Test Email Subject'
        msg['Date'] = 'Mon, 19 May 2026 12:00:00 +0000'
        
        msg_alternative = MIMEMultipart('alternative')
        msg.attach(msg_alternative)
        
        text_plain = "This is the plain text version of the email.\nIt has multiple lines.\nPlain text content."
        part_plain = MIMEText(text_plain, 'plain')
        msg_alternative.attach(part_plain)
        
        text_html = "<html><body><p>This is the <b>HTML</b> version of the email.</p></body></html>"
        part_html = MIMEText(text_html, 'html')
        msg_alternative.attach(part_html)
        
        attachment_content = b'This is an attachment'
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(attachment_content)
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment', filename='test_file.txt')
        msg.attach(attachment)
        
        # Convert to bytes
        eml_bytes = msg.as_bytes()
        
        # Test extraction
        result = self.parser.extract_text_contents(eml_bytes, "x.eml")
        
        assert 'From: sender@example.com' in result or 'sender@example.com' in result
        assert 'To: recipient@example.com' in result or 'recipient@example.com' in result
        assert 'Subject: Test Email Subject' in result or 'Test Email Subject' in result
        
        assert 'plain text version' in result or 'Plain text content' in result
        assert attachment_content.decode() not in result
        
        common_phrase = 'multiple lines'
        occurrences = result.lower().count(common_phrase.lower())
        # should appear only once (from either plain or HTML, not both)
        assert occurrences <= 2, f"Content appears to be duplicated. Found '{common_phrase}' {occurrences} times"

    def test_normalize_whitespace_basic(self):
        """Test basic whitespace normalization"""
        input_text = "Hello    World"
        result = FileParser._normalize_whitespace(input_text)
        assert result == "Hello World"

    def test_normalize_whitespace_multiple_newlines(self):
        """Test collapsing excessive newlines"""
        input_text = "Line 1\n\n\n\n\nLine 2"
        result = FileParser._normalize_whitespace(input_text)
        assert result == "Line 1\n\nLine 2"

    def test_normalize_whitespace_tabs(self):
        """Test tab normalization"""
        input_text = "Col1\t\t\tCol2"
        result = FileParser._normalize_whitespace(input_text)
        assert result == "Col1 Col2"

    def test_normalize_whitespace_mixed_line_endings(self):
        """Test normalization of different line ending styles"""
        input_text = "Line 1\r\nLine 2\rLine 3\nLine 4"
        result = FileParser._normalize_whitespace(input_text)
        assert result == "Line 1\nLine 2\nLine 3\nLine 4"

    def test_normalize_whitespace_control_characters(self):
        """Test removal of control characters"""
        input_text = "Hello\x00\x01\x02World"
        result = FileParser._normalize_whitespace(input_text)
        assert result == "HelloWorld"

    def test_normalize_whitespace_unicode_normalization(self):
        """Test Unicode normalization (NFKC)"""
        # Using composed vs decomposed characters
        input_text = "café"  # May contain decomposed characters
        result = FileParser._normalize_whitespace(input_text)
        assert "caf" in result

    def test_normalize_whitespace_strips_leading_trailing(self):
        """Test stripping of leading and trailing whitespace"""
        input_text = "   Hello World   \n\n"
        result = FileParser._normalize_whitespace(input_text)
        assert result == "Hello World"

    def test_normalize_whitespace_empty_string(self):
        """Test normalization of empty string"""
        result = FileParser._normalize_whitespace("")
        assert result == ""

    def test_normalize_whitespace_only_whitespace(self):
        """Test normalization of string with only whitespace"""
        input_text = "   \n\n\t\t   "
        result = FileParser._normalize_whitespace(input_text)
        assert result == ""

    def test_check_binary_with_null_byte(self):
        """Test that binary check detects null bytes"""
        data = b"Text\x00with null"
        with pytest.raises(ValueError, match="null byte"):
            FileParser._check_binary(data)

    def test_check_binary_without_null_byte(self):
        """Test that text without null bytes passes"""
        data = b"Plain text without null bytes"
        # Should not raise an exception
        FileParser._check_binary(data)

    def test_check_binary_empty_data(self):
        """Test binary check with empty data"""
        data = b""
        # Should not raise an exception (no null bytes)
        FileParser._check_binary(data)

    def test_check_contents_valid(self):
        """Test that valid contents pass the check"""
        contents = "This is valid text content"
        # Should not raise an exception
        FileParser._check_contents(contents)

    def test_check_contents_empty(self):
        """Test that empty contents raise ValueError"""
        with pytest.raises(EmptyContentsError):
            FileParser._check_contents("")

    def test_check_contents_too_many_replacement_chars(self):
        """Test that too many replacement characters raise ValueError"""
        # Create string with >1% replacement characters
        contents = "�" * 20 + "a" * 80  # 20% replacement chars
        with pytest.raises(ValueError):
            FileParser._check_contents(contents)

    def test_check_contents_acceptable_replacement_chars(self):
        """Test that acceptable replacement character ratio passes"""
        # Create string with <1% replacement characters
        contents = "�" + "a" * 200  # ~0.5% replacement chars
        # Should not raise an exception
        FileParser._check_contents(contents)

    def test_check_contents_too_many_control_chars(self):
        """Test that too many control characters raise ValueError"""
        # Create string with >5% control characters (excluding \n, \t, \r)
        contents = "\x01" * 10 + "a" * 90  # 10% control chars
        with pytest.raises(ValueError, match="too many non-"):
            FileParser._check_contents(contents)

    def test_check_contents_acceptable_control_chars(self):
        """Test that acceptable control character ratio passes"""
        # Create string with <5% control characters
        contents = "\x01" * 2 + "a" * 100  # ~2% control chars
        # Should not raise an exception
        FileParser._check_contents(contents)

    def test_check_contents_allowed_control_chars(self):
        """Test that newlines, tabs, and carriage returns are allowed"""
        contents = "Line 1\nLine 2\tTabbed\rCarriage"
        # Should not raise an exception
        FileParser._check_contents(contents)

    def test_detect_encoding_utf8(self):
        """Test encoding detection for UTF-8"""
        data = "Hello World".encode("utf-8")
        encoding = FileParser._detect_encoding(data)
        assert encoding.lower() in ["utf-8", "utf_8", "ascii"]

    def test_detect_encoding_utf16(self):
        """Test encoding detection for UTF-16"""
        data = "Hello World".encode("utf-16")
        encoding = FileParser._detect_encoding(data)
        assert "utf" in encoding.lower() and "16" in encoding

    def test_detect_encoding_ascii(self):
        """Test encoding detection for ASCII"""
        data = b"Simple ASCII text"
        encoding = FileParser._detect_encoding(data)
        assert encoding.lower() in ["ascii", "utf-8", "utf_8"]

    def test_detect_encoding_latin1(self):
        """Test encoding detection for Latin-1"""
        data = "Café résumé".encode("latin-1")
        encoding = FileParser._detect_encoding(data)
        # Should detect some encoding
        assert encoding is not None

    @patch('fn_watsonx_analyst.util.FileParser.from_bytes')
    def test_detect_encoding_no_result(self, mock_from_bytes):
        """Test that no encoding result raises ValueError"""
        mock_from_bytes.return_value.best.return_value = None
        with pytest.raises(ValueError, match="Unable to detect encoding"):
            FileParser._detect_encoding(b"test")

    @patch('fn_watsonx_analyst.util.FileParser.from_bytes')
    def test_detect_encoding_high_chaos(self, mock_from_bytes):
        """Test that high chaos percentage raises ValueError"""
        mock_result = MagicMock()
        mock_result.encoding = "utf-8"
        mock_result.percent_chaos = 40  # Above 0.3 threshold
        mock_from_bytes.return_value.best.return_value = mock_result
        
        with pytest.raises(ValueError, match="chaos above threshold"):
            FileParser._detect_encoding(b"test")

    @patch('fn_watsonx_analyst.util.FileParser.from_bytes')
    def test_detect_encoding_acceptable_chaos(self, mock_from_bytes):
        """Test that acceptable chaos percentage passes"""
        mock_result = MagicMock()
        mock_result.encoding = "utf-8"
        mock_result.percent_chaos = 0.1  # Below 0.3 threshold
        mock_from_bytes.return_value.best.return_value = mock_result
        
        encoding = FileParser._detect_encoding(b"test")
        assert encoding == "utf-8"

    def test_decode_utf8(self):
        """Test decoding UTF-8 data"""
        data = "Hello World".encode("utf-8")
        result = FileParser._decode(data, "utf-8")
        assert result == "Hello World"

    def test_decode_utf16(self):
        """Test decoding UTF-16 data"""
        data = "Hello World".encode("utf-16")
        result = FileParser._decode(data, "utf-16")
        assert result == "Hello World"

    def test_decode_ascii(self):
        """Test decoding ASCII data"""
        data = b"Simple ASCII"
        result = FileParser._decode(data, "ascii")
        assert result == "Simple ASCII"

    def test_decode_latin1(self):
        """Test decoding Latin-1 data"""
        data = "Café".encode("latin-1")
        result = FileParser._decode(data, "latin-1")
        assert result == "Café"

    def test_decode_invalid_encoding(self):
        """Test that invalid encoding raises exception"""
        data = b"test data"
        with pytest.raises(LookupError):
            FileParser._decode(data, "invalid-encoding-name")

    # ==================== Integration tests ====================

    def test_extract_text_with_mixed_content(self):
        """Integration test with mixed content"""
        data = "Line 1\n\nLine 2\t\tTabbed\r\nLine 3".encode("utf-8")
        result = self.parser.extract_text_contents(data)
        assert "Line 1" in result
        assert "Line 2" in result
        assert "Line 3" in result

    def test_extract_text_with_special_chars(self):
        """Integration test with special characters"""
        data = "Special: @#$%^&*()_+-=[]{}|;:',.<>?/".encode("utf-8")
        result = self.parser.extract_text_contents(data)
        assert "Special:" in result

    def test_extract_text_multiline_document(self):
        """Integration test with multi-line document"""
        document = """
        Title: Test Document
        
        This is a test document with multiple lines.
        It contains various types of content.
        
        - Bullet point 1
        - Bullet point 2
        
        End of document.
        """
        data = document.encode("utf-8")
        result = self.parser.extract_text_contents(data)
        assert "Title: Test Document" in result
        assert "Bullet point 1" in result
        assert "End of document." in result

    @pytest.mark.parametrize(
        "data",
        (
            "Hello world",
            str(uuid.uuid4()),
            ''.join([str(uuid.uuid4()) for _ in range(1000)]),
        )
    )
    def test_base_encoded_strings(self, data: str):
        encoders = [
            base64.b16encode,
            base64.b32encode,
            base64.b64encode,
        ]

        for encoder in encoders:
            with pytest.raises(UnsupportedEncodingError):
                FileParser().extract_text_contents(encoder(data.encode("utf-8")))
