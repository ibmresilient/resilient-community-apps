# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Zia integration specific exceptions """
class ZiaException(Exception):
    """
    Custom exception to be raised on request errors.
    """
    pass

class ZiaRateLimitException(Exception):
    """
    Custom exception to be raised on rate limit request errors.
    """
    pass
