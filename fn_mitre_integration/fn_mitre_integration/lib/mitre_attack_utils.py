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


def get_techniques(tactics_str):
    """
    Get techniques for all input tactics
    :param tactics_str: string of tactics separated by comma
    :return:            techniques
    """
    tactics = tactics_str.split(', ')

    ret = []
    mitre_attack = MitreAttack()
    for tactic in tactics:
        techs = mitre_attack.get_tactic_techniques(tactic)

        tactic_dict = {
            "tactic_name": tactic,
            "tactic_id": MitreAttackTactic.get_id(tactic),
            "tactic_ref": MitreAttack.get_tactic_url(tactic),
            "techs": techs
        }

        ret.append(tactic_dict)
      
    return ret

