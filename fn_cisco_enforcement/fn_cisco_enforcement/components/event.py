# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation"""
import logging
import re
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_enforcement.lib.resilient_common import validate_fields, readable_datetime

try:
    from urlparse import urlparse
except:
    from urllib.parse import urlparse

HEADERS = {'content-type': 'application/json'}
# This adds an event using the Cisco Event api. The inputs can be found with a description of the api here https://docs.umbrella.com/developer/enforcement-api/events2/
# The apikey is refernced in the app.config under [fn_cisco_enforcement]

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'event"""


    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cisco_enforcement", {})
        self.log = logging.getLogger(__name__)

        self._init()

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_enforcement", {})

        self._init()

    def _init(self):
        validate_fields(['api_token'], self.options)

        """get the api token for cisco access"""
        self.apikey = self.options.get('api_token')

    @function("cisco_post_event")
    def _event_function(self, event, *args, **kwargs):
        """Function: This is a function implementation that uses the Cisco API to post a Malware event"""
        try:
            url = '/'.join((self.options['url'], 'events?customerKey={}'))
            url = url.format(self.apikey)
            self.log.debug(url)

            data=self.createdataobject(kwargs)

            response = requests.post(url, json=data, verify=False, headers=HEADERS)

            result = None
            if response.status_code >= 300:
                resp = response.json()
                if response.status_code == 404:
                    response.content and self.log.warning(response.content)
                    yield StatusMessage(u"Cisco Enforcement issue: {}: {}".format(response.status_code, resp['message']))
                else:
                    response.content and self.log.error(response.content)
                    yield StatusMessage(u"Cisco Enforcement failure: {}: {}".format(response.status_code, resp['message']))
            else:
                result = response.content.decode('latin1')
                yield StatusMessage("Post Event was successful")

            self.log.debug(result)
            # Produce a FunctionResult with the results
            yield FunctionResult({ "value": result})
        except Exception as err:
            self.log.error(err)
            yield FunctionError(err)

    # Creates the data object to send
    def createdataobject(self, kwargs):

        validate_fields(['protocol_version', 'provider_name'], self.options)

        # Get the function parameters:
        protocolversion = self.options.get('protocol_version')
        providername = self.options.get('provider_name')

        if protocolversion and providername:
            cisco_protocolversion = protocolversion
            cisco_providername = providername
        else:
            raise ValueError('Please set protocol_version and provider_name in the app.config under [fn_cisco_enforcement]')

        validate_fields(['cisco_deviceid', 'cisco_deviceversion', 'cisco_eventtime', 'cisco_alerttime', 'cisco_dstdomain'], kwargs)

        # Convert timestamps from miliseconds to seconds
        cisco_deviceid = kwargs.get("cisco_deviceid")  # text
        cisco_deviceversion = kwargs.get("cisco_deviceversion")  # text

        cisco_eventtime = readable_datetime(kwargs.get("cisco_eventtime")) # datetimepicker - resilient is in milliseconds
        cisco_alerttime = readable_datetime(kwargs.get("cisco_alerttime")) # datetimepicker

        domain = kwargs.get("cisco_dstdomain")
        cisco_dsturl, cisco_dstdomain = self._parseUrl(domain)     # split url and domain

        cisco_disabledstsafeguards = self.get_select_param(kwargs.get("cisco_disabledstsafeguards"))  # text
        cisco_dstip = kwargs.get("cisco_dstip")  # text
        cisco_eventseverity = kwargs.get("cisco_eventseverity")  # text
        cisco_eventtype = kwargs.get("cisco_eventtype")  # text
        cisco_eventdescription = kwargs.get("cisco_eventdescription")  # text
        cisco_eventhash = kwargs.get("cisco_eventhash")  # text
        cisco_filename = kwargs.get("cisco_filename")  # text
        cisco_filehash = kwargs.get("cisco_filehash")  # text
        cisco_externalurl = kwargs.get("cisco_externalurl")  # text
        cisco_src = kwargs.get("cisco_src")  # text

        self.log.info("dstDomain: %s", cisco_dstdomain)
        self.log.info("dstUrl: %s", cisco_dsturl)
        self.log.info("cisco_deviceid: %s", cisco_deviceid)
        self.log.info("cisco_deviceversion: %s", cisco_deviceversion)
        self.log.info("cisco_eventtime: %s", cisco_eventtime)
        self.log.info("cisco_alerttime: %s", cisco_alerttime)
        self.log.info("cisco_protocolversion: %s", cisco_protocolversion)
        self.log.info("cisco_providername: %s", cisco_providername)
        self.log.info("cisco_disabledstsafeguards: %s", cisco_disabledstsafeguards)
        self.log.info("cisco_dstip: %s", cisco_dstip)
        self.log.info("cisco_eventseverity: %s", cisco_eventseverity)
        self.log.info("cisco_eventtype: %s", cisco_eventtype)
        self.log.info("cisco_eventdescription: %s", cisco_eventdescription)
        self.log.info("cisco_eventhash: %s", cisco_eventhash)
        self.log.info("cisco_filename: %s", cisco_filename)
        self.log.info("cisco_filehash: %s", cisco_filehash)
        self.log.info("cisco_externalurl: %s", cisco_externalurl)
        self.log.info("cisco_src: %s", cisco_src)

        basicdata = {
                "alertTime": cisco_alerttime,
                "deviceId": cisco_deviceid,
                "deviceVersion": cisco_deviceversion,
                "eventTime": cisco_eventtime,
                "protocolVersion": cisco_protocolversion,
                "providerName": cisco_providername,
                "dstDomain": cisco_dstdomain,
                "dstUrl": cisco_dsturl
                     }

        data = self.addothers(basicdata, cisco_dstip, cisco_eventseverity, cisco_eventtype, cisco_eventdescription, cisco_eventhash,
                  cisco_filename, cisco_filehash, cisco_externalurl, cisco_src)

        return data

    def _parseUrl(self, url_domain):
        """ split a url to also capture the domain """
        d = urlparse(url_domain)

        return d.geturl(), d.hostname if d.hostname else d.path

    # Adds the non mandatory parameters to the data object
    def addothers(self, data, cisco_dstip, cisco_eventseverity, cisco_eventtype, cisco_eventdescription, cisco_eventhash,
                  cisco_filename, cisco_filehash, cisco_externalurl, cisco_src):
        if cisco_dstip is not None:
            data['cisco_dstip'] = cisco_dstip
        if cisco_eventseverity is not None:
            data['cisco_eventseverity'] = cisco_eventseverity
        if cisco_eventtype is not None:
            data['cisco_eventtype'] = cisco_eventtype
        if cisco_eventdescription is not None:
            data['cisco_eventdescription'] = cisco_eventdescription
        if cisco_eventhash is not None:
            data['cisco_eventhash'] = cisco_eventhash
        if cisco_filename is not None:
            data['cisco_filename'] = cisco_filename
        if cisco_filehash is not None:
            data['cisco_filehash'] = cisco_filehash
        if cisco_externalurl is not None:
            data['cisco_externalurl'] = cisco_externalurl
        if cisco_src is not None:
            data['cisco_src'] = cisco_src

        return data
