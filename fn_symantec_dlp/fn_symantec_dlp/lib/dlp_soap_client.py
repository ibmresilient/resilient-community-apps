# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use


import datetime


class DLPSoapClient():
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

        cls.host = cls.get_config_option(app_configs=app_configs,
                                            option_name="sdlp_host",
                                            optional=False)



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
    def incident_list(cls, savedReportId=0, incidentCreationDateLaterThan=datetime.datetime.now()):
        """incident_list API Call to gather a list of incidents from a saved report.

        :param savedReportId: the ID of a saved report,
        if not provided no incidents will be found, defaults to 0
        :type savedReportId: int, optional
        :param incidentCreationDateLaterThan: Only incidents that were created after the incidentCreationDateLaterThan date will be returned, defaults to datetime.datetime.now()
        :type incidentCreationDateLaterThan: datetime, required
        :return: A list of incidentIds and incidentLongIds
        :rtype: [type]
        """
        incident_list = cls.soap_client.service.incidentList(
            savedReportId=savedReportId,
            incidentCreationDateLaterThan=incidentCreationDateLaterThan)

        return incident_list


