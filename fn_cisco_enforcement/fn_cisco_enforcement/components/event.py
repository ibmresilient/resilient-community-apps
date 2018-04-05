# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""
# Copyright IBM Corp. - Confidential Information
import logging
import requests
import datetime
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

# This adds an event using the Cisco Event api. The inputs can be found with a description of the api here https://docs.umbrella.com/developer/enforcement-api/events2/
# The apikey is refernced in the app.config under [fn_cisco_enforcement]

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'event"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cisco_enforcement", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_enforcement", {})

    @function("event")
    def _event_function(self, event, *args, **kwargs):
        """Function: This is a function implementation that uses the Cisco API to post a Malware event"""
        try:
            data=self.createdataobject(kwargs)
            apikey=self.options.get('apikey')
            api = "https://s-platform.api.opendns.com/1.0/events?customerKey={}".format(apikey)
            respose=requests.post(api,json=data, verify=False)

            results = {
                "value": respose.content
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()

    # Creates the data object to send
    def createdataobject(self,kwargs):
        # Get the function parameters:
        cisco_deviceid = str(kwargs.get("cisco_deviceid"))  # text
        cisco_deviceversion = str(kwargs.get("cisco_deviceversion"))  # text

        cisco_eventtime = datetime.datetime.utcfromtimestamp(kwargs.get("cisco_eventtime")/1000).strftime('%Y-%m-%dT%H:%M:%SZ')  # datetimepicker
        cisco_alerttime = datetime.datetime.utcfromtimestamp(kwargs.get("cisco_alerttime")/1000).strftime('%Y-%m-%dT%H:%M:%SZ')  # datetimepicker
        cisco_dsturl = str(kwargs.get("cisco_dsturl"))  # text
        cisco_dstdomain = str(kwargs.get("cisco_dstdomain"))  # text
        cisco_protocolversion = str(kwargs.get("cisco_protocolversion"))  # text
        cisco_providername = str(kwargs.get("cisco_providername"))  # text
        cisco_disabledstsafeguards = str(kwargs.get("cisco_disabledstsafeguards"))  # text

        cisco_dstip = kwargs.get("cisco_dstip")  # text
        cisco_eventseverity = kwargs.get("cisco_eventseverity")  # text
        cisco_eventtype = kwargs.get("cisco_eventtype")  # text
        cisco_eventdescription = kwargs.get("cisco_eventdescription")  # text
        cisco_eventhash = kwargs.get("cisco_eventhash")  # text
        cisco_filename = kwargs.get("cisco_filename")  # text
        cisco_filehash = kwargs.get("cisco_filehash")  # text
        cisco_externalurl = kwargs.get("cisco_externalurl")  # text
        cisco_src = kwargs.get("cisco_src")  # text

        log = logging.getLogger(__name__)
        log.info("cisco_deviceid: %s", cisco_deviceid)
        log.info("cisco_deviceversion: %s", cisco_deviceversion)
        log.info("cisco_eventtime: %s", cisco_eventtime)
        log.info("cisco_alerttime: %s", cisco_alerttime)
        log.info("cisco_dstdomain: %s", cisco_dstdomain)
        log.info("cisco_protocolversion: %s", cisco_protocolversion)
        log.info("cisco_providername: %s", cisco_providername)
        log.info("cisco_disabledstsafeguards: %s", cisco_disabledstsafeguards)
        log.info("cisco_dstip: %s", cisco_dstip)
        log.info("cisco_eventseverity: %s", cisco_eventseverity)
        log.info("cisco_eventtype: %s", cisco_eventtype)
        log.info("cisco_eventdescription: %s", cisco_eventdescription)
        log.info("cisco_eventhash: %s", cisco_eventhash)
        log.info("cisco_filename: %s", cisco_filename)
        log.info("cisco_filehash: %s", cisco_filehash)
        log.info("cisco_externalurl: %s", cisco_externalurl)
        log.info("cisco_src: %s", cisco_src)

        basicdata = {"alertTime": cisco_alerttime,
                "deviceId": cisco_deviceid,
                "deviceVersion": cisco_deviceversion,
                "dstDomain": cisco_dstdomain,
                "dstUrl": cisco_dsturl,
                "eventTime": cisco_eventtime,
                "protocolVersion": cisco_protocolversion,
                "providerName": cisco_providername}

        data=self.addothers(basicdata, cisco_dstip, cisco_eventseverity, cisco_eventtype, cisco_eventdescription, cisco_eventhash,
                  cisco_filename, cisco_filehash, cisco_externalurl, cisco_src)

        return data

    # Adds the non mandatory parameters to the data object
    def addothers(self,data,cisco_dstip,cisco_eventseverity,cisco_eventtype,cisco_eventdescription,cisco_eventhash,cisco_filename,cisco_filehash,cisco_externalurl,cisco_src):
        if cisco_dstip !=None:
            data['cisco_dstip']=cisco_dstip
        if cisco_eventseverity!=None:
            data['cisco_eventseverity']=cisco_eventseverity
        if cisco_eventtype!=None:
            data['cisco_eventtype']=cisco_eventtype
        if cisco_eventdescription!=None:
            data['cisco_eventdescription']=cisco_eventdescription
        if cisco_eventhash!=None:
            data['cisco_eventhash']=cisco_eventhash
        if cisco_filename!=None:
            data['cisco_filename']=cisco_filename
        if cisco_filehash!=None:
            data['cisco_filehash']=cisco_filehash
        if cisco_externalurl!=None:
            data['cisco_externalurl']=cisco_externalurl
        if cisco_src!=None:
            data['cisco_src']=cisco_src

        return data
