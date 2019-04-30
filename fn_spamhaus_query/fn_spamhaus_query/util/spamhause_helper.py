# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
import os


class ApikeyError(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return repr(self.message)


class SpamhauseRequestCallError(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return repr(self.error_msg)

def spamhause_call_error(response_object):
    """
    :param response_object: Object returned from request.get call
    :return: on 404 returns empty dict , on 200 returns resp code list
    """
    # Checking for status code
    if response_object.status_code == 400:
        raise SpamhauseRequestCallError("Bad request - there was a syntax error in the request")
    elif response_object.status_code == 401:
        raise SpamhauseRequestCallError("Authorization failed - please verify a valid DQS key was supplied")
    elif response_object.status_code == 403:
        raise SpamhauseRequestCallError("Forbidden - Authorization denied")
    elif response_object.status_code == 406:
        raise SpamhauseRequestCallError("Not Acceptable - The requested Content-Type is not supported")
    elif response_object.status_code == 429:
        raise SpamhauseRequestCallError("Too Many Requests - Rate limiting in effect, please decrease query rate")
    elif response_object.status_code == 504:
        raise SpamhauseRequestCallError("Gateway timeout - Query could not be successfully sent")