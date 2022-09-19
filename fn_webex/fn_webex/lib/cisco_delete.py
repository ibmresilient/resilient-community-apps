# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
from urllib import parse
from resilient_lib import IntegrationError
from resilient_circuits import FunctionResult

from fn_webex.lib import constants, cisco_commons


class WebexDelete:
    def __init__(self, requiredParameters):
        self.requiredParameters = requiredParameters
        self.rc = self.requiredParameters.get("rc")
        self.header = requiredParameters.get("header")
        self.LOG = self.requiredParameters.get("logger")
        self.resclient = requiredParameters.get("resclient")
        self.response_handler = cisco_commons.ResponseHandler()
        self.entityId, self.entityName, self.entityType = None, None, None
        self.delteionURL, self.callingKey = None, None


    def delete_team_room(self):
        """
        A wrapper function that executes all the below functions in the 
        required order. 
        
        * find_api      : determines if the deletion operation is to be
                          performed on a room or team and adapts the 
                          functions accordinly.
        * locate_entity : Locates the exact room or team to be deleted.
        * delete_entity : Tries to delete the room or team and returns
                          a response accordingly.

        Returns:
        -------
            (<FunctionResult>): A dictionary with the response, the reason
                                should the operation fail, and a success
                                flag.
        """
        try:
            self.find_api()
            self.locate_entity()
            return self.delete_entity()
        except IntegrationError as err:
            return FunctionResult(None, success=False, reason=str(err))


    def find_api(self):
        """
        This function detemines the operaiton that is being perofrmed.
        All the below functions work for Room as well as teams. So this
        detemine the API to be used.

        Returns:
        --------
            entityId   (<str>): teamId or RoomId depending on the API
            entityName (<str>): teamName or RoomName depending on the API
            entityType (<str>): Team or Room to be deleted
        """
        self.entityId   = self.requiredParameters.get("entityId")
        self.entityName = self.requiredParameters.get("entityName")
        self.entityType = self.requiredParameters.get("entityType").strip().lower()
        
        if not self.entityName and not self.entityId:
            raise IntegrationError(constants.MSG_INVALID_DELETE.format(self.entityType))

        if "room" in self.entityType:
            self.callingKey = constants.ROOMS_CALLING_KEY
            self.deletionURL = parse.urljoin(self.requiredParameters.get("baseURL"), 
                constants.ROOMS_URL)
        else :
            self.callingKey = constants.TEAMS_CALLING_KEY
            self.deletionURL = parse.urljoin(self.requiredParameters.get("baseURL"),
                constants.TEAMS_URL)


    def locate_entity(self):
        """
        Finds the room or team based on the name or id given to the application. If an
        ID is given, the application checks to see if a room or team exists with the same
        ID and extracts the name of the room. If only the name is given, the application
        checks to see if room or team is available by comparing the name with a list of 
        all Rooms or teams associated with the organization and then extracts the ID. This
        form of deletion is an expensive operation.

        Raises:
        -------
            IntegrationError: Raises an error where to Room or team is unable to be located
                              based on the ID
            IntegrationError: Raises an error where to Room or team is unable to be located
                              based on Name
            IntegrationError: Raises an error when there are no rooms or teams to be deleted
        
        Returns:
        --------
            entityName (<str>): Actual name of the Room or Team
            entityId   (<str>): The Id of the room or team
        """
        self.LOG.info(constants.LOG_FETCHING_ENTITY.format(self.entityType))

        if self.entityId:
            self.deletionURL = parse.urljoin(self.deletionURL, self.entityId)
            res = self.rc.execute("get", self.deletionURL, headers=self.header,
                callback=self.response_handler.check_response)
            self.entityName = res.get(self.callingKey)
            if not self.entityName:
                raise IntegrationError(constants.MSG_INVALID_ENTITY_ID.format(self.entityType,
                    self.entityId))
        else:
            res = self.rc.execute("get", self.deletionURL, headers=self.header,
                callback=self.response_handler.check_response)

            if len(res.get('items')) > 0:
                entityName = self.entityName.strip()
                for objs in res.get("items"):
                    print(objs.get(self.callingKey), entityName)
                    if objs.get(self.callingKey).strip() == entityName:
                        self.entityId = objs.get("id")
                        self.entityName = objs.get(self.callingKey)
                        self.LOG.info("Webex: Retrieved {}: {}".format(self.entityType,
                            self.entityName))
                        break
                if not self.entityId:
                    raise IntegrationError("Could not find {}: {}".format(
                        self.entityType,
                        self.entityName))
            else:
                raise IntegrationError("Unable to retrieve {}! Delete operation failed".format(
                        self.entityType))


    def delete_entity(self):
        """
        This function deletes a room or a team based on the id specified to it.
        It monitors the response returned from the endpoint for 204, 404 and 405 responses.

        Response Codes:
        ---------------
            204 - Successfully deleted the room or team.
            404 - Room or team not found.
            405 - Room cannot be deleted, delete the team associated.

        Returns:
        --------
            (<dict>): Response from the endpoint
        """
        self.deletionURL = parse.urljoin(self.deletionURL, self.entityId)

        self.LOG.info("Webex: Deleting {}: {}".format(self.entityType, self.entityName))
        self.response_handler.add_exempt_codes(codes=[404, 405])
        self.LOG.info(constants.LOG_EXEMPT_DELETE_CODES)

        response = self.rc.execute("delete", self.deletionURL, headers=self.header,
            callback=self.response_handler.check_response)
        self.response_handler.clear_exempt_codes()

        if response.get("status_code") == 204:
            response["message"] = constants.MSG_SUCCESS_DELETION.format(
                self.entityType, self.entityName)
            return FunctionResult(response, success=True)

        if response.get("status_code") == 404:
            return FunctionResult(response, success=False,
                reason = constants.MSG_ENTITY_NOT_FOUND.format(self.entityType, 
                self.entityName))

        if response.get("status_code") == 405:
            return FunctionResult(response, success=False,
                reason=constants.MSG_ENTITY_NO_DIRECT_DELETE)

        if "errors" in response and "description" in response["errors"][0]:
            response["message"] = " ".join([response["message"], response["errors"][0]["description"]])

        response["message"] = ". ".join([constants.MSG_UNFAMILIAR_RESPONSE_CODE.format(response.get("status_code")),
            response["message"]])
        return FunctionResult(response, success=False, reason=response["message"])
