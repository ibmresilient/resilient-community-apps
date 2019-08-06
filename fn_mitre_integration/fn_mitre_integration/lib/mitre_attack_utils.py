# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#

#
#   Utils collection for MitreAttack
#   --------------------------------
#

from fn_mitre_integration.lib.mitre_attack import MitreAttack
from fn_mitre_integration.lib.mitre_attack import MitreAttackTactic


def get_techniques(tactic_names=None, tactic_ids=None):
    """
    Get techniques for all input tactics
    :param tactic_names:    string of tactic names separated by comma
    :param tactic_ids:      string of tactic ids separated by comma
    :return:                techniques
    """
    mitre_attack = MitreAttack()

    tactics = []
    if tactic_names is not None:
        tactics = tactic_names.split(', ')
    elif tactic_ids is not None:
        t_ids = tactic_ids.split(', ')
        tactics =[MitreAttackTactic.get_name(tid) for tid in t_ids ]

    ret = []
    for tactic in tactics:
        techs = mitre_attack.get_tactic_techniques(tactic_name=tactic)

        tactic_dict = {
            "tactic_name": tactic,
            "tactic_id": MitreAttackTactic.get_id(tactic),
            "tactic_ref": MitreAttack.get_tactic_url(tactic),
            "techs": techs
        }

        ret.append(tactic_dict) 
    return ret

