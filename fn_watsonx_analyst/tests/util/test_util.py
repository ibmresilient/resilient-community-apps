from fn_watsonx_analyst.util.util import defang_text


class TestUtil:
    """Test the methods in util.py - defanging"""
    def test_defang_removes_anchors_dbl_qt(self):
        """Ensure anchors with double quotes are handled correctly"""
        input_str = '<a href="https://google.com">Google</a>'
        output = defang_text(input_str)
        assert output.startswith("Google")
        assert "https://google.com" not in output

    def test_defang_removes_anchors_sngl_qt(self):
        """Ensure anchors with single quotes are handled correctly"""
        input_str = "<a href='https://google.com'>Google</a>"
        output = defang_text(input_str)
        assert output.startswith("Google")
        assert "https://google.com" not in output

    def test_defang_with_other_text_at_start(self):
        """Ensure anchors suppressed while also maintaining starting text"""
        input_str = 'Test <a href="https://google.com">Google</a>'
        output = defang_text(input_str)
        assert output.startswith("Test")
        assert "https://google.com" not in output

    def test_defang_with_other_text_at_end(self):
        """Ensure anchors suppressed while also maintaining ending text"""
        input_str = '<a href="https://google.com">Google</a> Search'
        output = defang_text(input_str)
        assert output.endswith("Search")
        assert "https://google.com" not in output

    def test_defang_with_other_text_around(self):
        """Ensure anchors suppressed while also maintaining starting and ending text"""
        input_str = 'Test <a href="https://google.com">Google</a> Search'
        output = defang_text(input_str)
        assert output.startswith("Test") and output.endswith("Search")
        assert "https://google.com" not in output

    def test_defang_multiple_anchors(self):
        """Ensure multiple anchors are suppressed while also maintaining starting and ending text"""
        input_str = '<a href="https://ibm.com">IBM</a> Test <a href="https://google.com">Google</a>'
        output = defang_text(input_str)
        assert output.startswith("IBM") and output.endswith("Google")
        assert "https://google.com" not in output and "https://ibm.com" not in output
