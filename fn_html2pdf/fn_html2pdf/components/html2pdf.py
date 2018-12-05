# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import base64
import logging
try:
    import StringIO
except:
    from io import StringIO

try:
    from urllib2 import urlopen
except:
    from urllib.request import urlopen

import weasyprint
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """ Component that implements Resilient function 'utilities_html2pdf'
        This function takes html, either complete "<html> ... </html>" or a fragment "<table> ... </table>" and
        converts it to a pdf image. That image is converted to base64 and returned.
    """

    @function("fn_html2pdf")
    def _fn_html2pdf_function(self, event, *args, **kwargs):
        """Function: function accessible from Resilient to render html to binary pdf format """
        try:
            # Get the function parameters:
            html2pdf_data = kwargs.get("html2pdf_data")  # text
            html2pdf_data_type = kwargs.get("html2pdf_data_type")  # text
            html2pdf_stylesheet = self.get_select_param(kwargs.get("html2pdf_stylesheet")) # CSS data such as page orientation or font family

            log = logging.getLogger(__name__)
            log.info("html2pdf_data: %s", html2pdf_data)
            log.info("html2pdf_data_type: %s", html2pdf_data_type)
            log.info("html2pdf_stylesheet: %s", html2pdf_stylesheet)

            if not (html2pdf_data):
                raise ValueError("Specify html2pdf_data")

            yield StatusMessage("starting...")

            result_pdf = self.render_pdf(html2pdf_data, html2pdf_data_type, html2pdf_stylesheet)

            #  yield StatusMessage("done...")
            log.debug("pdf size {}".format(len(result_pdf)))

            results = {
                "content": base64.b64encode(result_pdf).decode("utf-8")
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()


    def render_pdf(self, input_data, input_data_type, stylesheet):
        '''
        convert html data to pdf
        :param input_data: url to read html or html already
        :param input_data_type: artifact data type. most important when data type is url or uri
        :param stylesheet: used to apply stylesheets for the pdf document. Most useful when showing
            landscape data or font family changes
        :return: binary pdf data
        '''
        if input_data_type and (input_data_type.lower().startswith("url") or input_data_type.lower().startswith("uri")):
            html = weasyprint.HTML(url=input_data)
        else:
            html = weasyprint.HTML(string=input_data)

        if stylesheet:
            css = [weasyprint.CSS(string=stylesheet)]
        else:
            css = None

        return html.write_pdf(None, css)