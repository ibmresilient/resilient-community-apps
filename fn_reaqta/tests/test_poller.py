#
import pytest
import resilient
from fn_reaqta.lib.poller_common import SOARCommon, eval_mapping

parser = resilient.ArgumentParser(config_file=resilient.get_config_file())
opts = parser.parse_args()

# Create SimpleClient for a REST connection to the Resilient services
client = resilient.get_client(opts)

def test_eval_mapping():
    assert eval_mapping('"A","B","C"', wrapper="[{}]") == ["A", "B", "C"]
    assert eval_mapping('"A":"B"', wrapper="{{ {} }}") == {"A": "B"}
    assert eval_mapping("x = 1") == None

def test_filter_soar_comments():
    sc = SOARCommon(client)
    # def filter_soar_comments(self, case_id, entity_comments, soar_header=SOAR_HEADER):
    entity_comments = ["one comment", "header\nsecond comment", "third comment\nthird comment2\nthird comment3"]

    assert sc._filter_comments(["one comment", "third comment\nthird comment2\nthird comment3"],
                              entity_comments,
                              soar_header=None) == ["header\nsecond comment"]
    assert sc._filter_comments(["one comment"],
                              entity_comments,
                              soar_header="header") == ["third comment\nthird comment2\nthird comment3"]
