

QUERY_PAGED_URL = "/incidents/query_paged?field_handle=-1"
QUERY_PAGED_FILTER = {"filters":[],"sorts":[{"field_name":"id","type":"desc"}],"start":0,"length":10}

WORKFLOW_URL = "/workflows"

def get_incident_limit(restclient, sort="desc"):
    inc_id = 0
    filter = QUERY_PAGED_FILTER.copy()
    filter['sorts'][0]['type'] = sort
    results = restclient.post(uri=QUERY_PAGED_URL, payload=filter)

    if results and results.get('recordsTotal', 0) > 0:
        inc_id = results['data'][0]['id']

    return inc_id

def get_workflow(rest_client, workflow_id):
    workflows = rest_client.get(WORKFLOW_URL)
    # find our specific workflow
    workflow_xml = None
    for entity in workflows['entities']:
        if entity['workflow_id'] == workflow_id:
            workflow_xml = entity['content']['xml']
            break

    return workflow_xml
