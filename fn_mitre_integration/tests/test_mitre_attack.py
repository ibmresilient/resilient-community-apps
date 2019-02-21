# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

"""
Note that the mitre_attack class encapsulates the
MITRE ATTACK STIX TAXII server. Since that sever is
available to public, this file is a system level test
"""

from fn_mitre_integration.lib.mitre_attack import MitreAttack
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


def test_get_tactic_url():
    tactics = mitre_attack.get_all_tactics()

    for tactic in tactics:
        url = mitre_attack.get_tactic_url(tactic.name)
        assert url_get(url)

    # Test error handling
    url = mitre_attack.get_tactic_url("Fake Tactic")
    assert (url is None)

def test_lookup_item():
    item_name = "Remote Services"

    item = mitre_attack.lookup_item(item_name=item_name)
    assert item
    print(item)



def test_get_tactic_techniques():
    tactics = mitre_attack.get_all_tactics()

    for tactic in tactics:
        print(tactic.name)
        techs = mitre_attack.get_tactic_techniques(tactic.name)
        print(len(techs))
        assert(len(techs) > 0)


def test_get_tech_mitigation():
    techs = mitre_attack.get_all_techniques()
    print(len(techs))
    try:
        #
        #   There are more than 200 techs. Try first 5 only
        #
        count = 0
        for tech in techs:
            id = mitre_attack.get_external_id(tech)
            assert(id)

            mitigation = mitre_attack.get_tech_mitigation(id)
            print(mitigation)
            count += 1
            if count > 5:
                break
    except:
        assert(False)


def test_mitre_attack_util():
    tactics = "Execution, Persistence"
    techs = get_techniques(tactics)
    print(len(techs))
    assert(len(techs[0]["techs"]) + len(techs[1]["techs"]) == 91)


def test_get_tech_info():

    tech = mitre_attack.get_tech(name="AppleScript")
    print(tech)
    assert(tech["name"] == "AppleScript")

    tech = mitre_attack.get_tech(ext_id="T1156")
    print(tech)
    assert(tech["mitre_tech_id"] == "T1156")

    #
    #   Error handling
    #
    tech = mitre_attack.get_tech()
    assert tech is None