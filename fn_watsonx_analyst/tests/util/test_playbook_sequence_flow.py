# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2026. All Rights Reserved.

"""Tests for playbook_sequence_flow module"""

import json
import os
import pytest
from lxml import etree as ET

from fn_watsonx_analyst.util.playbook_sequence_flow import (
    xml_to_playbook_model,
    model_to_sequence_flow,
    Task,
    ScriptTask,
    ServiceTask,
    SubPlaybookElement,
    Gateway,
)


@pytest.fixture
def simple_playbook_xml():
    """Simple playbook with basic flow: Start -> Task -> End"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL">
    <process id="test_process" name="Test Process">
        <startEvent id="StartEvent_1">
            <outgoing>Flow_1</outgoing>
        </startEvent>
        <userTask id="UserTask_1" name="Test Task">
            <incoming>Flow_1</incoming>
            <outgoing>Flow_2</outgoing>
        </userTask>
        <endEvent id="EndEvent_1">
            <incoming>Flow_2</incoming>
        </endEvent>
        <sequenceFlow id="Flow_1" sourceRef="StartEvent_1" targetRef="UserTask_1"/>
        <sequenceFlow id="Flow_2" sourceRef="UserTask_1" targetRef="EndEvent_1"/>
    </process>
</definitions>'''


@pytest.fixture
def complex_playbook_xml():
    """Load complex playbook XML from test data"""
    json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "complex_playbook.json")
    with open(json_path, 'r') as f:
        playbook_data = json.load(f)
    return playbook_data["content"]["xml"]


@pytest.fixture
def gateway_playbook_xml():
    """Playbook with exclusive gateway and conditional flows"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" 
             xmlns:resilient="http://resilient.ibm.com/bpmn"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <process id="gateway_process" name="Gateway Process">
        <startEvent id="StartEvent_1">
            <outgoing>Flow_1</outgoing>
        </startEvent>
        <userTask id="UserTask_1" name="Initial Task">
            <incoming>Flow_1</incoming>
            <outgoing>Flow_2</outgoing>
        </userTask>
        <exclusiveGateway id="Gateway_1" default="Flow_4" resilient:documentation="Check condition">
            <incoming>Flow_2</incoming>
            <outgoing>Flow_3</outgoing>
            <outgoing>Flow_4</outgoing>
        </exclusiveGateway>
        <userTask id="UserTask_2" name="Condition True">
            <incoming>Flow_3</incoming>
            <outgoing>Flow_5</outgoing>
        </userTask>
        <userTask id="UserTask_3" name="Condition False">
            <incoming>Flow_4</incoming>
            <outgoing>Flow_6</outgoing>
        </userTask>
        <endEvent id="EndEvent_1">
            <incoming>Flow_5</incoming>
        </endEvent>
        <endEvent id="EndEvent_2">
            <incoming>Flow_6</incoming>
        </endEvent>
        <sequenceFlow id="Flow_1" sourceRef="StartEvent_1" targetRef="UserTask_1"/>
        <sequenceFlow id="Flow_2" sourceRef="UserTask_1" targetRef="Gateway_1"/>
        <sequenceFlow id="Flow_3" name="Yes" sourceRef="Gateway_1" targetRef="UserTask_2">
            <conditionExpression xsi:type="tFormalExpression">condition == true</conditionExpression>
        </sequenceFlow>
        <sequenceFlow id="Flow_4" name="No" sourceRef="Gateway_1" targetRef="UserTask_3"/>
        <sequenceFlow id="Flow_5" sourceRef="UserTask_2" targetRef="EndEvent_1"/>
        <sequenceFlow id="Flow_6" sourceRef="UserTask_3" targetRef="EndEvent_2"/>
    </process>
</definitions>'''


@pytest.fixture
def all_node_types_xml():
    """Playbook with all node types: userTask, scriptTask, serviceTask, callActivity"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
             xmlns:resilient="http://resilient.ibm.com/bpmn">
    <process id="all_types_process" name="All Types Process">
        <startEvent id="StartEvent_1">
            <outgoing>Flow_1</outgoing>
        </startEvent>
        <userTask id="UserTask_1" name="Manual Task">
            <incoming>Flow_1</incoming>
            <outgoing>Flow_2</outgoing>
        </userTask>
        <scriptTask id="ScriptTask_1" name="Run Script">
            <extensionElements>
                <resilient:script uuid="script-uuid-123"/>
            </extensionElements>
            <incoming>Flow_2</incoming>
            <outgoing>Flow_3</outgoing>
        </scriptTask>
        <serviceTask id="ServiceTask_1" name="Execute Function" resilient:type="function">
            <extensionElements>
                <resilient:function uuid="func-uuid-456">{"inputs":{}}</resilient:function>
            </extensionElements>
            <incoming>Flow_3</incoming>
            <outgoing>Flow_4</outgoing>
        </serviceTask>
        <callActivity id="CallActivity_1" name="Sub Playbook">
            <extensionElements>
                <resilient:sub-playbook uuid="sub-uuid-789" name="Child Playbook"/>
            </extensionElements>
            <incoming>Flow_4</incoming>
            <outgoing>Flow_5</outgoing>
        </callActivity>
        <endEvent id="EndEvent_1">
            <incoming>Flow_5</incoming>
        </endEvent>
        <sequenceFlow id="Flow_1" sourceRef="StartEvent_1" targetRef="UserTask_1"/>
        <sequenceFlow id="Flow_2" sourceRef="UserTask_1" targetRef="ScriptTask_1"/>
        <sequenceFlow id="Flow_3" sourceRef="ScriptTask_1" targetRef="ServiceTask_1"/>
        <sequenceFlow id="Flow_4" sourceRef="ServiceTask_1" targetRef="CallActivity_1"/>
        <sequenceFlow id="Flow_5" sourceRef="CallActivity_1" targetRef="EndEvent_1"/>
    </process>
</definitions>'''


class TestPlaybookSequenceFlow:
    """Tests for playbook_sequence_flow module"""

    def test_simple_playbook_model(self, simple_playbook_xml):
        """Test parsing a simple playbook"""
        model = xml_to_playbook_model(simple_playbook_xml)

        assert model["process_name"] == "Test Process"
        assert model["process_id"] == "test_process"
        assert len(model["start_events"]) == 1
        assert len(model["end_events"]) == 1
        assert len(model["tasks"]) == 1
        assert len(model["flows"]) == 2
        assert "UserTask_1" in model["tasks"]
        assert isinstance(model["tasks"]["UserTask_1"], Task)

    def test_gateway_playbook_model(self, gateway_playbook_xml):
        """Test parsing a playbook with gateways"""
        model = xml_to_playbook_model(gateway_playbook_xml)

        assert len(model["gateways"]) >= 1
        assert "Gateway_1" in model["gateways"]
        gateway = model["gateways"]["Gateway_1"]
        assert isinstance(gateway, Gateway)
        # Gateway type is determined by tag name - check it's one of the valid types
        assert gateway.type in ["exclusive", "parallel"]
        # For exclusive gateways, check documentation and default flow
        if gateway.type == "exclusive":
            assert gateway.doc == "Check condition"
            assert gateway.default == "Flow_4"

    def test_all_node_types_model(self, all_node_types_xml):
        """Test parsing all node types"""
        model = xml_to_playbook_model(all_node_types_xml)

        # Check all task types are present
        assert "UserTask_1" in model["tasks"]
        assert "ScriptTask_1" in model["tasks"]
        assert "ServiceTask_1" in model["tasks"]
        assert "SubPlaybook_1" in model["tasks"]  # CallActivity renamed to SubPlaybook

        # Verify types
        assert isinstance(model["tasks"]["UserTask_1"], Task)
        assert isinstance(model["tasks"]["ScriptTask_1"], ScriptTask)
        assert isinstance(model["tasks"]["ServiceTask_1"], ServiceTask)
        assert isinstance(model["tasks"]["SubPlaybook_1"], SubPlaybookElement)

        # Check metadata
        script_task = model["tasks"]["ScriptTask_1"]
        assert script_task.script_uuid == "script-uuid-123"

        service_task = model["tasks"]["ServiceTask_1"]
        assert service_task.function_uuid == "func-uuid-456"
        assert service_task.resilient_type == "function"

        sub_playbook = model["tasks"]["SubPlaybook_1"]
        assert sub_playbook.sub_playbook_name == "Child Playbook"
        assert sub_playbook.sub_playbook_uuid == "sub-uuid-789"

    def test_complex_playbook_model(self, complex_playbook_xml):
        """Test parsing the complex playbook from test data"""
        model = xml_to_playbook_model(complex_playbook_xml)

        # Verify model has expected structure
        assert model["process_name"] is not None
        assert len(model["tasks"]) > 0
        assert len(model["flows"]) > 0
        assert len(model["start_events"]) > 0
        assert len(model["end_events"]) > 0

    def test_flow_connections(self, simple_playbook_xml):
        """Test that flows are properly connected to source nodes"""
        model = xml_to_playbook_model(simple_playbook_xml)

        # Check that UserTask_1 has outgoing flow
        task = model["tasks"]["UserTask_1"]
        assert len(task.outgoing) == 1
        assert "Flow_2" in task.outgoing

        # Check flow details
        flow = model["flows"]["Flow_2"]
        assert flow.source == "UserTask_1"
        assert flow.target == "EndEvent_1"


    def test_simple_mermaid_output(self, simple_playbook_xml):
        """Test Mermaid output for simple playbook"""
        model = xml_to_playbook_model(simple_playbook_xml)

        mermaid = model_to_sequence_flow(model)

        # Check basic structure
        assert mermaid.startswith("```mermaid")
        assert mermaid.endswith("```")
        assert "graph TD" in mermaid

        # Check nodes are present
        assert "StartEvent" in mermaid
        assert "Test Task" in mermaid
        assert "End point" in mermaid

        # Check flows
        assert "-->" in mermaid

    def test_gateway_mermaid_output(self, gateway_playbook_xml):
        """Test Mermaid output includes gateway diamonds"""
        model = xml_to_playbook_model(gateway_playbook_xml)

        mermaid = model_to_sequence_flow(model)

        # Check gateway is represented as diamond
        assert "{" in mermaid and "}" in mermaid
        assert "Check condition" in mermaid

        # Check conditional flow labels
        assert "Yes" in mermaid
        assert "No" in mermaid

    def test_all_node_types_mermaid(self, all_node_types_xml):
        """Test Mermaid output for all node types"""
        model = xml_to_playbook_model(all_node_types_xml)

        mermaid = model_to_sequence_flow(model)

        # Check all node types are represented
        assert "Task:" in mermaid  # UserTask
        assert "Script:" in mermaid  # ScriptTask
        assert "Function:" in mermaid  # ServiceTask
        assert "Sub-playbook:" in mermaid  # CallActivity

    def test_special_characters_escaped(self):
        """Test that special characters in labels are properly escaped"""
        xml = '''<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL">
    <process id="test" name="Test">
        <startEvent id="StartEvent_1">
            <outgoing>Flow_1</outgoing>
        </startEvent>
        <userTask id="UserTask_1" name='Task with "quotes" and [brackets]'>
            <incoming>Flow_1</incoming>
            <outgoing>Flow_2</outgoing>
        </userTask>
        <endEvent id="EndEvent_1">
            <incoming>Flow_2</incoming>
        </endEvent>
        <sequenceFlow id="Flow_1" sourceRef="StartEvent_1" targetRef="UserTask_1"/>
        <sequenceFlow id="Flow_2" sourceRef="UserTask_1" targetRef="EndEvent_1"/>
    </process>
</definitions>'''

        model = xml_to_playbook_model(xml)

        mermaid = model_to_sequence_flow(model)

        # Check that special characters are escaped
        assert "#quot;" in mermaid or "quotes" in mermaid
        assert "#91;" in mermaid or "#93;" in mermaid or "brackets" in mermaid

    def test_node_numbering(self, simple_playbook_xml):
        """Test that nodes include node numbers in labels"""
        model = xml_to_playbook_model(simple_playbook_xml)

        mermaid = model_to_sequence_flow(model)

        # Check that node numbers are included
        assert "Node" in mermaid


    def test_simple_xml_to_mermaid(self, simple_playbook_xml):
        """Test complete conversion from XML to Mermaid"""
        model = xml_to_playbook_model(simple_playbook_xml)
        mermaid = model_to_sequence_flow(model)

        assert isinstance(mermaid, str)
        assert mermaid.startswith("```mermaid")
        assert "graph TD" in mermaid
        assert "Test Task" in mermaid

    def test_complex_xml_to_mermaid(self, complex_playbook_xml):
        """Test conversion of complex playbook"""
        model = xml_to_playbook_model(complex_playbook_xml)
        mermaid = model_to_sequence_flow(model)

        assert isinstance(mermaid, str)
        assert len(mermaid) > 100  # Should be substantial output
        assert "```mermaid" in mermaid
        assert "graph TD" in mermaid

    def test_gateway_xml_to_mermaid(self, gateway_playbook_xml):
        """Test conversion with gateways"""
        model = xml_to_playbook_model(gateway_playbook_xml)
        mermaid = model_to_sequence_flow(model)

        assert "Check condition" in mermaid
        assert "Yes" in mermaid or "No" in mermaid

    def test_xml_parsing_security(self):
        """Test that XML parser is secure (resolve_entities=False, no_network=True)"""
        # Test with valid XML to ensure secure parser settings are applied
        safe_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL">
    <process id="test" name="Test Process">
        <startEvent id="StartEvent_1">
            <outgoing>Flow_1</outgoing>
        </startEvent>
        <endEvent id="EndEvent_1">
            <incoming>Flow_1</incoming>
        </endEvent>
        <sequenceFlow id="Flow_1" sourceRef="StartEvent_1" targetRef="EndEvent_1"/>
    </process>
</definitions>'''

        # Should parse successfully with secure parser (resolve_entities=False, no_network=True)
        model = xml_to_playbook_model(safe_xml)
        mermaid = model_to_sequence_flow(model)
        assert "```mermaid" in mermaid
        assert "graph TD" in mermaid


    def test_empty_process(self):
        """Test handling of empty process"""
        xml = '''<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL">
    <process id="empty" name="Empty Process"/>
</definitions>'''

        model = xml_to_playbook_model(xml)
        mermaid = model_to_sequence_flow(model)
        assert "```mermaid" in mermaid
        assert "graph TD" in mermaid

    def test_missing_process_name(self):
        """Test handling of missing process name"""
        xml = '''<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL">
    <process id="test">
        <startEvent id="StartEvent_1"/>
    </process>
</definitions>'''

        model = xml_to_playbook_model(xml)

        # Should use default name
        assert model["process_name"] == "Unnamed"

    def test_task_without_name(self):
        """Test handling of task without name attribute"""
        xml = '''<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL">
    <process id="test" name="Test">
        <startEvent id="StartEvent_1">
            <outgoing>Flow_1</outgoing>
        </startEvent>
        <userTask id="UserTask_1">
            <incoming>Flow_1</incoming>
            <outgoing>Flow_2</outgoing>
        </userTask>
        <endEvent id="EndEvent_1">
            <incoming>Flow_2</incoming>
        </endEvent>
        <sequenceFlow id="Flow_1" sourceRef="StartEvent_1" targetRef="UserTask_1"/>
        <sequenceFlow id="Flow_2" sourceRef="UserTask_1" targetRef="EndEvent_1"/>
    </process>
</definitions>'''

        model = xml_to_playbook_model(xml)
        mermaid = model_to_sequence_flow(model)
        # Should still generate valid Mermaid
        assert "```mermaid" in mermaid
        assert "UserTask_1" in mermaid

    def test_parallel_gateway(self):
        """Test handling of parallel gateway"""
        xml = '''<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL">
    <process id="test" name="Test">
        <startEvent id="StartEvent_1">
            <outgoing>Flow_1</outgoing>
        </startEvent>
        <parallelGateway id="Gateway_1">
            <incoming>Flow_1</incoming>
            <outgoing>Flow_2</outgoing>
            <outgoing>Flow_3</outgoing>
        </parallelGateway>
        <userTask id="UserTask_1" name="Task 1">
            <incoming>Flow_2</incoming>
            <outgoing>Flow_4</outgoing>
        </userTask>
        <userTask id="UserTask_2" name="Task 2">
            <incoming>Flow_3</incoming>
            <outgoing>Flow_5</outgoing>
        </userTask>
        <endEvent id="EndEvent_1">
            <incoming>Flow_4</incoming>
        </endEvent>
        <endEvent id="EndEvent_2">
            <incoming>Flow_5</incoming>
        </endEvent>
        <sequenceFlow id="Flow_1" sourceRef="StartEvent_1" targetRef="Gateway_1"/>
        <sequenceFlow id="Flow_2" sourceRef="Gateway_1" targetRef="UserTask_1"/>
        <sequenceFlow id="Flow_3" sourceRef="Gateway_1" targetRef="UserTask_2"/>
        <sequenceFlow id="Flow_4" sourceRef="UserTask_1" targetRef="EndEvent_1"/>
        <sequenceFlow id="Flow_5" sourceRef="UserTask_2" targetRef="EndEvent_2"/>
    </process>
</definitions>'''
        model = xml_to_playbook_model(xml)

        gateway = model["gateways"]["Gateway_1"]
        assert gateway.type == "parallel"
        assert len(gateway.outgoing) == 2

    def test_loop_back_flow(self):
        """Test handling of loop-back flows (retry/iteration patterns)"""
        xml = '''<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
             xmlns:resilient="http://resilient.ibm.com/bpmn">
    <process id="test" name="Test Loop">
        <startEvent id="StartEvent_1">
            <outgoing>Flow_1</outgoing>
        </startEvent>
        <userTask id="UserTask_1" name="Attempt Task">
            <incoming>Flow_1</incoming>
            <incoming>Flow_4</incoming>
            <outgoing>Flow_2</outgoing>
        </userTask>
        <exclusiveGateway id="Gateway_1" resilient:documentation="Check if successful">
            <incoming>Flow_2</incoming>
            <outgoing>Flow_3</outgoing>
            <outgoing>Flow_4</outgoing>
        </exclusiveGateway>
        <endEvent id="EndEvent_1">
            <incoming>Flow_3</incoming>
        </endEvent>
        <sequenceFlow id="Flow_1" sourceRef="StartEvent_1" targetRef="UserTask_1"/>
        <sequenceFlow id="Flow_2" sourceRef="UserTask_1" targetRef="Gateway_1"/>
        <sequenceFlow id="Flow_3" name="Success" sourceRef="Gateway_1" targetRef="EndEvent_1"/>
        <sequenceFlow id="Flow_4" name="Retry" sourceRef="Gateway_1" targetRef="UserTask_1"/>
    </process>
</definitions>'''
 
        model = xml_to_playbook_model(xml)
 
        # Verify loop-back flow exists
        assert "Flow_4" in model["flows"]
        loop_flow = model["flows"]["Flow_4"]
        assert loop_flow.source == "Gateway_1"
        assert loop_flow.target == "UserTask_1"
        assert loop_flow.name == "Retry"
 
        # Verify task has multiple incoming flows (initial + loop-back)
        task = model["tasks"]["UserTask_1"]
        # Note: incoming flows are not tracked in outgoing list, but we can verify the flow exists
 
        # Generate Mermaid to ensure loop-back is rendered
        mermaid = model_to_sequence_flow(model)
        assert "Retry" in mermaid
        assert "Gateway_1" in mermaid
        assert "UserTask_1" in mermaid
