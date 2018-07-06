# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

#
#   Mapping between x_ibm_security_toxicity and concern we show
#
CONCERN_MAPPING={
    u"very-high": u"Serious",
    u"high": u"Moderate",
    u"low" : u"Minimal",
    u"very-low": u"Negligible"
}

INDICATOR_NAME_TYPE={
    u"IpAddress":u"ipv4-addr",
    u"Url":u"url",
    u"DomainName":u"domain"
}

IBM_TOXICITY = u"x_ibm_security_toxicity"
IBM_RELEVANCE = u"x_ibm_security_relevance"


def get_observables(stix_json, log):
    """
    get observables from stix2 json
    :param stix_json:
    :param log:
    :return:
    """
    objects = stix_json["objects"]
    observables = []
    for obj in objects:
        observable = get_observable(obj, log)
        if observable:
            observables.append(observable)

    return observables


def get_observable_description(stix_obj, log):
    """
    Depends on the type of a stix obj, the information we want to show is hidden in
    different place
    :param stix_obj:
    :param log:
    :return:
    """
    desc = ""
    if stix_obj["type"] == "observed-data":
        #
        # This stix object type is special. We need to dig deeper for
        # the observable we care
        #
        '''
        {
            "objects": {"0": {"type": "ipv4-addr", "value": "83.217.8.127"}},
            "modified": "2018-06-19T15:54:11.000Z", 
            "x_ibm_security_toxicity": "very-high", 
            "type": "observed-data",
            "id": "observed-data--cd36a717-ac23-409f-a6bc-ab078ab1fcef", 
            "last_observed": "2018-06-12T13:10:09.000Z"
        }
        '''
        #
        # so far all the observed-data has only one embedded obj
        # if there is more, log the error
        #
        if len(stix_obj["objects"]) > 1:
            log.error("Observed-data {} has {} objects!".format(stix_obj["id"], str(len(stix_obj["objects"]))))

        # Only look at the first one
        obj = stix_obj["objects"]["0"]
        desc = obj.get("value", obj.get("name", obj.get("hashes", "")))
    elif stix_obj["type"] == u"indicator":
        if stix_obj[u"name"] == u"IpAddress":
            desc = stix_obj[u"pattern"].replace("[ipv4-addr:value='", '').replace("']", '')
        elif stix_obj[u"name"] == u"Url":
            desc = stix_obj[u"pattern"].replace("[url:value='", '').replace("']", '')
        elif stix_obj[u"name"] == u"Malicious URL":
            desc = stix_obj[u"pattern"].replace("[url:value = '", '').replace("']", '')
        elif stix_obj[u"name"] == u"DomainName":
            desc = stix_obj[u"pattern"].replace("[domain-name:value='", '').replace("']", '')
        else:
            # Don't know how to handle the pattern, just put everything
            desc = str(stix_obj[u"pattern"])
            log.debug("Not handling {}".format(str(stix_obj)))
    else:
        desc = stix_obj["name"]

    #
    # Make sure it is a string
    #
    desc_str = str(desc)

    return desc_str


def get_observable_type(stix_obj, log):
    """
    Get observable type for a stix object
    :param stix_obj: stix object input
    :param log:
    :return:
    """
    obj_type = stix_obj[u"type"]
    if obj_type == u"observed-data":
        #
        # so far all the observed-data has only one embedded obj
        # if there is more, log the error
        #
        if len(stix_obj[u"objects"]) > 1:
            log.error("Observed-data {} has {} objects!".format(stix_obj[u"id"], str(len(stix_obj[u"objects"]))))

        # Only look at the first one
        obj = stix_obj[u"objects"]["0"]
        obj_type = obj[u"type"]
    elif obj_type == u"indicator":
        obj_type = INDICATOR_NAME_TYPE.get(stix_obj[u"name"], None)

        if not obj_type:
            #
            # Out INDICATOR_NAME_TYPE mapping is not complete
            #
            log.error("Not handling {}".format(str(stix_obj)))
            obj_type = stix_obj[u"type"]

    return obj_type


def get_observable(stix_obj, log):
    """
    Convert a stix_obj into what we are going to show
    :param stix_obj: dict of a stix obj
    :return: {
        "concern": "Serious" or "Moderate" or "Minimal", or "Negligible",
        "type": stix obj type,
        "Description": name or label of a stix object
    """
    res_obj = {}

    if stix_obj[u"type"] == "relationship":
        return None

    res_obj[u"toxicity"] = stix_obj[IBM_TOXICITY]
    res_obj[u"relevance"] = stix_obj[IBM_RELEVANCE]
    res_obj[u"description"] = get_observable_description(stix_obj, log)
    res_obj[u"type"] = get_observable_type(stix_obj, log)

    return res_obj


def find_object_by_id(stix_objects, obj_id):
    """
    Find a stix obj using obj_id
    :param stix_objects: list of stix2 objects
    :param obj_id: object id to look for
    :return:
    """
    ret_obj = None
    for obj in stix_objects:
        if obj["id"] == obj_id:
            ret_obj = obj
            break
    return ret_obj

