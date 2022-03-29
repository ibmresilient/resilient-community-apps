# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use


def b_to_s(value):
    try:
        return value.decode()
    except:
        return value

def s_to_b(value):
    try:
        return bytes(value, 'utf-8')
    except:
        return value