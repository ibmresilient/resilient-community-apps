#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fn_resilient_ml.lib.file_manage import FileManage

# Test getting summary from vec file
fm_vec = FileManage(FileManage.DEFAULT_VEC_FILE)
summary = fm_vec.get_summary()
print(summary)
assert(summary is not None)
# Verify that we got the dimension result in summany[5]
assert("Feature dimensions:" in summary[5])
# Verify that we got it right
assert("50" in summary[5])

# Test getting summary from w2v file
fm_w2v = FileManage(FileManage.DEFAULT_NLP_FILE)
summary = fm_w2v.get_summary()
print(summary)
# Verify that we got the dimension result in summany[5]
assert("Feature dimensions:" in summary[5])
# Verify that we got it right
assert("50" in summary[5])
# Verify number of sentences
assert("6625" in summary[6])

# Test getting summary from sif file
fm_sif = FileManage(FileManage.DEFAULT_SIF_FILE)
summary = fm_sif.get_summary()
print(summary)
# Verify number of words read from the sif file
assert("9892" in summary[5])

