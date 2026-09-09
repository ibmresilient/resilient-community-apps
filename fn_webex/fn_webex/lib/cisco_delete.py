# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
from urllib import parse
from resilient_lib import IntegrationError
from resilient_circuits import FunctionResult

from fn_webex.lib import constants, cisco_commons


class WebexDelete:
    """
        This application allows for deleting a team or a room using the Cisco Webex API. This
        provides SOAR with the ability to delete teams and rooms from within a SOAR incident
        or a task. Either the name or the ID must 

        Inputs:
        -----
            incidentId         (<str>)  : Incident ID
            taskId             (<str>)  : Task ID
            entityId           (<str>)  : ID of the Team or Room to be deleted
            entityName         (<str>)  : Name of the Team or Room to be deleted
            entityURL          (<str>)  : Teams or Rooms API URL
            enityType          (<str>)  : Rooms or Teams API selector

        Returns:
        --------
            Response          (<dict>)  : A response with the room/team options and details
                                          or the error message if the meeting creation
                                          fails
    """
    def __init__(self, required_parameters):
        self.required_parameters = required_parameters
        self.rc = self.required_parameters.get("rc")
        self.header = self.required_parameters.get("header")
        self.LOG = self.required_parameters.get("logger")
        self.resclient = self.required_parameters.get("resclient")
        self.response_handler = cisco_commons.ResponseHandler()
        self.entity_id, self.entity_name, self.entity_type = None, None, None
        self.deletion_url, self.calling_key = None, None
        self.find_api()


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
            self.locate_entity()
            return self.delete_entity()
        except IntegrationError as err:
            return FunctionResult(None, success=False, reason=str(err))


    def find_api(self):
        """
        This function determines the operation that is being perofrmed.
        All the below functions work for Room as well as teams. So this
        detemine the API to be used.

        Returns:
        --------
            entityId   (<str>): teamId or RoomId depending on the API
            entityName (<str>): teamName or RoomName depending on the API
            entityType (<str>): Team or Room to be deleted
        """
        self.entity_id   = self.required_parameters.get("entityId")
        self.entity_name = self.required_parameters.get("entityName")
        self.entity_type = self.required_parameters.get("entityType").strip().lower()
        
        if not self.entity_name and not self.entity_id:
            raise IntegrationError(constants.MSG_INVALID_DELETE.format(self.entity_type))

        if constants.ROOM in self.entity_type:
            self.calling_key = constants.ROOMS_CALLING_KEY
            self.deletion_url = parse.urljoin(self.required_parameters.get("baseURL"), 
                constants.ROOMS_URL)
        else :
            self.calling_key = constants.TEAMS_CALLING_KEY
            self.deletion_url = parse.urljoin(self.required_parameters.get("baseURL"),
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
        self.LOG.info(constants.LOG_FETCHING_ENTITY.format(self.entity_type))

        if self.entity_id:
            self.deletion_url = parse.urljoin(self.deletion_url, self.entity_id)
            res = self.rc.execute("get", self.deletion_url, headers=self.header,
                callback=self.response_handler.check_response)
            self.entity_name = res.get(self.calling_key)
            if not self.entity_name:
                raise IntegrationError(constants.MSG_INVALID_ENTITY_ID.format(self.entity_type,
                    self.entity_id))
        else:
            res = self.rc.execute("get", self.deletion_url, headers=self.header,
                callback=self.response_handler.check_response)

            if len(res.get('items')) > 0:
                entityName = self.entity_name.strip()
                for objs in res.get("items"):
                    if objs.get(self.calling_key).strip() == entityName:
                        self.entity_id = objs.get("id")
                        self.entity_name = objs.get(self.calling_key)
                        self.LOG.info("Webex: Retrieved {}: {}".format(self.entity_type,
                            self.entity_name))
                        break
                if not self.entity_id:
                    raise IntegrationError("Could not find {}: {}".format(
                        self.entity_type,
                        self.entity_name))
            else:
                raise IntegrationError(constants.LOG_UNABLE_TO_FIND.format(
                        self.entity_type))


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
        self.deletion_url = parse.urljoin(self.deletion_url, self.entity_id)

        self.LOG.info("Webex: Deleting {}: {}".format(self.entity_type, self.entity_name))
        self.response_handler.add_exempt_codes(codes=[404, 405])
        self.LOG.info(constants.LOG_EXEMPT_DELETE_CODES)

        response = self.rc.execute("delete", self.deletion_url, headers=self.header,
            callback=self.response_handler.check_response)
        self.response_handler.clear_exempt_codes()

        if response.get("status_code") == 204:
            response["message"] = constants.MSG_SUCCESS_DELETION.format(
                self.entity_type, self.entity_name)
            return FunctionResult(response, success=True)

        if response.get("status_code") == 404:
            return FunctionResult(response, success=False,
                reason = constants.MSG_ENTITY_NOT_FOUND.format(self.entity_type, 
                self.entity_name))

        if response.get("status_code") == 405:
            return FunctionResult(response, success=False,
                reason=constants.MSG_ENTITY_NO_DIRECT_DELETE)

        if "errors" in response and "description" in response["errors"][0]:
            response["message"] = " ".join([response["message"], response["errors"][0]["description"]])

        response["message"] = ". ".join([constants.MSG_UNFAMILIAR_RESPONSE_CODE.format(response.get("status_code")),
            response["message"]])
        return FunctionResult(response, success=False, reason=response["message"])
