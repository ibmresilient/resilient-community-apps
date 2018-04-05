# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_mcafee_atd"""

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
            "fields": { '62d93105-705d-4876-9813-e60ee43e19ed': { 'blank_option': False,
                                            'input_type': 'number',
                                            'name': 'artifact_id',
                                            'placeholder': '',
                                            'required': 'always',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'artifact_id',
                                            'tooltip': '',
                                            'uuid': '62d93105-705d-4876-9813-e60ee43e19ed',
                                            'values': []},
  '811e99d7-d194-4ce8-86cc-aff5e01ab85c': { 'blank_option': False,
                                            'input_type': 'number',
                                            'name': 'incident_id',
                                            'placeholder': '',
                                            'required': 'always',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'incident_id',
                                            'tooltip': '',
                                            'uuid': '811e99d7-d194-4ce8-86cc-aff5e01ab85c',
                                            'values': []}}
        }
    )

    # Message destination: 'mcafee_atd_message_destination'
    yield MessageDestinationDefinition({ 'destination_type': 0,
  'expect_ack': True,
  'name': 'McAfee ATD Message Destination',
  'programmatic_name': 'mcafee_atd_message_destination'}
    )

    # Function: 'mcafee_atd_analyze_file'
    yield FunctionDefinition({ 'description': { 'content': '', 'format': 'text'},
  'destination_handle': 'mcafee_atd_message_destination',
  'display_name': 'McAfee ATD Analyze File',
  'name': 'mcafee_atd_analyze_file',
  'uuid': '501eb49b-1cf1-4f54-bc50-130d42c035ac',
  'view_items': [ { 'content': '811e99d7-d194-4ce8-86cc-aff5e01ab85c',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': '62d93105-705d-4876-9813-e60ee43e19ed',
                    'element': 'field_uuid',
                    'field_type': '__function'}]}
    )

    # Workflow: 'example_mcafee_atd_analyze_file'
    yield WorkflowDefinition({ 'content': { 'xml': '<?xml version="1.0" encoding="UTF-8"?><definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:omgdc="http://www.omg.org/spec/DD/20100524/DC" xmlns:omgdi="http://www.omg.org/spec/DD/20100524/DI" xmlns:resilient="http://resilient.ibm.com/bpmn" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" targetNamespace="http://www.camunda.org/test"><process id="example_mcafee_atd_analyze_file" isExecutable="true" name="(Example) McAfee ATD Analyze File"><documentation/><startEvent id="StartEvent_155asxm"><outgoing>SequenceFlow_0zujokq</outgoing></startEvent><serviceTask id="ServiceTask_1i4w1av" name="McAfee ATD Analyze File" resilient:type="function"><extensionElements><resilient:function uuid="501eb49b-1cf1-4f54-bc50-130d42c035ac"><![CDATA[{"inputs":{},"pre_processing_script":"inputs.artifact_id = artifact.id\\ninputs.incident_id = incident.id","post_processing_script":null,"result_name":""}]]></resilient:function></extensionElements><incoming>SequenceFlow_0zujokq</incoming><outgoing>SequenceFlow_1s6zhbh</outgoing></serviceTask><sequenceFlow id="SequenceFlow_0zujokq" sourceRef="StartEvent_155asxm" targetRef="ServiceTask_1i4w1av"/><endEvent id="EndEvent_0n0xpkg"><incoming>SequenceFlow_1s6zhbh</incoming></endEvent><sequenceFlow id="SequenceFlow_1s6zhbh" sourceRef="ServiceTask_1i4w1av" targetRef="EndEvent_0n0xpkg"/><textAnnotation id="TextAnnotation_1kxxiyt"><text>Start your workflow here</text></textAnnotation><association id="Association_1seuj48" sourceRef="StartEvent_155asxm" targetRef="TextAnnotation_1kxxiyt"/></process><bpmndi:BPMNDiagram id="BPMNDiagram_1"><bpmndi:BPMNPlane bpmnElement="undefined" id="BPMNPlane_1"><bpmndi:BPMNShape bpmnElement="StartEvent_155asxm" id="StartEvent_155asxm_di"><omgdc:Bounds height="36" width="36" x="162" y="188"/><bpmndi:BPMNLabel><omgdc:Bounds height="0" width="90" x="157" y="223"/></bpmndi:BPMNLabel></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement="TextAnnotation_1kxxiyt" id="TextAnnotation_1kxxiyt_di"><omgdc:Bounds height="30" width="100" x="99" y="254"/></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement="Association_1seuj48" id="Association_1seuj48_di"><omgdi:waypoint x="169" xsi:type="omgdc:Point" y="220"/><omgdi:waypoint x="153" xsi:type="omgdc:Point" y="254"/></bpmndi:BPMNEdge><bpmndi:BPMNShape bpmnElement="ServiceTask_1i4w1av" id="ServiceTask_1i4w1av_di"><omgdc:Bounds height="80" width="100" x="302" y="166"/></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement="SequenceFlow_0zujokq" id="SequenceFlow_0zujokq_di"><omgdi:waypoint x="198" xsi:type="omgdc:Point" y="206"/><omgdi:waypoint x="302" xsi:type="omgdc:Point" y="206"/><bpmndi:BPMNLabel><omgdc:Bounds height="13" width="0" x="250" y="184"/></bpmndi:BPMNLabel></bpmndi:BPMNEdge><bpmndi:BPMNShape bpmnElement="EndEvent_0n0xpkg" id="EndEvent_0n0xpkg_di"><omgdc:Bounds height="36" width="36" x="507" y="188"/><bpmndi:BPMNLabel><omgdc:Bounds height="13" width="0" x="525" y="227"/></bpmndi:BPMNLabel></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement="SequenceFlow_1s6zhbh" id="SequenceFlow_1s6zhbh_di"><omgdi:waypoint x="402" xsi:type="omgdc:Point" y="206"/><omgdi:waypoint x="507" xsi:type="omgdc:Point" y="206"/><bpmndi:BPMNLabel><omgdc:Bounds height="13" width="0" x="454.5" y="184"/></bpmndi:BPMNLabel></bpmndi:BPMNEdge></bpmndi:BPMNPlane></bpmndi:BPMNDiagram></definitions>'},
  'object_type': 'artifact',
  'programmatic_name': 'example_mcafee_atd_analyze_file'}
    )

    # Rule: '(Example) McAfee ATD Analyze File'
    yield ActionDefinition({ 'automations': [],
  'conditions': [],
  'logic_type': 'all',
  'message_destinations': [],
  'name': '(Example) McAfee ATD Analyze File',
  'object_type': 'artifact',
  'timeout_seconds': 86400,
  'type': 1,
  'view_items': [],
  'workflows': ['example_mcafee_atd_analyze_file']}
    )

