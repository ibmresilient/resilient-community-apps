#!/usr/bin/env python

# -*- coding: utf-8 -*-
# Resilient Systems, Inc. ("Resilient") is willing to license software
# or access to software to the company or entity that will be using or
# accessing the software and documentation and that you represent as
# an employee or authorized agent ("you" or "your") only on the condition
# that you accept all of the terms of this license agreement.
#
# The software and documentation within Resilient's Development Kit are
# copyrighted by and contain confidential information of Resilient. By
# accessing and/or using this software and documentation, you agree that
# while you may make derivative works of them, you:
#
# 1)  will not use the software and documentation or any derivative
#     works for anything but your internal business purposes in
#     conjunction your licensed used of Resilient's software, nor
# 2)  provide or disclose the software and documentation or any
#     derivative works to any third party.
#
# THIS SOFTWARE AND DOCUMENTATION IS PROVIDED "AS IS" AND ANY EXPRESS
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL RESILIENT BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
"""
Action to synchronize configured fields from one org to another org/instance
of resilient
"""

from __future__ import print_function
import os
import logging


import requests

import json

from ResilientOrg import ResilientOrg as ResOrg

from circuits import Component, Debugger
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent, ActionMessage

requests.packages.urllib3.disable_warnings()

# Lower the logging threshold for requests
logging.getLogger("requests.packages.urllib3").setLevel(logging.ERROR)

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
logging.Formatter('%(asctime)s:%(name)s:%(levelname)-8s %(message)s')


#log.setLevel(logging.DEBUG)  # force logging level to be DEBUG
CONFIG_DATA_SECTION = 'syncauto'
CONFIG_SOURCE_SECTION = 'resilient'
CONFIG_DEST_SECTION = 'resdestination'
CONFIG_SYNC_SECTION = 'syncconfig'


class PushHandler(ResilientComponent):
    """
    Object for resilient_circuits to invoke for push
    """
    # This component receives custom actions from Resilient and
    # executes searches in a local CSV file and stores it
    functionmap = [
        "stubfunction"
    ]

    def __init__(self, opts):
        super(PushHandler, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        self.source_opts = opts.get(CONFIG_SOURCE_SECTION, {})
        self.dest_opts = opts.get(CONFIG_DEST_SECTION, {})
        self.sync_opts = opts.get(CONFIG_SYNC_SECTION, {})
        log.debug("In init")
        log.debug(self.sync_opts)

        #self.sync_file = os.path.dirname(os.path.abspath(self.sync_opts.get('mapfile')))
        self.sync_file = os.path.abspath(self.sync_opts.get('mapfile'))
        log.debug("Syncfile = {}".format(self.sync_file))

        # The queue name can be specified in the config file, or default to 'filelookup'
        self.channel = "actions." + self.options.get("queue", "pushhandler")

        self.source_reso = ResOrg(client=self.rest_client)

        self.enums = self.source_reso.get_field_enums()
        self.users = self.source_reso.get_users()

    @handler("stubfunction")
    def _sync_action(self, event, *args, **kwargs):
        """The @handler() annotation without an event name makes this
           a default handler - for all events on this component's queue.
           This will be called with some "internal" events from Circuits,
           so you must declare the method with the generic parameters
           (event, *args, **kwargs), and ignore any messages that are not
           from the Actions module.
        """
        if not isinstance(event, ActionMessage):
            # Some event we are not interested in
            return

        log.debug("Event Name {}".format(event.name))

        func = self.get_function(event.name)
        if func is not None:
            retv = func(event)
            log.debug("-------------------------")
            if retv:
                yield retv
        else:
            raise Exception("Invalid event - no function to handle")

        yield "event handled"
        #end _invite_action


    def stubfunction(self, args):
        """
        method invoked based on the action name
        """
        log.debug("Stub function")
        with open(self.sync_file) as jdata:
            fieldmap = json.load(jdata)

        # create connection to the destination
        dest_reso = ResOrg(opts=self.dest_opts)
        source_incident = self.source_reso.get_incident_by_id(args.incident.get('id'))
        source_crosslink = source_incident.get('properties').get(fieldmap.get('crosslink').get('sourcefield'))
        if source_crosslink == "" or source_crosslink == 0 or source_crosslink is None:
            log.debug("Cross link is not set >{}<".format(source_crosslink))
        else:
            log.info("Cross link is set >{}<".format(source_crosslink))
            return "Cross link already set"

        # initialize the template for the new incident
        destdata = {}
        destdata['properties'] = {}
        for field in fieldmap.get('fields'):
            log.debug("FMAP = {}".format(field))
            source_loc = field.get('sourceloc')  # get the source location
            s_type = field.get('sourcetype')
            s_field = field.get('sourcefield')
            if source_loc  not in ['action', 'incident']:
                # only handle source data from Action fields and Incident fields
                log.warn("invalid source location in mapping:{}".format(field))
                continue  # just ignore this mapping definition

            if field.get('destcustom', False) is True:
                destinfo = destdata.get('properties')
            else:
                destinfo = destdata

            if  s_type in ['select', 'multiselect']:
                # set up the source of information
                if source_loc == 'action':
                    s_enum_defs = args['message']['type_info']['actioninvocation']['fields'].get(s_field)['values']
                    # there is a separate function for mapping action fields to their string value
                    # so the source list is the same as the enum definitions
                    slist = s_enum_defs
                    sourceinfo = args.properties
                    source_map_fcn = self.map_action_enum  # specify the mapping function for the
                    log.debug("source is action, info is args properties")
                elif source_loc == 'incident':
                    s_enum_defs = self.source_reso.get_field_enums_by_type(field.get('sourceloc'))
                    # get the list of enumeration values for the source field
                    slist = s_enum_defs.get(field.get('sourcefield'))
                    if field.get('sourcecustom', False) is True:
                        sourceinfo = source_incident.get('properties')
                        log.debug("Source info is incident properties")
                    else:
                        sourceinfo = source_incident
                        log.debug("Source info is incident ")
                    source_map_fcn = self.map_incident_enum  # specify the mapping function for the source
                                                             # this is the incident data mapping
                else:
                    continue  # unsuppoorted source location just skip

                d_enum_defs = dest_reso.get_field_enums_by_type(field.get('destloc'))
                # get the list of enumerations for the destination field
                dlist = d_enum_defs.get(field.get('destfield'))


                if s_type == 'select':
                    # select is mapping a single value
                    s_enum = source_map_fcn(sourceinfo.get(field.get('sourcefield')), slist)
                    d_enum = self.map_incident_enum(s_enum, dlist)

                elif s_type == 'multiselect':
                    # multi select needs to build a list of the enumerations
                    s_enum = []
                    svals = sourceinfo.get(field.get('sourcefield'))
                    # convert the numeric values to their string values for the source data
                    for val in svals:
                        mapv = source_map_fcn(val, slist)
                        if mapv is not None:
                            s_enum.append(mapv)

                    d_enum = []
                    # map the source strings to their destination numeric values
                    for val in s_enum:
                        mapv = self.map_incident_enum(val, dlist)
                        if mapv is not None:
                            d_enum.append(mapv)
                else:
                    d_enum = sourceinfo.get(field.get('sourcefield'))

                destinfo[field.get('destfield')] = d_enum
                log.debug("destdata {}".format(destdata))

            else:  # just copy the field data
                log.debug("Source field = {} val {}".format(field.get('sourcefield'), sourceinfo.get(field.get('sourcefield'))))
                destinfo[field.get('destfield')] = sourceinfo.get(field.get('sourcefield'))
                log.debug("destdata {}".format(destdata))



        # check if name and description have been mapped.  if not, always mapp name and description
        if destdata.get('name', None) is None:
            # name was not mapped, so we always map Name and Description
            destdata['name'] = source_incident.get('name')
        if destdata.get('description', None) is None:
            # description was not mapped, so we force the mapping
            destdata['description'] = source_incident.get('description')

        # set up the cross link information
        # if its not set, then we don't do a cross link.  NOTE: not having a cross link could result in multiple
        # records being created in the destination org
        crosslinks = fieldmap.get('crosslink', None)
        if crosslinks is not None:
            # cross link is always set in destination
            destdata['properties'][crosslinks.get('destfield')] = source_incident.get('id')

        # Force discovered_date for new case to be the same as the originating case
        # regardless of mapping
        destdata['discovered_date'] = source_incident.get('discovered_date')
        log.debug(destdata)


        # if the cross link in the source has already been set, then just skip.  Probably should move thie earlier in the handler since
        # there is no need to do the mapping.
        if source_incident['properties'][crosslinks.get('sourcefield')] is None or source_incident['properties'][crosslinks.get('sourcefield')] == "":
            (dest_incident, error) = dest_reso.create_case(destdata)
            #if the incident was created, then update the source incident cross link
            if dest_incident is None:
                log.error("ERROR creating destination incident: {}".format(error))
            else:
                log.debug("Incident id {} created".format(dest_incident.get('id')))
                source_incident['properties'][crosslinks.get('sourcefield')] = dest_incident.get('id')
                # this really should be a get_put of the source incident in case something changed
                self.source_reso.put_case(source_incident)
        else:
            log.info("source cross link has already been set")
            return "Destination case already created"

        return "Destination case {} created".format(dest_incident.get('id'))


    def map_incident_enum(self, value, enums):
        """
        map enumerations
        """
        log.debug("map incident enum")
        for enum in enums:
            if enum.get(value, None) is not None:
                return int(enum.get(value))
        return None

    def map_action_enum(self, value, typeinfo):
        log.debug("Map action enum {}".format(typeinfo))
        for itypeinfo in typeinfo:  #walk through the values and find the one that matches
            if itypeinfo == str(value):
                tinfo = typeinfo.get(itypeinfo)
                log.debug(tinfo)

                ilabel = tinfo.get('label')
                log.debug("MapAction enum {}".format(ilabel))
                return ilabel
        return None

    def get_function(self, funcname):
        if funcname in PushHandler.functionmap:
            log.debug("get function {}".format(funcname))
            return getattr(self, '%s'%funcname)
        log.debug("get function none")
        return None


