{
    "activation_type": "manual",
    "content": {
        "content_version": 4,
        "xml": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><definitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"><process id=\"playbook_59968a86_1a21_4733_aa82_413dcf76be38\" isExecutable=\"true\" name=\"playbook_59968a86_1a21_4733_aa82_413dcf76be38\"><documentation/><startEvent id=\"StartEvent_155asxm\"><outgoing>Flow_0ngwkq8</outgoing></startEvent><endEvent id=\"EndPoint_1\" resilient:documentation=\"End point\"><incoming>Flow_0r2dl6u</incoming><incoming>Flow_03noiae</incoming><incoming>Flow_0if6pxw</incoming><incoming>Flow_1f0swm7</incoming></endEvent><exclusiveGateway default=\"Flow_01g4xhr\" id=\"ConditionPoint_2\" resilient:documentation=\"Condition point\"><extensionElements/><incoming>Flow_0ngwkq8</incoming><outgoing>Flow_1wq4ua0</outgoing><outgoing>Flow_01g4xhr</outgoing><outgoing>Flow_1wp83ki</outgoing><outgoing>Flow_0bc3lvu</outgoing></exclusiveGateway><userTask id=\"UserTask_3\" name=\"Initial Triage\"><extensionElements><resilient:automaticTask programmaticName=\"initial_triage\" uuid=\"2d261a8a-14c3-4f0f-a237-7c6a76bf82b1\"/></extensionElements><incoming>Flow_1wq4ua0</incoming><outgoing>Flow_0if6pxw</outgoing></userTask><userTask id=\"UserTask_4\" name=\"Interview key individuals\"><extensionElements><resilient:automaticTask programmaticName=\"interview_key_individuals\" uuid=\"2e05bff9-8d15-4424-91c1-9e50d2c78bae\"/></extensionElements><incoming>Flow_01g4xhr</incoming><outgoing>Flow_0r2dl6u</outgoing></userTask><userTask id=\"UserTask_5\" name=\"Notify internal management chain (preliminary)\"><extensionElements><resilient:automaticTask programmaticName=\"notify_internal_management_chain_preliminary\" uuid=\"e799edeb-7bf2-4b9b-9802-4befb16c1ed7\"/></extensionElements><incoming>Flow_1wp83ki</incoming><outgoing>Flow_03noiae</outgoing></userTask><sequenceFlow id=\"Flow_0ngwkq8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ConditionPoint_2\"/><sequenceFlow id=\"Flow_0r2dl6u\" sourceRef=\"UserTask_4\" targetRef=\"EndPoint_1\"/><sequenceFlow id=\"Flow_03noiae\" sourceRef=\"UserTask_5\" targetRef=\"EndPoint_1\"/><sequenceFlow id=\"Flow_0if6pxw\" sourceRef=\"UserTask_3\" targetRef=\"EndPoint_1\"/><userTask id=\"UserTask_6\" name=\"Determine if inappropriate internal involvement\"><extensionElements><resilient:automaticTask programmaticName=\"determine_if_inappropriate_internal_involvement\" uuid=\"78b62efd-56f9-4deb-8566-135417d03efa\"/></extensionElements><incoming>Flow_0bc3lvu</incoming><outgoing>Flow_1f0swm7</outgoing></userTask><sequenceFlow id=\"Flow_1f0swm7\" sourceRef=\"UserTask_6\" targetRef=\"EndPoint_1\"/><sequenceFlow id=\"Flow_1wq4ua0\" name=\"true\" sourceRef=\"ConditionPoint_2\" targetRef=\"UserTask_3\"><extensionElements><resilient:condition label=\"true\" order=\"0\"/></extensionElements><conditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\">{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"result True\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python\"}}],\"logic_type\":\"all\",\"script_language\":null}</conditionExpression></sequenceFlow><sequenceFlow id=\"Flow_1wp83ki\" name=\"3rd condition\" sourceRef=\"ConditionPoint_2\" targetRef=\"UserTask_5\"><extensionElements><resilient:condition label=\"3rd condition\" order=\"1\"/></extensionElements><conditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\">{\"conditions\":[{\"evaluation_id\":null,\"field_name\":\"incident.city\",\"method\":\"contains\",\"type\":null,\"value\":\"Cambridge\"}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":null}</conditionExpression></sequenceFlow><sequenceFlow id=\"Flow_0bc3lvu\" name=\"False\" sourceRef=\"ConditionPoint_2\" targetRef=\"UserTask_6\"><extensionElements><resilient:condition label=\"False\" order=\"2\"/></extensionElements><conditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\">{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python\"}}],\"logic_type\":\"all\",\"script_language\":null}</conditionExpression></sequenceFlow><sequenceFlow id=\"Flow_01g4xhr\" name=\"Else\" sourceRef=\"ConditionPoint_2\" targetRef=\"UserTask_4\"/></process><bpmndi:BPMNDiagram id=\"BPMNDiagram_1\"><bpmndi:BPMNPlane bpmnElement=\"playbook_59968a86_1a21_4733_aa82_413dcf76be38\" id=\"BPMNPlane_1\"><bpmndi:BPMNEdge bpmnElement=\"Flow_0ngwkq8\" id=\"Flow_0ngwkq8_di\"><omgdi:waypoint x=\"722\" y=\"117\"/><omgdi:waypoint x=\"722\" y=\"154\"/></bpmndi:BPMNEdge><bpmndi:BPMNEdge bpmnElement=\"Flow_0r2dl6u\" id=\"Flow_0r2dl6u_di\"><omgdi:waypoint x=\"750\" y=\"382\"/><omgdi:waypoint x=\"750\" y=\"428\"/><omgdi:waypoint x=\"722\" y=\"428\"/><omgdi:waypoint x=\"722\" y=\"474\"/></bpmndi:BPMNEdge><bpmndi:BPMNEdge bpmnElement=\"Flow_03noiae\" id=\"Flow_03noiae_di\"><omgdi:waypoint x=\"882\" y=\"340\"/><omgdi:waypoint x=\"835\" y=\"340\"/><omgdi:waypoint x=\"835\" y=\"500\"/><omgdi:waypoint x=\"788\" y=\"500\"/></bpmndi:BPMNEdge><bpmndi:BPMNEdge bpmnElement=\"Flow_0if6pxw\" id=\"Flow_0if6pxw_di\"><omgdi:waypoint x=\"628\" y=\"340\"/><omgdi:waypoint x=\"642\" y=\"340\"/><omgdi:waypoint x=\"642\" y=\"500\"/><omgdi:waypoint x=\"656\" y=\"500\"/></bpmndi:BPMNEdge><bpmndi:BPMNEdge bpmnElement=\"Flow_1wq4ua0\" id=\"Flow_1wq4ua0_di\"><omgdi:waypoint x=\"722\" y=\"206\"/><omgdi:waypoint x=\"722\" y=\"252\"/><omgdi:waypoint x=\"530\" y=\"252\"/><omgdi:waypoint x=\"530\" y=\"298\"/><bpmndi:BPMNLabel><omgdc:Bounds height=\"14\" width=\"20\" x=\"616\" y=\"234\"/></bpmndi:BPMNLabel></bpmndi:BPMNEdge><bpmndi:BPMNEdge bpmnElement=\"Flow_01g4xhr\" id=\"Flow_01g4xhr_di\"><omgdi:waypoint x=\"722\" y=\"206\"/><omgdi:waypoint x=\"722\" y=\"252\"/><omgdi:waypoint x=\"750\" y=\"252\"/><omgdi:waypoint x=\"750\" y=\"298\"/><bpmndi:BPMNLabel><omgdc:Bounds height=\"14\" width=\"22\" x=\"725\" y=\"234\"/></bpmndi:BPMNLabel></bpmndi:BPMNEdge><bpmndi:BPMNEdge bpmnElement=\"Flow_1wp83ki\" id=\"Flow_1wp83ki_di\"><omgdi:waypoint x=\"844\" y=\"180\"/><omgdi:waypoint x=\"980\" y=\"180\"/><omgdi:waypoint x=\"980\" y=\"298\"/><bpmndi:BPMNLabel><omgdc:Bounds height=\"14\" width=\"65\" x=\"884\" y=\"157\"/></bpmndi:BPMNLabel></bpmndi:BPMNEdge><bpmndi:BPMNEdge bpmnElement=\"Flow_0bc3lvu\" id=\"Flow_0bc3lvu_di\"><omgdi:waypoint x=\"844\" y=\"180\"/><omgdi:waypoint x=\"1250\" y=\"180\"/><omgdi:waypoint x=\"1250\" y=\"298\"/><bpmndi:BPMNLabel><omgdc:Bounds height=\"14\" width=\"28\" x=\"1045\" y=\"158\"/></bpmndi:BPMNLabel></bpmndi:BPMNEdge><bpmndi:BPMNEdge bpmnElement=\"Flow_1f0swm7\" id=\"Flow_1f0swm7_di\"><omgdi:waypoint x=\"1250\" y=\"382\"/><omgdi:waypoint x=\"1250\" y=\"500\"/><omgdi:waypoint x=\"788\" y=\"500\"/></bpmndi:BPMNEdge><bpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"><omgdc:Bounds height=\"52\" width=\"187.1875\" x=\"628\" y=\"65\"/><bpmndi:BPMNLabel><omgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/></bpmndi:BPMNLabel></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"EndPoint_1\" id=\"EndPoint_1_di\"><omgdc:Bounds height=\"52\" width=\"132.21875\" x=\"656\" y=\"474\"/></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"ConditionPoint_2\" id=\"ConditionPoint_2_di\" isMarkerVisible=\"true\"><omgdc:Bounds height=\"52\" width=\"243.8125\" x=\"600\" y=\"154\"/></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"UserTask_3\" id=\"UserTask_3_di\"><omgdc:Bounds height=\"84\" width=\"196\" x=\"432\" y=\"298\"/></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"UserTask_4\" id=\"UserTask_4_di\"><omgdc:Bounds height=\"84\" width=\"196\" x=\"652\" y=\"298\"/></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"UserTask_5\" id=\"UserTask_5_di\"><omgdc:Bounds height=\"84\" width=\"196\" x=\"882\" y=\"298\"/></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement=\"UserTask_6\" id=\"UserTask_6_di\"><omgdc:Bounds height=\"84\" width=\"196\" x=\"1152\" y=\"298\"/></bpmndi:BPMNShape></bpmndi:BPMNPlane></bpmndi:BPMNDiagram></definitions>"
    },
    "create_date": 1743519777086,
    "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 20,
        "name": "sysadmin@example.com",
        "type": "user"
    },
    "deployment_id": "playbook_59968a86_1a21_4733_aa82_413dcf76be38",
    "description": {
        "format": "text",
        "content": null
    },
    "display_name": "Py2 3Conditions",
    "export_key": "py2_3conditions",
    "field_type_handle": "playbook_59968a86_1a21_4733_aa82_413dcf76be38",
    "fields_type": {
        "actions": [],
        "display_name": "Py2 3Conditions",
        "export_key": "playbook_59968a86_1a21_4733_aa82_413dcf76be38",
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
        "type_name": "playbook_59968a86_1a21_4733_aa82_413dcf76be38",
        "uuid": "339efefc-313c-42e4-855f-40a09f62bec1"
    },
    "has_logical_errors": false,
    "id": 216,
    "is_deleted": false,
    "is_locked": false,
    "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 20,
        "name": "sysadmin@example.com",
        "type": "user"
    },
    "last_modified_time": 1743520093050,
    "local_scripts": [],
    "manual_settings": {
        "activation_conditions": {
            "conditions": [],
            "logic_type": "all"
        },
        "view_items": []
    },
    "name": "py2_3conditions",
    "object_type": "incident",
    "status": "enabled",
    "tag": {
        "display_name": "Playbook_59968a86-1a21-4733-aa82-413dcf76be38",
        "id": 306,
        "name": "playbook_59968a86_1a21_4733_aa82_413dcf76be38",
        "type": "playbook",
        "uuid": "87c4dd97-7a15-47b2-a1df-b05e9b3d8f53"
    },
    "tags": [],
    "type": "default",
    "uuid": "59968a86-1a21-4733-aa82-413dcf76be38",
    "version": 9
}