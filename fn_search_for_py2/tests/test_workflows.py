from urllib.parse import unquote
from lxml import etree
import pytest

from .common import read_sample_file, MockSOAR
from fn_search_for_py2.lib.common import FindPY2_SOAR

WORKFLOW_ALL_FILE = "data/workflow_py2_all.res"
WORKFLOW_FUNC_PRE_FILE = "data/workflow_py2_function_pre_proc.res"
WORKFLOW_FUNC_POST_FILE = "data/workflow_py2_function_post_proc.res"
WORKFLOW_3CONDITIONS = "data/workflow_py2_3conditions.res"

class TestWorkFlows():
    @pytest.mark.parametrize("sample_py2", [
        (WORKFLOW_ALL_FILE)
    ])
    def test_wk_conditions(self, sample_py2):
        findpy2_helper = FindPY2_SOAR(MockSOAR(return_script_py2=False))

        sample_json = read_sample_file(sample_py2)
        xml = sample_json["content"]["xml"]
        etree_xml = etree.XML(bytes(unquote(xml), "utf-8"))

        assert findpy2_helper.analyze_conditions(etree_xml)

    @pytest.mark.parametrize("sample_py2", [
        (WORKFLOW_FUNC_PRE_FILE),
        (WORKFLOW_FUNC_POST_FILE),
        (WORKFLOW_3CONDITIONS)
    ])
    def test_wk_bpmn(self, sample_py2):
        findpy2_helper = FindPY2_SOAR(MockSOAR(return_script_py2=False))

        sample_json = read_sample_file(sample_py2)

        result = findpy2_helper.analyze_bpmn(sample_json)
        assert any(result)

    @pytest.mark.parametrize("sample_py2", [
        (WORKFLOW_ALL_FILE)
    ])
    def test_wk_not_py2(self, sample_py2):
        findpy2_helper = FindPY2_SOAR(MockSOAR(return_script_py2=False))

        sample_json = read_sample_file(sample_py2, replace_py3=True)

        result = findpy2_helper.analyze_bpmn(sample_json)

        assert not any(result)

    @pytest.mark.parametrize("sample_py2", [
        (WORKFLOW_ALL_FILE)
    ])
    def test_wk_convert(self, sample_py2):
        findpy2_helper = FindPY2_SOAR(MockSOAR(return_script_py2=False))

        sample_json = read_sample_file(sample_py2)

        result = findpy2_helper.fix_py2_bpmn(sample_json)
        assert  result[0]

        # confirm no python2 remains
        test_conversion = findpy2_helper.analyze_bpmn(result[1])

        assert not any(test_conversion)

    @pytest.mark.parametrize("sample_py2, filter_name", [
        (WORKFLOW_ALL_FILE, " SUB-workflow "),
    ])
    def test_filter_by_name(self, sample_py2, filter_name):
        findpy2_helper = FindPY2_SOAR(MockSOAR(return_script_py2=False))
        sample_json = read_sample_file(sample_py2)

        assert findpy2_helper.filter_on_tags(None, filter_name, [sample_json])
