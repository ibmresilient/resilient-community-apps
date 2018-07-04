# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Helper functions for Bigfix integration with Resilient circuits Functions  """
import logging

# TODO: Check how should be defined this logger
LOG = logging.getLogger(__name__)

__author__ = 'Resilient'


def get_hits(artifact_data, params):
    """Get endpoints with hits from results returned from BigFix.

    :param artifact_data: Data returned from Bigfix
    :param params: Dictionary of Resilient Function parameters
    :return hits: Dictionary of endpoints with hit

    """

    LOG.debug("Filtering incident %s with data for artifact %s", params["incident_id"], params["artifact_id"])

    hits = []
    for d in artifact_data:
        if (d["failure"] == 0 or d["failure"] == "False") and d["result"] == "True":
            hits.append(d)
    # if no hits result will be an empty list.
    if hits:
        LOG.info("Detected %s hits." % (len(hits)))
    else:
        LOG.info("Detected no hits")

    return hits