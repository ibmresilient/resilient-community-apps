#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from fn_mitre_integration.lib.mitre_attack import MitreAttack
import json

if len(sys.argv) < 2:
    print("Usage get_tech_mitigation.py tech_id")
    sys.exit()

tech_id = sys.argv[1]

mitigations = MitreAttack().get_tech_mitigation(tech_id)

print(str(mitigations))