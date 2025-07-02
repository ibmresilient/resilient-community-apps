from functools import cache
import os
from typing import List
import markdown2
from bs4 import BeautifulSoup
import nh3
import yaml

from fn_watsonx_analyst.util.util import create_logger

log = create_logger(__name__)


class RichTextHelper:
    """Converts markdown to HTML"""

    code_block_style = (
        "font-family: monospace; background-color: black; color: white; padding: 5px;"
    )
    code_inline_style = (
        f"{code_block_style} display: inline; padding: 1px; font-style: normal;"
    )

    @staticmethod
    @cache
    def get_config() -> dict:
        """retrieve the markdown config as a dictionary"""
        rich_text_config_path = os.path.abspath(
            os.path.join(os.path.dirname("fn_watsonx_analyst/config/"), "rich_text.yaml")
        )
        with open(rich_text_config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    @staticmethod
    def extract_text(text: str) -> str:
        """pull text from given html"""
        return BeautifulSoup(text, "html.parser").get_text(" ")

    @staticmethod
    def toHTML(text: str) -> str:
        """Convert markdown to HTML"""
        log.debug("Converting AI's markdown to HTML")
        config = RichTextHelper.get_config()
        original_text = text

        text = text.replace("_", "&#95;") # LLM rarely escapes underscores, so html escape the underscore
        text = text.replace("<br> ", "\\r")

        try:
            text = markdown2.markdown(
                text,
                extras=["fenced-code-blocks", "cuddled-lists", "tables"],
                safe_mode="escape",
            )

            text = text.replace("\n", "\\n") # allow for newlines in codeblocks to be persisted
            text = RichTextHelper.conv_code_to_rich_text(text)

            text = text.replace("\\n", "") # remove non-codeblock newlines
            text = text.replace("\\r", "\n")

            newline_tags = config["newline_tags"]

            # add N newlines after tag
            for n, tags in newline_tags.items():
                for tag in tags:
                    text = text.replace(tag, tag + str("\n" * n))

            # set heading font size
            soup = BeautifulSoup(text, "html.parser")
            for heading_num, heading_size in config["font_sizes"].items():
                for heading in soup.find_all(heading_num):
                    heading.attrs["style"] = f"font-size: {heading_size}em;"

            try:
                text = str(soup)
                text = RichTextHelper.construct_blockquotes(text)
            except:
                pass # ignore error - not an issue if blockquotes aren't styled

            text = RichTextHelper.sanitize(text, config["allowed_tags"])
            return text
        except:
            log.error("Unable to convert markdown to rich text HTML.", exc_info=True)
            return original_text

    @staticmethod
    def sanitize(text: str, allowed_tags: List[str]) -> str:
        """
        Use nh3 to sanitize, limiting the tags to a safe set, and stripping classes
        """
        try:

            return nh3.clean(
                text,
                tags=set(allowed_tags),
                attributes={"*": {"style"}},
            )
        except Exception as e:
            raise RuntimeError("Failed to sanitize HTML rich text") from e
    @staticmethod
    def construct_blockquotes(text: str) -> str:
        """add styling for blockquotes"""
        soup = BeautifulSoup(text, "html.parser")

        for bq in soup.find_all("blockquote"):
            bq.attrs["style"] = "border-left: 1px solid white; padding-left: 1em;"

        return str(soup)

    @staticmethod
    def conv_code_to_rich_text(text: str) -> str:
        """
        SOAR comments don't support <code> or <pre> tags, so we convert blocks to <p> tags, and inline code to <i> tags.
        Don't care about keeping any attributes
        """

        def unescape_code(_text: str) -> str:
            """
            Unescape escaped characters, like underscores, and periods, inside code tags.
            """
            _text = _text.replace("&#95;", "_")
            # turn newlines into escaped newlines, which will later be turned back to newlines
            _text = _text.replace("\\n", "\n")
            return _text

        soup = BeautifulSoup(text, "html.parser")

        for tag in ("pre", "code"):
            for el in soup.find_all(tag):
                code_text = el.get_text()
                code_text = unescape_code(code_text)

                new_tag = soup.new_tag("p" if tag == "pre" else "i")
                new_tag.string = code_text

                style = RichTextHelper.code_block_style if tag == "pre" else RichTextHelper.code_inline_style

                new_tag.attrs["style"] = style
                el.replaceWith(new_tag)
                if tag == "pre":
                    new_tag.insert_after("\n")

        return str(soup)
