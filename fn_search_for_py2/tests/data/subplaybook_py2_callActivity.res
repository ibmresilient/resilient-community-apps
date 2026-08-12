{
    "activation_details": {
        "activation_conditions": {
            "conditions": [
                {
                    "evaluation_id": null,
                    "field_name": "artifact.type",
                    "method": "equals",
                    "type": null,
                    "value": "IP Address"
                },
                {
                    "evaluation_id": null,
                    "field_name": null,
                    "method": "object_added",
                    "type": null,
                    "value": null
                }
            ],
            "logic_type": "all"
        }
    },
    "activation_type": "automatic",
    "content": {
        "content_version": 6,
        "xml": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><definitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:camunda=\"http://camunda.org/schema/1.0/bpmn\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"><process id=\"playbook_ce85838e_78ab_4d6e_895a_*****\" isExecutable=\"true\" name=\"playbook_ce85838e_78ab_4d6e_895a_*****\"><documentation/><startEvent id=\"StartEvent_155asxm\"><outgoing>Flow_034y19x</outgoing></startEvent><endEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"><incoming>Flow_1q8nfyc</incoming></endEvent><callActivity calledElement=\"playbook_b0bc1e1e_485f_4ed0_bf67_85e199bd41f8\" id=\"CallActivity_7\" name=\"CriminalIP IP Address Lookup\" resilient:type=\"sub-playbook\"><extensionElements><resilient:sub-playbook name=\"CriminalIP IP Address Lookup\" uuid=\"****-485f-4ed0-bf67-85e199bd41f8\">{\"inputs\":{},\"pre_processing_script\":\"\\ninputs.criminalip_api_key = \\\"your CriminalIP API key\\\"\\ninputs.criminalip_ip_address = artifact.value\",\"pre_processing_script_language\":\"python\",\"result_name\":\"criminalip_results\"}</resilient:sub-playbook><camunda:in source=\"RESILIENT_CONTEXT\" target=\"RESILIENT_CONTEXT\"/></extensionElements><incoming>Flow_034y19x</incoming><outgoing>Flow_1tnby5i</outgoing></callActivity><sequenceFlow id=\"Flow_034y19x\" sourceRef=\"StartEvent_155asxm\" targetRef=\"CallActivity_7\"/><sequenceFlow id=\"Flow_1tnby5i\" sourceRef=\"CallActivity_7\" targetRef=\"ScriptTask_8\"/><scriptTask id=\"ScriptTask_8\" name=\"Criminal IP Hits\"><extensionElements><resilient:script uuid=\"****-3925-4b55-ad95-39fc7a65f924\"/></extensionElements><incoming>Flow_1tnby5i</incoming><outgoing>Flow_1q8nfyc</outgoing><script>script</script></scriptTask><sequenceFlow id=\"Flow_1q8nfyc\" sourceRef=\"ScriptTask_8\" targetRef=\"EndPoint_3\"/></process><bpmndi:BPMNDiagram id=\"BPMNDiagram_1\"><bpmndi:BPMNPlane bpmnElement=\"playbook_ce85838e_78ab_4d6e_895a_*****\" id=\"BPMNPlane_1\"><bpmndi:BPMNEdge bpmnElement=\"Flow_1q8nfyc\" id=\"Flow_1q8nfyc_di\"><omgdi:waypoint x=\"720\" y=\"442\"/><omgdi:waypoint x=\"720\" y=\"494\"/></bpmndi:BPMNEdge><bpmndi:BPMNEdge bpmnElement=\"Flow_1tnby5i\" id=\"Flow_1tnby5i_di\"><omgdi:waypoint x=\"721\" y=\"308\"/><omgdi:waypoint x=\"721\" y=\"358\"/></bpmndi:BPMNEdge><bpmndi:BPMNEdge bpmnElement=\"Flow_034y19x\" id=\"Flow_034y19x_di\"><omgdi:waypoint x=\"720\" y=\"126\"/><omgdi:waypoint x=\"720\" y=\"191\"/></bpmndi:BPMNEdge><bpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"><omgdc:Bounds height=\"52\" width=\"181.515625\" x=\"629\" y=\"74\"/><bpmndi:BPMNLabel><omgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/></bpmndi:BPMNLabel></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"><omgdc:Bounds height=\"52\" width=\"132.21875\" x=\"653\" y=\"494\"/></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"CallActivity_7\" id=\"CallActivity_7_di\"><omgdc:Bounds height=\"117\" width=\"196\" x=\"623\" y=\"191\"/></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"ScriptTask_8\" id=\"ScriptTask_8_di\"><omgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"358\"/></bpmndi:BPMNShape></bpmndi:BPMNPlane></bpmndi:BPMNDiagram></definitions>"
    },
    "create_date": 1738335785246,
    "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
    },
    "deployment_id": "playbook_ce85838e_78ab_4d6e_895a_*****",
    "description": {
        "format": "text",
        "content": "Perform automatic threat data enrichment on IP addresses. Results are returned as hits to the artifact."
    },
    "display_name": "Criminal IP: IP Threat Service",
    "export_key": "criminal_ip_threat_service",
    "field_type_handle": "playbook_ce85838e_78ab_4d6e_895a_*****",
    "fields_type": {
        "actions": [],
        "display_name": "Criminal IP: IP Threat Service",
        "export_key": "playbook_ce85838e_78ab_4d6e_895a_*****",
        "fields": {},
        "for_actions": false,
        "for_custom_fields": false,
        "for_notifications": false,
        "for_workflows": false,
        "id": null,
        "parent_types": [
            "__playbook"
        ],
        "properties": {
            "can_create": false,
            "can_destroy": false,
            "for_who": []
        },
        "scripts": [],
        "tags": [],
        "type_id": 28,
        "type_name": "playbook_ce85838e_78ab_4d6e_895a_*****",
        "uuid": "****-ab6d-4f9d-bdb5-fc2fda99e2e3"
    }
}
