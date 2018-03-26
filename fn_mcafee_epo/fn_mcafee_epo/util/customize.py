# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_mcafee_epo"""

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
            "fields": { '134bfbe6-821d-4c29-9492-d594c38125d7': { 'blank_option': False,
                                            'input_type': 'text',
                                            'name': 'mcafee_epo_tag',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'mcafee_epo_tag',
                                            'tooltip': 'Tag managed on ePO',
                                            'uuid': '134bfbe6-821d-4c29-9492-d594c38125d7',
                                            'values': []},
  'bf25606e-96aa-4328-aa15-1cd5a8b8dc02': { 'blank_option': False,
                                            'input_type': 'text',
                                            'name': 'mcafee_epo_systems',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'mcafee_epo_systems',
                                            'tooltip': 'Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO',
                                            'uuid': 'bf25606e-96aa-4328-aa15-1cd5a8b8dc02',
                                            'values': []}}
        }
    )

    # Message destination: 'mcafee_epo_message_destination'
    yield MessageDestinationDefinition({ 'destination_type': 0,
  'expect_ack': True,
  'name': 'McAfee ePO Message Destination',
  'programmatic_name': 'mcafee_epo_message_destination'}
    )

    # Function: 'mcafee_tag_an_epo_asset'
    yield FunctionDefinition({ 'description': { 'content': 'A function which takes two inputs:\n\nmcafee_epo_system: Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO.\nmcafee_epo_tag: A Tag managed on ePO.\n\nApplies tag to the systems in ePO.',
                   'format': 'text'},
  'destination_handle': 'mcafee_epo_message_destination',
  'display_name': 'McAfee Tag an ePO asset',
  'name': 'mcafee_tag_an_epo_asset',
  'uuid': '67c5b852-f38f-40f7-8a68-1ae8e8a78549',
  'view_items': [ { 'content': 'bf25606e-96aa-4328-aa15-1cd5a8b8dc02',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': '134bfbe6-821d-4c29-9492-d594c38125d7',
                    'element': 'field_uuid',
                    'field_type': '__function'}]}
    )

    # Workflow: 'mcafee_tag_epo_asset_workflow'
    yield WorkflowDefinition({ 'content': { 'xml': '<?xml version="1.0" encoding="UTF-8"?><definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:omgdc="http://www.omg.org/spec/DD/20100524/DC" xmlns:omgdi="http://www.omg.org/spec/DD/20100524/DI" xmlns:resilient="http://resilient.ibm.com/bpmn" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" targetNamespace="http://www.camunda.org/test"><process id="mcafee_tag_epo_asset_workflow" isExecutable="true" name="(Example) McAfee Tag ePO asset workflow"><documentation>Workflow to trigger function to tag system managed by ePO.</documentation><startEvent id="StartEvent_155asxm"><outgoing>SequenceFlow_0i3hqk3</outgoing></startEvent><serviceTask id="ServiceTask_0v8ceni" name="McAfee Tag an ePO asset" resilient:type="function"><extensionElements><resilient:function uuid="67c5b852-f38f-40f7-8a68-1ae8e8a78549"><![CDATA[{"inputs":{"bf25606e-96aa-4328-aa15-1cd5a8b8dc02":{"input_type":"static","static_input":{"text_value":"10.0.2.15"}},"134bfbe6-821d-4c29-9492-d594c38125d7":{"input_type":"static","static_input":{"text_value":"Shut Down"}}},"pre_processing_script":null,"post_processing_script":null,"result_name":null}]]></resilient:function></extensionElements><incoming>SequenceFlow_0i3hqk3</incoming><outgoing>SequenceFlow_14llyc4</outgoing></serviceTask><sequenceFlow id="SequenceFlow_0i3hqk3" sourceRef="StartEvent_155asxm" targetRef="ServiceTask_0v8ceni"/><endEvent id="EndEvent_194e8ac"><incoming>SequenceFlow_14llyc4</incoming></endEvent><sequenceFlow id="SequenceFlow_14llyc4" sourceRef="ServiceTask_0v8ceni" targetRef="EndEvent_194e8ac"/><textAnnotation id="TextAnnotation_1kxxiyt"><text>Start your workflow here</text></textAnnotation><association id="Association_1seuj48" sourceRef="StartEvent_155asxm" targetRef="TextAnnotation_1kxxiyt"/></process><bpmndi:BPMNDiagram id="BPMNDiagram_1"><bpmndi:BPMNPlane bpmnElement="undefined" id="BPMNPlane_1"><bpmndi:BPMNShape bpmnElement="StartEvent_155asxm" id="StartEvent_155asxm_di"><omgdc:Bounds height="36" width="36" x="162" y="188"/><bpmndi:BPMNLabel><omgdc:Bounds height="0" width="90" x="157" y="223"/></bpmndi:BPMNLabel></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement="TextAnnotation_1kxxiyt" id="TextAnnotation_1kxxiyt_di"><omgdc:Bounds height="30" width="100" x="99" y="254"/></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement="Association_1seuj48" id="Association_1seuj48_di"><omgdi:waypoint x="169" xsi:type="omgdc:Point" y="220"/><omgdi:waypoint x="153" xsi:type="omgdc:Point" y="254"/></bpmndi:BPMNEdge><bpmndi:BPMNShape bpmnElement="ServiceTask_0v8ceni" id="ServiceTask_0v8ceni_di"><omgdc:Bounds height="80" width="100" x="291" y="166"/></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement="SequenceFlow_0i3hqk3" id="SequenceFlow_0i3hqk3_di"><omgdi:waypoint x="198" xsi:type="omgdc:Point" y="206"/><omgdi:waypoint x="291" xsi:type="omgdc:Point" y="206"/><bpmndi:BPMNLabel><omgdc:Bounds height="13" width="0" x="244.5" y="184"/></bpmndi:BPMNLabel></bpmndi:BPMNEdge><bpmndi:BPMNShape bpmnElement="EndEvent_194e8ac" id="EndEvent_194e8ac_di"><omgdc:Bounds height="36" width="36" x="517" y="188"/><bpmndi:BPMNLabel><omgdc:Bounds height="13" width="0" x="535" y="227"/></bpmndi:BPMNLabel></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement="SequenceFlow_14llyc4" id="SequenceFlow_14llyc4_di"><omgdi:waypoint x="391" xsi:type="omgdc:Point" y="206"/><omgdi:waypoint x="517" xsi:type="omgdc:Point" y="206"/><bpmndi:BPMNLabel><omgdc:Bounds height="13" width="0" x="454" y="184"/></bpmndi:BPMNLabel></bpmndi:BPMNEdge></bpmndi:BPMNPlane></bpmndi:BPMNDiagram></definitions>'},
  'object_type': 'incident',
  'programmatic_name': 'mcafee_tag_epo_asset_workflow'}
    )

    # Rule: '(Example) McAfee Tag ePO Asset'
    yield ActionDefinition({ 'automations': [],
  'conditions': [],
  'logic_type': 'all',
  'message_destinations': [],
  'name': '(Example) McAfee Tag ePO Asset',
  'object_type': 'incident',
  'timeout_seconds': 86400,
  'type': 1,
  'view_items': [],
  'workflows': ['mcafee_tag_epo_asset_workflow']}
    )

