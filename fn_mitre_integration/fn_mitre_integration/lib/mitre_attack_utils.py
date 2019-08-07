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
from fn_mitre_integration.lib.mitre_attack import MitreAttackTactic, MitreAttackTechnique


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
        tactics =[MitreAttackTactic.get_by_id(mitre_attack, tid).name for tid in t_ids]

    ret = []
    for tactic in tactics:
        t_obj = MitreAttackTactic.get_by_name(mitre_attack, tactic)
        techs = MitreAttackTechnique.get_by_tactic(mitre_attack, t_obj)
        tactic_dict = {
            "tactic_name": t_obj.name,
            "tactic_id": t_obj.id,
            "tactic_ref": t_obj.get_url(),
            "techs": [tech.dict_repr() for tech in techs]
        }

        ret.append(tactic_dict)
    return ret

