# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#pragma pylint: disable=unused-argument, line-too-long

import logging
from io import BytesIO
from resilient_lib import IntegrationError, s_to_b
from resilient import SimpleHTTPException
from requests import RequestException
from requests_toolbelt.multipart.encoder import MultipartEncoder
from xml.etree import ElementTree as ET
import posixpath

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

PLAYBOOK_URL = "/playbooks"
PLAYBOOK_QUERY_PAGED_URL = "/playbooks/query_paged?return_level=full"
PLAYBOOK_QUERY_PAGED_FILTER = {
  "filters": [
    {
      "conditions": [
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
    
    # need at least min_id or min_date to avoid excessive calls - removed
    # if not (min_id or min_date):
    #     raise ValueError("Either 'Min Incident Id' or 'Min Incident Date' is required")

    # if ids are missing then it will query on the current incident
    if not (min_id or max_id or min_date or max_date):
        min_id, max_id = get_incident_limit(restclient, sort="asc")

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
    query_filter = dict(QUERY_PAGED_FILTER)
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
    """get incidents created within a date range

    :param rest_client: client object for SOAR API access
    :type rest_client: object
    :param min_incident_date: date in milliseconds for minimum incident creation date
    :type min_incident_date: int
    :param max_incident_date: date in milliseconds for maximum incident creation date
    :type max_incident_date: int
    :return: json results of API call
    :rtype: dict
    """
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

def get_playbooks(rest_client, pb_types, pb_filter):
    """Get all playbooks based on the filter type

    :param rest_client: client object for SOAR API access
    :type rest_client: object
    :param pb_types: type of playbook to return: all, enabled, draft
    :type pb_types: str
    :param pb_filter: partial name of playbook to further filter
    :type pb_filter: str
    :return: dictionary of playbooks returned
    :rtype: dict
    """
    filter_conditions = dict(PLAYBOOK_EXECUTION_QUERY_PAGED_FILTER)

    if pb_types and pb_types != 'all':
        filter_conditions['filters'][0]['conditions'].append({
                        "method": "equals",
                        "field_name": "status",
                        "value": [pb_types]
                    })
    if pb_filter:
        filter_conditions['query'] = pb_filter

    LOG.debug(filter_conditions)
    try:
        return rest_client.post(PLAYBOOK_QUERY_PAGED_URL, filter_conditions)
    except SimpleHTTPException as err:
        LOG.error(str(err))
        return {}

def query_playbooks(rest_client, playbook_id=None, playbook_name=None):
    """[query for a specific playbook from all playbooks]

    Args:
        rest_client ([obj]): [class to make SOAR API calls]
        playbook_id ([int]): [playbook id to search]
        playbook_name ([str]): [name of playbook as option rather than playbook id]

    Returns:
        [list]: [list playbooks which meet the query citeria]
    """
    filter_conditions = dict(PLAYBOOK_QUERY_PAGED_FILTER)

    if playbook_id:
        id_condition = {
            "method": "equals",
            "field_name": "id",
            "value": playbook_id
            }
        filter_conditions['filters'][0]['conditions'].append(id_condition)

    if playbook_name:
        filter_conditions['query'] = playbook_name

    playbooks = rest_client.post(uri=PLAYBOOK_QUERY_PAGED_URL, payload=filter_conditions)

    return playbooks.get('data')

def export_playbook(rest_client, playbook_id, playbook_name):
    """export a playbook into a .resz format

    :param rest_client: object for API calls back to SOAR
    :type rest_client: object
    :param playbook_id: id of playbook. Either playbook_id or playbook_name can be used
    :type playbook_id: str
    :param playbook_name: name of playbook to export. Either playbook_id or playbook_name can be used
    :type playbook_name: str
    :return: export result and json result of api call
    :rtype: bool, dict
    """
    # find the playbook by id or name
    find_result = query_playbooks(rest_client,
                                  playbook_id=playbook_id,
                                  playbook_name=playbook_name)
    if not find_result:
        return False, "Playbook not found"

    # ensure the playbook is found
    export_start_result = rest_client.post(uri=posixpath.join(PLAYBOOK_URL, "exports"),
                                     payload={"id": find_result[0].get("id")})

    if export_start_result.get("success", True):
        multipart_data = {
                "file_name": "Unnused"
            }
        multipart_data.update({})
        encoder = MultipartEncoder(fields=multipart_data)

        # now down the specific export
        export_result = rest_client.post(posixpath.join(PLAYBOOK_URL, "exports", str(export_start_result.get("export_id"))),
                                         encoder,
                                         headers={"content-type": encoder.content_type})

        return True, export_result

    return False, export_start_result

def import_playbook(rest_client, playbook_body):
    """Import a playbook from a .resz file

    :param rest_client: object to make API calls to SOAR
    :type rest_client: object
    :param playbook_body: .resz file to import
    :type playbook_body: str
    :raises IntegrationError: error raised if import unsuccessful
    :return: json result of api call
    :rtype: dict
    """
    try:
        filehandle = BytesIO(s_to_b(playbook_body))
        multipart_data = {"file": ("export.resz", filehandle, "application/octet-stream")}
        multipart_data.update({})
        encoder = MultipartEncoder(fields=multipart_data)

        result = rest_client.post(posixpath.join(PLAYBOOK_URL, "imports"),
                                  encoder,
                                  headers={"content-type": encoder.content_type})
    except RequestException as upload_exception:
        LOG.debug(playbook_body)
        raise IntegrationError(upload_exception)
    else:
        assert isinstance(result, dict)

    # excepted result?
    if result.get("status", "") == "PENDING":
        return confirm_playbook_import(rest_client, result.get("id"))

    raise IntegrationError("Could not import because the server did not return an import ID")

def confirm_playbook_import(rest_client, import_id, status="ACCEPTED"):
    """Send confirmation back to SOAR to complete the import

    :param rest_client: object to make API calls to SOAR
    :type rest_client: object
    :param import_id: id returned from original import API call
    :type import_id: int
    :param status: status to return in API call, defaults to "ACCEPTED"
    :type status: str, optional
    :raises IntegrationError: raise error if import is unsuccessful
    :return: json result of API call
    :rtype: dict
    """
    uri = posixpath.join(PLAYBOOK_URL, "imports", str(import_id), "status")
    try:
        return rest_client.put(uri, status, headers={"content-type": "text/plain"})
    except RequestException as import_exception:
        raise IntegrationError(repr(import_exception))

def get_playbooks_by_incident_id(rest_client, min_incident_id, max_incident_id):
    """Find a playbooks instances run on incident(s)

        :param rest_client: object to make API calls to SOAR
        :type rest_client: object
        :param min_id: minimum incident_id
        :type min_id: int
        :param max_id: maximum incident_id
        :type max_id: int
        :return json result of API call
        :rtype: dict
    """
    filter_conditions = dict(PLAYBOOK_EXECUTION_QUERY_PAGED_FILTER)
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
    except SimpleHTTPException as err:
        LOG.error(str(err))
        return {}

def get_process_elements(xml, action_map=ACTION_MAP):
    """[parse the xml for a workflow and extract the names of it's elements: artifacts,
        tasks, attachements, scripts, sub-workflows]

    Args:
        xml ([string]): [xml data for workflow]
        action_map ([list], optional): [list of elements to extract]. Defaults to ACTION_MAP.
    """
    # parse the xml
    tree = ET.fromstring(xml)

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
