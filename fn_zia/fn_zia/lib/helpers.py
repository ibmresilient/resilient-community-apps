# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Helper functions for Resilient circuits Functions supporting ZIA """
from __future__ import print_function
import logging
import re

LOG = logging.getLogger(__name__)


def is_regex(regex_str):
    """"Test if sting is a correctly formed regular expression.

    :param regex_str: Regular expression string.
    :return: Boolean.
    """
    try:
        re.compile(regex_str)
        return True
    except re.error:
        return False

def filter_by_category(result, name_filter=None):
    """ Filter by category name the result returned from ZIA.

    :param result: Dict of categories from ZIA response.
    :param name_filter: A regex string used to filter result.
    :return: Filtered result.
    """
    categories = result.get("categories")
    regex = r'{}'.format(name_filter)
    # Add category total and filtered counts to result.
    result.update({
        "category_counts": {
            "total": len(categories),
            "filtered": len(categories)
        }
    })

    if name_filter and categories:
        filtered_categories = [c for c in categories if re.search(regex, c["configuredName"], re.I)]
        result["categories"] = filtered_categories
        result["category_counts"]["filtered"] = len(filtered_categories)

    return result

def filter_by_url(result, url_filter=None, url_type=None):
    """ Filter by url name the results returned from ZIA.

    :param result: Dict of category from ZIA response.
    :param url_filter: A regex string used to filter result.
    :param url_type: Type of url in ZIA response, result i.e. "urls", "whitelistUrls", "blacklistUrls", .
    :return: Filtered result.
    """
    if not url_type:
        raise ValueError("The 'url_type' parameter is not set correctly.")

    urls = result.get(url_type)
    regex = r'{}'.format(url_filter)

    result["url_counts"] = {}

    # Add url total and filtered counts to result.
    urls = result.get(url_type)
    result.update({
        "url_counts": {
            "total": len(urls),
            "filtered": len(urls)
        }
    })

    if url_filter and urls:
        filtered_urls = [u for u in urls if re.search(regex, u, re.I)]
        if filtered_urls:
            result[url_type] = filtered_urls
            result["url_counts"]["filtered"] = len(filtered_urls)
        else:
            result = None

    return result
