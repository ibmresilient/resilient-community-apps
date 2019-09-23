# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
# pragma pylint: disable=unused-argument, no-self-use
import datetime
import logging
import traceback
import uuid
import os



import zeep
from zeep.helpers import serialize_object
from requests import Session
from requests.auth import HTTPBasicAuth, AuthBase
from resilient_lib import validate_fields
from resilient_circuits import template_functions

LOG = logging.getLogger(__name__)


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
        # TODO: Look up validate_fields instead of this 

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

    @staticmethod
    def get_config_option(app_configs, option_name, optional=False, placeholder=None):
        """get_config_option Given option_name, checks if it is in appconfig.
        Raises ValueError if a mandatory option is missing

        :param app_configs: a dictionary containing key-value pairs used for
        setting up a client with Symantec DLP.
        :type app_configs: dict
        :param option_name: the name of the option to get
        :type option_name: string
        :param optional: defaults to False
        :type optional: bool, optional
        :param placeholder: defaults to None
        :type placeholder: optional
        :return: returns the specified app.config if found
        """
        option = app_configs.get(option_name)
        err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function".format(
            option_name)

        if not option and optional is False:
            raise ValueError(err)
        elif optional is False and placeholder is not None and option == placeholder:
            raise ValueError(err)
        else:
            return option

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
    def update_incident(cls, incident_id, status, note, custom_attributes=None):
        """update_incident is used to send changes to a DLP Incident
        Each request to DLP sets up an UpdateBatchRequest SOAP Type and then sends the request to DLP

        :param incident_id: The ID of the DLP Incident to update. The input is casted to an int, input itself should be a number or string representation of one
        :type incident_id: int
        :param status: Used to update the status of a DLP Incident, the provided status value must be a valid, 
        existing Incident Status option on your DLP Installation
        :type status: string
        :param custom_attributes: any custom attributes you want to update on the DLP Incident.
        Passed in attributes must be done as a list of dict objects and each custom attribute needs to be provided with this format 
        {"name": <custom attribute name>, "value": <custom attribute name>}

        :type custom_attributes: list , optional
        :return: the response of the request
        :rtype: dict
        """
        # Get the batch type which will be filled with our updates
        batch = cls.soap_client.get_type('{http://www.vontu.com/v2011/enforce/webservice/incident/schema}IncidentUpdateBatch')()
        # Get the type constructor for the IncidentAttributes type
        incidentAttributes = cls.soap_client.get_type('{http://www.vontu.com/v2011/enforce/webservice/incident/schema}IncidentAttributes')()
        # incidentAttributes = incidentAttributesType()
        batch.batchId = "_{}".format(uuid.uuid4())
        if status:
            incidentAttributes.status = status

        # Prepare an empty list for all the attributes
        attributes = []
        # Get the type constructor for the CustomAttributeType type
        attr = cls.soap_client.get_type(
                    '{http://www.vontu.com/v2011/enforce/webservice/incident/common/schema}CustomAttributeType')
        if custom_attributes:
            for attribute in custom_attributes:
                # Construct a CustomAttributeType with the kwargs from each attribute. Then append to our list
                attributes.append(attr(**attribute))
            # Add the list of customAttribute types to the incidentAttributes type
            incidentAttributes.customAttribute = attributes
        req = cls.soap_client.get_type('{http://www.vontu.com/v2011/enforce/webservice/incident/schema}IncidentUpdateRequest')
        batch.incidentAttributes = incidentAttributes
        batch.incidentId = [incident_id]
        # Init the IncidentUpdateRequest type providing our updateBatch, then serialize the whole thing as a dict.
        new_req = serialize_object(req(updateBatch=[batch]), target_cls=dict)
        # # Strict mode off to avoid an XMLParseError for custom attributes that are not expected
        request = req(updateBatch=batch)
        # request.updateBatch = batch
        with cls.soap_client.settings(strict=True):
            
            LOG.info(request)
            return cls.soap_client.service.updateIncidents(request)

    