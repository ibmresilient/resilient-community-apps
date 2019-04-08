# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
import os
import tempfile
from docx import Document
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
import xlrd


class IOCParserHelper(object):
    def __init__(self):
        # Resilient Rest Api calls url's
        self.ARTIFACT_META_DATA_URL = "/incidents/{0}/artifacts/{1}"
        self.ARTIFACT_DATA_URL = "/incidents/{0}/artifacts/{1}/contents"
        self.ATTACHMENT_META_DATA_URL = "/incidents/{0}/attachments/{1}"
        self.ATTACHMENT_DATA_URL = "/incidents/{0}/attachments/{1}/contents"
        self.TASK_META_DATA_URL = "/tasks/{0}/attachments/{1}"
        self.TASK_DATA_URL = "/tasks/{0}/attachments/{1}/contents"

    @classmethod
    def extract_text_from_bytes_data(cls, filename, file_data_bytes):
        if filename.find('.pdf') != -1:
            """
            Converting .pdf file data to plain text format
            """
            file_string_data = IOCParserHelper.extract_text_from_pdf(file_data_bytes)
        elif filename.find('.docx') != -1:
            """
            Converting .docx file data to plain text format
            """
            file_string_data = IOCParserHelper.extract_text_from_docx(file_data_bytes)
        elif filename.find('.xls') != -1 or filename.find('.xlsx') != -1:
            """
            Converting .xls/.xlsx file data to plain text format
            """
            file_string_data = IOCParserHelper.extract_text_from_xls_xlsx(file_data_bytes)
        elif filename.split('.')[-1].strip() in ['doc', 'odt', 'ott', 'dot']:
            file_string_data = None
        else:
            file_string_data = file_data_bytes

        if file_string_data:
            file_string_data = str(file_string_data)

        return file_string_data

    @classmethod
    def extract_text_from_pdf(cls, attachment_input):
        """
        Wrapper to convert bytes data in into PDF file and extracting the text data from .pdf file
        :param attachment_input:  attachment Bytes data from resilient api call
        :return:  Text Data
        """
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle)
        page_interpreter = PDFPageInterpreter(resource_manager, converter)

        extracted_input = u""

        with tempfile.NamedTemporaryFile(mode="w+b", delete=False) as temp_pdf_file:
            try:
                # Write and close temp file
                temp_pdf_file.write(attachment_input)

                # Reading the Data from Created Temp File
                for page in PDFPage.get_pages(temp_pdf_file, caching=True, check_extractable=True):
                    page_interpreter.process_page(page)

                extracted_input = fake_file_handle.getvalue()
            finally:
                # close open handles
                converter.close()
                fake_file_handle.close()
                os.unlink(temp_pdf_file.name)
        return extracted_input

    @classmethod
    def extract_text_from_docx(cls, attachment_input):
        """
        Wrapper to convert bytes data in into .docx file and extracting the text data from .doc/.docx file
        :param attachment_input:
        :return: Text Data
        """
        extracted_input = u""
        with tempfile.NamedTemporaryFile(mode="w+b", delete=False) as temp_doc_file:
            try:
                # Write and close temp file
                temp_doc_file.write(attachment_input)
                read_doc = Document(temp_doc_file)
                for paragraph in read_doc.paragraphs:
                    extracted_input += paragraph.text
            finally:
                os.unlink(temp_doc_file.name)
        return extracted_input

    @classmethod
    def extract_text_from_xls_xlsx(cls, attachment_input):
        """
        Wrapper to convert bytes data in into .xls/.xlsx file and extracting the text data from .xls/.xlsx file
        :param attachment_input:
        :return: Text Data
        """
        extracted_input = ""
        with tempfile.NamedTemporaryFile(mode="w+b", delete=False) as temp_doc_file:
            try:
                # Write and close temp file
                temp_doc_file.write(attachment_input)
                workbook_object = xlrd.open_workbook(temp_doc_file.name)
                total_sheets = workbook_object.nsheets
                for sheet_index in range(0, total_sheets):
                    each_sheet_obj = workbook_object.sheet_by_index(sheet_index)
                    total_rows_each_sheet = each_sheet_obj.nrows
                    for row_no in range(0, total_rows_each_sheet):
                        row_data_list = each_sheet_obj.row_values(row_no)
                        for data in row_data_list:
                            extracted_input += str(data) + " "
            finally:
                os.unlink(temp_doc_file.name)
        return extracted_input

    def _correct_ioc_value(self, kind, value):
        _formatted_value = ''
        if kind == 'uri':
            if value.find('https://') != -1 or value.find('http://') != -1:
                _formatted_value = value
            else:
                _formatted_value = "{0}{1}".format('https://', value)
        else:
            _formatted_value = value
        return _formatted_value

    def correct_iocs_format(self, ioc_parser_obj_list):
        """
        A wrapper to remove/correct invalid ioc's generated from IOC parser compatible to resilient artifacts
        :param ioc_parser_obj_list:  IOC Parser Library result object List
        :return:a python dict of result data
        """
        kind_map = {'uri': 'URL', 'IP': 'IP Address', 'md5': 'Malware MD5 Hash', 'sha1': 'Malware SHA-1 Hash',
                    'sha256': 'Malware SHA-256 Hash', 'CVE': 'Threat CVE ID', 'email': 'Email Body',
                    'filename': 'File Name'}
        temp_result_dict = dict()
        for ioc_res_obj in ioc_parser_obj_list:
            if not temp_result_dict.get(kind_map.get(ioc_res_obj.kind)):
                temp_result_dict[kind_map.get(ioc_res_obj.kind)] = []

            temp_result_dict[kind_map.get(ioc_res_obj.kind)].append(
                self._correct_ioc_value(ioc_res_obj.kind, ioc_res_obj.value))
        return temp_result_dict
