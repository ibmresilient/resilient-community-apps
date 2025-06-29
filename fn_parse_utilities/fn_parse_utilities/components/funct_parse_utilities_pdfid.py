# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

from os import unlink
from json import loads, dumps
from logging import getLogger
from base64 import b64decode
from tempfile import NamedTemporaryFile
from resilient_lib import SOARCommon
from pdfid.pdfid import PDFiD, PDFiD2JSON
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError

log = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'pdfid"""

    @function("parse_utilities_pdfid")
    def _pdfid_function(self, event, *args, **kwargs):
        """Function: """
        try:

            # Get the function parameters:
            base64content = kwargs.get("parse_utilities_base64content")  # text
            filename = kwargs.get("parse_utilities_filename")  # text
            incident_id = kwargs.get("parse_utilities_incident_id")  # number
            task_id = kwargs.get("parse_utilities_task_id")  # number
            attachment_id = kwargs.get("parse_utilities_attachment_id")  # number
            artifact_id = kwargs.get("parse_utilities_artifact_id")  # number

            if base64content == None:
                client = self.rest_client()
                soar_common = SOARCommon(client)
                filename, base64content = soar_common.get_case_attachment(incident_id, artifact_id, task_id, attachment_id)

            log.debug("base64content: %s", base64content)

            yield StatusMessage("Analyzing with pdfid...")
            try:
                pdfcontent = b64decode(base64content)

                with NamedTemporaryFile(delete=False) as temp_file:
                    try:
                        temp_file.write(pdfcontent)
                        temp_file.close()
                        xmldoc = PDFiD(temp_file.name)
                        data = loads(PDFiD2JSON(xmldoc, True))
                    finally:
                        unlink(temp_file.name)

                results = {
                    "filename": filename,
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

            log.info(dumps(results, indent=2))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
