# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
""" Helper functions for SOAR Functions supporting Bigfix integration """

from __future__ import print_function
from os import unlink
from logging import getLogger
from tempfile import NamedTemporaryFile

LOG = getLogger(__name__)
PACKAGE_NAME = "fn_bigfix"

def create_attachment(rest_client, file_name, file_content, params):
    """"Add file as SOAR incident attachment.
    :param rest_client: SOAR Rest client
    :param file_name: Name of file to add as attachment
    :param file_content: Content of file to add as attachment
    :param params: SOAR Function parameters (dict)
    :return att_report: Return result (dict) of SOAR post attachment request
    """

    temp_file_obj = NamedTemporaryFile('w', delete=False, encoding="utf8")

    # Create the temporary file save results in json format.
    with temp_file_obj as temp_file:
        temp_file.write(file_content)
        temp_file.flush()
        try:
            # Post file to SOAR
            att_report = rest_client.post_attachment(f"/incidents/{params['incident_id']}/attachments",
                                                     temp_file.name,
                                                     file_name,
                                                     "text/plain",
                                                     "")
            LOG.info(f"New attachment added to incident {params['incident_id']}")
        except Exception as err:
            raise err
        finally:
            unlink(temp_file.name)

    return att_report
