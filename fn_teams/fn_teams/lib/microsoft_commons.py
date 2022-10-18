from resilient_lib import IntegrationError
from fn_teams.lib import constants

class ResponseHandler:
    """
    Handles the responses received from the Webex endpoint.
    Used as a callback function for request_common.execute

    The behaviour of the response received can be customized by allowing
    certain response codes to pass through and not raise an exception.

    Input:
    ------
        Response  (<response>) : A response from rc.execute

    Defaults:
    ---------
        msg                    : Message in accordance with the error code
        default_exempt_codes   : default list of codes that are to be
                                 exempted from raising an exception
        exempt_codes           : list of codes that are to be exempted
                                 from raising an exception

    Returns:
    --------
            (<dict>) : Response with appropriate status code and message
    """
    def __init__(self):
        self.msg, self.response = None, None
        self.default_exempt_codes = [204]
        self.exempt_codes = self.default_exempt_codes.copy()


    def clear_exempt_codes(self, default=None):
        """
        Clears the exempt code list or resets it back to the
        default value.

        Arguments:
        ----------
            default (<bool>) : Resets the code to default list of codes
                               else, clears all codes
        """
        if default:
            self.exempt_codes = self.default_exempt_codes.copy()
        else:
            self.exempt_codes = []


    def add_exempt_codes(self, codes):
        """
        Allows for adding codes to the exempt list

        Args:
        -----
            codes (<int>) or (<list>): A code or a list of codes to be added
                                       to the exempt code list

        Raises:
        -------
            TypeError: When unsupported type supplied for codes.
            Supported type <list> or <int>
        """
        if isinstance(codes, int):
            self.exempt_codes.append(codes)
        elif isinstance(codes, list):
            self.exempt_codes.extend(codes)
        else:
            raise IntegrationError(constants.MSG_UNSUPPORTED_TYPE.format(codes))


    def monitor_status(self):
        """
        Monitors the response recieved from the endpoint and generates a custom message
        for the webex application.

        Raises:
        -------
            IntegrationError : If the recieved response is None, raises this error. This
                               could be due to an invalid call methord being passed.
        """
        if self.response is None:
            raise IntegrationError(constants.MSG_RESPONSE_NONE)
        if self.response.status_code == 204:
            self.msg = constants.MSG_RESPONSE_204
        elif "error" in self.response.json():
            response = self.response.json()
            error = "{} {}".format(
                response.get('error').get('message'),
                response.get('error_description'))
            if self.response.status_code == 400:
                self.msg = constants.MSG_RESPONSE_400.format(error)
            elif self.response.status_code == 401:
                self.msg = constants.MSG_RESPONSE_404.format(error)
            elif self.response.status_code == 404:
                self.msg = constants.MSG_RESPONSE_404.format(error)
            elif self.response.status_code == 405:
                self.msg = constants.MSG_RESPONSE_405.format(error)


    def raise_or_return_erros(self):
        """
        Filters through the response to either raise or return the request.
            * If the status code matches with the exempt list, the method
              will allow it to pass and returns the message body.
            * If the status_code is not > 204 and not in exempt list, the method
              raises an exception.
            * If the status code is 204 and in exempt list, creates a message
              body and returns it with a custom message

        Raises:
        -------
            IntegrationError: When an exception occurs and not exempted.

        Returns:
        --------
            (<dict>): If the methord doesnot raise an error, it the returns the response
                      in the form of a dictionary.
        """
        if self.msg:
            if self.response.status_code in self.exempt_codes:

                if self.response.status_code == 204:
                    res = {}
                else:
                    res = self.response.json()
                res["status_code"] = self.response.status_code
                if self.msg:
                    res["message"] = self.msg
                return res
            raise IntegrationError(self.msg)
        res = self.response.json()
        res["status_code"] = self.response.status_code
        return res


    def check_response(self, response):
        """
        Wrapper to run the object

        Args:
        -----
            response (<response>): Response from the rc object

        Returns:
        --------
            (<dict>) : Response body with status code.
        """
        self.msg = None
        self.response = response
        self.monitor_status()
        return self.raise_or_return_erros()
