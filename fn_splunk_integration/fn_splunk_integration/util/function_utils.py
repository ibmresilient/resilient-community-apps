# -*- coding: utf-8 -*-
#
# Copyright IBM Corp. - Confidential Information
#
import logging
LOG = logging.getLogger(__name__)

class ItemDataError(Exception):
    """ Search failed to execute """
    def __init__(self, msg):
        super(ItemDataError, self).__init__(msg)

def make_query_string(query, params):
    """
    Substitute parameters into the query
    :param query: input query with params
    :param params: values used to substitute
    :return:
    """
    query_string = query

    index = 1
    for param in params:
        if param:
            to_replace = "%%param%d%%" % index
            query_string = query_string.replace(to_replace, param)
        index += 1

    return query_string


def make_item_dict(params):
    """
    Use the params list to build a dict
    :param params: parameter list
    :return: dict
    """
    ret = {}

    list_len = len(params)
    if list_len%2 != 0:
        raise ItemDataError(str(params))

    index = 0
    while index < list_len:
        if params[index]:
            # Allow the value (params[index + 1] here) to be empty (None)?
            # Let Splunk to return an error if it does not support empty value
            ret[params[index]] = params[index + 1]
        else:
            # If key is None, we can not add it to the dictionary
            LOG.debug("The {}th key is None with value {}".format(str(index), str(params[index + 1])))
        index += 2

    return ret
