# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long
import xml.etree.ElementTree as ET

QUERY_PAGED_URL = "/incidents/query_paged?field_handle=-1"
QUERY_PAGED_FILTER = {"filters":[],"sorts":[{"field_name":"id","type":"desc"}],"start":0,"length":10}

WORKFLOW_URL = "/workflows"

ACTION_MAP = {
    'callActivity': 'Workflows',
    'serviceTask': 'Functions',
    'scriptTask': 'Scripts',
    'userTask': 'Tasks'
}

PLAYBOOKS_QUERY_PAGED_URL = "/playbooks/query_paged?return_level=full"
PLAYBOOKS_QUERY_PAGED_FILTER = {
  "query": None,
  "sorts": [
    {
      "field_name": "display_name",
      "type": "asc"
    }
  ],
  "start": 0,
  "length": 10
}

def get_incident_limit(restclient, sort="desc"):
    """[get incidents sorted either ascending or descending in order to get the min or max incident id]

    Args:
        restclient ([obj]): [class to make SOAR API calls]
        sort (str, optional): ['asc' or 'desc']. Defaults to "desc".

    Returns:
        [int]: [min or max incident_id]
    """
    inc_id = 0
    query_filter = QUERY_PAGED_FILTER.copy()
    query_filter['sorts'][0]['type'] = sort
    results = restclient.post(uri=QUERY_PAGED_URL, payload=query_filter)

    if results and results.get('recordsTotal', 0) > 0:
        inc_id = results['data'][0]['id']

    return inc_id

def get_workflow(rest_client, workflow_id):
    """[get a specific workflow from all workflows]

    Args:
        rest_client ([obj]): [class to make SOAR API calls]
        workflow_id ([int]): [workflow id to search]

    Returns:
        [str]: [xml document for the found workflow or None]
    """
    workflows = rest_client.get(WORKFLOW_URL)
    # find our specific workflow
    workflow_xml = None
    for entity in workflows['entities']:
        if entity['workflow_id'] == workflow_id:
            workflow_xml = entity['content']['xml']
            break

    return workflow_xml

def get_playbook(rest_client, playbook_id):
    """[get a specific playbook from all playbooks]

    Args:
        rest_client ([obj]): [class to make SOAR API calls]
        playbook_id ([int]): [playbook id to search]

    Returns:
        [str]: [xml document for the found workflow or None]
    """
    playbooks = rest_client.post(uri=PLAYBOOKS_QUERY_PAGED_FILTER, payload=PLAYBOOKS_QUERY_PAGED_FILTER)
    # find our specific workflow
    playbook_xml = None
    for entity in playbooks['entities']:
        if entity['workflow_id'] == playbook_id:
            playbook_xml = entity['content']['xml']
            break

    return playbook_xml

def get_process_elements(xml, action_map=ACTION_MAP):
    """[parse the xml for a workflow and extract the names of it's elements: artifacts,
        tasks, attachements, scripts, sub-workflows]

    Args:
        xml ([string]): [xml data for workflow]
        action_map ([list], optional): [list of elements to extract]. Defaults to ACTION_MAP.
    """
    # parse the xml
    tree = ET.ElementTree(ET.fromstring(xml))

    results = {}
    # walk the xml looking for the content we want
    for el in tree.find('{http://www.omg.org/spec/BPMN/20100524/MODEL}process').iter():
        # remove the name space
        _, has_namespace, postfix = el.tag.partition('}')
        if has_namespace:
            el.tag = postfix  # strip all namespaces

        if el.tag in action_map.keys():
            el_type = action_map[el.tag]
            if results.get(el_type):
                results[el_type].append(el.attrib['name'])
            else:
                results[el_type] = [ el.attrib['name'] ]

    return results
