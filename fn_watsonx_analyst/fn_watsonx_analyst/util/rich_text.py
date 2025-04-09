from markdown import markdown
import nh3

from fn_watsonx_analyst.util.util import create_logger

log = create_logger(__name__)

class RichTextHelper:

    replacers = {
        "<li>\n": "<li>",
        "<ul>\n": "<ul>"
    }

    @staticmethod
    def toHTML(text: str):
        log.info("Converting AI's markdown to HTML")
        unsanitized_html = markdown(
            text, safe_mode=True, tab_length=2, output_format="html",
        )
        log.debug("Rendered HTML:\n%s", text)
        sanitized_html = RichTextHelper.__sanitize(unsanitized_html)
        log.debug("Sanitized HTML:\n%s", text)
        return sanitized_html

    @staticmethod
    def __sanitize(text: str):
        log.info("Sanitizing HTML")
        # pylint: disable=no-member
        # this method does exist, but pylint doesn't pick that up.
        text = nh3.clean(
            text,
            tags={
                "p",
                "strong",
                "em",
                "ol",
                "ul",
                "li",
                "i",
                "b",
                "code",
                "pre",
                "blockquote",
            },
        )

        for src, replc in RichTextHelper.replacers.items():
            text = text.replace(src, replc)

        return text
