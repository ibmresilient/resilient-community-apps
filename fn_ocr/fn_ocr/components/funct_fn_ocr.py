# -*- coding: utf-8 -*-

"""AppFunction implementation"""


from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError
from resilient_lib import IntegrationError, validate_fields, get_file_attachment, get_file_attachment_metadata, write_file_attachment

import numpy as np
import cv2
import pytesseract
import json
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
        Function: runs OCR on an image in byte string format and returns the relevant results
        Inputs:
            -   fn_inputs.ocr_artifact_id
            -   fn_inputs.ocr_incident_id
            -   fn_inputs.ocr_task_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))
        # self.LOG.debug(fn_inputs)

        incident_id = fn_inputs.ocr_incident_id  # number
        task_id = fn_inputs.ocr_task_id  # number
        artifact_id = fn_inputs.ocr_artifact_id  # number
        attachment_id = None # Need to fix this in SOAR
        confidence_threshold = fn_inputs.ocr_confidence_threshold if fn_inputs.ocr_confidence_threshold else 49
        lang = fn_inputs.ocr_language if fn_inputs.ocr_language else 'eng'

        self.LOG.debug(incident_id, task_id, artifact_id)
        self.LOG.info("incident_id: %s", incident_id)
        self.LOG.info("task_id: %s", task_id)
        self.LOG.info("artifact_id: %s", artifact_id)
        self.LOG.info("OCR Confidence Threshold: %.2f", confidence_threshold)
        self.LOG.info("OCR Lanuage is: %s", lang)

        if incident_id is None:
            raise FunctionError("Error: incident_id must be specified.")
        elif artifact_id is None:
            raise FunctionError("Error: attachment_id or artifact_id must be specified.")
        else:
            yield self.status_message("> Function inputs OK")


        yield self.status_message("> Reading attachment...")

        client = self.rest_client()
        data = get_file_attachment(client, incident_id, artifact_id=artifact_id, task_id=task_id, attachment_id=attachment_id)
        metadata = get_file_attachment_metadata(client, incident_id, artifact_id=artifact_id, task_id=task_id, attachment_id=attachment_id)
        # self.LOG.debug(data)
        
        arr_from_string = np.frombuffer(data, np.uint8)
        img_from_arr = cv2.imdecode(arr_from_string, cv2.IMREAD_COLOR)
        img_rgb = cv2.cvtColor(img_from_arr,cv2.COLOR_BGR2RGB)
        # img_oriented = self.orient_image(img_rgb)
        # img_thresh = self.threshold_image(img_oriented) 

        # detected_text = pytesseract.image_to_string(img_rgb)
        # cleaned_text  = detected_text.strip()
        
        # default page segmentaion is `--psm 3`, which expects a page of text and automatically looks for lines/paragraphs etc 
        detected_data = pytesseract.image_to_data(img_rgb, output_type="data.frame", config=f'-l {lang} --psm 1')
        detected_text = detected_data[detected_data.conf != -1]
        detected_lines = detected_text.groupby('block_num')['text'].apply(list)
        line_conf = detected_text.groupby(['block_num'])['conf'].mean()
        # output_text = "Below are the lines detected by OCR, along with their confidence scores:\n\n" 
        line_dicts = []

        # self.LOG.debug(detected_data)
        # self.LOG.debug(detected_lines)
        # self.LOG.debug(line_conf)

        for text,conf in zip(detected_lines,line_conf):
            text = ' '.join(text).strip()
            
            if text == "": continue

            # self.LOG.debug('\n'*4)
            # self.LOG.debug(text)
            # self.LOG.debug('\n'*4)

            # conf = str(round(conf,2))
            if conf < confidence_threshold: self.LOG.debug("Confidence low, skipping line"); continue

            # output_text += '"' + text + '",' +"\t\t" + f"Confidence: {round(conf,2)}%\n"
            line_dicts.append({"text":text,"confidence":conf})

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        # Note this is only used for demo purposes! Put your own key/value pairs here that you want to access on the Platform
        # results = {"text": detected_text}
        results = line_dicts 
        self.LOG.debug(json.dumps(results, indent=2))

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
