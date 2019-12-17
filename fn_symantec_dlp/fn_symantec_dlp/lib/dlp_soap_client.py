# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
# pragma pylint: disable=unused-argument, no-self-use
import datetime
import logging
import traceback
import uuid
import os



import zeep
from zeep.cache import InMemoryCache
from jinja2 import Environment, PackageLoader

from requests import Session
from requests.auth import HTTPBasicAuth, AuthBase
from requests.exceptions import HTTPError, Timeout
from resilient_lib import validate_fields

LOG = logging.getLogger(__name__)

DEFAULT_TEMPLATES_PATH = os.path.join("data", "templates")
DEFAULT_JINJA_UPDATE_TEMPLATE = "_dlp_update_incident_xml_template.jinja2"


class SymantecAuth(AuthBase):
    """SymantecAuth a class which inherits from requests.AuthBase,
    if the URL starts with our DLP Instance hostname, add Basic Authentication to requests
    otherwise send a request without credentials.

    Needed due to a call to www.w3.org/2005/05/xmlmime which fails if credentials are passed

    :param AuthBase: [description]
    :type AuthBase: [type]
    :return: [description]
    :rtype: [type]
    """
    def __init__(self, username, password, host):
        self.basic = HTTPBasicAuth(username, password)
        self.host = host

    def __call__(self, r):
        if r.url.startswith(self.host):
            return self.basic(r)
        else:
            # In some cases the call to w3.org can fail with http
            # If we encounter a http url, replace with https
            if r.url.startswith("http"):
                r.url = r.url.replace("http", "https")
            return r


class DLPSoapClient():
    """DLPSoapClient a class which is used to interface with the Incident and Reporting API for Symantec DLP
    Contains methods which encapsulate SOAP calls to your DLP Instance

    Takes config values such as the host through an app_configs dict exposed in the init.
    DLPSoapClient has a number of class variables which are shared among invocations
    """
    class_vars_loaded = False

    def __init__(self, app_configs):
        """__init__ setup the DLPSOAPClient;
        loading in the parameters from app_configs
        then initialise a soap_client with the details

        :param app_configs: a dictionary containing key-value pairs used for
        setting up a client with Symantec DLP.
        :type app_configs: dict
        """
        if not self.class_vars_loaded:
            self.load_class_variables(app_configs)

    @classmethod
    def load_class_variables(cls, app_configs):
        """load_class_variables loads in the app_configs dict
        and assigned each value as a class variable.
        After loading, a zeep SOAP Client is created with our credentials

        :param app_configs: a dictionary containing key-value pairs used for
        setting up a client with Symantec DLP.
        :type app_configs: dict
        """
        cls.is_connected = False # Set is_connected to false initially
        
        validate_fields(['sdlp_host', 'sdlp_wsdl', 'sdlp_username', 'sdlp_password', 'sdlp_savedreportid', 'sdlp_incident_endpoint'], kwargs=app_configs)

        LOG.debug("Validated Mandatory app.configs for DLPSoapClient")

        cls.host = app_configs.get('sdlp_host')
        cls.wsdl = app_configs.get('sdlp_wsdl')
        # Gather the DLP User Name
        cls.dlp_username = app_configs.get('sdlp_username')
        # Gather the DLP User Password
        cls.dlp_password = app_configs.get('sdlp_password')

        # Gather the DLP Cert
        cls.dlp_cert = app_configs.get('sdlp_cafile', False)

        # Gather the DLP Saved Report ID
        cls.dlp_saved_report_id = app_configs.get('sdlp_savedreportid')

        # Gather the DLP Incident Endpoint
        cls.sdlp_incident_endpoint = app_configs.get('sdlp_incident_endpoint')

        cls.session = Session()
        # Use DLP Cert if provided or if None, set verify to false
        cls.session.verify = cls.dlp_cert
        cls.session.auth = SymantecAuth(cls.dlp_username, cls.dlp_password, cls.host)


        mimefile_abs_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.path.pardir, "data", "xmlmime.xml")
        # If the Xmlmime file was provided
        if os.path.isfile(mimefile_abs_path):
            LOG.info("A Local XML file was found in the data directory, %s \n Loading this into the cache", mimefile_abs_path)
            # Open it and add it to a Cache
            with open(mimefile_abs_path, mode="rb") as f:
                filecontent = f.read()
                dlp_cache = InMemoryCache()
                dlp_cache.add("http://www.w3.org/2005/05/xmlmime", filecontent)
                dlp_cache.add("https://www.w3.org/2005/05/xmlmime", filecontent)
            # Setup Transport with credentials and the cached mimefile
            cls.transport = zeep.Transport(session=cls.session, cache=dlp_cache)
        else:
            # Setup Transport with our credentials
            cls.transport = zeep.Transport(session=cls.session)

        try: # Try to create a soap_client from the wsdl and transport
            cls.soap_client = zeep.Client(wsdl=cls.wsdl, transport=cls.transport)
        except Exception as caught_exc: # We got an error when setting up a client, catch and release the error in logs so circuits doesn't stop
            # Put the traceback into DEBUG
            LOG.debug(traceback.format_exc())
            # Log the Connection error to the user
            LOG.error(u"Problem: %s", repr(caught_exc))
            LOG.error(u"[Symantec DLP] Encountered an exception when setting up the SOAP Client")
            
        else: # No connection error, client is setup with the URL. Allow the poller to be setup
            cls.is_connected = True
        cls.class_vars_loaded = True

    @classmethod
    def incident_list(cls, saved_report_id=0, incident_creation_date_later_than=datetime.datetime.now()):
        """incident_list API Call to gather a list of incidents from a saved report.

        :param saved_report_id: the ID of a saved report,
        defaults to 0 which means if not provided no incidents will be found, 
        :type saved_report_id: int, optional
        :param incident_creation_date_later_than: Only incidents that were created after the incidentCreationDateLaterThan date will be returned, defaults to datetime.datetime.now()
        :type incident_creation_date_later_than: datetime, required
        :return: A list of incidentIds and incidentLongIds
        :rtype: [type]
        """
        incident_list = cls.soap_client.service.incidentList(
            savedReportId=saved_report_id,
            incidentCreationDateLaterThan=incident_creation_date_later_than)

        return incident_list

    @classmethod
    def incident_detail(cls, incident_id=None):
        """incident_detail API Call to gather the details for a specified incident
        Even though incidentLongId isin't exposed in the function call,
        that is usable for a query also

        :param incident_id: the ID of the incident to retreive, defaults to None
        :type incident_id: [type], optional
        :return: [description]
        :rtype: [type]
        """
        # Strict mode off to avoid an XMLParseError for custom attributes that are not expected
        with cls.soap_client.settings(strict=False):

            incident_detail = cls.soap_client.service.incidentDetail(incidentId=incident_id)

            return incident_detail

    @classmethod
    def incident_binaries(cls, incident_id=None, include_original_message=False, include_all_components='?'):
        """incident_binaries API Call to gather the binaries (Attachments) for an incident.

        :param incident_id: [description], defaults to None
        :type incident_id: [type], optional
        :param include_original_message:  defaults to False
        :type include_original_message: bool, optional
        :param include_all_components: optional element which indicates whether the Web Service should include all message components
        defaults to '?'
        :type include_all_components: str, optional
        """
        binaries = cls.soap_client.service.incidentBinaries(
            incidentId=incident_id,
            includeOriginalMessage=include_original_message,
            includeAllComponents=include_all_components)
        return binaries

    @classmethod
    def incident_status(cls):
        """incident_status Used to retreive the incident status

        :return: [description]
        :rtype: incidentStatusList Object
        """
        status = cls.soap_client.service.listIncidentStatus()

        return status

    @classmethod
    def list_custom_attributes(cls):
        """list_custom_attributes return a list of all custom attribute names

        :return: [description]
        :rtype: list
        """
        custom_attributes = cls.soap_client.service.listCustomAttributes()

        return custom_attributes

    @classmethod
    def update_incident(cls, incident_id, **kwargs):        
        headers = {'content-type': 'text/xml'}
        try:
            update_payload = {
                "batchId":"_{}".format(uuid.uuid4()),
                "dlp_id":incident_id
            }
            # Originally was getting an issue trying to pass **kwargs to the jinja template on py2
            # Now we prepare a dict with our custom values and then update that dict with the kwargs
            update_payload.update(kwargs)

            default_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, "data", "templates")
            rendered_xml = cls.map_values(
                template_file=os.path.abspath(default_dir + "/_dlp_update_incident_xml_template.jinja2"),
                message_dict=update_payload)

            response = cls.session.post(cls.sdlp_incident_endpoint,
                                        data=rendered_xml.encode('utf-8'), headers=headers)

            # Catch any request issues and raise them
            response.raise_for_status() 
            # If the request returns with a success code but does not have a SUCCESS status, return an error
            if b"<statusCode>SUCCESS</statusCode>" not in response.content:
                raise ValueError("API Call did not Return a Success code. Check that the SDLP incident has not been removed.")
            LOG.info("Sent new update to DLP Incident %s", incident_id)

            return response
        except (HTTPError, Timeout) as upload_ex: # Catch any Fault or ValidationError, other Exceptions should be caught
            LOG.debug(traceback.format_exc())
            # Log the Connection error to the user
            LOG.error(u"Problem: %s", repr(upload_ex))
            LOG.error(u"[Symantec DLP] Encountered an exception when sending an UpdateRequest to DLP.")

        
    @staticmethod
    def map_values(template_file, message_dict):
        """Map_Values is used to :
        Take in a forwarded Event from DLP
        Import a Jinja template
        Map Event data to a new Incidents data including artifact data"""
        LOG.debug("Attempting to map message to an IncidentDTO. Message provided : %d", message_dict)


        # Setup the Jinja2 Environment with path to Jinja2 templates
        # Uses PackageLoader to load all the templates in the templates dir
        jinja_env = Environment(
            loader=PackageLoader("fn_symantec_dlp", DEFAULT_TEMPLATES_PATH),
            trim_blocks=True # Used to get rid of line endings that we may put in the template for readability
        )
        # Get the template use for the update. 
        jinja_template = jinja_env.get_template(DEFAULT_JINJA_UPDATE_TEMPLATE)
        # Now render the template with our message
        jinja_rendered_text = jinja_template.render(message_dict)
        LOG.debug("-----Template Rendered-----\n%s\n-------End-------",  jinja_rendered_text)
        return jinja_rendered_text
