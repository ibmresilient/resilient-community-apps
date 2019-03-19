# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Test helper functions"""
import pytest
from fn_sep.lib.helpers import *
from xml.etree import ElementTree as ElementTree
import json
import xmltodict
"""
Suites of tests to test the Symantec SEP Helper functions
"""

def setup_test_xml():
    test_xml = dedent("""\
        <?xml version="1.0" encoding="UTF-8"?>
        <EOC creator="Creator" version="1.1" id="60">
          <DataSource name="Third-Party Provider" id="23" version="1.0"/>
          <ScanType>FULL_SCAN</ScanType>
          <Threat category="Suspects" type="to_investigate" severity="Medium" time="2017-01-29 4:54:01 PM">
            <Description>Just a test.</Description>
            <Attacker>
            </Attacker>
          </Threat>
          <Activity>
            <OS id="1" name="" version="" patch="">
              <Process>
              </Process>
              <Files>
                <File name="C:\temp\eicar.zip" action="write">
                  <Hash name="SHA256" value="131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267"/>
                </File>
              </Files>
              <Registry>
              </Registry>
              <Network>
              </Network>
            </OS>
          </Activity>
        </EOC>""")

    return test_xml

def xml_to_json(xml):
    """Receive 1 lxml etree object and return a json string"""

    def recursive_dict(element):
        return (element.tag.split('}')[1],
                dict(map(recursive_dict, element.getchildren()),
                     **element.attrib))

    return json.dumps(dict([recursive_dict(xml)]),
                      default=lambda x: str(x))

def convert_value_to_none(v):
    # Convert "None" string value to None value.
    if type(v) == str and v.lower() == 'none':
        v = None
    return v


class TestSepHelpersTransformKwargs:
    """Test transform_kwargs function"""

    @pytest.mark.parametrize("sep_hardwarekey, sep_group_id", [
        ("DC7D24D6465566D2941F35BC8D17801E","8E20F39B0946C25D118925C2E28C2D59"),
        (None, None),
        ('none', 'None')
    ])
    def test_transform_kwargs(self, sep_hardwarekey, sep_group_id):
        new_kwargs = {
            "hardwarekey": convert_value_to_none(sep_hardwarekey),
            "group_id": convert_value_to_none(sep_group_id)
        }
        kwargs = {
            "sep_hardwarekey": sep_hardwarekey,
            "sep_group_id": sep_group_id
        }
        transform_kwargs(kwargs)
        for key in new_kwargs:
            assert (key in kwargs)
            assert(kwargs[key] == new_kwargs[key])

class TestSepHelpersSetupEocCommand:
    """Test transform_kwargs function"""

    def xml_to_json(self, xml):
        """Receive 1 lxml etree object and return a json string"""

        def recursive_dict(element):
            return (element.tag.split('}')[1],
                    dict(map(recursive_dict, element.getchildren()),
                         **element.attrib))

        return json.dumps(dict([recursive_dict(xml)]),
                          default=lambda x: str(x))

    def assertEqualXML(self, xml_real, xml_expected):
        """Receive 2 objectify objects and show a diff assert if exists."""
        xml_expected_str = json.loads(self.xml_to_json(xml_expected))
        xml_real_str = json.loads(self.xml_to_json(xml_real))
        self.maxDiff = None
        self.assertEqual(xml_real_str, xml_expected_str)

    @pytest.mark.parametrize("scan_type, file_path, sha256, description", [
        ("FULL_SCAN","C:\\temp\\eicar.zip", "131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267", "Just a test."),
    ])
    def test_setup_eoc_command(self, scan_type, file_path, sha256, description):

        eoc_xml = setup_eoc_command(scan_type, file_path, sha256, description)
        test_xml = setup_test_xml()
        eoc_xml_dict = xmltodict.parse(eoc_xml)
        test_xml_dict = xmltodict.parse(test_xml)
        #root = ElementTree.fromstring("eoc_xml")
        test=1
