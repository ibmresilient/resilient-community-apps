#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Debugging tool:
    example:
    get_tactic_url.py "Initial Access"
"""
import sys
from fn_mitre_integration.lib.mitre_attack import MitreAttack
import json

if len(sys.argv) < 2:
    print("Usage get_tactic_url.py tactic_name")
    sys.exit()

tactic_name = sys.argv[1]

url = MitreAttack().get_tactic_url(tactic_name)

print(url)