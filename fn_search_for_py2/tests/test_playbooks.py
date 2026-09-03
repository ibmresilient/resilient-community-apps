from urllib.parse import unquote
from lxml import etree
import pytest

from .common import read_sample_file, MockSOAR
from fn_search_for_py2.lib.common import FindPY2_SOAR

PLAYBOOK_PY2_ALL = "data/playbook_py2_all.res"
PLAYBOOK_PY2_CALLACTIVITY = "data/subplaybook_py2_callActivity.res"
PLAYBOOK_PY2_ENDEVENT = "data/playbook_py2_endEvent.res"
PLAYBOOK_PY2_CASECONDITION = "data/playbook_py2_caseCondition.res"
PLAYBOOK_PY2_3CONDITIONS = "data/playbook_py2_conditions.res"

class TestPlaybooks():

    @pytest.mark.parametrize("sample_py2", [
        (PLAYBOOK_PY2_CALLACTIVITY),
        (PLAYBOOK_PY2_ENDEVENT),
        (PLAYBOOK_PY2_CASECONDITION),
        (PLAYBOOK_PY2_ALL)
    ])
    def test_pb_bpmn(self, sample_py2):
        findpy2_helper = FindPY2_SOAR(MockSOAR(return_script_py2=False))

        sample_json = read_sample_file(sample_py2)

        result = findpy2_helper.analyze_bpmn(sample_json)
        assert any(result)

    @pytest.mark.parametrize("sample_py2", [
        (PLAYBOOK_PY2_ALL)
    ])
    def test_pb_fail(self, sample_py2):
        findpy2_helper = FindPY2_SOAR(MockSOAR(return_script_py2=False))

        sample_json = read_sample_file(sample_py2, replace_py3=True)

        result = findpy2_helper.analyze_bpmn(sample_json)
        assert not any(result)

    @pytest.mark.parametrize("sample_py2", [
        (PLAYBOOK_PY2_ALL),
        (PLAYBOOK_PY2_3CONDITIONS)
    ])
    def test_pb_convert(self, sample_py2):
        findpy2_helper = FindPY2_SOAR(MockSOAR(return_script_py2=False))

        sample_json = read_sample_file(sample_py2)

        result = findpy2_helper.fix_py2_bpmn(sample_json)
        assert  result[0]

        # confirm no python2 remains
        test_conversion = findpy2_helper.analyze_bpmn(result[1])

        assert not any(test_conversion)

    @pytest.mark.parametrize("sample_py2, filter_name", [
        (PLAYBOOK_PY2_ALL, "CriminalIP URL Lookup Subplaybook"),
    ])
    def test_filter_by_name(self, sample_py2, filter_name):
        findpy2_helper = FindPY2_SOAR(MockSOAR(return_script_py2=False))
        sample_json = read_sample_file(sample_py2)

        assert findpy2_helper.filter_on_tags(None, filter_name, [sample_json])
