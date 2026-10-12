"""File parser module to parse Artifacts and Attachments in the incident"""
import json
# pylint: disable=wildcard-import, method-hidden, import-outside-toplevel, import-error, broad-exception-caught, invalid-name

import re
import unicodedata
from email import policy, parser as email_parser, message_from_bytes
from email.message import EmailMessage

from bs4 import BeautifulSoup
from charset_normalizer import from_bytes

from fn_watsonx_analyst.util.logging_helper import create_logger

# Configure logging
log = create_logger(__name__)

METADATA_USED_INSTEAD = "Metadata will be analyzed to identify potential indicators of compromise (IOCs)."

EMPTY_CONTENTS = "Contents could not be parsed, file is likely empty or corrupt."
CONTENT_TYPE_INVALID: str = "For security reasons, content extraction is not supported for this file type."

class UnsupportedEncodingError(ValueError):
    """Raised when a file is not plain text"""
    msg = f"{CONTENT_TYPE_INVALID} {METADATA_USED_INSTEAD}"

    def __init__(self):
        super().__init__(self.msg)

class EmptyContentsError(ValueError):
    """Raised when contents of a plain text file are empty or only whitespace"""
    msg = f"{EMPTY_CONTENTS} {METADATA_USED_INSTEAD}"

    def __init__(self):
        super().__init__(self.msg)

class FileParser:
    """Class to parse multiple file types"""

    def __init__(self):
        """Initialize the file parser with supported extensions and parser mapping."""
        pass

    def extract_text_contents(self, data: bytes, filename = "") -> str:
        """Extract text from plaintext file contents"""
        try:
            if not data:
                raise EmptyContentsError()

            if filename and filename.lower().endswith(".eml"):
                return self._extract_eml_body(data)
            else:
                encoding = self._detect_encoding(data)

                # utf16 and utf32 encodings are expected to contain null bytes
                if not [encoding.startswith(enc) for enc in ["utf_16", "utf_32"]]:
                    self._check_binary(data)

                contents = self._decode(data, encoding)
            cleaned = self._normalize_whitespace(contents)
            if not cleaned:
                raise EmptyContentsError()
            self._check_base_n_encoded(cleaned)
            return cleaned

        except EmptyContentsError as e:
            raise e
        except Exception as e:
            raise UnsupportedEncodingError() from e

    @staticmethod
    def _normalize_whitespace(contents: str) -> str:

        control_chars_re = re.compile(
            r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]"
        )

        # normalize Unicode (important for consistency)
        contents = unicodedata.normalize("NFKC", contents)

        # remove control characters (except \n \t \r)
        contents = control_chars_re.sub("", contents)

        # normalize line endings
        contents = contents.replace("\r\n", "\n").replace("\r", "\n")

        # collapse excessive whitespace
        contents = re.sub(r"[ \t]+", " ", contents)  # spaces/tabs → single space
        contents = re.sub(r"\n{3,}", "\n\n", contents)  # max 2 newlines

        return contents.strip()

    @staticmethod
    def _check_binary(data: bytes):
        if b'\x00' in data:
            raise ValueError("Contents contain null byte, likely non-text binary file")

    @staticmethod
    def _check_contents(contents: str):
        if not contents:
            raise EmptyContentsError()

        length = len(contents)

        replacement_ratio = contents.count("�") / length
        if replacement_ratio > 0.01:
            raise ValueError("Contents contain too many contain non-textual bytes")

        # ensure control characters don't exceed a threshold
        control = sum(
            1 for ch in contents
            if ord(ch) < 32 and ch not in "\n\t\r"
        )
        if control / length > 0.05:
            raise ValueError("Contents contain too many non-")

    @staticmethod
    def _detect_encoding(data: bytes):
        result = from_bytes(data).best()
        if not result or not result.encoding:
            raise ValueError("Unable to detect encoding")

        if result.percent_chaos >= 30:
            raise ValueError("Encoding chaos above threshold, unlikely to be plain text")

        return result.encoding

    @staticmethod
    def _decode(data: bytes, encoding: str):
        return data.decode(encoding)

    @staticmethod
    def _check_base_n_encoded(contents: str):
        patterns = [
            r"^[0-9A-Fa-f]{8,}$",           # base-16
            r"^[A-Z2-7]{8,}=*$",            # base-32
            r"^[A-Za-z0-9+/_-]{8,}={0,2}$"  # base-64
        ]

        for pattern in patterns:
            if re.search(pattern, contents):
                raise UnsupportedEncodingError()

    def _extract_eml_body(self, data: bytes) -> str:
        log.warning("Parsing EML file")
        msg: EmailMessage = email_parser.BytesParser(policy=policy.default).parsebytes(data)
        contents = '\n'.join([f"{item[0]}: {item[1]}" for item in msg.items()])
        body = msg.get_body(("plain", "html"))
        if body:
            contents += "\n---\n" + BeautifulSoup(body.get_content(), "html.parser").get_text()
        else:
            contents += self.CONTENT_TYPE_INVALID
        return self._normalize_whitespace(contents)
