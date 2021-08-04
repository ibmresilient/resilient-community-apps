# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long
import logging
import xml.etree.ElementTree as ET
from resilient import SimpleHTTPException

LOG = logging.getLogger(__name__)

QUERY_PAGED_URL = "/incidents/query_paged?field_handle=-1"
QUERY_PAGED_FILTER = {"filters":[],"sorts":[{"field_name":"id","type":"desc"}],"start":0,"length":10}

WORKFLOW_URL = "/workflows"

ACTION_MAP = {
    'callActivity': 'Workflows',
    'serviceTask': 'Functions',
    'scriptTask': 'Scripts',
    'userTask': 'Tasks'
}

PLAYBOOK_QUERY_PAGED_URL = "/playbooks/query_paged?return_level=full"
PLAYBOOK_QUERY_PAGED_FILTER = {
  "filters": [
    {
      "conditions": [
        {
          "method": "equals",
          "field_name": "id",
          "value": None
        }
      ]
    }
  ]
}

PLAYBOOK_EXECUTION_QUERY_PAGED_FILTER_URL = "/playbooks/execution/query_paged"
PLAYBOOK_EXECUTION_QUERY_PAGED_FILTER = {
  "sorts": [
  ],
  "filters": [
    {
      "conditions": [
      ]
    }
  ]
}

def parse_inputs(restclient, fn_inputs):
    """[parse inputs, determinging the platform min and max incident id]

    Args:
        restclient ([class]): [resilient client to make API calls]
        fn_inputs ([dict]): [function input dictionary]

    Returns:
        [int, int]: [min_id and max_id]
    """
    min_id = fn_inputs.pb_min_incident_id if hasattr(fn_inputs, 'pb_min_incident_id') else None
    max_id = fn_inputs.pb_max_incident_id if hasattr(fn_inputs, 'pb_max_incident_id') else None

    min_date = fn_inputs.pb_min_incident_date if hasattr(fn_inputs, 'pb_min_incident_date') else None
    max_date = fn_inputs.pb_max_incident_date if hasattr(fn_inputs, 'pb_max_incident_date') else None

    # if ids are missing and at least one date is available
    if not (min_id and max_id) and (min_date or max_date):
        if max_date:
            max_date += 60*60*24*1000   # search for date based on midnight
        min_id, max_id = get_incidents_by_date(restclient, min_date, max_date)
    else:
        # don't make excessive API calls, use system limits if customer provided values are out of range
        sys_min_id  = get_incident_limit(restclient, sort="asc")
        if not min_id or min_id < sys_min_id:
            min_id = sys_min_id

        sys_max_id = get_incident_limit(restclient, sort="desc")
        if not max_id or max_id > sys_max_id:
            max_id = sys_max_id

    return min_id, max_id

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

def get_incidents_by_date(rest_client, min_incident_date, max_incident_date):
    filter_conditions = {
        "filters": [
            {
                "conditions": [
                ]
            }
        ],
        "sorts": [
            {
                "field_name": "id",
                "type": "asc"
            }
        ]
    }

    if min_incident_date:
        filter_conditions['filters'][0]['conditions'].append({
                        "method": "gte",
                        "field_name": "create_date",
                        "value": min_incident_date
                    })

    if max_incident_date:
        filter_conditions['filters'][0]['conditions'].append({
                        "method": "lte",
                        "field_name": "create_date",
                        "value": max_incident_date
                    })

    LOG.debug(filter_conditions)

    search_results = rest_client.post(QUERY_PAGED_URL, filter_conditions)
    min_incident_id = max_incident_id = None
    LOG.debug(search_results)
    if search_results.get('data'):
        min_incident_id = search_results['data'][0]['id']
        max_incident_id = search_results['data'][-1]['id']

    return min_incident_id, max_incident_id

def get_playbook(rest_client, playbook_id):
    """[get a specific playbook from all playbooks]

    Args:
        rest_client ([obj]): [class to make SOAR API calls]
        playbook_id ([int]): [playbook id to search]

    Returns:
        [str]: [xml document for the found workflow or None]
    """
    filter_conditions = PLAYBOOK_QUERY_PAGED_FILTER.copy()
    filter_conditions['filters'][0]['conditions'][0]['value'] = playbook_id
    playbooks = rest_client.post(uri=PLAYBOOK_QUERY_PAGED_URL, payload=filter_conditions)
    # find our specific workflow
    playbook_xml = None
    if playbooks.get('data'):
        playbook_xml = playbooks['data'][0]['content']['xml']

    return playbook_xml

def get_playbooks_by_incident_id(rest_client, min_incident_id, max_incident_id):
    """[summary]

    Args:
        rest_client ([type]): [description]
        min_id ([type]): [description]
        max_id ([type]): [description]
    """
    filter_conditions = PLAYBOOK_EXECUTION_QUERY_PAGED_FILTER.copy()
    if min_incident_id:
        filter_conditions['filters'][0]['conditions'].append({
                        "method": "gte",
                        "field_name": "incident_id",
                        "value": min_incident_id
                    })

    if max_incident_id:
        filter_conditions['filters'][0]['conditions'].append({
                        "method": "lte",
                        "field_name": "incident_id",
                        "value": max_incident_id
                    })

    LOG.debug(filter_conditions)
    try:
        return rest_client.post(PLAYBOOK_EXECUTION_QUERY_PAGED_FILTER_URL, filter_conditions)
    except SimpleHTTPException:
        return {}

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
