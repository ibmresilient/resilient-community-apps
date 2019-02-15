#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from fn_mitre_integration.lib.mitre_attack import MitreAttack
from fn_mitre_integration.lib.mitre_attack_utils import get_techniques
import json

if len(sys.argv) < 2:
    print("Usage get_tech_tactic.py tactic_name")
    sys.exit()

tactic_name = sys.argv[1]

tactics = tactic_name.split(", ")

if len(tactics) == 1:
    techs = MitreAttack().get_tactic_techniques(tactic_name)
else:
    techs = get_techniques(tactic_name)

print(str(techs))