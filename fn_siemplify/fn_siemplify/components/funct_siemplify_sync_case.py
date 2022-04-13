# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, clean_html
from fn_siemplify.lib.soar_common import SOARCommon, eval_mapping, make_case_linkback_url
from fn_siemplify.lib.siemplify_common import SiemplifyCommon, PACKAGE_NAME, IBMSOAR_TAGS, \
            build_siemplify_case_url

FN_NAME = "siemplify_sync_case"
SIEMPLIFY_CASE_URL = "{}/#/main/cases/classic-view/{}"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'siemplify_sync_case'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Sync a SOAR Case to Siemplify
        Inputs:
            -   fn_inputs.siemplify_incident_id
            -   fn_inputs.siemplify_sync_attachments
            -   fn_inputs.siemplify_sync_comments
            -   fn_inputs.siemplify_sync_artifacts
            -   fn_inputs.siemplify_environment
            -   fn_inputs.siemplify_assigned_user
            -   fn_inputs.siemplify_case_id
            -   fn_inputs.siemplify_alert_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        if self.opts.get("sync_new_cases", "both").lower() not in ["soar", "both"]:
            FunctionResult({}, success=False, reason="sync_new_cases disabled")

        inputs = fn_inputs._asdict()
        app_settings = self.app_configs._asdict()

        # validate app.config settings
        validate_fields([
                {"name": "api_key"},
                {"name": "base_url"},
                {"name": "default_environment"}
            ],
            app_settings)

        # set the default if the default isn't set
        inputs['siemplify_environment'] = inputs['siemplify_environment'] if inputs.get('siemplify_environment') else self.app_configs.default_environment

        soar_env = SOARCommon(self.rest_client())

        # collect the incident information
        incident_info = soar_env.get_incident(inputs['siemplify_incident_id'])
        incident_info['description'] = clean_html(incident_info['description'])

        # assemble all the data for Siemplify incident creation
        incident_info['siemplify_assigned_user'] = inputs['siemplify_assigned_user']
        incident_info['siemplify_environment'] = inputs['siemplify_environment']
        incident_info['siemplify_alert_id'] = inputs['siemplify_alert_id']
        incident_info['siemplify_tags'] = IBMSOAR_TAGS

        incident_info['siemplify_playbooks'] = self._map_playbooks(incident_info['incident_type_ids'],
                                                                   eval_mapping(app_settings.get('playbook_mappings'), wrapper="{{ {} }}"),
                                                                   soar_env.get_incident_types())

        incident_info['soar_linkback_url'] = make_case_linkback_url(self.opts.get('resilient'), fn_inputs.siemplify_incident_id)
        self.LOG.debug(incident_info)

        siemplify_env = SiemplifyCommon(self.rc, self.app_configs)
        results, error_msg = siemplify_env.sync_case(incident_info)

        # get the results based on the data returned
        if not error_msg:
            # get the full case information
            case_results, error_msg = siemplify_env.get_case(results)

            if error_msg:
                self.LOG.error("Unable to get newly created Siemplify case: %s, %s", results, error_msg)
            elif case_results.get("alerts"):
                # save the case_id and alert_id
                inputs['siemplify_case_id'] = results
                inputs['siemplify_alert_id'] = case_results['alerts'][0]['identifier']

                case_results['siemplify_case_url'] = build_siemplify_case_url(self.app_configs.base_url, results)
                results = case_results

                inputs['siemplify_comment'] = '<div><a href="{}" target="blank">SOAR CASE {}</a></div>'.format(incident_info['soar_linkback_url'],
                                                                                    incident_info['id'])
                siemplify_env.sync_comment(inputs)

                # S Y N C   A L L   O T H E R S
                # collect the incident comments
                if fn_inputs.siemplify_sync_comments:
                    self.sync_comments(soar_env, siemplify_env, inputs)

                # collect the incident artifacts
                if fn_inputs.siemplify_sync_artifacts:
                    self.sync_artifacts(soar_env, siemplify_env, inputs)

                # collect the incident attachments
                if fn_inputs.siemplify_sync_attachments:
                    self.sync_attachments(soar_env, siemplify_env, inputs)

                yield self.status_message("Endpoint reached successfully and returning results for App Function: '{0}'".format(FN_NAME))
        yield FunctionResult(results, success=isinstance(error_msg, type(None)), reason=error_msg)


    def _map_playbooks(self, incident_type_ids, playbook_mapping, incident_type_mapping):
        """[identify the playbooks to add to the siemplify case]

        Args:
            incident_type_ids ([list]): [SOAR incident type ids]
            playbook_mapping ([dict]): [mapping of SOAR incident types to playbook names]
            incident_type_mapping ([dict]): [mapping of SOAR incident type Ids to their names]

        Returns:
            [list]: [playbooks to add to a case]
        """

        siemplify_playbooks = incident_types = []
        # convert any existing incident type ids
        if incident_type_ids:
            incident_types = [incident_type_mapping[id] for id in incident_type_ids \
                                if id in incident_type_mapping]

        if playbook_mapping and incident_types:
            siemplify_playbooks = [playbook_mapping[inc_type]  \
                                    for inc_type in incident_types if inc_type in playbook_mapping]
            # set default playbook if no mapping found
            if not siemplify_playbooks and playbook_mapping.get('DEFAULT'):
                siemplify_playbooks = [ playbook_mapping['DEFAULT'] ]

        return siemplify_playbooks

    def sync_comments(self, soar_env, siemplify_env, fn_inputs):
        # get all SOAR incident comments and sync each to Siemplify
        for comment in soar_env.get_incident_comments(fn_inputs['siemplify_incident_id']):
            inputs = {
                'siemplify_case_id': fn_inputs['siemplify_case_id'],
                'siemplify_alert_id': fn_inputs['siemplify_alert_id'],
                'siemplify_comment': comment['text']
            }
            siemplify_env.sync_insight(inputs)

    def sync_artifacts(self, soar_env, siemplify_env, fn_inputs):
        # get all SOAR incident artifacts and sync each to Siemplify
        for artifact in soar_env.get_incident_artifacts(fn_inputs['siemplify_incident_id']):
            if not artifact.get('attachment'):
                inputs = {
                    'siemplify_case_id': fn_inputs['siemplify_case_id'],
                    'siemplify_alert_id': fn_inputs['siemplify_alert_id'],
                    'siemplify_artifact_type': soar_env.lookup_artifact_type(artifact['type']),
                    'siemplify_artifact_value': artifact['value'],
                    'siemplify_environment': fn_inputs['siemplify_environment'],
                }
                siemplify_env.sync_artifact(inputs)

    def sync_attachments(self, soar_env, siemplify_env, fn_inputs):
        # get all SOAR incident attachments and sync each to Siemplify
        for attachment in soar_env.get_incident_attachments(fn_inputs['siemplify_incident_id']):
            siemplify_env.sync_attachment(fn_inputs['siemplify_case_id'],
                                          attachment['content'],
                                          attachment['name'])
