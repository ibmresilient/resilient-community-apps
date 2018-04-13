# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

import os
import json
import logging
import base64
import tempfile
from fn_utilities.util.pdfid import PDFiD, PDFiD2JSON
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'pdfid"""

    @function("utilities_pdfid")
    def _pdfid_function(self, event, *args, **kwargs):
        """Function: """
        try:
            # Get the function parameters:
            base64content = kwargs.get("base64content")  # text

            log = logging.getLogger(__name__)
            log.debug("base64content: %s", base64content)

            yield StatusMessage("Analysing with pdfid...")
            try:
                pdfcontent = base64.b64decode(base64content)

                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    try:
                        temp_file.write(pdfcontent)
                        temp_file.close()
                        xmldoc = PDFiD(temp_file.name)
                        data = json.loads(PDFiD2JSON(xmldoc, True))
                    finally:
                        os.unlink(temp_file.name)

                results = {
                    "header": data[0]["pdfid"]["header"],
                    "isPdf": data[0]["pdfid"]["isPdf"]
                }
                for keyword in data[0]["pdfid"]["keywords"]["keyword"]:
                    results[keyword["name"]] = keyword["count"]
            except Exception as exc:
                results = {
                    "header": None,
                    "isPdf": False,
                    "error": str(exc)
                }

            log.info(json.dumps(results, indent=2))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()