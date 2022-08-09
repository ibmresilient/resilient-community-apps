# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

from resilient_lib import IntegrationError
from resilient_circuits import FunctionError


class WebexAuthentication:
    def __init__(self, requiredParameters):
        self.requiredParameters = requiredParameters
        self.rc  = requiredParameters["rc"]
        self.LOG = self.requiredParameters["logger"]


    def Authenticate(self):
        '''
        Helper method that establishes a connection with the Client servers and performs an OAuth
        authentication. The server returns a beareID for the session, which then is used to make
        requests. This bearerID is incorporated with the header for every request henceforth
        '''
        bearerID = self.generate_bearerID()
        header = self.generate_header(bearerID)
        return header

    def generate_bearerID(self):
        '''
        This function perfroms OAuth authentication and retrieves the bearerID which is necessary
        to interact with the webex endpoint.

        Options:
        -------
        client_id : This ID is generated while creating an integration on the webex endpoint
        
        '''
        data = {
            "client_id": self.requiredParameters["clientID"],
            "scope": self.requiredParameters["scope"],
            "client_secret": self.requiredParameters["clientSecret"],
            "refresh_token": self.requiredParameters["refreshToken"],
            "grant_type": "refresh_token"
        }
        try:
            result = self.rc.execute("POST", self.requiredParameters["tokenURL"], data=data)
        except IntegrationError as err:
                raise IntegrationError("Unable to authenticate: Error: Is the refresh_token up to date?")

        if "access_token" in result.json():
            return result.json().get("access_token")

        msg = u"Unable to authenticate: Error: {}\nDescription: {}"\
            .format(result.json().get("error"), result.json().get("error_description"))
        raise FunctionError(msg)


    def generate_header(self, bearerID):
        '''
        Checks for bearerID and returns it in a json format for request header
        
        Arguments:
        ---------
        bearerID : Integer
                   Session ID that is required for authentication
        '''
        if not bearerID:
            raise ValueError("Bearer ID not specified")
        return {
            'Authorization' : "Bearer {}".format(bearerID),
            'Content-Type'  : 'application/json'}
