#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
#
from fn_resilient_ml.lib.file_manage import FileManage
from fn_resilient_ml.lib.nlp.res_sen2vec import ResSen2Vec
from fn_resilient_ml.lib.nlp.res_sif import ResSIF
from fn_resilient_ml.lib.nlp.res_nlp import ResNLP

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


def get_incident_href(inc_id, org_id, base_url, num_return):
    """

    :param inc_id:
    :param org_id:
    :param base_url:
    :param num_return:
    :return:
    """
    # SIF (Smooth Inverse Frequency) file
    sif = ResSIF
    sif.load_sif(FileManage.DEFAULT_SIF_FILE)

    # Word2Vec NLP model
    nlp = ResNLP
    nlp.load_model(FileManage.DEFAULT_NLP_FILE)

    # sentence to vector
    vec = ResSen2Vec(nlp.word2vec, sif)
    # load cached vectors for old incidents
    vec.load_s2v(FileManage.DEFAULT_VEC_FILE)

    # load pca
    vec.load_pca(FileManage.DEFAULT_PCA_FILE)

    incident_ids = vec.get_closest(inc_id, num_return)
    hrefs = [{"inc_link": make_incident_href(inc["inc_id"], org_id, base_url),
              "similarity": inc["similarity"],
              "keywords": inc["keywords"]} for inc in incident_ids]
    return hrefs

