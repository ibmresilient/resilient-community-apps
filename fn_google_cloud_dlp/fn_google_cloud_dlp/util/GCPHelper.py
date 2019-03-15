# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
import logging
import os
import tempfile
import PyPDF2

# Import the client library
import google.cloud.dlp
import resilient_lib

log = logging.getLogger(__name__)


class GCPHelper:
    class_vars_loaded = False

    def __init__(self, app_configs, res_client):
        if not self.class_vars_loaded:
            self.load_class_variables(app_configs, res_client)

    @classmethod
    def load_class_variables(cls, app_configs, res_client):
        # TODO: Add connection option by specifying path to keyfile
        cls.dlp_client = google.cloud.dlp.DlpServiceClient()
        cls.project = cls.get_config_option(app_configs=app_configs,
                                            option_name="gcp_project",
                                            optional=False)
        # Default to '#' if config not set.
        cls.masking_character = cls.get_config_option(app_configs=app_configs,
                                                      option_name="gcp_dlp_masking_char",
                                                      optional=True) or '#'
        cls.res_client = res_client


    @staticmethod
    def get_config_option(app_configs, option_name, optional=False, placeholder=None):
        """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
        option = app_configs.get(option_name)
        err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function".format(
            option_name)

        if not option and optional is False:
            raise ValueError(err)
        elif optional is False and placeholder is not None and option == placeholder:
            raise ValueError(err)
        else:
            return option

    @staticmethod
    def get_function_input(inputs, input_name, optional=False):
        """Given input_name, checks if it defined. Raises ValueError if a mandatory input is None"""
        log = logging.getLogger(__name__)
        log.debug("Trying to get function input: %s from %s. optional = %s", input_name, inputs, optional)

        the_input = inputs.get(input_name)

        if the_input is None and optional is False:
            err = "'{0}' is a mandatory function input".format(input_name)
            raise ValueError(err)
        else:
            log.debug("Got function input: %s", input_name)
            return the_input

    @classmethod
    def download_attachment_if_available(cls, artifact_id, attachment_id, gcp_artifact_input, incident_id, log,
                                         task_id):
        attachment_input = None
        attachment_name = None
        # Check whether we are dealing with an attachment or artifact
        if (artifact_id or attachment_id or task_id) and gcp_artifact_input is None:
            log.info("Input appears to be an attachment, downloading from REST API")

            # Get the files data
            attachment_input = resilient_lib.get_file_attachment(
                incident_id=incident_id, artifact_id=artifact_id,
                attachment_id=attachment_id, task_id=task_id, res_client=cls.res_client)

            # Get the files name
            attachment_name = resilient_lib.get_file_attachment_name(
                incident_id=incident_id, artifact_id=artifact_id,
                attachment_id=attachment_id, task_id=task_id, res_client=cls.res_client)

            # Perform some special handling to get the text out of a PDF
            if '.pdf' in attachment_name:
                log.info("Dealing with a PDF")
                attachment_input = cls.extract_text_from_pdf(attachment_input)

        else:
            # We are not dealing with an attachment
            log.debug("Working with an artifact")

        return attachment_input, attachment_name

    @classmethod
    def extract_text_from_pdf(cls, attachment_input):
        extracted_input = u""
        with tempfile.NamedTemporaryFile(mode="w+b", delete=False) as temp_pdf_file:
            try:
                # Write and close tempfile
                temp_pdf_file.write(attachment_input)

                read_pdf = PyPDF2.PdfFileReader(temp_pdf_file)
                number_of_pages = read_pdf.getNumPages()
                full_output = u""
                for page_num in range(0, number_of_pages):
                    page = read_pdf.getPage(page_num)

                    extracted_input += page.extractText()

            finally:
                os.unlink(temp_pdf_file.name)
        return extracted_input

    @classmethod
    def upload_attachment_to_resilient(cls, artifact_id, attachment_id, attachment_name, de_identified_text,
                                       gcp_artifact_input, incident_id, task_id):
        # Check whether we are dealing with an attachment or artifact
        if (artifact_id or attachment_id or task_id) and gcp_artifact_input is None:
            with tempfile.NamedTemporaryFile(mode="w+t", delete=False) as temp_upload_file:
                try:
                    # Write and close tempfile
                    temp_upload_file.write(de_identified_text)
                    temp_upload_file.close()

                    #  Access Resilient API
                    client = cls.res_client

                    # Create POST uri
                    # ..for a task, if task_id is defined
                    if task_id:
                        attachment_uri = '/tasks/{}/attachments'.format(task_id)
                    # ...else for an attachment
                    else:
                        attachment_uri = '/incidents/{}/attachments'.format(incident_id)
                    new_attachment_name = u"""[PII Removed]{}.txt""".format(attachment_name)
                    # POST the new attachment
                    new_attachment = client.post_attachment(attachment_uri, temp_upload_file.name,
                                                            filename=new_attachment_name,
                                                            mimetype='text/plain')

                finally:
                    os.unlink(temp_upload_file.name)


    @classmethod
    def deidentify_with_mask(cls, content_string, info_types, number_to_mask=None):
        """Uses the Data Loss Prevention API to deidentify sensitive data in a
        string by masking it with a character.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            item: The string to deidentify (will be treated as text).
            masking_character: The character to mask matching sensitive data with.
            number_to_mask: The maximum number of sensitive characters to mask in
                a match. If omitted or set to zero, the API will default to no
                maximum.
        Returns:
            None; the response from the API is printed to the terminal.
        """

        # Convert the project id into a full resource id.
        parent = cls.dlp_client.project_path(cls.project)

        # Construct inspect configuration dictionary
        inspect_config = {
            'info_types': [{'name': info_type} for info_type in info_types]
        }

        # Construct deidentify configuration dictionary
        deidentify_config = {
            'info_type_transformations': {
                'transformations': [
                    {
                        'primitive_transformation': {
                            'character_mask_config': {
                                'masking_character': cls.masking_character,
                                'number_to_mask': number_to_mask
                            }
                        }
                    }
                ]
            }
        }

        # Construct item
        item = {'value': content_string}

        # Call the API
        response = cls.dlp_client.deidentify_content(
            parent, inspect_config=inspect_config,
            deidentify_config=deidentify_config, item=item)

        return response, response.item.value

    @classmethod
    def inspect_string(cls, content_string, info_types,
                       custom_dictionaries=None, custom_regexes=None,
                       min_likelihood=None, max_findings=None, include_quote=True):
        """Uses the Data Loss Prevention API to analyze strings for protected data.
        Excepts a string input for inspection but images and other files are also supported by DLP
        Args:
            project: The Google Cloud project id to use as a parent resource.
            content_string: The string to inspect.
            info_types: A list of strings representing info types to look for.
                A full list of info type categories can be fetched from the API.
            min_likelihood: A string representing the minimum likelihood threshold
                that constitutes a match. One of: 'LIKELIHOOD_UNSPECIFIED',
                'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY'.
            max_findings: The maximum number of findings to report; 0 = no maximum.
            include_quote: Boolean for whether to display a quote of the detected
                information in the results.
        Returns:
            None; the response from the API is printed to the terminal.
        """

        # Prepare info_types by converting the list of strings into a list of
        # dictionaries (protos are also accepted).
        info_types = [{'name': info_type} for info_type in info_types]

        # Prepare custom_info_types by parsing the dictionary word lists and
        # regex patterns.
        if custom_dictionaries is None:
            custom_dictionaries = []
        dictionaries = [{
            'info_type': {'name': 'CUSTOM_DICTIONARY_{}'.format(i)},
            'dictionary': {
                'word_list': {'words': custom_dict.split(',')}
            }
        } for i, custom_dict in enumerate(custom_dictionaries)]
        if custom_regexes is None:
            custom_regexes = []
        regexes = [{
            'info_type': {'name': 'CUSTOM_REGEX_{}'.format(i)},
            'regex': {'pattern': custom_regex}
        } for i, custom_regex in enumerate(custom_regexes)]
        custom_info_types = dictionaries + regexes

        # Construct the configuration dictionary. Keys which are None may
        # optionally be omitted entirely.
        inspect_config = {
            'info_types': info_types,
            'custom_info_types': custom_info_types,
            'min_likelihood': min_likelihood,
            'include_quote': include_quote,
            'limits': {'max_findings_per_request': max_findings},
        }

        # Construct the `item`.
        item = {'value': content_string}

        # Convert the project id into a full resource id.
        parent = cls.dlp_client.project_path(cls.project)

        # Call the API.
        response = cls.dlp_client.inspect_content(parent, inspect_config, item)
        findings = list()
        # Print out the results.
        if response.result.findings:
            log.info('Findings were found from DLP Inspection')
            for finding in response.result.findings:
                findings.append({'quote': finding.quote, 'info_type': finding.info_type.name, 'likelihood': finding.likelihood})
                try:
                    if finding.quote:
                        log.debug('Quote: {}'.format(finding.quote))
                except AttributeError:
                    pass
                log.debug('Info type: {}'.format(finding.info_type.name))
                log.debug('Likelihood: {}'.format(finding.likelihood))
        else:
            log.info('No findings were found from DLP Inspection')
        return findings
