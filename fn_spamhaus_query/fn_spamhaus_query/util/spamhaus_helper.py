# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

CONFIG_DATA_SECTION = 'fn_spamhaus_query'


class SpamhausRequestCallError(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return repr(self.error_msg)


def make_api_call(base_url, api_key, search_resource, qry, rc):
    """
    Function that makes the api call to IP Void

    :param base_url: The spamhaus_wqs_url from the app.config
    :param api_key: The API Key to IP Void read from the app.config file
    :param search_resource: The dataset to search
    :param qry: The artifact value
    :param rc: RequestsCommon object

    :return: The response of the API call
    :rtype: response
    """

    auth_header = {'Authorization': 'Bearer {}'.format(api_key)}

    qry_url = base_url + "/".join([str(search_resource), str(qry)])

    return rc.execute_call_v2(
        method="get",
        url=qry_url,
        headers=auth_header,
        callback=spamhaus_call_error
    )


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
