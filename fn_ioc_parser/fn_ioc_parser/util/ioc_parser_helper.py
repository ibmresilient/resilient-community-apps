import os
import tempfile
from docx import Document
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

class IOCParserHelper(object):
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
                # Write and close tempfile
                temp_pdf_file.write(attachment_input)
                print(temp_pdf_file.name)

                # Reading the Data from Created Temp File
                for page in PDFPage.get_pages(temp_pdf_file, caching=True, check_extractable=True):
                    page_interpreter.process_page(page)

                extracted_input = fake_file_handle.getvalue()

                # close open handles
                converter.close()
                fake_file_handle.close()
            finally:
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
                # Write and close tempfile
                temp_doc_file.write(attachment_input)
                read_doc = Document(temp_doc_file)
                print("Docuement file name - ", temp_doc_file.name)
                for paragraph in read_doc.paragraphs:
                    extracted_input += paragraph.text
                print("#################", extracted_input)
            except:
                os.unlink(temp_doc_file.name)
            finally:
                os.unlink(temp_doc_file.name)
        return extracted_input

