# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#

#
#   Utils collection for MitreAttack
#   --------------------------------
#

from fn_mitre_integration.lib.mitre_attack import MitreAttackConnection
from fn_mitre_integration.lib.mitre_attack import MitreAttackTactic, MitreAttackTechnique


def get_tactics_and_techniques(tactic_names=None, tactic_ids=None):
    """
    Get techniques for all input tactics
    :param tactic_names:    string of tactic names separated by comma
    :param tactic_ids:      string of tactic ids separated by comma
    :return:                techniques
    """
    mitre_conn = MitreAttackConnection()

    tactics = []
    if tactic_names is not None:
        # It's possible for multiple tactics to have the same name
        # And we want to make sure that all of them are processed in that case
        tactic_names = tactic_names.split(', ')
        for t_name in tactic_names:
            tactic = MitreAttackTactic.get_by_name(mitre_conn, t_name)
            if tactic is None:
                raise ValueError("Tactic with name {} does not exist.".format(t_name))
            elif isinstance(tactic, list):
                for t in tactic:
                    tactics.append(t.id)
            else:
                tactics.append(tactic.id)
    elif tactic_ids is not None:
        t_ids = tactic_ids.split(', ')
        for tid in t_ids:
            tactic = MitreAttackTactic.get_by_id(mitre_conn, tid)
            if tactic is not None:
                tactics.append(tactic.id)
            else:
                raise ValueError("Tactic with id {} does not exist.".format(tid))

    ret = []
    for tactic_id in tactics:
        t_obj = MitreAttackTactic.get_by_id(mitre_conn, tactic_id)
        techs = t_obj.get_techniques(mitre_conn)

        # get the dict for tactic and include techniques into it
        tactic_dict = t_obj.dict_form()
        tactic_dict.update({
            "mitre_techniques": [tech.dict_form() for tech in techs]
        })

        ret.append(tactic_dict)
    return ret

