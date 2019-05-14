# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
import os


class ApikeyError(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return repr(self.message)


class SpamhausRequestCallError(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return repr(self.error_msg)


def spamhaus_call_error(response_object):
    """
    :param response_object: Object returned from request.get call
    :return: if response object doesn't fall any below specified category returns response object else raises respective
    errors.
    """
    # Checking for status code
    if response_object.status_code == 400:
        raise SpamhausRequestCallError("Bad request - there was a syntax error in the request")
    elif response_object.status_code == 401:
        raise SpamhausRequestCallError("Authorization failed - please verify a valid DQS key was supplied")
    elif response_object.status_code == 403:
        raise SpamhausRequestCallError("Forbidden - Authorization denied")
    elif response_object.status_code == 406:
        raise SpamhausRequestCallError("Not Acceptable - The requested Content-Type is not supported")
    elif response_object.status_code == 429:
        raise SpamhausRequestCallError("Too Many Requests - Rate limiting in effect, please decrease query rate")
    elif response_object.status_code == 504:
        raise SpamhausRequestCallError("Gateway timeout - Query could not be successfully sent")
    else:
        return response_object
