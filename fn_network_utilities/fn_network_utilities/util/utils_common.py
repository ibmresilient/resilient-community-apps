# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

def remove_punctuation(line, punctuation):
    # punctuation is a boolean. True means that a parenthesis can be expected and false means brackets
    if punctuation == True:
        if line.startswith('(') and line.endswith(')'):
                return line[1:-1]
    elif punctuation == False:
        if line.startswith('[') and line.endswith(']'):
                return line[1:-1]

    return line