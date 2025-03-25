from fn_watsonx_analyst.util.rich_text import RichTextHelper

class TestRichText:

    def test_ensure_script_not_parsed(self):
        output = RichTextHelper.toHTML("<script>alert('hi')</script>")
        assert output == ""

    def test_ensure_unallowed_tags_in_pre_code(self):
        inputstr = """# hello world"""

        output = RichTextHelper.toHTML(inputstr)
        assert output == "hello world"

    def test_ensure_anchors_not_parsed(self):
        inputstr = "[test.com](https://test.com)"

        output = RichTextHelper.toHTML(inputstr)
        assert output == "<p>test.com</p>"

    def test_ensure_ol_structure(self):
        inputstr="""
1. hello
2. world"""

        output = RichTextHelper.toHTML(inputstr)
        assert output.replace("\n", "") == """<ol>
<li>hello</li>
<li>world</li>
</ol>""".replace("\n", "")
