# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

import unittest

import data.pb_mandiant_scan_artifact_script as playbook
from data.pb_mandiant_scan_artifact_script import *


class TestPBFunctions(unittest.TestCase):
        
    def test_compile_section_by_dtype(self):
        ret = compile_section_by_dtype("https://www.example.com", "primary url")
        assert len(ret) == 3
        assert all([key in ret for key in ["name", "type", "value"]])
        assert ret["name"]  == "primary url"
        assert ret["type"]  == "uri"
        assert ret["value"] == "https://www.example.com"

        ret = compile_section_by_dtype("http://www.example.com", "primary url")
        assert len(ret) == 3
        assert all([key in ret for key in ["name", "type", "value"]])
        assert ret["name"]  == "primary url"
        assert ret["type"]  == "uri"
        assert ret["value"] == "http://www.example.com"

        ret = compile_section_by_dtype("2", "count")
        assert len(ret) == 3
        assert all([key in ret for key in ["name", "type", "value"]])
        assert ret["name"]  == "count"
        assert ret["type"]  == "number"
        assert ret["value"] == 2

        ret = compile_section_by_dtype("ibm", "name")
        assert len(ret) == 3
        assert all([key in ret for key in ["name", "type", "value"]])
        assert ret["name"]  == "name"
        assert ret["type"]  == "string"
        assert ret["value"] == "ibm"


    def test_dedup_section(self):
        section = [{
            'name': 'id',
            'type': 'string',
            'value': 'url--333112233'
        }, {
            'name': 'id',
            'type': 'number',
            'value': 99
        }, {
            'name': 'val',
            'type': 'string',
            'value': 'url'
        }, {
            'name': 'not_id',
            'type': 'uri',
            'value': 'http://achren.org'
        }, {
            'name': 'id',
            'type': 'string',
            'value': 'True'
        }, {
            'name': 'val',
            'type': 'string',
            'value': 'url'
        }]
        ret = dedup_section(section)
        names, exp = [], ['id', 'id1', 'val', 'not_id', 'id2', 'val1']
        for item in ret:
            names.append(item.get("name"))
        assert len(set(names)) == len(section)
        assert all([item in names for item in exp])


    def test_dedup_verdict_section(self):
        source = [
            {'name': 'name', 'type': 'string', 'value': 'Bulletproof Hosting'},
            {'name': 'response_count', 'type': 'number', 'value': 0},
            {'name': 'source_count', 'type': 'number', 'value': 1},
            {'name': 'benign_count', 'type': 'number', 'value': 1},
            {'name': 'confidence', 'type': 'string', 'value': 'low'},
            {'name': 'malicious_count', 'type': 'number', 'value': 0},
            {'name': 'name', 'type': 'string', 'value': 'FQDN Analysis'},
            {'name': 'response_count', 'type': 'number', 'value': 1},
            {'name': 'source_count', 'type': 'number', 'value': 2},
            {'name': 'benign_count', 'type': 'number', 'value': 0},
            {'name': 'confidence', 'type': 'string', 'value': 'None'},
            {'name': 'malicious_count', 'type': 'number', 'value': 0},
            {'name': 'name', 'type': 'string', 'value': 'Knowledge Graph'},
            {'name': 'response_count', 'type': 'number', 'value': 0},
            {'name': 'source_count', 'type': 'number', 'value': 1},
            {'name': 'benign_count', 'type': 'number', 'value': 0},
            {'name': 'confidence', 'type': 'string', 'value': 'None'},
            {'name': 'malicious_count', 'type': 'number', 'value': 0}
        ]

        expected = [
            {'name': 'Bulletproof Hosting name', 'type': 'string', 'value': 'Bulletproof Hosting'},
            {'name': 'Bulletproof Hosting response_count', 'type': 'number', 'value': 0},
            {'name': 'Bulletproof Hosting source_count', 'type': 'number', 'value': 1},
            {'name': 'Bulletproof Hosting benign_count', 'type': 'number', 'value': 1},
            {'name': 'Bulletproof Hosting confidence', 'type': 'string', 'value': 'low'},
            {'name': 'Bulletproof Hosting malicious_count', 'type': 'number', 'value': 0},
            {'name': 'FQDN Analysis name', 'type': 'string', 'value': 'FQDN Analysis'},
            {'name': 'FQDN Analysis response_count', 'type': 'number', 'value': 1},
            {'name': 'FQDN Analysis source_count', 'type': 'number', 'value': 2},
            {'name': 'FQDN Analysis benign_count', 'type': 'number', 'value': 0},
            {'name': 'FQDN Analysis confidence', 'type': 'string', 'value': 'None'},
            {'name': 'FQDN Analysis malicious_count', 'type': 'number', 'value': 0},
            {'name': 'Knowledge Graph name', 'type': 'string', 'value': 'Knowledge Graph'},
            {'name': 'Knowledge Graph response_count', 'type': 'number', 'value': 0},
            {'name': 'Knowledge Graph source_count', 'type': 'number', 'value': 1},
            {'name': 'Knowledge Graph benign_count', 'type': 'number', 'value': 0},
            {'name': 'Knowledge Graph confidence', 'type': 'string', 'value': 'None'},
            {'name': 'Knowledge Graph malicious_count', 'type': 'number', 'value': 0}
        ]
        assert len(dedup_verdict_section(source)) == len(source)
        names = []
        for key in dedup_verdict_section(source):
            names.append(key.get("name"))
        assert len(set(names)) == len(names)
        [self.assertDictEqual(item[0], item[1]) for item in zip(dedup_verdict_section(source), expected)]


    def test_add_response_as_hits(self):

        class artifact:
            def addHit(_, name, section):

                if name == "Mandiant Threat intelligence: Item4":
                    self.assertDictEqual({name:section}, {
                        'Mandiant Threat intelligence: Item4': [
                            {'name': 'subitem1', 'type': 'string', 'value': 'subvalue1'},
                            {'name': 'subitem2', 'type': 'string', 'value': 'subvalue2'}]})

                elif name == "Mandiant Threat intelligence: Item5":
                    self.assertDictEqual({name:section}, {
                        'Mandiant Threat intelligence: Item5': [
                            {'name': 'subitem1', 'type': 'string', 'value': 'subvalue1'},
                            {'name': 'subitem2', 'type': 'string', 'value': 'subvalue2'},
                            {'name': 'subitem3', 'type': 'string', 'value': 'subvalue3'}]})

                elif name == 'Mandiant Threat intelligence: Verdict':
                    self.assertDictEqual({name:section}, {
                        'Mandiant Threat intelligence: Verdict': [
                            {'name': 'analysis1 name', 'type': 'string', 'value': 'analysis1'},
                            {'name': 'analysis1 count', 'type': 'number', 'value': 0},
                            {'name': 'analysis2 name', 'type': 'string', 'value': 'analysis2'},
                            {'name': 'analysis2 count', 'type': 'number', 'value': 1}]})

                elif name == 'Mandiant Threat intelligence: MScore':
                    self.assertDictEqual({name:section}, {
                        'Mandiant Threat intelligence: MScore': [
                            {'name': 'item1', 'type': 'string', 'value': 'value1'},
                            {'name': 'item2', 'type': 'string', 'value': 'value2'},
                            {'name': 'item3', 'type': 'string', 'value': 'value3'}]})

                else:
                    raise AssertionError("Unknown section provided")

        playbook.artifact = artifact()
        section = {
            "item1" : "value1",
            "item2" : "value2",
            "item3" : "value3",
            "item4" : {
                "subitem1" : "subvalue1",
                "subitem2" : "subvalue2"
                },
            "item5" : [
                {"subitem1" : "subvalue1"},
                {"subitem2" : "subvalue2"},
                {"subitem3" : "subvalue3"}
            ],
            "verdict" : {
                "item5" : [
                {"name"  : "analysis1"},
                {"count" : 0},
                {"name"  : "analysis2"},
                {"count" : 1},
                ],
            }
        }
        add_response_as_hits(section)


if __name__ == "__main__":
    unittest.main()