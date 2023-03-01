# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

def remove_punctuation(line, punctuation):
    if punctuation == "parentheses":
        if line.startswith('(') and line.endswith(')'):
                return line[1:-1]
    elif punctuation == "brackets":
        if line.startswith('[') and line.endswith(']'):
                return line[1:-1]

    return line