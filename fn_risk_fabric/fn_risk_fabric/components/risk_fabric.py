import requests


def _make_rest_call(config, api_url, api_params=None, method='get'):
    api_url = config['server'] + api_url
    api_auth = (config['username'], config['password'])
    if method == 'get':
        res = requests.get(api_url, auth=api_auth, params=api_params)
    else:
        res = requests.post(api_url, auth=api_auth, json=api_params)
    return res.json()


def get_risk_info(config, entityType, queryvalue):
    api_params = [('query', queryvalue), ('entityType', entityType), ('fields', 'riskinfo')]
    response = _make_rest_call(config, '/restapi/search', api_params)
    total = response['Paging']['TotalRecords']
    msg = 'No Records Found'
    if total == 1:
        return response['Data'][0]['RiskInfo']['Overview']['RiskScore']
    elif total > 1:
        msg = 'Multiple Records Found'
    return msg  # { "RiskRating": msg, "RiskScore": msg }


def get_risk_model_instances(config, params):
    api_params = {'Limit':params['Limit']}
    response = _make_rest_call(config, '/restapi/RiskModel', api_params, 'post')
    return response


def get_risk_model_details(config, params):
    api_params = {'RiskModelInstanceID':params['riskModelInstanceID']}
    response = _make_rest_call(config, '/restapi/RiskModel/Details', api_params, 'post')
    return response


def get_action_plans(config):
    response = _make_rest_call(config, '/restapi/ActionPlans/List', None, 'post')
    return response


def set_action_plan_comment(config, params):
    api_params = {'ActionPlanGUID': params['ActionPlanGUID'], 'Comment': params['Comment']}
    response = _make_rest_call(config, '/restapi/ActionPlans/Comment', api_params, 'post')
    return response


def get_filters(params):
    filters = []
    if params['RiskModelInstanceID']:
        filters.append({'FilterID':None, 'ValueName': 'RiskModelInstanceID', 'Value':params['RiskModelInstanceID']})
    if params['CardInstanceID']:
        filters.append({'FilterID':None, 'ValueName': 'CardInstanceID', 'Value':params['CardInstanceID']})
    if params['FocusEntityID']:
        filters.append({'FilterID':None, 'ValueName': 'FocusEntityID', 'Value':params['FocusEntityID']})
    if params['ActionPlanGUID']:
        filters.append({'FilterID':None, 'ValueName': 'ActionPlanGUID', 'Value':params['ActionPlanGUID']})
    return filters


def set_event_classifications(config, params):
    filters = get_filters(params)
    api_params = {'AdHocFilters': filters, 'Classification': params['Classification']}
    response = _make_rest_call(config, '/restapi/RiskModel/SetEventClassifications', api_params, 'post')
    return response


def set_event_mitigations(config, params):
    filters = get_filters(params)
    mitigated = params['Mitigated'] == 'Mitigate'
    api_params = {'AdHocFilters': filters, 'Mitigated': mitigated}
    response = _make_rest_call(config, '/restapi/RiskModel/SetEventMitigations', api_params, 'post')
    return response
