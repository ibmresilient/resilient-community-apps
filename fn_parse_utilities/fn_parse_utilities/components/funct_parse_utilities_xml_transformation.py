# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
from fn_parse_utilities.components.funct_parse_utilities_email_parse import PACKAGE_NAME
from lxml import etree
from defusedxml import lxml as defused_etree
from os.path import isdir, join, exists, isfile
from resilient_lib import validate_fields, get_file_attachment
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

LOG = getLogger(__name__)

PACKAGE_NAME = "fn_parse_utilities"

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'utilities_xml_transformation"""

    XML_DIR = "xml_stylesheet_dir"

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("parse_utilities_xml_transformation")
    def _utilities_xml_transformation_function(self, event, *args, **kwargs):
        """Function: Perform a transformation of an xml document based on a given stylesheet"""

        try:
            # Get the function parameters:
            xml_source = kwargs.get("parse_utilities_xml_source")  # text
            xml_stylesheet = kwargs.get("parse_utilities_xml_stylesheet")  # text

            validate_fields(("parse_utilities_xml_stylesheet"), kwargs)
            # Confirm that our required parameter exists and is a directory
            if not (self.options[FunctionComponent.XML_DIR] and isdir(self.options[FunctionComponent.XML_DIR])):
                raise ValueError("Missing or incorrectly specified configuration property: {}".format(FunctionComponent.XML_DIR))

            LOG.info("xml_source: %s", xml_source)
            LOG.info("xml_stylesheet: %s", xml_stylesheet)

            if not xml_source:
                res_client = self.rest_client()
                xml_source = get_file_attachment(
                    res_client=res_client,
                    incident_id=kwargs.get("parse_utilities_incident_id"),
                    artifact_id=kwargs.get("parse_utilities_artifact_id"),
                    task_id=kwargs.get("parse_utilities_task_id"),
                    attachment_id=kwargs.get("parse_utilities_attachment_id")
                )
            else:
                xml_source = xml_source.encode("utf-8")

            # Get the stylesheet
            stylesheet = join(self.options.get(FunctionComponent.XML_DIR), xml_stylesheet)
            if not (exists(stylesheet) and isfile(stylesheet)):
                raise ValueError("Stylesheet file not found: {}".format(stylesheet))

            yield StatusMessage("Starting...")

            parser = etree.XMLParser(ns_clean=True, recover=True, encoding="utf-8")
            # Read xsl file
            xsl = open(stylesheet, mode="rb").read()
            xsl_root = defused_etree.fromstring(xsl, parser=parser)

            transform = etree.XSLT(xsl_root)

            # Read xml
            xml_root = defused_etree.fromstring(xml_source, parser=parser)

            # Transform xml with xslt
            transformation_doc = transform(xml_root)

            # Return transformation result
            result = etree.tostring(transformation_doc)

            results = {
                "content": result.decode("utf-8")
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
