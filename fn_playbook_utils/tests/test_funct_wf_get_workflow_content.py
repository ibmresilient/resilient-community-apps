# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from fn_playbook_utils.components.funct_pb_get_workflow_content import get_process_elements

COMPLEX_XML = """<?xml version="1.0" encoding="UTF-8"?>
<definitions
    xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
    xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI"
    xmlns:camunda="http://camunda.org/schema/1.0/bpmn"
    xmlns:omgdc="http://www.omg.org/spec/DD/20100524/DC"
    xmlns:omgdi="http://www.omg.org/spec/DD/20100524/DI"
    xmlns:resilient="http://resilient.ibm.com/bpmn"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" targetNamespace="http://www.camunda.org/test">
    <process id="test_wf" isExecutable="true" name="test_wf">
        <documentation/>
        <startEvent id="StartEvent_155asxm">
            <outgoing>SequenceFlow_1en6rib</outgoing>
        </startEvent>
        <serviceTask id="ServiceTask_1wn2zk8" name="DNSDB Flex" resilient:type="function">
            <extensionElements>
                <resilient:function uuid="d9e15e65-9df6-423e-bb5d-f5592fe927aa">
                    <![CDATA[{"inputs":{"441d1e44-46a8-4a60-b257-fdb0e19ac98c":{"input_type":"static","static_input":{"select_value":"9cafddf6-ec89-42d5-9743-bd3d63bd6409"}},"c1b4ab4b-4119-40b3-be5c-36ba7238620b":{"input_type":"static","static_input":{"select_value":"185e0926-ae6a-43e6-bd35-f3cb93eb59ae"}}},"pre_processing_script":null,"pre_processing_script_language":null,"post_processing_script":null,"post_processing_script_language":null,"result_name":null}]]>
                </resilient:function>
            </extensionElements>
            <incoming>SequenceFlow_1ivyz4m</incoming>
            <outgoing>SequenceFlow_119d8py</outgoing>
        </serviceTask>
        <sequenceFlow id="SequenceFlow_1en6rib" sourceRef="StartEvent_155asxm" targetRef="UserTask_1byuuto"/>
        <scriptTask id="ScriptTask_1drvhx6" name="Convert JSON to rich text v1.1">
            <extensionElements>
                <resilient:script uuid="874d929b-7b4c-4f47-983a-58295c93d6bf"/>
            </extensionElements>
            <incoming>SequenceFlow_119d8py</incoming>
            <outgoing>SequenceFlow_1rz4zac</outgoing>
            <script>script</script>
        </scriptTask>
        <serviceTask id="ServiceTask_1v36lbh" name="DNSDB Pivot" resilient:type="function">
            <extensionElements>
                <resilient:function uuid="5e06db24-d82d-43f1-ae88-bbcf9845689b">
                    <![CDATA[{"inputs":{},"pre_processing_script":null,"pre_processing_script_language":null,"post_processing_script":null,"post_processing_script_language":null,"result_name":null}]]>
                </resilient:function>
            </extensionElements>
            <incoming>SequenceFlow_0eoa9rg</incoming>
            <outgoing>SequenceFlow_1n7mpzf</outgoing>
        </serviceTask>
        <sequenceFlow id="SequenceFlow_1rz4zac" sourceRef="ScriptTask_1drvhx6" targetRef="CallActivity_0hdhj10"/>
        <parallelGateway id="ParallelGateway_0a2spbe">
            <incoming>SequenceFlow_1n7mpzf</incoming>
            <outgoing>SequenceFlow_1swup2s</outgoing>
            <outgoing>SequenceFlow_0m529j3</outgoing>
        </parallelGateway>
        <serviceTask id="ServiceTask_0uvaf9y" name="DNSDB RData" resilient:type="function">
            <extensionElements>
                <resilient:function uuid="5e10f620-6e00-45c4-9c80-6a57e34649b6">
                    <![CDATA[{"inputs":{"18c8830c-b7db-40d8-ae31-55cd0ad17f87":{"input_type":"static","static_input":{"select_value":"93e92972-d1d5-4e90-89a8-f4805f05787b"}}},"pre_processing_script":null,"pre_processing_script_language":null,"post_processing_script":null,"post_processing_script_language":null,"result_name":null}]]>
                </resilient:function>
            </extensionElements>
            <incoming>SequenceFlow_1swup2s</incoming>
            <outgoing>SequenceFlow_045vro6</outgoing>
        </serviceTask>
        <sequenceFlow id="SequenceFlow_1swup2s" sourceRef="ParallelGateway_0a2spbe" targetRef="ServiceTask_0uvaf9y"/>
        <serviceTask id="ServiceTask_0cwzxhv" name="DNSDB Rate Limit" resilient:type="function">
            <extensionElements>
                <resilient:function uuid="6d21c436-47ec-4595-85ad-c209a511c893">
                    <![CDATA[{"inputs":{},"pre_processing_script":null,"pre_processing_script_language":null,"post_processing_script":null,"post_processing_script_language":null,"result_name":null}]]>
                </resilient:function>
            </extensionElements>
            <incoming>SequenceFlow_0m529j3</incoming>
            <outgoing>SequenceFlow_01jt46j</outgoing>
        </serviceTask>
        <sequenceFlow id="SequenceFlow_0m529j3" sourceRef="ParallelGateway_0a2spbe" targetRef="ServiceTask_0cwzxhv"/>
        <exclusiveGateway id="ExclusiveGateway_02pyvm4">
            <incoming>SequenceFlow_01jt46j</incoming>
            <incoming>SequenceFlow_045vro6</incoming>
            <outgoing>SequenceFlow_0s3l3xo</outgoing>
        </exclusiveGateway>
        <sequenceFlow id="SequenceFlow_01jt46j" sourceRef="ServiceTask_0cwzxhv" targetRef="ExclusiveGateway_02pyvm4"/>
        <sequenceFlow id="SequenceFlow_045vro6" sourceRef="ServiceTask_0uvaf9y" targetRef="ExclusiveGateway_02pyvm4"/>
        <endEvent id="EndEvent_06hymn3">
            <incoming>SequenceFlow_0s3l3xo</incoming>
        </endEvent>
        <sequenceFlow id="SequenceFlow_0s3l3xo" sourceRef="ExclusiveGateway_02pyvm4" targetRef="EndEvent_06hymn3"/>
        <sequenceFlow id="SequenceFlow_1n7mpzf" sourceRef="ServiceTask_1v36lbh" targetRef="ParallelGateway_0a2spbe"/>
        <userTask id="UserTask_1byuuto" name="Initial Triage">
            <extensionElements>
                <resilient:automaticTask programmaticName="initial_triage" uuid="2d261a8a-14c3-4f0f-a237-7c6a76bf82b1"/>
            </extensionElements>
            <incoming>SequenceFlow_1en6rib</incoming>
            <outgoing>SequenceFlow_1ivyz4m</outgoing>
        </userTask>
        <sequenceFlow id="SequenceFlow_1ivyz4m" sourceRef="UserTask_1byuuto" targetRef="ServiceTask_1wn2zk8"/>
        <callActivity calledElement="example_kafka_send" id="CallActivity_0hdhj10" name="Example: Kafka Send">
            <extensionElements>
                <camunda:in source="RESILIENT_CONTEXT" target="RESILIENT_CONTEXT"/>
            </extensionElements>
            <incoming>SequenceFlow_1rz4zac</incoming>
            <outgoing>SequenceFlow_0eoa9rg</outgoing>
        </callActivity>
        <sequenceFlow id="SequenceFlow_0eoa9rg" sourceRef="CallActivity_0hdhj10" targetRef="ServiceTask_1v36lbh"/>
        <sequenceFlow id="SequenceFlow_119d8py" sourceRef="ServiceTask_1wn2zk8" targetRef="ScriptTask_1drvhx6"/>
        <textAnnotation id="TextAnnotation_1kxxiyt">
            <text>Start your workflow here</text>
        </textAnnotation>
        <association id="Association_1seuj48" sourceRef="StartEvent_155asxm" targetRef="TextAnnotation_1kxxiyt"/>
    </process>
    <bpmndi:BPMNDiagram id="BPMNDiagram_1">
        <bpmndi:BPMNPlane bpmnElement="undefined" id="BPMNPlane_1">
            <bpmndi:BPMNShape bpmnElement="StartEvent_155asxm" id="StartEvent_155asxm_di">
                <omgdc:Bounds height="36" width="36" x="162" y="188"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="0" width="90" x="157" y="223"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="TextAnnotation_1kxxiyt" id="TextAnnotation_1kxxiyt_di">
                <omgdc:Bounds height="30" width="100" x="99" y="254"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNEdge bpmnElement="Association_1seuj48" id="Association_1seuj48_di">
                <omgdi:waypoint x="169" xsi:type="omgdc:Point" y="220"/>
                <omgdi:waypoint x="153" xsi:type="omgdc:Point" y="254"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNShape bpmnElement="ServiceTask_1wn2zk8" id="ServiceTask_1wn2zk8_di">
                <omgdc:Bounds height="80" width="100" x="280" y="166"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNEdge bpmnElement="SequenceFlow_1en6rib" id="SequenceFlow_1en6rib_di">
                <omgdi:waypoint x="196" xsi:type="omgdc:Point" y="197"/>
                <omgdi:waypoint x="405" xsi:type="omgdc:Point" y="83"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="14" width="90" x="255.5" y="118"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNShape bpmnElement="ScriptTask_1drvhx6" id="ScriptTask_1drvhx6_di">
                <omgdc:Bounds height="80" width="100" x="463" y="289"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="ServiceTask_1v36lbh" id="ServiceTask_1v36lbh_di">
                <omgdc:Bounds height="80" width="100" x="671" y="289"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNEdge bpmnElement="SequenceFlow_1rz4zac" id="SequenceFlow_1rz4zac_di">
                <omgdi:waypoint x="563" xsi:type="omgdc:Point" y="329"/>
                <omgdi:waypoint x="607" xsi:type="omgdc:Point" y="329"/>
                <omgdi:waypoint x="607" xsi:type="omgdc:Point" y="329"/>
                <omgdi:waypoint x="607" xsi:type="omgdc:Point" y="123"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="14" width="90" x="577" y="322"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNShape bpmnElement="ParallelGateway_0a2spbe" id="ParallelGateway_0a2spbe_di">
                <omgdc:Bounds height="50" width="50" x="812" y="181"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="14" width="0" x="837" y="234"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="ServiceTask_0uvaf9y" id="ServiceTask_0uvaf9y_di">
                <omgdc:Bounds height="80" width="100" x="912" y="43"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNEdge bpmnElement="SequenceFlow_1swup2s" id="SequenceFlow_1swup2s_di">
                <omgdi:waypoint x="837" xsi:type="omgdc:Point" y="181"/>
                <omgdi:waypoint x="837" xsi:type="omgdc:Point" y="83"/>
                <omgdi:waypoint x="912" xsi:type="omgdc:Point" y="83"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="14" width="0" x="852" y="125"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNShape bpmnElement="ServiceTask_0cwzxhv" id="ServiceTask_0cwzxhv_di">
                <omgdc:Bounds height="80" width="100" x="912" y="289"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNEdge bpmnElement="SequenceFlow_0m529j3" id="SequenceFlow_0m529j3_di">
                <omgdi:waypoint x="837" xsi:type="omgdc:Point" y="231"/>
                <omgdi:waypoint x="837" xsi:type="omgdc:Point" y="329"/>
                <omgdi:waypoint x="912" xsi:type="omgdc:Point" y="329"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="14" width="0" x="852" y="273"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNShape bpmnElement="ExclusiveGateway_02pyvm4" id="ExclusiveGateway_02pyvm4_di" isMarkerVisible="true">
                <omgdc:Bounds height="50" width="50" x="1121.8508508508507" y="181"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="14" width="0" x="1146.8508508508507" y="234"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNEdge bpmnElement="SequenceFlow_01jt46j" id="SequenceFlow_01jt46j_di">
                <omgdi:waypoint x="1012" xsi:type="omgdc:Point" y="329"/>
                <omgdi:waypoint x="1147" xsi:type="omgdc:Point" y="329"/>
                <omgdi:waypoint x="1147" xsi:type="omgdc:Point" y="231"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="14" width="0" x="1079.5" y="307"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="SequenceFlow_045vro6" id="SequenceFlow_045vro6_di">
                <omgdi:waypoint x="1012" xsi:type="omgdc:Point" y="83"/>
                <omgdi:waypoint x="1147" xsi:type="omgdc:Point" y="83"/>
                <omgdi:waypoint x="1147" xsi:type="omgdc:Point" y="181"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="14" width="0" x="1079.5" y="61"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNShape bpmnElement="EndEvent_06hymn3" id="EndEvent_06hymn3_di">
                <omgdc:Bounds height="36" width="36" x="1252.8508508508507" y="188"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="14" width="0" x="1270.8508508508507" y="227"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNEdge bpmnElement="SequenceFlow_0s3l3xo" id="SequenceFlow_0s3l3xo_di">
                <omgdi:waypoint x="1172" xsi:type="omgdc:Point" y="206"/>
                <omgdi:waypoint x="1253" xsi:type="omgdc:Point" y="206"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="14" width="0" x="1212.5" y="184"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="SequenceFlow_1n7mpzf" id="SequenceFlow_1n7mpzf_di">
                <omgdi:waypoint x="771" xsi:type="omgdc:Point" y="329"/>
                <omgdi:waypoint x="837" xsi:type="omgdc:Point" y="329"/>
                <omgdi:waypoint x="837" xsi:type="omgdc:Point" y="231"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="14" width="90" x="759" y="307"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNShape bpmnElement="UserTask_1byuuto" id="UserTask_1byuuto_di">
                <omgdc:Bounds height="80" width="100" x="408" y="43"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNEdge bpmnElement="SequenceFlow_1ivyz4m" id="SequenceFlow_1ivyz4m_di">
                <omgdi:waypoint x="458" xsi:type="omgdc:Point" y="123"/>
                <omgdi:waypoint x="458" xsi:type="omgdc:Point" y="173"/>
                <omgdi:waypoint x="377" xsi:type="omgdc:Point" y="173"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="14" width="90" x="428" y="141"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNShape bpmnElement="CallActivity_0hdhj10" id="CallActivity_0hdhj10_di">
                <omgdc:Bounds height="80" width="100" x="578" y="43"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNEdge bpmnElement="SequenceFlow_0eoa9rg" id="SequenceFlow_0eoa9rg_di">
                <omgdi:waypoint x="628" xsi:type="omgdc:Point" y="123"/>
                <omgdi:waypoint x="628" xsi:type="omgdc:Point" y="206"/>
                <omgdi:waypoint x="721" xsi:type="omgdc:Point" y="206"/>
                <omgdi:waypoint x="721" xsi:type="omgdc:Point" y="289"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="14" width="0" x="674.5" y="184"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNEdge bpmnElement="SequenceFlow_119d8py" id="SequenceFlow_119d8py_di">
                <omgdi:waypoint x="380" xsi:type="omgdc:Point" y="206"/>
                <omgdi:waypoint x="422" xsi:type="omgdc:Point" y="206"/>
                <omgdi:waypoint x="422" xsi:type="omgdc:Point" y="329"/>
                <omgdi:waypoint x="463" xsi:type="omgdc:Point" y="329"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="14" width="0" x="437" y="260.5"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNEdge>
        </bpmndi:BPMNPlane>
    </bpmndi:BPMNDiagram>
</definitions>"""

SIMPLE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<definitions
    xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
    xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI"
    xmlns:omgdc="http://www.omg.org/spec/DD/20100524/DC"
    xmlns:omgdi="http://www.omg.org/spec/DD/20100524/DI"
    xmlns:resilient="http://resilient.ibm.com/bpmn"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" targetNamespace="http://www.camunda.org/test">
    <process id="stix_shifter_msapt" isExecutable="true" name="stix shifter mysql">
        <documentation/>
        <startEvent id="StartEvent_155asxm">
            <outgoing>SequenceFlow_0sj4div</outgoing>
        </startEvent>
        <serviceTask id="ServiceTask_02zpijh" name="Stix Shifter Wrapper" resilient:type="function">
            <extensionElements>
                <resilient:function uuid="128c1713-3bdd-4d74-8cd1-944d0b4a19a3">
                    <![CDATA[{"inputs":{"6adc9abe-17c5-44b5-977f-43801f94bef5":{"input_type":"static","static_input":{"text_value":"mysql"}},"103f4d21-93ac-4aac-beee-69771032a552":{"input_type":"static","static_input":{"date_value":1625112000000}},"f2289997-7652-42c2-84ed-fc8d00559d4a":{"input_type":"static","static_input":{"date_value":1627704000000}}},"pre_processing_script":"inputs.ss_artifact_type = artifact.type\\ninputs.ss_artifact_value = artifact.value\\n","pre_processing_script_language":"python3","post_processing_script":null,"post_processing_script_language":null,"result_name":null}]]>
                </resilient:function>
            </extensionElements>
            <incoming>SequenceFlow_0sj4div</incoming>
            <outgoing>SequenceFlow_0v1wafo</outgoing>
        </serviceTask>
        <sequenceFlow id="SequenceFlow_0sj4div" sourceRef="StartEvent_155asxm" targetRef="ServiceTask_02zpijh"/>
        <endEvent id="EndEvent_0i20ae9">
            <incoming>SequenceFlow_0v1wafo</incoming>
        </endEvent>
        <sequenceFlow id="SequenceFlow_0v1wafo" sourceRef="ServiceTask_02zpijh" targetRef="EndEvent_0i20ae9"/>
        <textAnnotation id="TextAnnotation_1kxxiyt">
            <text>Start your workflow here</text>
        </textAnnotation>
        <association id="Association_1seuj48" sourceRef="StartEvent_155asxm" targetRef="TextAnnotation_1kxxiyt"/>
    </process>
    <bpmndi:BPMNDiagram id="BPMNDiagram_1">
        <bpmndi:BPMNPlane bpmnElement="undefined" id="BPMNPlane_1">
            <bpmndi:BPMNShape bpmnElement="StartEvent_155asxm" id="StartEvent_155asxm_di">
                <omgdc:Bounds height="36" width="36" x="162" y="188"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="0" width="90" x="157" y="223"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNShape bpmnElement="TextAnnotation_1kxxiyt" id="TextAnnotation_1kxxiyt_di">
                <omgdc:Bounds height="30" width="100" x="99" y="254"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNEdge bpmnElement="Association_1seuj48" id="Association_1seuj48_di">
                <omgdi:waypoint x="169" xsi:type="omgdc:Point" y="220"/>
                <omgdi:waypoint x="153" xsi:type="omgdc:Point" y="254"/>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNShape bpmnElement="ServiceTask_02zpijh" id="ServiceTask_02zpijh_di">
                <omgdc:Bounds height="80" width="100" x="277" y="166"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNEdge bpmnElement="SequenceFlow_0sj4div" id="SequenceFlow_0sj4div_di">
                <omgdi:waypoint x="198" xsi:type="omgdc:Point" y="206"/>
                <omgdi:waypoint x="277" xsi:type="omgdc:Point" y="206"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="14" width="0" x="237.5" y="184"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNEdge>
            <bpmndi:BPMNShape bpmnElement="EndEvent_0i20ae9" id="EndEvent_0i20ae9_di">
                <omgdc:Bounds height="36" width="36" x="448" y="188"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="14" width="0" x="466" y="227"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNEdge bpmnElement="SequenceFlow_0v1wafo" id="SequenceFlow_0v1wafo_di">
                <omgdi:waypoint x="377" xsi:type="omgdc:Point" y="206"/>
                <omgdi:waypoint x="448" xsi:type="omgdc:Point" y="206"/>
                <bpmndi:BPMNLabel>
                    <omgdc:Bounds height="14" width="0" x="412.5" y="184"/>
                </bpmndi:BPMNLabel>
            </bpmndi:BPMNEdge>
        </bpmndi:BPMNPlane>
    </bpmndi:BPMNDiagram>
</definitions>"""

class TestWfGetWorkflowContent:
    """ Tests for the wf_get_workflow_content function"""

    def test_complex(self):
        """ Test calling with sample values for the parameters """

        results = get_process_elements(COMPLEX_XML)
        assert(results.get('Tasks'))
        assert("Initial Triage" in results.get('Tasks', []))

        assert(results.get('Functions'))
        assert("DNSDB Flex" in results.get('Functions', []))
        assert("DNSDB Pivot" in results.get('Functions', []))

        assert(results.get('Scripts'))
        assert("Convert JSON to rich text v1.1" in results.get('Scripts', []))

        assert(results.get('Workflows'))
        assert("Example: Kafka Send" in results.get('Workflows', []))

    def test_simple(self):
        results = get_process_elements(SIMPLE_XML)
        assert(not results.get('Tasks'))
        assert(not results.get('Scripts'))
        assert(not results.get('Workflows'))
        assert(results.get('Functions'))
        assert("Stix Shifter Wrapper" in results.get('Functions', []))
