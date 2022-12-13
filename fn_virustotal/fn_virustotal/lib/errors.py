# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

class IntegrationError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)