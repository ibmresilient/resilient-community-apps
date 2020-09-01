#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""
    Debugging tool
        get_tech_mitigation AppleScript

"""
import sys
from fn_mitre_integration.lib.mitre_attack import MitreAttack
from fn_mitre_integration.lib.mitre_attack_utils import get_techniques
import json
from proxies import get_proxies

if len(sys.argv) < 2:
    print("Usage get_tech_mitigation.py <tech name>")
    sys.exit()

tactic_name = sys.argv[1]

tactics = tactic_name.split(", ")

if len(tactics) == 1:
    techs = MitreAttack(opts=None, function_opts=get_proxies()).get_tactic_techniques(tactic_name)
else:
    techs = get_techniques(tactic_name)

print(str(techs))