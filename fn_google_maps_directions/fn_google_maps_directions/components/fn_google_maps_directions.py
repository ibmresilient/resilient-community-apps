# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
try:
    from urllib import quote as url_encode  # Python 2.X
except ImportError:
    from urllib.parse import quote as url_encode  # Python 3+

class FunctionPayload:
  """Class that contains the payload sent back to UI and available in the post-processing script"""
  def __init__(self, inputs):
    self.success = True
    self.inputs = {}
    self.directions_link = None

    for input in inputs:
      self.inputs[input] = inputs[input]
  
  def asDict(self):
    """Return this class as a Dictionary"""
    return self.__dict__

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    @function("fn_google_maps_directions")
    def _fn_google_maps_directions_function(self, event, *args, **kwargs):
        """Function: A Function that takes an Origin and a Destination and returns a Google Maps Link with Directions"""

        log = logging.getLogger(__name__)

        # Base URL to Google Maps
        GOOGLE_MAPS_URL = "https://www.google.com/maps/dir/?api=1"

        def get_function_input(inputs, input_name, optional=False):
          """Given input_name, checks if it defined. Raises ValueError if a mandatory input is None"""
          input = inputs.get(input_name)

          if input is None and optional is False:
            err = "'{0}' is a mandatory function input".format(input_name)
            raise ValueError(err)
          else:
            return input

        try:
            # Get the function inputs:
            inputs = {
              "google_maps_origin": get_function_input(kwargs, "google_maps_origin"), # text (required)
              "google_maps_destination": get_function_input(kwargs, "google_maps_destination"), # text (required)
            }

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # url_encode origin and destination
            origin = url_encode(payload.inputs["google_maps_origin"].encode('utf8'))
            destination = url_encode(payload.inputs["google_maps_destination"].encode('utf8'))

            yield StatusMessage("Generating Link")

            # Generate Link
            payload.directions_link = "{0}&origin={1}&destination={2}".format(GOOGLE_MAPS_URL, origin, destination)

            # Send payload back to Appliance
            results = payload.asDict()

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
