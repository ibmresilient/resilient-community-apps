#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fn_resilient_ml.lib.file_manage import FileManage
import os


def test_vec_file():
    # Test getting summary from vec file, use os to determine absolute path from any directory
    path = os.path.join(os.path.dirname(__file__), FileManage.DEFAULT_VEC_FILE)
    fm_vec = FileManage(path)
    summary = fm_vec.get_summary()
    print(summary)
    assert (summary is not None)
    # Verify that we got the dimension result in summary[5]
    assert ("Feature dimensions:" in summary[5])
    # Verify that we got it right
    assert ("50" in summary[5])


def test_w2v_file():
    # Test getting summary from w2v file, use os to determine absolute path from any directory
    path = os.path.join(os.path.dirname(__file__), FileManage.DEFAULT_NLP_FILE)
    fm_w2v = FileManage(path)
    summary = fm_w2v.get_summary()
    print(summary)
    # Verify that we got the dimension result in summary[5]
    assert ("Feature dimensions:" in summary[5])
    # Verify that we got it right
    assert ("50" in summary[5])
    # Verify number of sentences
    assert ("6625" in summary[6])


def test_sif_file():
    # Test getting summary from sif file, use os to determine absolute path from any directory
    path = os.path.join(os.path.dirname(__file__), FileManage.DEFAULT_SIF_FILE)
    fm_sif = FileManage(path)
    summary = fm_sif.get_summary()
    print(summary)
    # Verify number of words read from the sif file
    assert ("9892" in summary[5])
