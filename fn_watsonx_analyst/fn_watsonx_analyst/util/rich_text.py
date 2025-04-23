import markdown2
from bs4 import BeautifulSoup
import nh3

from fn_watsonx_analyst.util.util import create_logger

log = create_logger(__name__)

class RichTextHelper:

    code_block_style = "font-family: monospace; background-color: black; color: white; padding: 5px;"
    code_inline_style = f"{code_block_style} display: inline; padding: 1px; font-style: normal;"

    @staticmethod
    def extract_text(text: str) -> str:
        return BeautifulSoup(text, "html.parser").get_text(" ")

    @staticmethod
    def toHTML(text: str) -> str:
        log.info("Converting AI's markdown to HTML")

        text = text.replace("_", "&#95;")

        text = markdown2.markdown(
            text, extras=["fenced-code-blocks", "cuddled-lists"], safe_mode="escape"
        )

        # newline whitespace handling and preparation
        text = text.replace("\n"*3, "\r") # for 3 newlines (aka two blank lines), add one newline
        text = text.replace("\n", "\\n") #
        text = RichTextHelper.conv_code_to_rich_text(text)
        text = text.replace("\\n", "")

        newline_tags = {
            1: ["</p>", "</ul>", "</ol>"]
        }

        for n, tags in newline_tags.items():
            for tag in tags:
                text = text.replace(tag, tag + str('\n' * n))

        text = RichTextHelper.sanitize(text)
        return text

    @staticmethod
    def sanitize(text: str) -> str:
        """
        Use nh3 to sanitize, limiting the tags to a safe set, and stripping classes
        """

        return nh3.clean(
            text, tags={"p", "i", "b", "em", "strong", "span", "ul", "ol", "li", "hr"},
            attributes={"*": {"style"}})

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
            # unescape dots
            _text = _text.replace("\.", ".")
            # turn newlines into escaped newlines, which will later be turned back to newlines
            _text = _text.replace("\\n", "\n")
            return _text

        soup = BeautifulSoup(text, "html.parser")

        for pre in soup.find_all("pre"):
            log.debug(f"Found pre: {pre}")
            # get the text of the code block
            code_text = pre.get_text()
            code_text = unescape_code(code_text)

            p = soup.new_tag("p")
            p.string = code_text
            p.attrs["style"] = RichTextHelper.code_block_style
            pre.replaceWith(p)
            p.insert_after("\n")


        for code in soup.find_all("code"):
            log.debug(f"Found code: {code}")
            # get the text of the inline code block
            code_text = code.get_text()
            code_text = unescape_code(code_text)

            i = soup.new_tag("i")
            i.string = code_text
            i.attrs["style"] = RichTextHelper.code_inline_style
            code.replaceWith(i)

        return str(soup)
