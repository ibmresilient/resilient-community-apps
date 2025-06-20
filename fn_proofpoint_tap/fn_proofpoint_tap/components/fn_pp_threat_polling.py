# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.

"""Polling implementation"""

import calendar
import logging
import os
import time
from datetime import datetime
from threading import Thread
import jinja2
from resilient_circuits import ResilientComponent, handler, template_functions
from resilient import SimpleHTTPException
from pkg_resources import Requirement, resource_filename
from resilient_lib import RequestsCommon
from resilient_lib import get_artifacts
from fn_proofpoint_tap.util.proofpoint_common import get_threat_list


log = logging.getLogger(__name__)

PROOFPOINT_ID_FIELDS = [
    'campaignId',   # in main body
    'campaignID',   # in threat map
    'messageID',
]

# do not rename the values in this dict - they match Proofpoint TAP values
ARTIFACT_TYPES = {
    'Proofpoint Campaign ID': ['campaignId', 'campaignID'],
    'Proofpoint Threat ID': ['threatID'],
}

ARTIFACT_TYPE_API_NAME = {
    'Proofpoint Campaign ID': 'proofpoint_campaign_id',
    'Proofpoint Threat ID': 'proofpoint_threat_id'
}

timefields = [
    'threatTime',
    'messageTime',
    'clickTime',
]

# Map for Proofpoint threat type to Resilient incident type
TYPE_2_TYPE_ID_MAP = {
    'impostor': 'Other',
    'malware': 'Malware',
    'phish': 'Phishing',
    'spam': 'Other',
    'unknown': 'TBD / Unknown',
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
        super().__init__(opts)

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

        # Type Filters  - Set of incident type filters by name.
        self.type_filter  = self._get_type_filter(self.options.get("type_filter", None))
        # Create a new Resilient incident from this event
        # using an optional JSON (JINJA2) template file
        threat_path = self.options.get("threat_template", self.default_path)
        if threat_path and not os.path.exists(threat_path):
            log.warning("Template file '%s' not found.", threat_path)
            threat_path = None
        if not threat_path:
            # Use the template file installed by this package
            threat_path = resource_filename(Requirement("fn-proofpoint_tap"), "fn_proofpoint_tap/data/templates/pp_threat_description.jinja")
            if not os.path.exists(threat_path):
                raise Exception("Template file '{}' not found".format(threat_path))

        log.info("Template file: %s", threat_path)
        with open(threat_path, "r") as threat_file:
            self.threat_template = threat_file.read()

        # initialize last update to startup interval if present, otherwise update interval
        interval = self.options.get('startup_interval')
        if interval is None or interval.strip() == "":
            self.lastupdate = None
        else:
            self.lastupdate = 60 * int(interval)

    def _get_type_filter(self, tp_filter):
        """
        Get set of filter types by name for the type_filter option.

        :return: Type filter set.
        """

        if not tp_filter:
            return None

        type_filter = tp_filter.strip().lower()
        if not type_filter or 'all' in type_filter:
            # none or "all" specified, no filtering
            return None

        filters_by_name = set()

        for typestring in type_filter.split(','):
            t_f = typestring.strip()

            if t_f in TYPE_2_TYPE_ID_MAP:
                filters_by_name.add(t_f)
            else:
                log.info(f"Invalid incident type filter option '{t_f}'.")

        return filters_by_name

    def main(self):
        """main entry point, instantiate polling thread"""
        options = self.options
        interval = int(options.get("polling_interval", 0))

        if interval > 0:
            # Create and start polling thread
            thread = Thread(target=self.polling_thread)
            thread.daemon = True
            thread.start()
            log.info(f"Polling for threats in Proofpoint every {interval} minutes")
        else:
            log.info("Polling for threats in Proofpoint not enabled")

    def polling_thread(self):
        """contents of polling thread, alternately check for new data and wait"""
        cafile = self.options.get('cafile')
        bundle = os.path.expanduser(cafile) if cafile else False
        rc = RequestsCommon(opts=self.opts, function_opts=self.options)
        siem_event_types_string =  self.options.get('siem_event_types') if self.options.get('siem_event_types') != "" else "siem_all"
        siem_event_types = [event_type.strip() for event_type in siem_event_types_string.split(",")]

        while True:
            try:
                # Loop through user selected SIEM endpoints to poll and process threats
                for siem_event_type in siem_event_types:
                    threat_list = get_threat_list(rc, self.options, self.lastupdate, bundle, siem_event_type)
                    self.process_threat_list(threat_list)
            except Exception as err:
                log.error(err)

            # Amount of time (seconds) to wait to check cases again, defaults to 10 mins if not set
            time.sleep(int(self.options.get("polling_interval", 10)) * 60)

    def process_threat_list(self, threat_list):
        """ Process a list to Proofpoint TAP threats and create incidents if not in SOAR otherwise update the incident. """
        for kind, datas in threat_list.items():
            if kind == 'queryEndTime':
                self.lastupdate = datas
                continue
            for data in datas:
                incident_id = None
                threat_id, idtype = self.find_id(data)
                if not threat_id:
                    log.error("Threat ID not found for ProofPoint TAP event '%s' of kind '%s'.", data, kind)
                    continue
                existing_incidents = self._find_resilient_incident_for_req(threat_id, idtype)
                if len(existing_incidents) == 0:
                    # incident doesn't already exist, create Incident data
                    incident_payload = self.build_incident_dto(data, kind, threat_id)
                    if incident_payload:
                        incident_id = self.create_incident(incident_payload)
                        log.debug(f"created Incident ID {incident_id}")
                    else:
                        log.debug('Incident filtered')
                else:
                    # incident already exists, extract its ID
                    log.debug(f"incident {idtype} {threat_id} already exists")
                    incident_id = existing_incidents[0]['id']

                if incident_id:
                    # created or found an Incident, attach any (possibly new) artifacts
                    artifact_payloads = self.build_artifacts(data)
                    self.update_incident(incident_id, artifact_payloads)

    def build_incident_dto(self, data, kind, threat_id):
        """build Incident data structure in Resilient DTO format"""
        properties = {}

        for field in PROOFPOINT_ID_FIELDS:
            value = data.get(field)
            if value:
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
        data['kind'] = kind
        data['id'] = threat_id
        data['classification'] = classification

        try:
            return {'format': 'text', 'content': template_functions.render(self.threat_template, data)}

        except jinja2.exceptions.TemplateSyntaxError as err:
            log.info(f"threat template is not set correctly in config file {err}")
            raise err

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
                    log.debug(f"dt is {dt}")
                    seconds = calendar.timegm(dt.utctimetuple())
                    millis = int(dt.microsecond / 1000)
                    combined = seconds * 1000 + millis
                    log.debug(f"seconds {seconds} millis {millis} combined {combined}")
                    return combined
                except ValueError as err:
                    log.exception(f"{val} Not in expected timestamp format {ts_format} - {err}")
                    raise err

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
        if set_to_format is None or not isinstance(set_to_format, set):
            return "N/A"

        if len(set_to_format) == 0:
            return "None"

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
        log.debug(f"TAP event threat type classification is '{self._format_set(original_threat_types)}'")

        # score_threshold is an optional param
        # if score_threshold was defined in the config file
        # filter the score values and pull appropriate threat types
        if self.score_threshold:
            # extract spam, phishing, malware and impostor scores, if no value default is -1
            spamscore = float(data.get('spamScore', '-1'))
            phishscore = float(data.get('phishScore', '-1'))
            malwarescore = float(data.get('malwareScore', '-1'))
            impostorscore = float(data.get('impostorScore', '-1'))

            log.debug(f"spamScore {spamscore}")
            log.debug(f"phishScore {phishscore}")
            log.debug(f"malwareScore {malwarescore}")
            log.debug(f"impostorScore {impostorscore}")

            # create a copy of original_threat_types, keep the original values separate
            score_threat_types = original_threat_types.copy()

            self._check_if_score_above_threshold(spamscore, 'spam', score_threat_types)
            self._check_if_score_above_threshold(phishscore, 'phishing', score_threat_types)
            self._check_if_score_above_threshold(malwarescore, 'malware', score_threat_types)
            self._check_if_score_above_threshold(impostorscore, 'impostor', score_threat_types)

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
        if score_value < 0:
            return threat_types

        if score_value >= self.score_threshold:
            threat_types.add(score_type)
            log.debug(f"'{score_type}' classification was added because its score value '{score_value}' is higher than the score_threshold value '{self.score_threshold}'")
        else:
            if score_type in threat_types:
                threat_types.remove(score_type)
                log.debug(f"'{score_type}' classification was removed because its score value '{score_value}' is lower than the score_threshold value '{self.score_threshold}'")
        return threat_types

    def map_to_incident_type_ids(self, threat_types):
        """
        Map the threat types to incident type ids based on the class2typeids map.
        :param threat_types:
        :return: set of incident_type_ids
        """
        incident_type_ids = set()

        if not threat_types:
            return incident_type_ids

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
        if self.type_filter is None or self.type_filter.intersection(threat_types):
            # no filter or incident type in filter, return list
            return list(incident_type_ids)

        log.info(f"Events with threat type '{self._format_set(threat_types)}' have been filtered due to type_filter set in app.config")
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

        log.debug(artifact_payloads)
        return artifact_payloads

    @staticmethod
    def _build_artifact_for_data(data, artifact_payloads):
        """
        Add artifact type and value to the artifact_payload
        :param data:
        :param artifact_payloads:
        :return:
        """
        for artifact_type, pp_keys in ARTIFACT_TYPES.items():
            for pp_key in pp_keys:
                artifact_id = data.get(pp_key)
                if artifact_id:
                    log.debug(f"artifact type {artifact_type} ({pp_key}) ID {artifact_id}")
                    artifact_payloads[artifact_id] = artifact_type

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
            log.info(f"Something went wrong when attempting to create the Incident: {ex}")
            raise ex

    def update_incident(self, incident_id, artifacts):
        """Update Resilient Incident"""
        try:
            resilient_client = self.rest_client()
            artifact_uri = get_artifacts(res_client=resilient_client, incident_id=incident_id, query_filters=None, headers=None)

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
                    artifact_payload['type']['name'] = ARTIFACT_TYPE_API_NAME.get(artifact_type, "String")
                    artifact_payload['description']['content'] = artifact_type
                    # attach new Artifact to Incident
                    resilient_client.post(uri=artifact_uri, payload=artifact_payload)

        except SimpleHTTPException as ex:
            log.info(f"Something went wrong when attempting to create the Incident: {ex}")
            raise ex

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
            if idfield in threat and threat[idfield]:
                # Return threat id a field name if field found and it has a value.
                return threat[idfield], idfield

        return None, None

    def _find_resilient_artifacts_for_incident(self, incident_id):
        """Return list of artifacts for the given Incident ID, else returns empty list"""
        r_artifacts = {}
        resilient_client = self.rest_client()
        artifacts_uri = get_artifacts(res_client=resilient_client, incident_id=incident_id, query_filters=None, headers=None)
        artifact_results = resilient_client.get(uri=artifacts_uri)

        if artifact_results:
            for artifact_result in artifact_results:
                artifact_type = artifact_result.get('description')
                if artifact_type in ARTIFACT_TYPES:
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
                        'field_name': f"properties.{idtype}",
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
            query_uri = f"/incidents/query?return_level=normal&field_handle={threat_id}"
            query = {
                'filters': [{
                    'conditions': [
                        {
                            'field_name': f"properties.{idtype}",
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
