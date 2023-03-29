"""Common JINJA Filters"""

import logging
LOG = logging.getLogger(__name__)


def prefix_filter(val, sep):
    try:
        i = val.index(sep)
    except (ValueError, AttributeError):
        return val
    return val[:i]


def suffix_filter(val, sep):
    try:
        i = val.index(sep) + 1
    except (ValueError, AttributeError):
        return ""
    return val[i:]


def fmt_filter(val, formatstring):
    # A reverse of the built-in 'format' filter
    # that does tuple stuff
    if isinstance(val, dict):
        fmt = formatstring % tuple(val.values())
    else:
        fmt = formatstring % tuple(val)
    return fmt


def split_filter(val, splitter):
    # Split the value
    result = val.split(splitter)
    return result


def dict_filter(val, *args):
    # Convert a list into a dict
    result = {}
    i = iter(val)
    for arg in args:
        result[arg] = i.next()
    return result


def zip_filter(list1, list2):
    # zip lists
    result = zip(list1, list2)
    return result


def artifact_type_filter(val):
    """ JINJA filter to extract artifact type label """
    try:
        type_values = val["artifact"]["fields"]["type"]["values"]
        label = type_values.values()[0]["label"]
    except KeyError as e:
        LOG.exception("Failed to find artifact type label")
        label = ""

    return label


def properties_select_value_filter(properties, name=None, type_info=None):
    """JINJA filter function to replace Action Properties select value ID with String"""
    # Could also use the 'value' filter for these, but this is more efficient
    val = properties.get(name)
    # If the value is a list, produce a list
    if isinstance(val, list):
        # return a list if value is a list
        val_str = [type_info["actioninvocation"]["fields"][name]["values"][str(val_id)]["label"] for val_id in val]
    else:
        val_str = type_info["actioninvocation"]["fields"][name]["values"][str(val)]["label"]

    return val_str
