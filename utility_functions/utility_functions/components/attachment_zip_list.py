# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import tempfile
import zipfile
import os
import datetime
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'attachment_zip_list"""

    @function("attachment_zip_list")
    def _attachment_zip_list_function(self, event, *args, **kwargs):
        """Function: For a zipfile attachment, return a list of its contents."""
        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("attachment_id: %s", attachment_id)

            if not incident_id:
                raise FunctionError("Error: Incident ID must be specified.")
            if not attachment_id:
                raise FunctionError("Error: Attachment ID must be specified.")

            yield StatusMessage("Reading attachment...")
            client = self.rest_client()
            metadata_uri = "/incidents/{}/attachments/{}".format(incident_id, attachment_id)
            metadata = client.get(metadata_uri)
            data_uri = "/incidents/{}/attachments/{}/contents".format(incident_id, attachment_id)
            data = client.get_content(data_uri)

            def epoch_millis(zipdate):
                epoch = datetime.datetime.utcfromtimestamp(0)
                dt = datetime.datetime(*zipdate)
                return int((dt - epoch).total_seconds() * 1000)

            result = {}
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                try:
                    temp_file.write(data)
                    temp_file.close()
                    # Examine with zip
                    zf = zipfile.ZipFile(temp_file.name, "r")
                    result["namelist"] = zf.namelist()
                    result["infolist"] = [{"filename": zi.filename,
                                           "date_time": epoch_millis(zi.date_time),
                                           "compress_type": zi.compress_type,
                                           "comment": zi.comment,
                                           "extra": zi.extra,
                                           "create_system": zi.create_system,
                                           "create_version": zi.create_version,
                                           "extract_version": zi.extract_version,
                                           "flag_bits": zi.flag_bits,
                                           "volume": zi.volume,
                                           "internal_attr": zi.internal_attr,
                                           "external_attr": zi.external_attr,
                                           "header_offset": zi.header_offset,
                                           "CRC": zi.CRC,
                                           "compress_size": zi.compress_size,
                                           "file_size": zi.file_size}
                                          for zi in zf.infolist()]
                except (zipfile.LargeZipFile, zipfile.BadZipfile) as exc:
                    result["error"] = str(exc)
                finally:
                    os.unlink(temp_file.name)
            # Produce a FunctionResult with the return value
            yield FunctionResult(result)
        except Exception:
            yield FunctionError()