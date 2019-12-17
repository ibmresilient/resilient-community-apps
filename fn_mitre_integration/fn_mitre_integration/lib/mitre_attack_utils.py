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


def get_multiple_techniques(mitre_conn, mitre_technique_ids=None, mitre_technique_names=None):
    """
    Gets multiple techniques from a comma separated input of IDs or names.
    If both are given, the IDs are used.
    :param mitre_conn: MitreAttackConnection instance
    :param mitre_technique_ids: Comma separated string with MITRE IDs
    :param mitre_technique_names: Comma separated string with MITRE names
    :return: List of techniques
    :rtype: list(MitreAttackTechnique)
    """
    if mitre_technique_ids is not None:
        # Try id first, because it's less ambiguous
        technique_ids = mitre_technique_ids.split(',')
        techniques = []
        for t_id in technique_ids:
            technique = MitreAttackTechnique.get_by_id(mitre_conn, t_id)
            if not technique:
                raise ValueError("Technique with id {} doesn't exist".format(t_id))
            techniques.extend(technique)
    else:
        # It's possible for multiple tactics to have the same name
        # And we want to make sure that all of them are processed in that case
        technique_names = mitre_technique_names.split(',')
        techniques = []
        for name in technique_names:
            technique = MitreAttackTechnique.get_by_name(mitre_conn, name)
            if not technique:
                raise ValueError("Techniques with name {} don't exist".format(name))
            techniques.extend(technique)

    return techniques


def get_tactics_and_techniques(tactic_names=None, tactic_ids=None):
    """
    Get techniques for all input tactics
    :param tactic_names:    string of tactic names separated by comma
    :param tactic_ids:      string of tactic ids separated by comma
    :return:                techniques
    """
    mitre_conn = MitreAttackConnection()

    tactics = []

    # Check ids first, as it takes priority in querying
    if tactic_ids is not None:
        t_ids = tactic_ids.split(',')

        for tid in t_ids:
            tactics_id = MitreAttackTactic.get_by_id(mitre_conn, tid)
            if tactics_id is not None:
                for tactic in tactics_id:
                    tactics.append(tactic.id)
            else:
                raise ValueError("Tactics with id {} do not exist.".format(tid))
    elif tactic_names is not None:
        # It's possible for multiple tactics to have the same name
        # And we want to make sure that all of them are processed in that case
        tactic_names = tactic_names.split(',')

        for t_name in tactic_names:
            tactics_named = MitreAttackTactic.get_by_name(mitre_conn, t_name)
            if not tactics_named:
                raise ValueError("Tactics with name {} do not exist.".format(t_name))
            else:
                for tactic in tactics_named:
                    tactics.append(tactic.id)

    ret = []
    for tactic_id in tactics:
        t_obj = MitreAttackTactic.get_by_id(mitre_conn, tactic_id)[0]  # since we search by id, its unique

        techs = t_obj.get_techniques(mitre_conn)

        # get the dict for tactic and include techniques into it
        tactic_dict = t_obj.dict_form()
        tactic_dict.update({
            "mitre_techniques": [tech.dict_form() for tech in techs]
        })

        ret.append(tactic_dict)
    return ret

