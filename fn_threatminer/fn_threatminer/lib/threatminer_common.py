# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""Function implementation"""

from resilient_lib import RequestsCommon

PACKAGE = 'fn_threatminer'

class ThreatMiner():
    """
    class for making request calls and reviewing the responses
    """
    def __init__(self, opts, function_opts):
        self.requestscommon = RequestsCommon(opts=opts, function_opts=function_opts)
        self.url = function_opts.get('url', None)
        if not self.url:
            raise ValueError('missing url from [fn_threatminer] in app_config')

    def get(self, uri):
        """
        make the https get call
        :param uri:
        :return: response.json, msg
        """
        url = self.url + uri
        return self.requestscommon.execute_call_v2("get", url, callback=self.threatminer_callback)


    def threatminer_callback(self, response):
        """
        callback to review the responses based on status_code
        :param response:
        :return: response.json, msg
        """
        resp_json = response.json()
        if resp_json.get('status_code', None) == '200':
            msg = u'Results returned'
        elif resp_json.get('status_code', None) == '404':
            msg = u'No Results returned'
        else:
            msg = u'Unexpected return code of {}'.format(resp_json.get('status_code', None))

        return resp_json, msg
