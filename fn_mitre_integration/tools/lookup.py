
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#

import sys
from fn_mitre_integration.lib.mitre_attack import MitreAttack
import json

if len(sys.argv) < 2:
    print("Usage lookup.py item_name type_name[optional] collection_name[optional]")
    sys.exit()

item_name = sys.argv[1]
type_name = None
collection_name = None
if len(sys.argv) > 2:
    type_name = sys.argv[2]

if len(sys.argv) > 3:
    collection_name = sys.argv[3]

attack = MitreAttack()

attack.connect_server()

item = attack.lookup_item(item_name)

item_dict = json.loads(item.serialize())

print(item_dict)

