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
from fn_proofpoint_tap.util.proofpoint_common import get_threat_list
from resilient_lib import RequestsCommon


log = logging.getLogger(__name__)

PROOFPOINT_ID_FIELDS = [
    'campaignId',   # in main body
    'campaignID',   # in threat map
    'messageID',
]

# do not rename the values in this dict - they match Proofpoint TAP values
artifact_types = {
    'Proofpoint Campaign ID': 'campaignId',
    'Proofpoint Threat ID': 'threatID',
}

timefields = [
    'threatTime',
    'messageTime',
    'clickTime',
]

# Map for Proofpoint threat type to Resilient incident type
TYPE_2_TYPE_ID_MAP = {
    u'impostor': u'Other',
    u'malware': u'Malware',
    u'phish': u'Phishing',
    u'spam': u'Other',
    u'unknown': u'TBD / Unknown',
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

        # Proofpoint score threshold
        self.score_threshold = float(self.options.get("score_threshold")) \
            if self.options.get("score_threshold") else None

        # Filter - Set types of incidents to import to Resilient
        self.id_type_filter = self._get_type_filter()

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

    def _get_type_filter(self):
        """
        Get set of type ids for the type_filter options if set, otherwise None.
        :return: set of threat ids
        """
        if 'type_filter' in self.options:
            type_filter = self.options.get('type_filter').strip().lower()
            if not type_filter or 'all' in type_filter:
                # none or "all" specified, no filtering
                return None

            filters = set()
            for typestring in type_filter.split(','):
                incident_type_id = self._get_incident_type_id(typestring.strip())
                if incident_type_id:
                    filters.add(incident_type_id)

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

        for field in PROOFPOINT_ID_FIELDS:
            value = data.get(field)
            if value is not None:
                properties[field] = value

        # pull the threat types from the data
        threat_types = self._get_threat_types(data)

        # map threat types to incident type ids and check to see if filtering is requested
        threat_type_ids = self._filtered_threat_types(threat_types)

        if threat_type_ids is None:
            log.debug("no threat_types, discarding")
            return None

        # look for threat name and classification in main body, else in threatsInfoMap
        threatsinfo = data.get('threatsInfoMap')
        threatinfo = threatsinfo[0] if threatsinfo else {}
        threatname = data.get('threat', threatinfo.get('threat'))
        classification = self._format_set(self._get_event_classification(data))

        return {
            'description': self.mkdescription(data, kind, threat_id, classification),
            'discovered_date': self.getdiscovereddate(data),
            'incident_type_ids': threat_type_ids,
            'name': 'Proofpoint TAP Event: {0} {1}'.format(threatname if threatname else "", classification),
            'properties': properties,
        }

    def mkdescription(self, data, kind, threat_id, classification):
        """Make Incident description text"""
        data[u'kind'] = kind
        data[u'id'] = threat_id
        data[u'classification'] = classification

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

    @staticmethod
    def _get_event_classification(data):
        """
        Get the "original" TAP classification for this event
        :param data:
        :return:
        """
        # Use set() to automatically avoid duplication and support disjoint filtering
        original_threat_types = set()

        # pull the threat type data from classification field
        event_classification = data.get('classification')
        if event_classification:
            original_threat_types.add(event_classification.lower())

        # examine Threat Info Map for possible threat types
        threatinfos = data.get('threatsInfoMap')
        if threatinfos:
            for threatinfo in threatinfos:  # There may be more than one threat per message.
                # check info map classification field
                event_classification = threatinfo.get('classification')
                if event_classification:
                    original_threat_types.add(event_classification.lower())

        return original_threat_types

    @staticmethod
    def _format_set(set_to_format):
        """
        Format content of set and return str.
        :param set_to_format:
        :return:
        """
        if not set_to_format or not isinstance(set_to_format, set):
            return "N/A"

        formatted_list = list(set_to_format)
        return ', '.join(formatted_list)

    def _get_threat_types(self, data):
        """
        Pull the the threat types from the data.
        :param data:
        :return: set with threat_types
        """
        # Get the TAP classification for this event
        original_threat_types = self._get_event_classification(data)
        log.debug("TAP event threat type classification is '{}'".format(self._format_set(original_threat_types)))

        # score_threshold is an optional param
        # if score_threshold was defined in the config file
        # filter the score values and pull appropriate threat types
        if self.score_threshold is not None:
            # extract spam, phishing, malware and imposter scores, if no value default is -1
            spamscore = float(data.get('spamScore', '-1'))
            phishscore = float(data.get('phishScore', '-1'))
            malwarescore = float(data.get('malwareScore', '-1'))
            imposterscore = float(data.get('impostorScore', '-1'))

            log.debug("spamScore {}".format(spamscore))
            log.debug("phishScore {}".format(phishscore))
            log.debug("malwareScore {}".format(malwarescore))
            log.debug("impostorScore {}".format(imposterscore))

            # create a copy of original_threat_types, keep the original values separate
            score_threat_types = original_threat_types.copy()

            self._check_if_score_above_threshold(spamscore, 'spam', score_threat_types)
            self._check_if_score_above_threshold(phishscore, 'phishing', score_threat_types)
            self._check_if_score_above_threshold(malwarescore, 'malware', score_threat_types)
            self._check_if_score_above_threshold(imposterscore, 'imposter', score_threat_types)

            if len(original_threat_types) != len(score_threat_types):
                log.debug("Updated threat type classification based on score values is '{}'".format(self._format_set(score_threat_types)))

            # validation for irregular results
            # example of an irregular result: if the TAP classification is "spam" and the score_threshold is set to 60
            # and the incoming spamscore is 50 and phishscore is 70 the code will remove "spam" from the threat_types
            # set (because it's lower than score_threshold) but will add "phishing" to the threat_types set making
            # the result inconsistent with the TAP classification of this event. In this case we log the error.

            # verify the size of the threat_types set, if it includes at least one element but it doesn't include
            # elements from original_threat_types then we have found an irregularity
            if len(score_threat_types) > 0:
                for orig_threat in original_threat_types:
                    if orig_threat not in score_threat_types:
                        log.info("Irregular result. The original TAP threat type classification '{}' was discarded "
                                 "because its score value is lower than the app.config score_threshold value. "
                                 "'{}' - updated threat type classification based on score values is inconsistent with "
                                 "'{}' - the original TAP event threat type classification.".format(
                        orig_threat, self._format_set(score_threat_types), self._format_set(original_threat_types)))

            return score_threat_types

        return original_threat_types

    def _check_if_score_above_threshold(self, score_value, score_type, threat_types):
        """
        If scores found and are higher then the score_threshold add the threat type to the set.
        Otherwise remove the threat type from the set if the set already contains it.
        :param score_value:
        :param score_type:
        :param threat_types:
        :return: threat_types
        """
        # if the endpoint didn't provide the score value then don't do any filtering based on the score
        if score_value == -1:
            return threat_types

        if score_value >= self.score_threshold:
            threat_types.add(score_type)
            log.debug("'{}' classification was added because its score value '{}' is higher "
                      "than the score_threshold value '{}'".format(score_type, score_value, self.score_threshold))
        else:
            if score_type in threat_types:
                threat_types.remove(score_type)
                log.debug("'{}' classification was removed because its score value '{}' is lower "
                          "than the score_threshold value '{}'".format(score_type, score_value, self.score_threshold))
        return threat_types

    def map_to_incident_type_ids(self, threat_types):
        """
        Map the threat types to incident type ids based on the class2typeids map.
        :param threat_types:
        :return: set of incident_type_ids
        """
        incident_type_ids = set()

        for threat_type in threat_types:
            inc_type_id = self._get_incident_type_id(threat_type)
            if inc_type_id:
                incident_type_ids.add(inc_type_id)

        return incident_type_ids

    def _filtered_threat_types(self, threat_types):
        """
        Map the threat types to incident type ids and check to see if filtering is requested.
        :param threat_types:
        :return: list of incident_type_ids or None
        """
        # Map the threat types to incident type ids
        incident_type_ids = self.map_to_incident_type_ids(threat_types)

        # check to see if filtering is requested
        if self.id_type_filter is None or self.id_type_filter.intersection(incident_type_ids):
            # no filter or incident type in filter, return list
            return list(incident_type_ids)

        log.info('incident types {} filtered due to {}'.format(incident_type_ids, self.id_type_filter))
        return None

    def _get_incident_type_id(self, threat_type):
        """
        Find the Resilient incident type id from class2typeids map for given threat type name.
        :param threat_type:
        :return: value
        """
        if not threat_type:
            return None

        for key, value in self.class2typeids.items():
            if key.lower() == threat_type.lower():
                return value

    def build_artifacts(self, data):
        """Build Artifacts containing Threat and Campaign IDs in Incident for further analysis"""
        artifact_payloads = {}

        maps = data.get('threatsInfoMap')
        if maps:
            for threat_map in maps:
                self._build_artifact_for_data(threat_map, artifact_payloads)

        else:
            self._build_artifact_for_data(data, artifact_payloads)

        return artifact_payloads

    @staticmethod
    def _build_artifact_for_data(data, artifact_payloads):
        """
        Add artifact type and value to the artifact_payload
        :param data:
        :param artifact_payloads:
        :return:
        """
        for key, value in artifact_types.items():
            artifact_id = data.get(value)
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
            for alternate, typeid in TYPE_2_TYPE_ID_MAP.items():
                if incident_type['label'] == typeid:
                    class2typeids[alternate] = incident_type['value']

        return class2typeids

    @staticmethod
    def find_id(threat):
        """
        Find ID key and ID for threat
        :param threat:
        :return: value for the chosen proofpoint field, idfield
        """
        for idfield in PROOFPOINT_ID_FIELDS:
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
