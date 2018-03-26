# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for test"""

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
            "fields": { '1fbd9156-b2c4-49c2-82e8-041832e990b6': { 'blank_option': False,
                                            'input_type': 'text',
                                            'name': 'mcafee_tie_hash',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'mcafee_tie_hash',
                                            'tooltip': 'The value of the hash',
                                            'uuid': '1fbd9156-b2c4-49c2-82e8-041832e990b6',
                                            'values': []},
  '88c38278-7078-455b-9029-0ec47d21a3d8': { 'blank_option': False,
                                            'input_type': 'text',
                                            'name': 'mcafee_tie_hash_type',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'mcafee_tie_hash_type',
                                            'tooltip': 'The type of file hash (md5, sha1, sha256)',
                                            'uuid': '88c38278-7078-455b-9029-0ec47d21a3d8',
                                            'values': []}}
        }
    )

    # Message destination: 'mcafee_tie_md'
    yield MessageDestinationDefinition({ 'destination_type': 0,
  'expect_ack': True,
  'name': 'McAfee TIE MD',
  'programmatic_name': 'mcafee_tie_md'}
    )

    # Function: 'mcafee_tie_search_hash'
    yield FunctionDefinition({ 'description': { 'content': 'A function which takes two inputs:\n\nmcafee_tie_hash_type: The type of file hash (md5, sha1, sha256).\nmcafee_tie_hash: The value of the hash.\n\nThe function returns back a dict of all the available information from the different file providers (Enterprise, GTI, ATD, MWG) along with the list of systems related to it.',
                   'format': 'text'},
  'destination_handle': 'mcafee_tie_md',
  'display_name': 'McAfee TIE search hash',
  'name': 'mcafee_tie_search_hash',
  'uuid': '44a9cf5b-16b7-4cea-adc4-3956b079a1ab',
  'view_items': [ { 'content': '88c38278-7078-455b-9029-0ec47d21a3d8',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': '1fbd9156-b2c4-49c2-82e8-041832e990b6',
                    'element': 'field_uuid',
                    'field_type': '__function'}]}
    )

    # Workflow: 'mcafee_tie_hash_search_workflow'
    yield WorkflowDefinition({ 'content': { 'xml': '<?xml version="1.0" encoding="UTF-8"?><definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:camunda="http://camunda.org/schema/1.0/bpmn" xmlns:omgdc="http://www.omg.org/spec/DD/20100524/DC" xmlns:omgdi="http://www.omg.org/spec/DD/20100524/DI" xmlns:resilient="http://resilient.ibm.com/bpmn" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" targetNamespace="http://www.camunda.org/test"><process id="mcafee_tie_hash_search_workflow" isExecutable="true" name="(Example) McAfee TIE hash search workflow"><documentation>Workflow to trigger function to search hash in TIE.</documentation><startEvent id="StartEvent_155asxm"><outgoing>SequenceFlow_159kb3y</outgoing></startEvent><serviceTask id="ServiceTask_0trnpek" name="McAfee TIE search hash" resilient:type="function"><extensionElements><resilient:function uuid="44a9cf5b-16b7-4cea-adc4-3956b079a1ab"><![CDATA[{"inputs":{"88c38278-7078-455b-9029-0ec47d21a3d8":{"input_type":"static","static_input":{"text_value":null}},"1fbd9156-b2c4-49c2-82e8-041832e990b6":{"input_type":"static","static_input":{"text_value":null}}},"pre_processing_script":"if artifact.type == \\"Malware MD5 Hash\\":\\n  inputs.mcafee_tie_hash_type = \\"md5\\"\\n  inputs.mcafee_tie_hash = artifact.value\\nelif artifact.type == \\"Malware SHA-1 Hash\\":\\n  inputs.mcafee_tie_hash_type = \\"sha1\\"\\n  inputs.mcafee_tie_hash = artifact.value\\nelif artifact.type == \\"Malware SHA-256 Hash\\":\\n  inputs.mcafee_tie_hash_type = \\"sha256\\"\\n  inputs.mcafee_tie_hash = artifact.value\\nelse:\\n  helper.fail(\\"Artifact hash was not set correctly\\")\\n","post_processing_script":null,"result_name":""}]]></resilient:function></extensionElements><incoming>SequenceFlow_159kb3y</incoming><outgoing>SequenceFlow_17q1ve9</outgoing></serviceTask><sequenceFlow id="SequenceFlow_159kb3y" sourceRef="StartEvent_155asxm" targetRef="ServiceTask_0trnpek"/><endEvent id="EndEvent_1ahf1kb"><incoming>SequenceFlow_17q1ve9</incoming></endEvent><sequenceFlow id="SequenceFlow_17q1ve9" sourceRef="ServiceTask_0trnpek" targetRef="EndEvent_1ahf1kb"/><textAnnotation id="TextAnnotation_1kxxiyt"><text>Start your workflow here</text></textAnnotation><association id="Association_1seuj48" sourceRef="StartEvent_155asxm" targetRef="TextAnnotation_1kxxiyt"/></process><bpmndi:BPMNDiagram id="BPMNDiagram_1"><bpmndi:BPMNPlane bpmnElement="undefined" id="BPMNPlane_1"><bpmndi:BPMNShape bpmnElement="StartEvent_155asxm" id="StartEvent_155asxm_di"><omgdc:Bounds height="36" width="36" x="162" y="188"/><bpmndi:BPMNLabel><omgdc:Bounds height="0" width="90" x="157" y="223"/></bpmndi:BPMNLabel></bpmndi:BPMNShape><bpmndi:BPMNShape bpmnElement="TextAnnotation_1kxxiyt" id="TextAnnotation_1kxxiyt_di"><omgdc:Bounds height="30" width="100" x="99" y="254"/></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement="Association_1seuj48" id="Association_1seuj48_di"><omgdi:waypoint x="169" xsi:type="omgdc:Point" y="220"/><omgdi:waypoint x="153" xsi:type="omgdc:Point" y="254"/></bpmndi:BPMNEdge><bpmndi:BPMNShape bpmnElement="ServiceTask_0trnpek" id="ServiceTask_0trnpek_di"><omgdc:Bounds height="80" width="100" x="354" y="166"/></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement="SequenceFlow_159kb3y" id="SequenceFlow_159kb3y_di"><omgdi:waypoint x="198" xsi:type="omgdc:Point" y="206"/><omgdi:waypoint x="354" xsi:type="omgdc:Point" y="206"/><bpmndi:BPMNLabel><omgdc:Bounds height="13" width="0" x="276" y="184.5"/></bpmndi:BPMNLabel></bpmndi:BPMNEdge><bpmndi:BPMNShape bpmnElement="EndEvent_1ahf1kb" id="EndEvent_1ahf1kb_di"><omgdc:Bounds height="36" width="36" x="636" y="188"/><bpmndi:BPMNLabel><omgdc:Bounds height="13" width="0" x="654" y="227"/></bpmndi:BPMNLabel></bpmndi:BPMNShape><bpmndi:BPMNEdge bpmnElement="SequenceFlow_17q1ve9" id="SequenceFlow_17q1ve9_di"><omgdi:waypoint x="454" xsi:type="omgdc:Point" y="206"/><omgdi:waypoint x="636" xsi:type="omgdc:Point" y="206"/><bpmndi:BPMNLabel><omgdc:Bounds height="13" width="0" x="545" y="184.5"/></bpmndi:BPMNLabel></bpmndi:BPMNEdge></bpmndi:BPMNPlane></bpmndi:BPMNDiagram></definitions>'},
  'object_type': 'artifact',
  'programmatic_name': 'mcafee_tie_hash_search_workflow'}
    )

    # Rule: '(Example) McAfee artifact hash search'
    yield ActionDefinition({ 'automations': [],
  'conditions': [ { 'evaluation_id': None,
                    'field_name': 'artifact.type',
                    'method': 'in',
                    'type': None,
                    'value': [ 'Malware MD5 Hash',
                               'Malware SHA-1 Hash',
                               'Malware SHA-256 Hash']}],
  'logic_type': 'all',
  'message_destinations': [],
  'name': '(Example) McAfee artifact hash search',
  'object_type': 'artifact',
  'timeout_seconds': 86400,
  'type': 1,
  'view_items': [],
  'workflows': ['mcafee_tie_hash_search_workflow']}
    )
