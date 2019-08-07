# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

"""
Note that the mitre_attack class encapsulates the
MITRE ATTACK STIX TAXII server. Since that sever is
available to public, this file is a system level test
"""

from fn_mitre_integration.lib.mitre_attack import MitreAttack, MitreAttackTactic
from fn_mitre_integration.lib.mitre_attack_utils import get_techniques
import requests

mitre_attack = MitreAttack()

def url_get(url):
    ret = False
    try:
        response = requests.get(url)
        if response.status_code == 200:
            ret = True
    except:
        ret = False

    return ret

class TestMitre(object):
    def test_get_all_tactics_from_all_framework(self):
        tactics = mitre_attack.get_all_tactics()
        # As 8/5/19 there are 40 tactics
        assert len(tactics) >= 40

    def test_get_by_id_works(self):
        assert MitreAttackTactic.get_by_id(mitre_attack, "Collection") is not None
        assert MitreAttackTactic.get_by_id(mitre_attack, "Clearly Absurd") is None

    def test_get_tactic_url(self):
        tactics = mitre_attack.get_all_tactics()

        for tactic in tactics:
            url = mitre_attack.get_tactic_url(tactic.name)
            assert url_get(url)

        # Test error handling
        url = mitre_attack.get_tactic_url("Fake Tactic")
        assert (url is None)

    def test_lookup_item(self):
        item_name = "Remote Services"

        item = mitre_attack.lookup_item(item_name=item_name)
        assert item
        print(item)

    def test_get_tactic_techniques(self):
        tactics = mitre_attack.get_all_tactics()

        for tactic in tactics:
            print(tactic.name)
            techs = mitre_attack.get_tactic_techniques(tactic_name=tactic.name)
            print(len(techs))
            assert(len(techs) > 0)
        #
        # Test using tactic id as well
        #
        techs = mitre_attack.get_tactic_techniques(tactic_id="TA0001")
        assert (len(techs) > 1)

    def test_get_tech_mitigation(self):
        techs = mitre_attack.get_all_techniques()
        print(len(techs))
        try:
            #
            #   There are more than 200 techs. Try first 5 only
            #
            count = 0
            for tech in techs:
                id = tech.id
                assert(id)
                mitigation = mitre_attack.get_tech_mitigation(tech_id=id)
                assert mitigation
                print(mitigation)
                count += 1
                if count > 5:
                    break
                # Test getting mitigation using name
                mitigation = mitre_attack.get_tech_mitigation(tech_name=tech.name)
                assert mitigation
                print(mitigation)
        except:
            assert(False)

    def test_mitre_attack_util(self):
        tactics = "Execution, Persistence"
        techs = get_techniques(tactic_names=tactics)
        print(len(techs))
        assert(len(techs[0]["techs"]) + len(techs[1]["techs"]) == 98)

        tactics = "TA0001, TA0002, TA0008"
        techs = get_techniques(tactic_ids=tactics)
        print(len(techs))
        assert(len(techs) > 0)

    def test_get_tech_info(self):
        tech = mitre_attack.get_technique(name="AppleScript")
        print(tech)
        assert(tech["name"] == "AppleScript")

        tech = mitre_attack.get_technique(ext_id="T1156")
        print(tech)
        assert(tech["mitre_tech_id"] == "T1156")

        #
        #   Error handling
        #
        tech = mitre_attack.get_technique()
        assert tech is None

