# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from lxml import etree
import os
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_xml_transformation"""

    XML_DIR = "xml_stylesheet_dir"

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_utilities", {})
        # confirm that our required parameter exists and is a directory
        if not (self.options.get(FunctionComponent.XML_DIR) and os.path.isdir(self.options.get(FunctionComponent.XML_DIR))):
            raise ValueError("missing or incorrectly specified configuration property: {}".format(FunctionComponent.XML_DIR))

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_utilities", {})

    @function("utilities_xml_transformation")
    def _utilities_xml_transformation_function(self, event, *args, **kwargs):
        """Function: Perform a transformation of an xml document based on a given stylesheet"""

        try:
            # Get the function parameters:
            xml_source = kwargs.get("xml_source")  # text
            xml_stylesheet = kwargs.get("xml_stylesheet")  # text

            validate_fields(("xml_source", "xml_stylesheet"), kwargs)

            log = logging.getLogger(__name__)
            log.info("xml_source: %s", xml_source)
            log.info("xml_stylesheet: %s", xml_stylesheet)

            # get the stylesheet
            stylesheet = os.path.join(self.options.get(FunctionComponent.XML_DIR), xml_stylesheet)
            if not (os.path.exists(stylesheet) and os.path.isfile(stylesheet)):
                raise ValueError("stylesheet file not found: {}".format(stylesheet))

            yield StatusMessage("starting...")

            parser = etree.XMLParser(ns_clean=True, recover=True, encoding="utf-8")
            # read xsl file
            xsl = open(stylesheet, mode="rb").read()
            xsl_root = etree.fromstring(xsl, parser=parser)

            transform = etree.XSLT(xsl_root)

            # read xml
            xml_root = etree.fromstring(xml_source.encode("utf-8"), parser=parser)

            # transform xml with xslt
            transformation_doc = transform(xml_root)

            # return transformation result
            result = etree.tostring(transformation_doc)

            results = {
                "content": result.decode("utf-8")
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()


def validate_fields(fieldList, kwargs):
    """
    ensure required fields are present. Throw ValueError if not
    :param fieldList:
    :param kwargs:
    :return: no return
    """
    for field in fieldList:
            if field not in kwargs or kwargs.get(field) == '':
                raise ValueError('Required field is missing or empty: '+field)