# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
from resilient_lib.components.templates_common import sh_filter, ps_filter

COMMA_ESCAPED = "\,"
COMMA_SUBSTITUTE = "|"
COMMA = ","
SHELL_TYPE = "sh"

def remove_punctuation(line, punctuation):
    # punctuation is a boolean. True means that a parenthesis can be expected and false means brackets
    if punctuation is True:
        if line.startswith('(') and line.endswith(')'):
            return line[1:-1]
    elif punctuation is False:
        if line.startswith('[') and line.endswith(']'):
            return line[1:-1]

    return line

def separate_params(shell_params, shell_escaping=SHELL_TYPE):
    """separate parameters into dictionary key/value pairs

    :param shell_params: _description_
    :type shell_params: str
    :param shell_escaping: type of escaping to , defaults to "sh"
    :type shell_escaping: str, optional
    :return: dictionary of keys/values such as shell_param[1234]
    :rtype: dict
    """
    # handle the potential for escaped commas
    rendered_shell_params = {}
    if shell_params:
        params_list = shell_params.replace(COMMA_ESCAPED, COMMA_SUBSTITUTE).split(COMMA)
        for i, param in enumerate(params_list):
            param_name = f"shell_param{i+1}"
            if shell_escaping == SHELL_TYPE:
                converted_param = sh_filter(param)
            else:
                converted_param = ps_filter(param)
            rendered_shell_params[param_name] = converted_param.replace(COMMA_SUBSTITUTE, COMMA)

    return rendered_shell_params
