#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""
    Debugging tool:

    Example:
        get_technique_info.py AppleScript
"""
import sys
from fn_mitre_integration.lib.mitre_attack import MitreAttack
import json
from proxies import get_proxies

if len(sys.argv) < 2:
    print("Usage get_technique_info.py tech_id <mitigation>")
    sys.exit()

tech_id = sys.argv[1]

mitigation_only = False
if len(sys.argv) == 3:
    mitigation_only = True

if mitigation_only:
    mitigations = MitreAttack(opts=None, function_opts=get_proxies()).get_tech_mitigation(tech_id)
    print(str(mitigations))
else:
    tech = MitreAttack().get_tech(tech_id)
    print(str(tech))