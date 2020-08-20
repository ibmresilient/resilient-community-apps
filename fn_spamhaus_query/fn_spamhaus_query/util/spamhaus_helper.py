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
        headers=auth_header
    )


def format_dict(dict_to_format):
    """
    Function that formats the passed dictionary
    and returns a string

    :param dict_to_format: A dict you want to format

    :return: String of the keys and values in the dict formatted
    :rtype: str
    """
    str_to_rtn = "\n-----------------\n"

    if not dict_to_format:
        str_to_rtn += "NONE\n"

    for (k, v) in dict_to_format.items():

        str_to_rtn += "{0}: {1}\n".format(k, v)

    str_to_rtn += "-----------------\n"

    return str_to_rtn
