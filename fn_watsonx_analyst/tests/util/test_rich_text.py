import pytest
from fn_watsonx_analyst.util.rich_text import RichTextHelper

class TestRichText:
    font_sizes = RichTextHelper.get_config()["font_sizes"]

    def test_ensure_script_not_parsed(self):
        output = RichTextHelper.toHTML('<script>alert("hi")</script>')
        assert '<script>' not in output

    def test_ensure_unallowed_heading(self):
        inputstr = """# hello world"""

        output = RichTextHelper.toHTML(inputstr)
        assert output == f"<h1 style=\"font-size: {self.font_sizes['h1']}em;\">hello world</h1>\n"

    def test_ensure_anchors_not_parsed(self):
        inputstr = "[test.com](https://test.com)"
        output = RichTextHelper.toHTML(inputstr)

        assert output == '<p style="display: inline">test.com</p>\n'

    def test_ensure_ol_structure(self):
        inputstr="""
1. hello
2. world"""

        output = RichTextHelper.toHTML(inputstr)
        assert output.replace("\n", "") == """<ol>
<li>hello</li>
<li>world</li>
</ol>""".replace("\n", "")

    def test_ensure_code_block(self):
        inputstr = """```bash
echo 'hello world'
```
"""
        output = RichTextHelper.toHTML(inputstr)
        assert f"""<div style=\"{RichTextHelper.code_block_style}\">echo \'hello world\'\n</div>\n""" in output

    @pytest.mark.livetest # this test fails in travis, but passes locally
    def test_ensure_code_block_in_body(self):
        inputstr="""Here's some of my code, I hope you like it :)

```bash
echo 'hello world'
```
"""
        output = RichTextHelper.toHTML(inputstr)

        expected = """<p style="display: inline">Here's some of my code, I hope you like it :)</p>
<div><div style="font-family: monospace; background-color: black; color: white; padding: 5px;">echo 'hello world'
</div>
</div>"""
        assert output.startswith(expected)

    def test_inline_code(self):
        inputstr = "Hi there, `bruh`"
        output = RichTextHelper.toHTML(inputstr)
        assert output.strip() == f"""<p style="display: inline">Hi there, <i style="{RichTextHelper.code_inline_style}">bruh</i></p>"""

    def test_ensure_underscores_kept(self):
        inputstr = "bruh_moment_"

        assert RichTextHelper.toHTML(inputstr).strip() == '<p style="display: inline">bruh_moment_</p>'

    def test_ensure_ordered_tags_whitespace(self):
        inputstr = """
1. test 1
1. test 2
1. test 3
""".strip()
        assert RichTextHelper.toHTML(inputstr) == """<ol>
<li>test 1</li><li>test 2</li><li>test 3</li></ol>
"""

    def test_nested_lists(self):
        inputstr = """ - **Email Details:**
      * Sent to: frank-adams@baneandox.com
    * Received Date & Time: 20/09/2023 at 15:00
    * Target Domain: baneandox.com

    - **Malicious URLs Found:**
      * HTTPS://BANEAND0XE.COM/:
        + Threat Score: 70.3
        + Explainability Severity Score: 0.8

      - **Malware Detected:**
      * MD5 Hash: 7e37ab34ecdcc3e77e24522ddfd4852d
      * Threat Score: 94.9
      * Explainability Severity Score: 0.8

    - **IP Address Observed:**
      * 128.210.157.251
      * Threat Score: 10.0
      * VirusTotal Threat Score: 73.4

    - **Vulnerability Assessment Indicators:**
      * URL: HTTPS://BANEAND0XE.COM/
      * Threat Score: 70.3
      * Explainability Severity Score: 0.8
      
      * Malware MD5 Hash: 7e37ab34ecdcc3e77e24522ddfd4852d
      * Threat Score: 94.9
      * Explainability Severity Score: 0.8
      
    - **SANS Internet Storm Center Rating:**
      * IP Address: 128.210.157.251
      * Threat Score: 10.0"""
        assert (
            RichTextHelper.toHTML(inputstr)
            == """<ul>
<li><p style="display: inline"><strong>Email Details:</strong></p>
<ul>
<li><p style="display: inline">Sent to: frank-adams@baneandox.com</p>
<ul>
<li>Received Date &amp; Time: 20/09/2023 at 15:00</li><li><p style="display: inline">Target Domain: baneandox.com</p>
</li><li><p style="display: inline"><strong>Malicious URLs Found:</strong></p>
</li></ul>
</li><li><p style="display: inline">HTTPS://BANEAND0XE.COM/:</p>
<ul>
<li>Threat Score: 70.3</li><li>Explainability Severity Score: 0.8</li></ul>
</li><li><p style="display: inline"><strong>Malware Detected:</strong></p>
</li><li>MD5 Hash: 7e37ab34ecdcc3e77e24522ddfd4852d</li><li>Threat Score: 94.9</li><li><p style="display: inline">Explainability Severity Score: 0.8</p>
<ul>
<li><strong>IP Address Observed:</strong></li></ul>
</li><li>128.210.157.251</li><li>Threat Score: 10.0</li><li><p style="display: inline">VirusTotal Threat Score: 73.4</p>
<ul>
<li><strong>Vulnerability Assessment Indicators:</strong></li></ul>
</li><li>URL: HTTPS://BANEAND0XE.COM/</li><li>Threat Score: 70.3</li><li><p style="display: inline">Explainability Severity Score: 0.8</p>
</li><li><p style="display: inline">Malware MD5 Hash: 7e37ab34ecdcc3e77e24522ddfd4852d</p>
</li><li>Threat Score: 94.9</li><li><p style="display: inline">Explainability Severity Score: 0.8</p>
<ul>
<li><strong>SANS Internet Storm Center Rating:</strong></li></ul>
</li><li>IP Address: 128.210.157.251</li><li>Threat Score: 10.0</li></ul>
</li></ul>
"""
        )
