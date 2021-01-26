# (c) Copyright IBM Corp. 2018. All Rights Reserved.

# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from piplapis.search import SearchAPIRequest
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload, RequestsCommon
import json

from fn_pipl.util.example_response import ExampleResponse

PACKAGE_NAME = "fn_pipl"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'pipl_search_function"""

    def load_opts(self, opts):
        """
        Get app.config values and validate them.
        """
        self.options = opts.get(PACKAGE_NAME, {})
        self.opts = opts

        # Validate required fields
        required_fields = ["pipl_api_key", "pipl_max_no_possible_per_matches"]
        validate_fields(required_fields, self.options)

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.load_opts(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.load_opts(opts)

    @function("pipl_search_function")
    def _pipl_search_function_function(self, event, *args, **kwargs):
        """Function: Function enriches your leads (name, email address, phone number, or social media username) with Pipl
        and gets their personal, professional, demographic, and contact information.

        The minimal requirement to run a search is to have at least one full name, email, phone, username, user_id,
        URL or a single valid US address (down to a house number)."""

        try:
            # Get the function parameters:
            artifact_type = kwargs.get("pipl_artifact_type")  # text
            artifact_value = kwargs.get("pipl_artifact_value")  # text

            log = logging.getLogger(__name__)
            log.info("artifact_type: %s", artifact_type)
            log.info("artifact_value: %s", artifact_value)

            # Read configuration settings:
            pipl_api_key = self.options.get("pipl_api_key")
            max_matches = int(self.options.get("pipl_max_no_possible_per_matches"))
            minimum_match = float(self.options.get("pipl_minimum_match", 0))
            minimum_probability = float(self.options.get("pipl_minimum_probability", 0))
            infer_persons = parse_bool(self.options.get("pipl_infer_persons"))

            email = raw_name = username = None
            if artifact_type in ("Email Sender", "Email Recipient"):
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

            # get response and cast to a dictionary
            response = request.send().to_dict()

            # Create payload dict
            rp = ResultPayload(PACKAGE_NAME, **kwargs)
            content = {}
            person_list = []

            if response:
                # If success extract person data
                if response["@http_status_code"] == 200:

                    persons_count = response.get("@persons_count")

                    if persons_count:
                        # A response can return either a Person or possible_persons array
                        pipl_person = response.get("person")
                        possible_persons = response.get("possible_persons")

                        if pipl_person:
                            person_list.append(pipl_person)
                            content["pipl_response"] = "definite match"
                            yield StatusMessage("The data sent/found to Pipl is enough to identify a single, matching person.")

                        elif possible_persons:
                            # Include only this number of possible person matches in the results
                            new_list = possible_persons[:max_matches]
                            person_list.extend(new_list)

                            content["pipl_response"] = "possible person matches"
                            yield StatusMessage("The data sent/found to Pipl is not enough to identify a single person. "
                                                "A list of possible person matches was returned.")
                        else:
                            content["pipl_response"] = "no match"
                            yield StatusMessage("No data was found in Pipl. "
                                                "Try adjusting the search settings in app.config.")

                        # Save the response in payload
                        content["person_list"] = person_list
                        # Pretty printing
                        content["raw_data"] = json.dumps(person_list, sort_keys=True, indent=4, separators=(',', ': '))

                    # No data returned
                    else:
                        content["person_list"] = person_list
                        content["pipl_response"] = "no match"
                        yield StatusMessage("No data was found in Pipl. "
                                            "Try adjusting the search settings in app.config.")

                    # rp done for 200 code cases
                    results = rp.done(True, content)

                # If not a 200 code
                else:
                    success = False
                    content = "Error with Pipl API. Status Code: {0}".format(response["error"])
                    reason = "; ".join(response.get("warnings"))
                    results = rp.done(success, content, reason)
                    yield StatusMessage(content)

            else:
                success = False
                content = "No response from Pipl. Check your connection/credentials."
                reason = "No response."
                results = rp.done(success, content, reason)
                yield StatusMessage(content)

            # Send payload back to Appliance
            # Backwards compatibility
            results["person_list"] = content.get("person_list")
            results["pipl_response"] = content.get("pipl_response")
            results["raw_data"] = content.get("raw_data")

            log.info(json.dumps(results))
            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            log.error(err)
            yield FunctionError(err)


def parse_bool(value):
    """Represents value as boolean.
    :param value:
    :rtype: bool
    """
    value = str(value).lower()
    return value in ('1', 'true', 'yes')