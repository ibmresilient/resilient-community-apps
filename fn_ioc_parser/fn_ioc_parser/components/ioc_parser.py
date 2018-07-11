# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
""" This function is for extracting iocs from documents. Please see Readme for more information. """
# Copyright IBM Corp. - Confidential Information

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import tempfile
import logging
from iocp import Parser
import sys
import ast

# This function is for extracting iocs from documents. Please see Readme for more information
class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ioc_parser"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get('fn_ioc_parser')

    # uses the rest service to go to /incidents/<num>/artifacts/<num>/contents
    def getContentsFromArtifact(self, incidentID, artifactID):
        resilientClient = self.rest_client();
        """ 
             Example of call:
            /incidents/2095/artifacts/13/contents 
        """
        api = "/incidents/{}/artifacts/{}/contents".format(incidentID, artifactID)
        response = resilientClient.get_content(api)
        return response

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_ioc_parser", {})

    @function("ioc_parser")
    def _ioc_parser_function(self, event, *args, **kwargs):
        try:
            if kwargs.get("artifactId") is None:
                raise ValueError('artifactId is empty')
            if kwargs.get("incidentId") is None:
                raise ValueError('incidentId is empty')
            if kwargs.get("inputType") is None:
                raise ValueError('inputType is empty')

            # Get the function parameters:
            artifactId = str(kwargs.get("artifactId"))  # number
            incidentId = str(kwargs.get("incidentId"))  # number
            inputType = str(self.get_select_param(kwargs.get("inputType")))  # select, values: "pdf", "txt", "html"

            log = logging.getLogger(__name__)
            log.info("artifactId: %s", artifactId)
            log.info("incidentId: %s", incidentId)
            log.info("inputType: %s", inputType)

            log.info("Http call using rest")
            resp = self.getContentsFromArtifact(incidentId, artifactId)
            log.info("Create temporary output file")
            # create temp output file for rest contents
            temprestoutput = tempfile.NamedTemporaryFile('w', 0, dir=self.options.get("filepath"), delete='false')
            temprestoutput.write(resp)

            log.info("Create temporary redirect file")
            # Create redirected output file. This is where I expect to output the results of the parser
            tempiocoutput = tempfile.NamedTemporaryFile('w', 0, dir=self.options.get("filepath"), delete='false')

            try:
                # Redirect stdout to tempiocoutput
                orig_stdout = sys.stdout
                f = open(tempiocoutput.name, "w")
                sys.stdout = f

                # Parse the iocs
                parser = Parser.Parser(None, inputType, 'false', 'pdfminer', 'json')
                log.info("Call ioc_parser")
                parser.parse(temprestoutput.name)
            except Exception:
                yield FunctionError()
            finally:
                f.close()

            # Read self.filepath and return contents
            inputStream = open(tempiocoutput.name, "r")
            contents = inputStream.readlines()
            results = []
            for line in contents:
                # Convert string to dict.The ioc parser produces lines of json however becasue
                # we write it to a temp file and read it back it gets read in as a string The ioc been read from the file is a string.
                # This safely evaluates the string to make sure it can be tranformed into a dict.
                newline = ast.literal_eval(line.strip())
                results.append(newline)
            log.info("Return results to Resilient")

            yield FunctionResult({"value": results})

        except Exception as err:
            yield FunctionError(err)
        finally:
            # Reset stdout
            sys.stdout = orig_stdout
            log.info("Delete temporary files")

            inputStream.close()
            temprestoutput.close()
            tempiocoutput.close()
