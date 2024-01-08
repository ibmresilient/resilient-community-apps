""" mock object """
import json
class MockClient:
    """ Mock """

    def __init__(self, options, rc=None):
        self.options = options

    # def request_access(self):
    #     """Function to access the Symantec SEP"""

    #     return self

    def transform_inputs(self, input_dict: dict) -> dict:
        """
        Update input dictionary.
        This function will perform the following actions:
            - Removes common prefix 'Symantec_SEP_' from all keys in 'input_dict'.
            - Strip whitespaces from beginning and end of string parameters in 'input_dict'.

        :param input_dict: Resilient Function input parameters.
        :type input_dict: dict
        :return: Processed input parameters for Symantec SEP api.
        :rtype: dict
        """
        params = {
            key.replace('sep_','') \
            : val.strip() if isinstance(val, str) else val \
            for key,val in input_dict.items()
        }
        return params

    def make_api_call(self, method: str, url: str, query_params: dict=None, payload_data: dict=False, message: str='OK', use_callback=False,) -> dict:

        # Get
        if method == 'GET' :
            # Binary File Content
            if '/file/123/details' in url:
                return {"message":"ok"}
            # Command Status Details
            if 'command-queue/123' in url:
                return {"message":"ok"}
            # Get Computer
            if '/computers' in url and query_params["computerName"]=="IBM_SOAR":
                return {"message":"ok"}
            # Get Critical Events Info
            if '/events/critical' in url and query_params["pageSize"]==123:
                return {"message":"ok"}
            # Excerption Policy
            if 'policies/exceptions/123' in url: 
                return {"message":"ok"}, None
            # Finger Print Name List
            if "/policy-objects/fingerprints/123" in url:
                return {"message":"ok"}
            # Finger Print List BY name
            if 'policy-objects/fingerprints' in url and query_params["domainId"]=="123":
                return {"message":"ok"}
            # Firewall Policy
            if "policies/firewall/123" in url:
                return {"message":"ok"}, None
            # Groups
            if "/groups/123" in url:
                return {"message":"ok"}
            # Policy Summary
            if "/policies/summary" in url and query_params["domainId"]=="123":
                return {"message":"ok"}
            else :
                raise ValueError("Issue with input data or in original function implementation.")

        # Post
        if method == 'POST' :
            # Add BlackList
            if 'policy-objects/fingerprints' in url and payload_data['name']=="IBM_SOAR" :
                return json.dumps({'id': 'F8059449FE8F49B4AD472327F2774BD4'}), None
            # Update BlackList
            if 'policy-objects/fingerprints' in url and payload_data['name']=="Test Blacklist File" :
                return {'message': 'ok'}, None
            # cancel a command
            if '123/cancel' in url:
                return {'message': 'ok'}, None
            # initiate Full Scan
            if '/command-queue/fullscan' in url and query_params['group_ids']=="123" :
                return {'message': 'ok'}
             # initiate Full Scan
            if '/command-queue/activescan' in url and query_params['group_ids']=="123" :
                return {'message': 'ok'}
            else :
                raise ValueError("Issue with input data or in original function implementation.")

        # Put
        if method == 'PUT' :
            # Assign Fingerprint to Group
            if 'system-lockdown/fingerprints/123' in url:
                return {'message': 'ok'}
            else:
                raise ValueError("Issue with input data or in original function implementation.")

        # Patch
        if method == 'PATCH' :
            # Move clients
            if '/computers' in url and json.loads(payload_data)[0]["group"]["id"]=='123':
                return {'message': 'ok'}
            else :
                raise ValueError("Issue with input data or in original function implementation.")
           
        #Delete
        if method == 'DELETE' :
            # Delete Black List
            if 'fingerprints/123' in url:
                return {'message': 'ok'}
            else :
                raise ValueError("Issue with input data or in original function implementation.")


        