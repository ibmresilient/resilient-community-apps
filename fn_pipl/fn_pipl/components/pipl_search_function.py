# (c) Copyright IBM Corp. 2018. All Rights Reserved.

# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from piplapis.search import SearchAPIRequest
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_pipl.util.selftest as selftest
import json


class FunctionPayload:
    """Class that contains the payload sent back to UI and available in the post-processing script"""

    def __init__(self):
        self.success = True
        self.person_list = None
        self.pipl_response = None
        self.raw_data = None

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'pipl_search_function"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_pipl", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_pipl", {})

    @function("pipl_search_function")
    def _pipl_search_function_function(self, event, *args, **kwargs):
        """Function: Function enriches your leads (name, email address, phone number, or social media username) with Pipl
        and gets their personal, professional, demographic, and contact information.

        The minimal requirement to run a search is to have at least one full name, email, phone, username, user_id,
        URL or a single valid US address (down to a house number)."""

        def get_config_option(option_name, optional=False):
            """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
            option = self.options.get(option_name)

            if not option and optional is False:
                err = "'{0}' is mandatory and is not set in the app.config file. " \
                      "You must set this value to run this function".format(option_name)
                raise ValueError(err)
            else:
                return option

        def get_function_input(inputs, input_name, optional=False):
            """Given input_name, checks if it defined. Raises ValueError if a mandatory input is None"""
            input = inputs.get(input_name)

            if input is None and optional is False:
                err = "'{0}' is a mandatory function input".format(input_name)
                raise ValueError(err)
            else:
                return input

        try:
            # Get the function parameters:
            artifact_type = get_function_input(kwargs, "pipl_artifact_type")  # text
            artifact_value = get_function_input(kwargs, "pipl_artifact_value")  # text

            log = logging.getLogger(__name__)
            log.info("artifact_type: %s", artifact_type)
            log.info("artifact_value: %s", artifact_value)

            # Read configuration settings:
            pipl_api_key = get_config_option("pipl_api_key")
            max_matches = int(get_config_option("pipl_max_no_possible_per_matches"))
            pipl_minimum_match = get_config_option("pipl_minimum_match", True)
            minimum_match = float(pipl_minimum_match) if pipl_minimum_match else None
            pipl_minimum_probability = get_config_option("pipl_minimum_probability", True)
            minimum_probability = float(pipl_minimum_probability) if pipl_minimum_probability else None
            pipl_infer_persons = get_config_option("pipl_infer_persons", True)
            infer_persons = parse_bool(pipl_infer_persons) if pipl_infer_persons else None

            email, raw_name, username = None, None, None
            if artifact_type == "Email Sender" or artifact_type == "Email Recipient":
                # In Pipl Data this are full email addresses. Personal and Work emails.
                email = artifact_value

            elif artifact_type == "User Account":
                # In Pipl Data this are usernames in use by the person online. This includes screen names,
                # handles and nicknames from across the web, social media sites, forums and more.
                username = artifact_value
            else:
                # In Pipl Data this is current name as well as maiden name and nicknames.
                raw_name = artifact_value

            # Set the required request data
            request = SearchAPIRequest(email=email, raw_name=raw_name, username=username, api_key=pipl_api_key,
                                       minimum_match=minimum_match, minimum_probability=minimum_probability,
                                       infer_persons=infer_persons)

            # get response
            response = request.send()  # returns SearchAPIResponse object not dict

            # Create payload dict
            payload = FunctionPayload()

            if response:
                # If success extract person data
                if response.http_status_code == 200:

                    response_json = response.raw_json
                    persons_count = response.persons_count
                    if persons_count and response_json:

                        response_dict = json.loads(response_json)

                        person_list = []
                        # A response can return either a Person or possible_persons array
                        pipl_person = response_dict.get("person")
                        possible_persons = response_dict.get("possible_persons")

                        if pipl_person:
                            person_list.append(pipl_person)
                            payload.pipl_response = "definite match"
                            yield StatusMessage("The data sent/found to Pipl is enough to identify a single, matching person.")

                        elif possible_persons:
                            # Include only this number of possible person matches in the results
                            new_list = possible_persons[:max_matches]
                            person_list.extend(new_list)

                            payload.pipl_response = "possible person matches"
                            yield StatusMessage("The data sent/found to Pipl is not enough to identify a single person. "
                                                "A list of possible person matches was returned.")
                        else:
                            payload.pipl_response = "no match"
                            yield StatusMessage("No data was found in Pipl. "
                                                "Try adjusting the search settings in app.config.")

                        # Save the response in payload
                        payload.person_list = person_list
                        # Pretty printing
                        payload.raw_data = json.dumps(person_list, sort_keys=True, indent=4, separators=(',', ': '))

                    # No data returned
                    else:
                        payload.possible_persons = []
                        payload.pipl_response = "no match"
                        yield StatusMessage("No data was found in Pipl. "
                                            "Try adjusting the search settings in app.config.")

                # If not a 200 code
                else:
                    payload.success = False
                    raise ValueError("Error with Pipl API. Status Code: {0}".format(response.error))
            else:
                payload.success = False
                raise ValueError("No response from Pipl. Check your connection/credentials.")

            # Send payload back to Appliance
            results = payload.as_dict()

            log.info(json.dumps(results))
            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            log.error(err)
            yield FunctionError()


def parse_bool(value):
    """Represents value as boolean.
    :param value:
    :rtype: bool
    """
    value = str(value).lower()
    return value in ('1', 'true', 'yes')