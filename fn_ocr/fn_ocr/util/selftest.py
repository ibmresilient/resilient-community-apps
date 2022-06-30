# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-ocr
    resilient-circuits selftest --print-env -l fn-ocr

Return examples:
    return {
        "state": "success",
        "reason": "Successful connection to third party endpoint"
    }

    return {
        "state": "failure",
        "reason": "Failed to connect to third party endpoint"
    }
"""

import logging
import pytesseract

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """

    try:
        version = pytesseract.get_tesseract_version
    except pytesseract.pytesseract.TesseractNotFoundError:
        return {"state": "failure", "reason": "Tesseract Not Found"}

    if version:
        return {"state": "success","reason":f"Version == {version}"}
