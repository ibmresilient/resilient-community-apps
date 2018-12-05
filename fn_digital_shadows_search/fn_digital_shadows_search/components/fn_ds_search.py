# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_digital_shadows_search.util.selftest as selftest
import requests
from requests.auth import HTTPBasicAuth
from requests.adapters import HTTPAdapter
import json
try:
    from urllib import quote as url_encode  # Python 2.X
except ImportError:
    from urllib.parse import quote as url_encode  # Python 3+

class FunctionPayload:
  """Class that contains the payload sent back to UI and available in the post-processing script"""
  def __init__(self, inputs):
    self.success = True
    self.inputs = {}
    self.data = None
    self.link = None
    self.href = None

    for input in inputs:
      self.inputs[input] = inputs[input]
  
  def asDict(self):
    """Return this class as a Dictionary"""
    return self.__dict__

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_ds_search"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_digital_shadows_search", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_digital_shadows_search", {})

    @function("fn_ds_search")
    def _fn_ds_search_function(self, event, *args, **kwargs):
        """Function: Function to send a Query to the Digital Shadows Platform and returns a Python List of the results"""

        log = logging.getLogger(__name__)

        def get_config_option(option_name, optional=False):
          """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
          option = self.options.get(option_name)

          if not option and optional is False:
            err = "'{0}' is mandatory and is not set in the app.config file. You must set this value to run this function".format(option_name)
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
            inputs = {
              "ds_search_value": get_function_input(kwargs, "ds_search_value")
            }
            
            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Get configs
            api_key = get_config_option("ds_api_key")
            api_secret = get_config_option("ds_api_secret")
            base_url = get_config_option("ds_base_url")

            headers = {'content-type': 'application/json; charset=utf-8', 'Accept': 'application/json'}
            basic_auth = HTTPBasicAuth(api_key, api_secret)

            qry_url = "{0}{1}".format(base_url, "/api/search/find")
            filter = {"query": payload.inputs["ds_search_value"]}

            try:
              yield StatusMessage("Sending POST request to {0}".format(qry_url))
              res = requests.post(
                qry_url,
                json.dumps(filter),
                auth=basic_auth,
                headers=headers,
                verify=True)

              res.raise_for_status()
              
              if res.status_code == 200:
                payload.data = json.loads(res.text)["content"]

                q = url_encode(payload.inputs["ds_search_value"].encode('utf8'))
                link = "{0}/search?q={1}&view=List".format(base_url, q)
                payload.link = link
                payload.href = """<a href={0}>Link</a>""".format(link)

              else:
                payload.success = False
                raise ValueError('Request to {0} failed with code {1}'.format(qry_url, res.status_code))

            except requests.exceptions.Timeout:
              raise ValueError('Request to {0} timedout'.format(qry_url))

            except requests.exceptions.TooManyRedirects:
              raise ValueError('A bad url request', qry_url)

            except requests.exceptions.HTTPError as err:
              if(err.response.content):
                custom_error_content = json.loads(err.response.content)
                raise ValueError(custom_error_content['error']['message'])
              else:
                raise ValueError(err)
            except requests.exceptions.RequestException as e:
              raise ValueError(e)

            results = payload.asDict()

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()