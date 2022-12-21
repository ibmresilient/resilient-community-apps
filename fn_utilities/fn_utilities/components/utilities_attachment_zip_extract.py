# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

import logging
import os
import tempfile
import zipfile
import base64
import datetime
from fn_utilities.util.utils_common import b_to_s, s_to_b
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from resilient_lib import get_file_attachment


def epoch_millis(zipdate):
    """Produce milliseconds timestamp from a datetime-tuple"""
    epoch = datetime.datetime.utcfromtimestamp(0)
    dtime = datetime.datetime(*zipdate)
    return int((dtime - epoch).total_seconds() * 1000)


class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'attachment_zip_extract"""

    @function("utilities_attachment_zip_extract")
    def _attachment_zip_extract_function(self, event, *args, **kwargs):
        """Function: Extract a file from a zipfile attachment, producing a base64 string."""
        try:
            log = logging.getLogger(__name__)

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number
            file_path = kwargs.get("file_path")  # text
            zipfile_password = kwargs.get("zipfile_password")  # text

            if incident_id is None and task_id is None:
                raise FunctionError("Error: incident_id or task_id must be specified.")
            if attachment_id is None:
                raise FunctionError("Error: attachment_id must be specified.")
            if file_path is None:
                raise FunctionError("Error: file_path must be specified.")

            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("attachment_id: %s", attachment_id)
            log.info("file_path: %s", file_path)

            yield StatusMessage("Reading attachment...")

            client = self.rest_client()
            data = get_file_attachment(client, incident_id, task_id=task_id, attachment_id=attachment_id)

            results = {}
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                try:
                    temp_file.write(data)
                    temp_file.close()
                    # Examine with zip
                    zfile = zipfile.ZipFile(temp_file.name, "r")
                    # Read the metadata, since it may be useful
                    zinfo = zfile.getinfo(file_path)
                    # Don't include zinfo.extra since it's not a string
                    results["info"] = {"filename": zinfo.filename,
                                       "date_time": epoch_millis(zinfo.date_time),
                                       "compress_type": zinfo.compress_type,
                                       "comment": b_to_s(zinfo.comment),
                                       "create_system": zinfo.create_system,
                                       "create_version": zinfo.create_version,
                                       "extract_version": zinfo.extract_version,
                                       "flag_bits": zinfo.flag_bits,
                                       "volume": zinfo.volume,
                                       "internal_attr": zinfo.internal_attr,
                                       "external_attr": zinfo.external_attr,
                                       "header_offset": zinfo.header_offset,
                                       "CRC": zinfo.CRC,
                                       "compress_size": zinfo.compress_size,
                                       "file_size": zinfo.file_size}
                    # Extract the file we want
                    b64data = base64.b64encode(zfile.read(file_path, s_to_b(zipfile_password)))
                    results["content"] = b_to_s(b64data)
                except (KeyError, zipfile.LargeZipFile, zipfile.BadZipfile) as exc:
                    # results["error"] = str(exc)
                    # To help debug, list the contents
                    log.info(zfile.namelist())
                    raise
                finally:
                    os.unlink(temp_file.name)
            # Produce a FunctionResult with the return value
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
