# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
import re
from datetime import datetime


def unix_to_datetime(unix):
    return(datetime.fromtimestamp(int(unix / 1000)).strftime('%m/%d/%Y %H:%M:%S'))


def list_children(table):
    incidents = []
    childid_regex = re.compile(r'#incidents/(\d+)"')
    for row in table['rows']:
        inc_id = int(re.findall(childid_regex,row['cells']['relations_incident_id']['value'])[0])
        if inc_id not in incidents:
            incidents.append(inc_id)
    return(incidents)


def list_open_children(table):
    incidents = []
    childid_regex = re.compile(r'#incidents/(\d+)"')
    for row in table['rows']:
        if row['cells']['relations_incident_status']['value'] != 'Closed':
            inc_id = int(re.findall(childid_regex,row['cells']['relations_incident_id']['value'])[0])
            if inc_id not in incidents:
                incidents.append(inc_id)
    return(incidents)


def list_artifacts(artifacts):
    artifact_parent_ids = []
    for artifact in artifacts:
        if artifact['type'] == "related_parent_incident" and int(artifact['value']) not in artifact_parent_ids:
            artifact_parent_ids.append(int(artifact['value']))
    return(artifact_parent_ids)


def locate_note_id(original_note, notes_list):
    clean = re.compile('<.*?>')
    for note in notes_list:
        if note['text']:
            if re.sub(clean, '', original_note['text']) in re.sub(clean, '', note['text']):
                return(note['id'])
        if note['children']:
            results = locate_note_id(original_note, note['children'])
            if results:
                return(results)
