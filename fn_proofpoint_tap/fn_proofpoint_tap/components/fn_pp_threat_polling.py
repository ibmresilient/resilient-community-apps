# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""Polling implementation"""

import calendar
import jinja2
import logging
import os
import time
from datetime import datetime
from threading import Thread
from resilient_circuits import ResilientComponent, handler, template_functions
from resilient import SimpleHTTPException
from pkg_resources import Requirement, resource_filename
from fn_proofpoint_tap.components.get_threat_list import get_threat_list
from resilient_lib import RequestsCommon


log = logging.getLogger(__name__)

idfields = [
    'campaignId',   # in main body
    'campaignID',   # in threat map
    'messageID',
]

artifact_types = {
    'Proofpoint Campaign ID': 'campaignID',
    'Proofpoint Threat ID': 'threatID',
}

timefields = [
    'threatTime',
    'messageTime',
    'clickTime',
]

type2typeid = {
    'MALWARE': 'Malware',
    'phish': 'Phishing',
    'Spam': 'Other',
    'Unknown': 'TBD / Unknown',
}

threats_info_map = {
    'threat_id': 'threatID',
    'threat_status': 'threatStatus',
    'classification': 'classification',
    'threat_url': 'threatUrl',
    'threat': 'threat',
}

data_table_ids = [
    'threat_info_map',
]


class PP_ThreatPolling(ResilientComponent):
    """Component that polls for new data arriving from Proofpoint"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(PP_ThreatPolling, self).__init__(opts)

        current_path = os.path.dirname(os.path.realpath(__file__))
        self.default_path = os.path.join(current_path, os.path.pardir, "data/templates/pp_threat_description.jinja")
        self.class2typeids = self.getclass2typeids()
        self.lastupdate = None
        self._parseopts(opts)
        self.main()

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self._parseopts(opts)

    def _parseopts(self, opts):
        """Parse and process configuration options, called from __init__ and _reload"""
        self.opts = opts
        self.options = opts.get("fn_proofpoint_tap", {})

        # Proofpoint score
        self.score_threshold = float(self.options.get("score_threshold")) \
            if self.options.get("score_threshold") else None
        # Types of incidents to import to Resilient
        self.type_filter = self.gettypefilter()

        # Create a new Resilient incident from this event
        # using an optional JSON (JINJA2) template file
        threat_path = self.options.get("threat_template", self.default_path)
        if threat_path and not os.path.exists(threat_path):
            log.warn(u"Template file '%s' not found.", threat_path)
            threat_path = None
        if not threat_path:
            # Use the template file installed by this package
            threat_path = resource_filename(Requirement("fn-proofpoint_tap"), "fn_proofpoint_tap/data/templates/pp_threat_description.jinja")
            if not os.path.exists(threat_path):
                raise Exception(u"Template file '{}' not found".format(threat_path))

        log.info(u"Template file: %s", threat_path)
        with open(threat_path, "r") as threat_file:
            self.threat_template = threat_file.read()

        # initialize last update to startup interval if present, otherwise update interval
        interval = self.options.get('startup_interval')
        if interval is None or interval.strip() == "":
            self.lastupdate = None
        else:
            self.lastupdate = 60 * int(interval)

    def gettypefilter(self):
        """get lowercase set of type filter options if set, otherwise None"""
        if 'type_filter' in self.options:
            type_filter = self.options.get('type_filter').lower()
            if not type_filter or type_filter == 'all':
                # none or "all" specified, no filtering
                return None
            filters = set()
            for typestring in type_filter.split(','):
                for threat_type, threat_id in self.class2typeids.items():
                    if threat_type.lower() == typestring:
                        filters.add(threat_id)

            return filters

    def main(self):
        """main entry point, instantiate polling thread"""
        options = self.options
        interval = int(options.get("polling_interval", 0))

        if interval > 0:
            # Create and start polling thread
            thread = Thread(target=self.polling_thread)
            thread.daemon = True
            thread.start()
            log.info("Polling for threats in Proofpoint every {0} minutes".format(interval))
        else:
            log.info("Polling for threats in Proofpoint not enabled")

    def polling_thread(self):
        """contents of polling thread, alternately check for new data and wait"""
        cafile = self.options.get('cafile')
        bundle = os.path.expanduser(cafile) if cafile else False
        rc = RequestsCommon(opts=self.opts, function_opts=self.options)

        while True:
            try:
                threat_list = get_threat_list(rc, self.options, self.lastupdate, bundle)
                for kind, datas in threat_list.items():
                    if kind == 'queryEndTime':
                        self.lastupdate = datas
                    else:
                        for data in datas:
                            incident_id = None
                            threat_id, idtype = self.find_id(data)
                            existing_incidents = self._find_resilient_incident_for_req(threat_id, idtype)
                            if len(existing_incidents) == 0:
                                # incident doesn't already exist, create Incident data
                                incident_payload = self.build_incident_dto(data, kind, threat_id)
                                if incident_payload is not None:
                                    incident_id = self.create_incident(incident_payload)
                                    log.debug('created Incident ID {}'.format(incident_id))
                                else:
                                    log.debug('Incident filtered')
                            else:
                                # incident already exists, extract its ID
                                log.debug('incident {} {} already exists'.format(idtype, threat_id))
                                incident_id = existing_incidents[0]['id']

                            if incident_id is not None:
                                # created or found an Incident, attach any (possibly new) artifacts
                                artifact_payloads = self.build_artifacts(data)
                                self.update_incident(incident_id, artifact_payloads)
            except Exception as err:
                log.error(err)

            # Amount of time (seconds) to wait to check cases again, defaults to 10 mins if not set
            time.sleep(int(self.options.get("polling_interval", 10)) * 60)

    def build_incident_dto(self, data, kind, threat_id):
        """build Incident data structure in Resilient DTO format"""
        properties = {}

        for field in idfields:
            value = data.get(field)
            if value is not None:
                properties[field] = value

        threat_types = self.getincidenttypes(data)

        if threat_types is None:
            log.debug("no threat_types, discarding")
            return None

        # look for threat type and classification in main body, else in threatsInfoMap

        threatsinfo = data.get('threatsInfoMap')
        threatinfo = threatsinfo[0] if threatsinfo else {}
        threatname = data.get('threat', threatinfo.get('threat'))
        classification = data.get('classification', threatinfo.get('classification'))

        return {
            'description': self.mkdescription(data, kind, threat_id),
            'discovered_date': self.getdiscovereddate(data),
            'incident_type_ids': threat_types,
            'name': '{0} {1}'.format(threatname, classification),
            'properties': properties,
        }

    def mkdescription(self, data, kind, threat_id):
        """Make Incident description text"""
        data['kind'] = kind
        data['id'] = threat_id

        try:
            return {'format': 'text', 'content': template_functions.render(self.threat_template, data)}

        except jinja2.exceptions.TemplateSyntaxError:
            log.info('threat template is not set correctly in config file')

    @staticmethod
    def getdiscovereddate(data):
        """Find field to use for discovered date, convert to millisecond timestamp"""
        for field in timefields:
            if field in data:
                val = data.get(field)
                ts_format = '%Y-%m-%dT%H:%M:%S.%fZ'

                if not val:
                    continue
                try:
                    dt = datetime.strptime(val, ts_format)
                    log.debug('dt is {}'.format(dt))
                    seconds = calendar.timegm(dt.utctimetuple())
                    millis = int(dt.microsecond / 1000)
                    combined = seconds * 1000 + millis
                    log.debug('seconds {} millis {} combined {}'.format(seconds, millis, combined))
                    return combined
                except ValueError:
                    log.exception("{} Not in expected timestamp format {}".format(val, ts_format))

    def getincidenttypes(self, data):
        """Figure out what Incident types this threat is"""
        # Use set() to automatically avoid duplication and support disjoint filtering
        incident_types = set()
        # Try classification field
        incident_type = self.class2typeids.get(data.get('classification'))
        if incident_type:
            incident_types.add(incident_type)

        # examine Threat Info Map for possible Incident types

        threatinfos = data.get('threatsInfoMap')

        if threatinfos:
            for threatinfo in threatinfos:
                # check info map classification field
                incident_type = self.class2typeids.get(threatinfo.get('classification'))
                if incident_type:
                    incident_types.add(incident_type)

        # extract spam, phishing, and malware scores
        spamscore = float(data.get('spamScore', '0'))
        phishscore = float(data.get('phishScore', '0'))
        malwarescore = float(data.get('malwareScore', '0'))

        # if scores found and nonzero, see which are higher
        if spamscore and phishscore and malwarescore:
            if spamscore > phishscore and spamscore > malwarescore:
                # spam
                if self.score_threshold is not None and spamscore < self.score_threshold:
                    log.info('spam score {} < {}, filtering'.format(spamscore, self.score_threshold))
                    return
                incident_types.add(self.class2typeids.get('Spam'))

            if phishscore >= spamscore and phishscore > malwarescore:
                # phishing
                if self.score_threshold is not None and phishscore < self.score_threshold:
                    log.info('phishing score {} < {}, filtering'.format(phishscore, self.score_threshold))
                    return
                incident_types.add(self.class2typeids.get('Phishing'))

            if malwarescore > spamscore and malwarescore > phishscore:
                # malware
                if self.score_threshold is not None and malwarescore < self.score_threshold:
                    log.info('malware score {} < {}, filtering'.format(malwarescore, self.score_threshold))
                    return
                incident_types.add(self.class2typeids.get('Malware'))

        if not incident_types:
            # didn't match any known incident types
            incident_types.add(self.class2typeids.get('Unknown'))

        # check to see if filtering is requested
        if self.type_filter is None or not self.type_filter.isdisjoint(incident_types):
            # no filter or incident type in filter, return list
            return list(incident_types)

        log.info('incident types {} filtered due to {}'.format(incident_types, self.type_filter))

    @staticmethod
    def build_artifacts(data):
        """Build Artifacts containing Threat and Campaign IDs in Incident for further analysis"""
        artifact_payloads = {}

        maps = data.get('threatsInfoMap')

        if not maps:
            return artifact_payloads

        for threat_map in maps:
            for key, value in artifact_types.items():
                artifact_id = threat_map.get(value)
                if artifact_id is not None:
                    log.debug('artifact type {} ({}) ID {}'.format(key, value, artifact_id))
                    artifact_payloads[artifact_id] = key

        return artifact_payloads

    def create_incident(self, data):
        """Create Resilient Incident"""
        try:
            resilient_client = self.rest_client()
            uri = '/incidents'
            # create Incident itself first
            incident_response = resilient_client.post(uri=uri, payload=data)
            # extract new Incident ID from response
            return incident_response['id']

        except SimpleHTTPException as ex:
            log.info('Something went wrong when attempting to create the Incident: {}'.format(ex))

    def update_incident(self, incident_id, artifacts):
        """Update Resilient Incident"""
        try:
            resilient_client = self.rest_client()
            artifact_uri = '/incidents/{}/artifacts'.format(incident_id)

            # set up Artifact payload skeleton
            artifact_payload = {
                'type': {
                    'name': 'String',
                },
                'description': {
                    'format': 'text',
                }
            }

            # find artifacts that are already associated with this Incident
            existing_artifacts = self._find_resilient_artifacts_for_incident(incident_id)

            # loop through Artifacts provided with this Threat
            for artifact_id, artifact_type in artifacts.items():
                # if this Artifact doesn't match an existing value and type
                if artifact_id not in existing_artifacts or existing_artifacts[artifact_id] != artifact_type:
                    # populate payload with ID and type
                    artifact_payload['value'] = artifact_id
                    artifact_payload['description']['content'] = artifact_type
                    # attach new Artifact to Incident
                    resilient_client.post(uri=artifact_uri, payload=artifact_payload)

        except SimpleHTTPException as ex:
            log.info('Something went wrong when attempting to create the Incident: {}'.format(ex))

    def getclass2typeids(self):
        """Extract incident types from Resilient, build mapping from names to IDs"""
        class2typeids = {}
        for incident_type in self._fields['incident_type_ids']['values']:
            # install canonical name
            class2typeids[incident_type['label']] = incident_type['value']
            # install alternate names
            for alternate, typeid in type2typeid.items():
                if incident_type['label'] == typeid:
                    class2typeids[alternate] = incident_type['value']

        return class2typeids

    @staticmethod
    def find_id(threat):
        """Find ID key and ID for threat"""
        for idfield in idfields:
            if idfield in threat:
                return threat[idfield], idfield

    def _find_resilient_artifacts_for_incident(self, incident_id):
        """Return list of artifacts for the given Incident ID, else returns empty list"""
        r_artifacts = {}
        resilient_client = self.rest_client()
        artifacts_uri = '/incidents/{}/artifacts'.format(incident_id)
        artifact_results = resilient_client.get(uri=artifacts_uri)

        if artifact_results is not None:
            for artifact_result in artifact_results:
                artifact_type = artifact_result.get('description')
                if artifact_type in artifact_types:
                    r_artifacts[artifact_result['value']] = artifact_type

        return r_artifacts

    def _find_resilient_incident_for_req(self, threat_id, idtype):
        """Return list of incidents if there are any with the same case ID, else returns empty list"""
        resilient_client = self.rest_client()
        query_uri = '/incidents/query?return_level=partial'
        query = {
            'filters': [{
                'conditions': [
                    {
                        'field_name': 'properties.{}'.format(idtype),
                        'method': 'equals',
                        'value': threat_id
                    },
                    {
                        'field_name': 'plan_status',
                        'method': 'equals',
                        'value': 'A'
                    }
                ]
            }],
            'sorts': [{
                'field_name': 'create_date',
                'type': 'desc'
            }]
        }
        try:
            r_incidents = resilient_client.post(query_uri, query)
        except SimpleHTTPException:
            # Some versions of Resilient 30.2 onward have a bug that prevents query for numeric fields.
            # To work around this issue, let's try a different query, and filter the results. (Expensive!)
            query_uri = '/incidents/query?return_level=normal&field_handle={}'.format(threat_id)
            query = {
                'filters': [{
                    'conditions': [
                        {
                            'field_name': 'properties.{}'.format(idtype),
                            'method': 'has_a_value'
                        },
                        {
                            'field_name': 'plan_status',
                            'method': 'equals',
                            'value': 'A'
                        }
                    ]
                }]
            }
            r_incidents_tmp = resilient_client.post(query_uri, query)
            r_incidents = [r_inc for r_inc in r_incidents_tmp
                           if r_inc['properties'].get(idtype) == threat_id]

        return r_incidents
