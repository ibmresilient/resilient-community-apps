#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
#

def make_incident_href(inc_id, org_id, base_url):
    """
    Create a html hyper link for an incident
    :param inc_id: incident ID
    :param org_id: organization ID
    :param base_url: base url for Resilient
    :return:
    """
    LINK_TEMPLATE = '<a href="{url}/#incidents/{inc_id}?orgId={org_id}">{inc_id}</a>'

    return LINK_TEMPLATE.format(url=base_url,
                                inc_id=inc_id,
                                org_id=org_id)


def get_indent_href(inc_id, org_id, base_url, num_return):
    """

    :param inc_id:
    :param org_id:
    :param base_url:
    :param num_return:
    :return:
    """
    incident_ids = get_similar_incidents(inc_id, num_return)
    hrefs = [{"inc_link": make_incident_href(inc["inc_id"], org_id, base_url),
              "similarity": inc["similarity"]} for inc in incident_ids]
    return hrefs


def get_similar_incidents(inc_id, num_return):
    """
    Get incidents similar to input incident (specified by inc_id). Return
    top n (n=num_return) of them
    :param inc_id: incident ID
    :param num_return: number of top incidents to return
    :return: list of incident
    """

    # @TODO need real implementation using NLP later
    similarity = 0.98
    if inc_id > num_return:
        return [{"inc_id": inc_id - i, "similarity": similarity-0.01*i} for i in range(num_return)]
    else:
        return [{"inc_id": inc_id + i, "similarity": similarity-0.01*i} for i in range(num_return)]


def get_artifact_des(inc_id, artifact_json):
    """
    Extract description of artifacts of a given incident
    :param inc_id:
    :param artifact_json:
    :return: String as "{artifact_value} {artifact description} {artifact_value} {artifact description}"
    """
    ret_str = ""

    artifacts = artifact_json.get("results")
    artifacts_for_inc = [artifact for artifact in artifacts if artifact["inc_id"] == inc_id]

    for art in artifacts_for_inc:
        result = art.get("result", None)
        if result:
            ret_str += result.get("value", "") + " "
            ret_str += result.get("description", "").get("content", "") + " "

    return ret_str
