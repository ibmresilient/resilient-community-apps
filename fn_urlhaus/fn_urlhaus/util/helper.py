# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-

from resilient_lib import IntegrationError

CONFIG_DATA_SECTION = "fn_urlhaus"


# convert artifact type to type of API call to make
TYPE_MAP = {
    "DNS Name": "host",
    "IP Address": "host",
    "Malware MD5 Hash": "payload:md5_hash",
    "Malware SHA-256 Hash": "payload:sha256_hash",
    "Server Name": "host",
    "String": "tag",
    "URL": "url"
}


def make_api_call(call_type, base_url, artifact_value, rc, artifact_type=None, api_key=None):
    """
    Function that makes the api call to URLhaus

    :param call_type: A string, either 'lookup' or 'submission'
    :param base_url: The url from the app.config
    :param artifact_value: The artifact value
    :param rc: RequestsCommon object
    :param artifact_type: The artifact type (only needed for a lookup)
    :param api_key: The API Key to URLhaus (only needed for a submission)

    :return: The response of the API call
    :rtype: response
    """

    if call_type == "lookup":
        header = {"Content-Type": "application/x-www-form-urlencoded"}

        lookup_type = TYPE_MAP.get(artifact_type)
        if not lookup_type:
            raise KeyError("Unable to lookup: '{0}'. Supported keys: {1}".format(artifact_type, TYPE_MAP.keys()))

        lookup_type_parts = lookup_type.split(':')

        qry_url = "/".join((base_url, lookup_type_parts[0]))

        payload = {lookup_type_parts[1] if len(lookup_type_parts) == 2 else lookup_type_parts[0]: artifact_value}

        return rc.execute_call_v2(
            method="post",
            url=qry_url,
            headers=header,
            data=payload
        )

    elif call_type == "submission":
        header = {"Content-Type": "application/json"}

        payload = {
            "token": api_key,
            "anonymous": "0",
            "submission": [
                {
                    "url": artifact_value,
                    "threat": "malware_download"
                }
            ]
        }

        return rc.execute_call_v2(
            method="post",
            url=base_url,
            headers=header,
            json=payload
        )

    else:
        raise IntegrationError(u"API call type not supported: {0}".format(call_type))


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
