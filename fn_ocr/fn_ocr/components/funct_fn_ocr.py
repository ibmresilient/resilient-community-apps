# -*- coding: utf-8 -*-

"""AppFunction implementation"""


from email.mime import base
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError 
from resilient_lib import IntegrationError, validate_fields, get_file_attachment, get_file_attachment_metadata, write_file_attachment

import base64
import cv2
import json
import numpy as np
import pytesseract
import pandas as pd

PACKAGE_NAME = "fn_ocr"
FN_NAME = "fn_ocr"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_ocr'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: runs OCR on an image in byte string format and returns a list with one {"text":text,"confidence":conf} per line
        Inputs:
            -   fn_inputs.ocr_artifact_id
            -   fn_inputs.ocr_incident_id
            -   fn_inputs.ocr_task_id
            -   fn_inputs.ocr_attachment_id
            -   fn_inputs.ocr_confidence_threshold
            -   fn_inputs.ocr_language
            -   fn_inputs.ocr_base64 
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        incident_id = getattr(fn_inputs,"ocr_incident_id",None)
        attachment_id = getattr(fn_inputs,"ocr_attachment_id",None)
        task_id = getattr(fn_inputs,"ocr_task_id", None)
        artifact_id = getattr(fn_inputs,"ocr_artifact_id", None)
        confidence_threshold = getattr(fn_inputs,"ocr_confidence_threshold", 50)
        lang = getattr(fn_inputs,"ocr_language", "eng")
        base64_string = getattr(fn_inputs,"ocr_base64", None)

        self.LOG.info("incident_id: %s", incident_id)
        self.LOG.info("artifact_id: %s", artifact_id)
        self.LOG.info("attachment_id: %s", attachment_id) 
        self.LOG.info("task_id: %s", task_id)
        self.LOG.info("OCR Confidence Threshold: %.2f", confidence_threshold)
        self.LOG.info("OCR Language is: %s", lang)
        # self.LOG.info("OCR Base64 Input is: %s", base64_string)

        if incident_id is None:
            raise FunctionError("Error: incident_id must be specified.")
        elif artifact_id is None and base64_string is None and attachment_id is None:
            raise FunctionError("Error: no input to the function! Could not find artifact id, attachment id, or a base64 string")
        elif sum(bool(x) for x in [artifact_id,base64_string,attachment_id]) > 1: # checks to see if we have more than one of our inputs
            raise FunctionError("Too many inputs! Please choose only one of: Artifact ID, Attachment ID, Base64 String")
        else:
            yield self.status_message("> Function inputs OK")


        client = self.rest_client()
        if base64_string:
            data = base64.b64decode(base64_string)
        else:
            data = get_file_attachment(client, incident_id, artifact_id=artifact_id, task_id=task_id, attachment_id=attachment_id)

        arr_from_string = np.frombuffer(data, np.uint8) # data comes as a bytestring, need to read it into an array
        img_from_arr = cv2.imdecode(arr_from_string, cv2.IMREAD_COLOR) # use cv2 to open the array as a color image
        img_rgb = cv2.cvtColor(img_from_arr,cv2.COLOR_BGR2RGB) # open-cv (cv2) defaults to BGR colors, we convert just in case
        
        # page segmentation mode is set to --psm 1 to account for orientation 
        detected_data = pytesseract.image_to_data(img_rgb, output_type="data.frame", config=f'-l {lang} --psm 1') # runs Tesseract OCR
        detected_text = detected_data[detected_data.conf != -1] # Drops empty entries in the dataframe
        detected_lines = detected_text.groupby('block_num')['text'].apply(list) # turn the dataframe into a list of lines
        line_conf = detected_text.groupby(['block_num'])['conf'].mean() # gets an equally long list as above, but of average confidences

        line_dicts = []


        for text,conf in zip(detected_lines,line_conf):
            text = ' '.join(text).strip() # strip \n and similar characters so we can control the formatting ourselves
            
            if text == "":self.LOG.debug("Line Empty, Skipping"); continue # if an empty line is found, continue 
            if conf < confidence_threshold: self.LOG.debug("Confidence Low, Skipping"); continue # if confidence of current line is below threshold, continue

            line_dicts.append({"text":text,"confidence":conf})

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        results = line_dicts 
        self.LOG.debug(json.dumps(results, indent=2))

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
