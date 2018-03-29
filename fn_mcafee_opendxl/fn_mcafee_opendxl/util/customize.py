# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_mcafee_opendxl"""

from __future__ import print_function
from resilient_circuits.util import *


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # Function-field definitions
    yield TypeDefinition(
        {
            "type_name": "__function",
            "fields": { '3e44c51b-22a8-4350-906d-6ae038bb6779': { 'blank_option': False,
                                            'input_type': 'select',
                                            'name': 'mcafee_publish_method',
                                            'placeholder': '',
                                            'required': 'always',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'mcafee_publish_method',
                                            'tooltip': 'Specify whether to publish an event or invoke a service',
                                            'uuid': '3e44c51b-22a8-4350-906d-6ae038bb6779',
                                            'values': [ { 'label': 'Event'},
                                                        { 'label': 'Service'}]},
  '7e569052-b786-4933-9d87-eab57280624f': { 'blank_option': False,
                                            'input_type': 'text',
                                            'name': 'mcafee_topic_name',
                                            'placeholder': '',
                                            'required': 'always',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'mcafee_topic_name',
                                            'tooltip': 'String of the topic name. ie: /mcafee/service/epo/remote/epo1',
                                            'uuid': '7e569052-b786-4933-9d87-eab57280624f',
                                            'values': []},
  '85e0711e-c573-405a-b590-47ae04ba67dc': { 'blank_option': False,
                                            'input_type': 'text',
                                            'name': 'mcafee_dxl_payload',
                                            'placeholder': '',
                                            'required': 'always',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'mcafee_dxl_payload',
                                            'tooltip': 'The text of the payload to publish to the topic',
                                            'uuid': '85e0711e-c573-405a-b590-47ae04ba67dc',
                                            'values': []},
  'dbeed36a-23bf-4189-9f5b-b53ee54ecdc3': { 'blank_option': False,
                                            'input_type': 'select',
                                            'name': 'mcafee_return_response',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'mcafee_return_response',
                                            'tooltip': 'Specify whether or not to wait for and return the response. Uses synchronous/asynchronous service',
                                            'uuid': 'dbeed36a-23bf-4189-9f5b-b53ee54ecdc3',
                                            'values': [ { 'label': 'Yes'},
                                                        { 'label': 'No'}]}}
        }
    )

    # Message destination: 'mcafee_dxl_message_destination'
    yield MessageDestinationDefinition({ 'destination_type': 0,
  'expect_ack': True,
  'name': 'McAfee DXL Message Destination',
  'programmatic_name': 'mcafee_dxl_message_destination'}
    )

    # Function: 'mcafee_publish_to_dxl'
    yield FunctionDefinition({ 'description': { 'content': 'A function which takes 4 inputs:\n\nmcafee_topic_name: String of the topic name. ie: /mcafee/service/epo/remote/epo1.\nmcafee_dxl_payload: The text of the payload to publish to the topic.\nmcafee_publish_method: Specify whether to publish an event or invoke a service.\nmcafee_return_response: Specify whether or not to wait for and return the response. Uses synchronous/asynchronous service.\n\n\nThe function will send the provided message to the provided topic.',
                   'format': 'text'},
  'destination_handle': 'mcafee_dxl_message_destination',
  'display_name': 'McAfee Publish to DXL',
  'name': 'mcafee_publish_to_dxl',
  'uuid': 'f987ed22-27d4-4383-9aa4-81e3999ede25',
  'view_items': [ { 'content': '7e569052-b786-4933-9d87-eab57280624f',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': '85e0711e-c573-405a-b590-47ae04ba67dc',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': '3e44c51b-22a8-4350-906d-6ae038bb6779',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': 'dbeed36a-23bf-4189-9f5b-b53ee54ecdc3',
                    'element': 'field_uuid',
                    'field_type': '__function'}]}
    )

    # Workflow: 'example_mcafee_publish_to_dxl_tag_system'
    yield WorkflowDefinition({ 'content': { 'xml': '<?xml version="1.0" encoding="UTF-8"?><definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:omgdc="http://www.omg.org/spec/DD/20100524/DC" xmlns:omgdi="http://www.omg.org/spec/DD/20100524/DI" xmlns:resilient="http://resilient.ibm.com/bpmn" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" targetNamespace="http://www.camunda.org/test"><process id="example_mcafee_publish_to_dxl_tag_system" isExecutable="true" name="(Example) McAfee Publish to DXL (Tag System)"><documentation>Workflow to trigger the McAfee Publish to DXL function and set a system tag.</documentation><startEvent id="StartEvent_155asxm"><outgoing>SequenceFlow_0oiswie</outgoing></startEvent><serviceTask id="ServiceTask_00weioq" name="McAfee Publish to DXL" resilient:type="function"><extensionElements><resilient:function uuid="f987ed22-27d4-4383-9aa4-81e3999ede25"><![CDATA[{"inputs":{"7e569052-b786-4933-9d87-eab57280624f":{"input_type":"static","static_input":{"text_value":"/mcafee/service/epo/remote/epo1"}},"85e0711e-c573-405a-b590-47ae04ba67dc":{"input_type":"static","static_input":{"text_value":"{\\"command\\": \\"system.applyTag\\", \\"output\\": \\"json\\", \\"params\\": {\\"names\\": \\"10.0.2.15\\", \\"tagName\\": \\"Shut Down\\"}}"}},"3e44c51b-22a8-4350-906d-6ae038bb6779":{"input_type":"static","static_input":{"select_value":"cfcdbf7e-1765-4b87-b164-46c0c7297e5a"}},"dbeed36a-23bf-4189-9f5b-b53ee54ecdc3":{"input_type":"static","static_input":{"select_value":"b45fc834-7cab-48bc-8437-b214ece47678"}}},"pre_processing_script":null,"post_processing_script":null,"result_name":null}]]></resilient:function></extensionElements><incoming>SequenceFlow_0oiswie</incoming><outgoing>SequenceFlow_1w42sy3</outgoing></serviceTask><endEvent id="EndEvent_166kyf6"><incoming>SequenceFlow_1w42sy3</incoming></endEvent><sequenceFlow id="SequenceFlow_1w42sy3" sourceRef="ServiceTask_00weioq" targetRef="EndEvent_166kyf6"/><sequenceFlow id="SequenceFlow_0oiswie" sourceRef="StartEvent_155asxm" targetRef="ServiceTask_00weioq"/><textAnnotation id="TextAnnotation_1kxxiyt"><text>Start your workflow here</text></textAnnotation><association id="Association_1seuj48" sourceRef="StartEvent_155asxm" targetRef="TextAnnotation_1kxxiyt"/></process><bpmndi:BPMNDiagram id="BPMNDiagram_1"><bpmndi:BPMNPlane bpmnElement="undefined" id="BPMNPlane_1"><bpmndi:BPMNShape bpmnElement="StartEvent_155asxm" id="StartEvent_155asxm_di"><omgdc:Bounds height="36" width="36" x="162" y="188"/><bpmndi:BPMNLabel><omgdc:Bounds height="0" width="90" x="157" y="223"/></bpmndi:BPMNLabel></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement="TextAnnotation_1kxxiyt" id="TextAnnotation_1kxxiyt_di"><omgdc:Bounds height="30" width="100" x="99" y="254"/></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement="Association_1seuj48" id="Association_1seuj48_di"><omgdi:waypoint x="169" xsi:type="omgdc:Point" y="220"/><omgdi:waypoint x="153" xsi:type="omgdc:Point" y="254"/></bpmndi:BPMNEdge><bpmndi:BPMNShape bpmnElement="ServiceTask_00weioq" id="ServiceTask_00weioq_di"><omgdc:Bounds height="80" width="100" x="332" y="166"/></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement="EndEvent_166kyf6" id="EndEvent_166kyf6_di"><omgdc:Bounds height="36" width="36" x="583" y="188"/><bpmndi:BPMNLabel><omgdc:Bounds height="13" width="0" x="601" y="227"/></bpmndi:BPMNLabel></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement="SequenceFlow_1w42sy3" id="SequenceFlow_1w42sy3_di"><omgdi:waypoint x="432" xsi:type="omgdc:Point" y="206"/><omgdi:waypoint x="583" xsi:type="omgdc:Point" y="206"/><bpmndi:BPMNLabel><omgdc:Bounds height="13" width="0" x="507.5" y="184"/></bpmndi:BPMNLabel></bpmndi:BPMNEdge><bpmndi:BPMNEdge bpmnElement="SequenceFlow_0oiswie" id="SequenceFlow_0oiswie_di"><omgdi:waypoint x="198" xsi:type="omgdc:Point" y="206"/><omgdi:waypoint x="332" xsi:type="omgdc:Point" y="206"/><bpmndi:BPMNLabel><omgdc:Bounds height="13" width="0" x="265" y="184"/></bpmndi:BPMNLabel></bpmndi:BPMNEdge></bpmndi:BPMNPlane></bpmndi:BPMNDiagram></definitions>'},
  'object_type': 'incident',
  'programmatic_name': 'example_mcafee_publish_to_dxl_tag_system'}
    )

    # Workflow: 'example_mcafee_publish_to_dxl_set_tie_reputation'
    yield WorkflowDefinition({'content': { 'xml': '<?xml version="1.0" encoding="UTF-8"?><definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:omgdc="http://www.omg.org/spec/DD/20100524/DC" xmlns:omgdi="http://www.omg.org/spec/DD/20100524/DI" xmlns:resilient="http://resilient.ibm.com/bpmn" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" targetNamespace="http://www.camunda.org/test"><process id="example_mcafee_publish_to_dxl_set_tie_reputation" isExecutable="true" name="(Example) McAfee Publish to DXL (Set TIE Reputation)"><documentation>Workflow to trigger the McAfee Publish to DXL function and set a TIE reputation.</documentation><startEvent id="StartEvent_155asxm"><outgoing>SequenceFlow_05d6x2p</outgoing></startEvent><serviceTask id="ServiceTask_0ahio5z" name="McAfee Publish to DXL" resilient:type="function"><extensionElements><resilient:function uuid="f987ed22-27d4-4383-9aa4-81e3999ede25"><![CDATA[{"inputs":{"7e569052-b786-4933-9d87-eab57280624f":{"input_type":"static","static_input":{"text_value":"/mcafee/service/tie/file/reputation/set"}},"85e0711e-c573-405a-b590-47ae04ba67dc":{"input_type":"static","static_input":{"text_value":"{\\"hashes\\": [{\\"type\\": \\"md5\\", \\"value\\": \\"Dk0TzJrwTMZLaPw4/goNrA==\\"}], \\"providerId\\": 3, \\"trustLevel\\": 1}"}},"3e44c51b-22a8-4350-906d-6ae038bb6779":{"input_type":"static","static_input":{"select_value":"cfcdbf7e-1765-4b87-b164-46c0c7297e5a"}},"dbeed36a-23bf-4189-9f5b-b53ee54ecdc3":{"input_type":"static","static_input":{"select_value":"66837bc7-65fd-4ff4-b79f-b7f38d684327"}}},"pre_processing_script":null,"post_processing_script":null,"result_name":null}]]></resilient:function></extensionElements><incoming>SequenceFlow_05d6x2p</incoming><outgoing>SequenceFlow_1q4scjf</outgoing></serviceTask><sequenceFlow id="SequenceFlow_05d6x2p" sourceRef="StartEvent_155asxm" targetRef="ServiceTask_0ahio5z"/><endEvent id="EndEvent_1798gkf"><incoming>SequenceFlow_1q4scjf</incoming></endEvent><sequenceFlow id="SequenceFlow_1q4scjf" sourceRef="ServiceTask_0ahio5z" targetRef="EndEvent_1798gkf"/><textAnnotation id="TextAnnotation_1kxxiyt"><text>Start your workflow here</text></textAnnotation><association id="Association_1seuj48" sourceRef="StartEvent_155asxm" targetRef="TextAnnotation_1kxxiyt"/></process><bpmndi:BPMNDiagram id="BPMNDiagram_1"><bpmndi:BPMNPlane bpmnElement="undefined" id="BPMNPlane_1"><bpmndi:BPMNShape bpmnElement="StartEvent_155asxm" id="StartEvent_155asxm_di"><omgdc:Bounds height="36" width="36" x="162" y="188"/><bpmndi:BPMNLabel><omgdc:Bounds height="0" width="90" x="157" y="223"/></bpmndi:BPMNLabel></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement="TextAnnotation_1kxxiyt" id="TextAnnotation_1kxxiyt_di"><omgdc:Bounds height="30" width="100" x="99" y="254"/></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement="Association_1seuj48" id="Association_1seuj48_di"><omgdi:waypoint x="169" xsi:type="omgdc:Point" y="220"/><omgdi:waypoint x="153" xsi:type="omgdc:Point" y="254"/></bpmndi:BPMNEdge><bpmndi:BPMNShape bpmnElement="ServiceTask_0ahio5z" id="ServiceTask_0ahio5z_di"><omgdc:Bounds height="80" width="100" x="319" y="166"/></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement="SequenceFlow_05d6x2p" id="SequenceFlow_05d6x2p_di"><omgdi:waypoint x="198" xsi:type="omgdc:Point" y="206"/><omgdi:waypoint x="319" xsi:type="omgdc:Point" y="206"/><bpmndi:BPMNLabel><omgdc:Bounds height="12" width="0" x="258.5" y="185"/></bpmndi:BPMNLabel></bpmndi:BPMNEdge><bpmndi:BPMNShape bpmnElement="EndEvent_1798gkf" id="EndEvent_1798gkf_di"><omgdc:Bounds height="36" width="36" x="568" y="188"/><bpmndi:BPMNLabel><omgdc:Bounds height="12" width="0" x="586" y="228"/></bpmndi:BPMNLabel></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement="SequenceFlow_1q4scjf" id="SequenceFlow_1q4scjf_di"><omgdi:waypoint x="419" xsi:type="omgdc:Point" y="206"/><omgdi:waypoint x="568" xsi:type="omgdc:Point" y="206"/><bpmndi:BPMNLabel><omgdc:Bounds height="12" width="0" x="493.5" y="185"/></bpmndi:BPMNLabel></bpmndi:BPMNEdge></bpmndi:BPMNPlane></bpmndi:BPMNDiagram></definitions>'},
  'object_type': 'incident',
  'programmatic_name': 'example_mcafee_publish_to_dxl_set_tie_reputation'}
    )

    # Rule: '(Example) McAfee Publish to DXL (Tag System)'
    yield ActionDefinition({ 'automations': [],
  'conditions': [],
  'logic_type': 'all',
  'message_destinations': [],
  'name': '(Example) McAfee Publish to DXL (Tag System)',
  'object_type': 'incident',
  'timeout_seconds': 86400,
  'type': 1,
  'view_items': [],
  'workflows': ['example_mcafee_publish_to_dxl_tag_system']}
    )

    # Rule: '(Example) McAfee Publish to DXL (Set TIE Reputation)'
    yield ActionDefinition({'automations': [],
  'conditions': [],
  'logic_type': 'all',
  'message_destinations': [],
  'name': '(Example) McAfee Publish to DXL (Set TIE Reputation)',
  'object_type': 'incident',
  'timeout_seconds': 86400,
  'type': 1,
  'view_items': [],
  'workflows': ['example_mcafee_publish_to_dxl_set_tie_reputation']}
   )

