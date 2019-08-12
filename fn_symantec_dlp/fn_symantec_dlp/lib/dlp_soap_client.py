# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use



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

