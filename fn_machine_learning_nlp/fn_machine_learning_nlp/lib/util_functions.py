#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
#
import os
from datetime import datetime
from fn_machine_learning_nlp.lib.file_manage import FileManage
from fn_machine_learning_nlp.lib.nlp.res_sen2vec import ResSen2Vec
from fn_machine_learning_nlp.lib.nlp.res_sif import ResSIF
from fn_machine_learning_nlp.lib.nlp.res_nlp import ResNLP
from fn_machine_learning_nlp.lib.res_utils import ResUtils

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


def get_incident_href(nlp_str, res_client, num_return, model_path, inc_id):
    """
    For the given nlp_str, find the top num_return (old) incidents that
    are similar to it (from NLP point of view).

    Generate the href links for each of those returned incident as well.

    :param nlp_str:     input sentence to do nlp search
    :param res_client:  resilient client
    :param num_return:  number of closest incidents to return
    :param model_path:  (required) Specify the path to find the saved model
    :param inc_id:      (new) incident id. Don't include this in return.
    :return:
    """
    file_path = model_path
    if not file_path.endswith('/'):
        file_path += '/'

    sif_file = FileManage.DEFAULT_SIF_FILE
    w2v_file = FileManage.DEFAULT_NLP_FILE
    vec_file = FileManage.DEFAULT_VEC_FILE
    pca_file = FileManage.DEFAULT_PCA_FILE

    model_files = os.listdir(model_path)
    # If a custom model name was used to build, the specific files that make up the model can be identified by
    # the second half of the filename which is standardized depending on the type of file it is
    for filename in model_files:
        if "-sif.pkl" in filename:
            sif_file = filename
        elif "-w2v.txt" in filename:
            w2v_file = filename
        elif "-vec.json" in filename:
            vec_file = filename
        elif "-pca.json" in filename:
            pca_file = filename

    # SIF (Smooth Inverse Frequency) file
    sif = ResSIF()
    sif.load_sif(os.path.join(file_path, sif_file))

    # Word2Vec NLP model
    nlp = ResNLP()
    nlp.load_model(os.path.join(file_path, w2v_file))

    # sentence to vector
    vec = ResSen2Vec(nlp.word2vec, sif)
    # load cached vectors for old incidents
    vec.load_s2v(os.path.join(file_path, vec_file))

    # load pca
    vec.load_pca(os.path.join(file_path, pca_file))

    # find the highest inc id in the vec file. Note that the vec file contains
    # all the incidents at the point the model is built. We want to find incidents
    # created after that.
    highest_id = vec.get_highest_inc_id()
    res_utils = ResUtils(resclient=res_client)
    other_incidents = res_utils.get_incidents_after(highest_id)

    incident_ids = vec.get_closest(nlp_str, other_incidents, num_return, inc_id)
    hrefs = [{"inc_link": make_incident_href(inc["ref"], res_client.org_id, res_client.base_url),
              "similarity": inc["sim"],
              "keywords": inc["keywords"]} for inc in incident_ids]
    return hrefs

def get_cur_time():
    cur_time = datetime.now()
    return cur_time.strftime("%Y-%m-%d, %H:%M:%S")
