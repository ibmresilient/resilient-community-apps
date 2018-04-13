# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
#
# Util functions


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


def fix_dict_value(events):
    """
    When the returned data from QRadar is used to update a datatable, we need to
    convert types like dict/list into strings
    :param events: list of dicts
    :return:
    """
    for event in events:
        # event is a dict
        if isinstance(event, dict):
            for key, value in event.iteritems():
                if not isinstance(value, str):
                    event[key] = str(value)

    return events
