from lxml import etree as ET # type: ignore (vscode seems to not find the module)
from abc import ABC
from dataclasses import dataclass
from typing import Dict, List, Optional, Union, TypedDict

from fn_watsonx_analyst.util.rest import RestHelper, RestUrls


class Namespaces:
    """XML namespace constants for BPMN parsing."""
    BPMN = "http://www.omg.org/spec/BPMN/20100524/MODEL"
    RESILIENT = "http://resilient.ibm.com/bpmn"
    XSI = "http://www.w3.org/2001/XMLSchema-instance"

    @classmethod
    def as_dict(cls) -> Dict[str, str]:
        """Return namespaces as a dictionary for XPath queries."""
        return {
            "bpmn": cls.BPMN,
            "resilient": cls.RESILIENT,
        }


class XPathQueries:
    """XPath query constants for BPMN elements."""

    PROCESS = ".//bpmn:process"
    START_EVENT = ".//bpmn:startEvent"
    END_EVENT = ".//bpmn:endEvent"

    USER_TASK = ".//bpmn:userTask"

    SCRIPT_TASK = ".//bpmn:scriptTask"

    EXCLUSIVE_GATEWAY = ".//bpmn:exclusiveGateway"
    PARALLEL_GATEWAY = ".//bpmn:parallelGateway"
    ALL_GATEWAYS = ".//bpmn:exclusiveGateway | .//bpmn:parallelGateway"
    SEQUENCE_FLOW = ".//bpmn:sequenceFlow"

    CALL_ACTIVITY = ".//bpmn:callActivity" # sub-playbook
    SERVICE_TASK = ".//bpmn:serviceTask" # function


class FormatConstants:
    """Formatting constants for output."""
    INDENT = "    "
    SEPARATOR = "-" * 60
    CONDITION_PREVIEW_LENGTH = 120
    JSON_PREVIEW_LENGTH = 120


class PlaybookModel(TypedDict):
    """Type definition for the parsed playbook model."""
    process_name: str
    process_id: str
    tasks: Dict[str, Union['Task', 'ScriptTask', 'ServiceTask', 'SubPlaybookElement']]
    gateways: Dict[str, 'Gateway']
    flows: Dict[str, 'Flow']
    start_events: List[str]
    end_events: List[str]

class BPMNElement(ABC):
    """Base class for all BPMN elements."""

    def __init__(self, elem: ET.Element):
        self.id: str = elem.attrib["id"]
        self.name: str = elem.attrib.get("name", "")
        self.outgoing: List[str] = []  # flow IDs

    def get_display_name(self) -> str:
        """Return a human-readable display name for this element."""
        return self.name or self.id


@dataclass
class Task(BPMNElement):
    """User task (human-performed step)."""

    auto_name: Optional[str] = None
    auto_uuid: Optional[str] = None

    def __init__(self, elem: ET.Element):
        super().__init__(elem)

@dataclass
class ScriptTask(BPMNElement):
    """BPMN scriptTask - contains a reference to a stored script."""

    script_uuid: Optional[str] = None

    def __init__(self, elem: ET.Element):
        super().__init__(elem)
        script_elem = elem.find(
            ".//resilient:script",
            {"resilient": Namespaces.RESILIENT},
        )
        if script_elem is not None:
            self.script_uuid = script_elem.attrib.get("uuid")

@dataclass
class ServiceTask(BPMNElement):
    """BPMN serviceTask - represents a SOAR function."""

    resilient_type: Optional[str] = None
    function_uuid: Optional[str] = None
    function_json: Optional[str] = None

    def __init__(self, elem: ET.Element):
        super().__init__(elem)
        self.resilient_type = elem.attrib.get(f"{{{Namespaces.RESILIENT}}}type")

        func_elem = elem.find(
            ".//resilient:function",
            {"resilient": Namespaces.RESILIENT},
        )
        if func_elem is not None:
            self.function_uuid = func_elem.attrib.get("uuid")
            if func_elem.text:
                self.function_json = func_elem.text.strip()

@dataclass
class Gateway(BPMNElement):
    """Exclusive or parallel gateway."""

    type: str = ""
    doc: Optional[str] = None
    default: Optional[str] = None  # default flow ID (exclusive only)

    def __init__(self, elem: ET.Element):
        super().__init__(elem)
        self.type = "exclusive" if "exclusiveGateway" in elem.tag.lower() else "parallel"
        self.doc = elem.attrib.get(f"{{{Namespaces.RESILIENT}}}documentation")
        self.default = elem.attrib.get("default")

@dataclass
class Flow:
    """Sequence flow - may carry a human-readable name and a condition."""

    id: str
    source: str
    target: str
    name: str = ""
    condition: Optional[str] = None

    def __init__(self, elem: ET.Element):
        self.id = elem.attrib["id"]
        self.source = elem.attrib["sourceRef"]
        self.target = elem.attrib["targetRef"]
        self.name = elem.attrib.get("name", "")

@dataclass
class SubPlaybookElement(BPMNElement):
    """BPMN call activity that refers to a subplaybook"""

    sub_playbook_name: Optional[str] = None
    sub_playbook_uuid: Optional[str] = None

    def __init__(self, elem: ET.Element):
        super().__init__(elem)


        sub_pb_elem = elem.find(
            "./bpmn:extensionElements/resilient:sub-playbook",
            {"bpmn": Namespaces.BPMN, "resilient": Namespaces.RESILIENT}
        )

        if sub_pb_elem is not None:
            self.sub_playbook_name = sub_pb_elem.attrib.get("name")
            self.sub_playbook_uuid = sub_pb_elem.attrib.get("uuid")

        self.id = self.id.replace("CallActivity_", "SubPlaybook_")

def _register_tasks(
    root: ET.Element,
    xpath: str,
    task_class: type,
    tasks_dict: Dict,
    ns: Dict[str, str]
) -> None:
    """
    Register tasks of a specific type into the tasks dictionary.
    
    Args:
        root: XML root element
        xpath: XPath query string for finding elements
        task_class: Class constructor (Task, ScriptTask, or ServiceTask)
        tasks_dict: Dictionary to store task objects
        ns: Namespace dictionary for XPath queries
    """
    for elem in root.findall(xpath, ns):
        task = task_class(elem)
        tasks_dict[task.id] = task


def _parse_all_tasks(root: ET.Element, ns: Dict[str, str]) -> Dict[str, Union[Task, ScriptTask, ServiceTask]]:
    """Parse all task types using a loop over task configurations."""
    tasks: Dict[str, Union[Task, ScriptTask, ServiceTask]] = {}
    task_configs = [
        (XPathQueries.USER_TASK, Task),
        (XPathQueries.SCRIPT_TASK, ScriptTask),
        (XPathQueries.SERVICE_TASK, ServiceTask),
        (XPathQueries.CALL_ACTIVITY, SubPlaybookElement)
    ]
    for xpath, task_class in task_configs:
        _register_tasks(root, xpath, task_class, tasks, ns)
    return tasks


def _parse_gateways(root: ET.Element, ns: Dict[str, str]) -> Dict[str, Gateway]:
    """Parse all gateway elements."""
    gateways: Dict[str, Gateway] = {}
    for g in root.findall(XPathQueries.PARALLEL_GATEWAY, ns):
        gateways[g.attrib["id"]] = Gateway(g)

    for g in root.findall(XPathQueries.EXCLUSIVE_GATEWAY, ns):
        gateways[g.attrib["id"]] = Gateway(g)

    return gateways


def _parse_flows(root: ET.Element, ns: Dict[str, str], tasks: Dict, gateways: Dict) -> Dict[str, Flow]:
    """Parse sequence flows and register outgoing connections."""
    flows: Dict[str, Flow] = {}
    for f in root.findall(XPathQueries.SEQUENCE_FLOW, ns):
        flow = Flow(f)
        # Replace CallActivity references with SubPlaybook to match renamed IDs
        flow.source = flow.source.replace("CallActivity_", "SubPlaybook_")
        flow.target = flow.target.replace("CallActivity_", "SubPlaybook_")
        flows[flow.id] = flow
        source_node = tasks.get(flow.source) or gateways.get(flow.source)
        if source_node:
            source_node.outgoing.append(flow.id)
    return flows


def _parse_events(root: ET.Element, ns: Dict[str, str]) -> tuple[List[str], List[str]]:
    """Parse start and end events."""
    start_events = [s.attrib["id"] for s in root.findall(XPathQueries.START_EVENT, ns)]
    end_events = [e.attrib["id"] for e in root.findall(XPathQueries.END_EVENT, ns)]
    return start_events, end_events


def _parse_process_metadata(root: ET.Element, ns: Dict[str, str]) -> tuple[str, str]:
    """Parse process name and ID with defaults."""
    process = root.find(XPathQueries.PROCESS, ns)
    process_name = process.attrib.get("name", "Unnamed") if process is not None else "Unnamed"
    process_id = process.attrib.get("id", "unknown") if process is not None else "unknown"
    return process_name, process_id


def build_model(root: ET.Element) -> PlaybookModel:
    """
    Parse BPMN XML tree and create a structured model.
    
    Returns a dictionary containing:
        - process_name: Name of the playbook
        - process_id: ID of the playbook
        - tasks: Dictionary of Task/ScriptTask/ServiceTask objects
        - gateways: Dictionary of Gateway objects
        - flows: Dictionary of Flow objects
        - start_events: List of start event IDs
        - end_events: List of end event IDs
    
    Args:
        root: XML root element from parsed BPMN file
    
    Returns:
        PlaybookModel dictionary with all parsed elements
    """
    ns = Namespaces.as_dict()

    tasks = _parse_all_tasks(root, ns)
    gateways = _parse_gateways(root, ns)
    flows = _parse_flows(root, ns, tasks, gateways)
    start_events, end_events = _parse_events(root, ns)
    process_name, process_id = _parse_process_metadata(root, ns)

    return {
        "process_name": process_name,
        "process_id": process_id,
        "tasks": tasks,
        "gateways": gateways,
        "flows": flows,
        "start_events": start_events,
        "end_events": end_events,
    }

def _truncate_text(text: str, max_length: int = FormatConstants.CONDITION_PREVIEW_LENGTH) -> str:
    """Truncate text to max_length with ellipsis if needed."""
    text = text.replace("\n", " ").strip()
    if len(text) > max_length:
        return text[:max_length - 3] + "..."
    return text

def format_mermaid_flowchart(model: PlaybookModel) -> str:
    """
    Generate a Mermaid TD (Top-Down) flowchart of the sequence flow.
    
    Features:
        - TD (Top-Down) orientation
        - Start events as rounded rectangles
        - Tasks as rectangles with appropriate labels
        - Gateways as diamonds
        - End events as rounded rectangles
        - Flow labels showing conditions
        - Sanitized node labels for Mermaid compatibility
    
    Returns:
        Mermaid flowchart syntax as a string
    """
    lines: List[str] = []
    lines.append("```mermaid")
    lines.append("graph TD")

    # Helper function to sanitize node IDs for Mermaid identifiers
    def sanitize_id(node_id: str) -> str:
        """Convert node ID to Mermaid-safe identifier."""
        if node_id.startswith("StartEvent"):
            return "StartEvent"
        # Replace special characters with underscores
        safe = node_id.replace("-", "_").replace(".", "_").replace(" ", "_")
        safe = safe.replace("(", "_").replace(")", "_").replace("`", "")
        safe = safe.replace(",", "_").replace(":", "_").replace("/", "_")
        # Remove consecutive underscores
        while "__" in safe:
            safe = safe.replace("__", "_")
        # Remove leading/trailing underscores
        return safe.strip("_")

    # Helper function to escape special characters in labels
    def escape_label(text: str) -> str:
        """Escape special characters for Mermaid labels."""
        return text.replace('"', '#quot;').replace('[', '#91;').replace(']', '#93;')

    # Create mapping from node_id to sanitized ID (use node ID itself, not label)
    node_id_to_safe_id: Dict[str, str] = {}

    node_ids = model.get('start_events', []) +\
        model.get('end_events', []) +\
        list(model["tasks"].keys()) +\
        list(model["gateways"].keys())

    for node_id in node_ids:
        node_id_to_safe_id[node_id] = sanitize_id(node_id)

    # Helper function to get node shape and label
    def get_node_definition(node_id: str) -> str:
        """Return Mermaid node definition with appropriate shape."""
        safe_id = node_id_to_safe_id[node_id]

        # Start events - rounded rectangle
        if node_id in model.get("start_events", []):
            return f'{safe_id}(["Start Event"])'

        # End events - rounded rectangle
        if node_id in model.get("end_events", []):
            node_num = node_id.split('_')[-1] if '_' in node_id else node_id
            return f'{safe_id}(["End point (Node {node_num})"])'

        # Tasks - rectangle
        if node_id in model["tasks"]:
            task_obj = model["tasks"][node_id]
            name = escape_label(task_obj.name or node_id)
            node_num = node_id.split('_')[-1] if '_' in node_id else node_id

            if isinstance(task_obj, Task):
                return f'{safe_id}["Task: {name}<br/>(Node {node_num})"]'
            elif isinstance(task_obj, ScriptTask):
                return f'{safe_id}["Script: {name}<br/>(Node {node_num})"]'
            elif isinstance(task_obj, ServiceTask):
                return f'{safe_id}["Function: {name}<br/>(Node {node_num})"]'
            elif isinstance(task_obj, SubPlaybookElement):
                return f'{safe_id}["Sub-playbook: {name}<br/>(Node {node_num})"]'

            return f'{safe_id}["{name}<br/>(Node {node_num})"]'

        # Gateways - diamond
        if node_id in model["gateways"]:
            gateway = model["gateways"][node_id]
            node_num = node_id.split('_')[-1] if '_' in node_id else node_id

            if gateway.doc:
                label = escape_label(gateway.doc)
                return '{0}{{"{1}<br/>(Node {2})"}}'.format(safe_id, label, node_num) # pylint: disable=consider-using-f-string
            else:
                return '{safe_id}{{"Condition point<br/>(Node {node_num})"}}'.format(safe_id=safe_id, node_num=node_num) # pylint: disable=consider-using-f-string

        # Default - rectangle
        return f'{safe_id}["{escape_label(node_id)}"]'

    # Collect all nodes that need to be defined
    all_nodes: set[str] = set()
    all_nodes.update(model.get("start_events", []))
    all_nodes.update(model.get("end_events", []))
    all_nodes.update(model["tasks"].keys())
    all_nodes.update(model["gateways"].keys())

    # Define all nodes first (optional but helps with readability)
    for node_id in sorted(all_nodes):
        node_def = get_node_definition(node_id)
        lines.append(f"    {node_def}")

    lines.append("")

    # Sort flows by execution order for better readability
    # Use BFS from start events to order flows logically
    def sort_flows_by_execution_order(flows: Dict[str, Flow], start_events: List[str]) -> List[Flow]:
        """Sort flows in execution order using breadth-first traversal."""
        visited_nodes = set()
        ordered_flows = []
        queue = list(start_events)

        while queue:
            current_node = queue.pop(0)
            if current_node in visited_nodes:
                continue
            visited_nodes.add(current_node)

            # Find all flows from this node and add them in order
            node_flows = [f for f in flows.values() if f.source == current_node]
            # Sort by target to ensure consistent ordering
            node_flows.sort(key=lambda f: f.target)

            for flow in node_flows:
                if flow not in ordered_flows:
                    ordered_flows.append(flow)
                    if flow.target not in visited_nodes:
                        queue.append(flow.target)

        # Add any remaining flows not reached from start events
        for flow in flows.values():
            if flow not in ordered_flows:
                ordered_flows.append(flow)

        return ordered_flows

    # Define all flows in execution order
    ordered_flows = sort_flows_by_execution_order(model["flows"], model.get("start_events", []))

    for flow in ordered_flows:
        # Use sanitized node IDs instead of labels
        src_id = node_id_to_safe_id.get(flow.source, sanitize_id(flow.source))
        tgt_id = node_id_to_safe_id.get(flow.target, sanitize_id(flow.target))

        # Build flow label
        flow_label = ""
        if flow.name:
            flow_label = escape_label(flow.name)
        elif flow.condition:
            # Truncate condition for readability
            cond = _truncate_text(flow.condition, 50)
            flow_label = escape_label(cond)

        # Create flow connection
        if flow_label:
            lines.append(f'    {src_id} -->|"{flow_label}"| {tgt_id}')
        else:
            lines.append(f'    {src_id} --> {tgt_id}')

    lines.append("```")

    return "\n".join(lines)

def xml_to_playbook_model(xml: str) -> PlaybookModel:
    # setup safe parser
    parser = ET.XMLParser(resolve_entities=False, no_network=True)
    root = ET.fromstring(xml.encode("utf-8"), parser=parser)

    # build data model
    return build_model(root)

def model_to_scripts(model: PlaybookModel) -> List[str]:
    rh = RestHelper()
    org_scripts = rh.do_request(RestUrls.GET_PLAYBOOK_SCRIPTS)
    output = []
    if not org_scripts:
        return output

    for task_obj in model["tasks"].values():
        if isinstance(task_obj, ScriptTask):
            matching = next(matching for matching in org_scripts if matching["uuid"] == task_obj.script_uuid)
            if matching:
                script_object = rh.do_request(RestUrls.GET_PLAYBOOK_SCRIPT, script_id=matching["id"])
                out = f"Playbook script name: {matching['name']}. Description: {matching['description'] or 'None'}"
                out += "\nPython script contents:"
                out += f"\n\n```{script_object['script_text'].encode().decode('unicode_escape')}```"
                output.append(out)

    if len(output) > 0:
        output = ["\n\nPLAYBOOK SCRIPTS:\n", *output]

    return output

def model_to_sequence_flow(model: PlaybookModel) -> str:
    """
    Convert SOAR playbook xml to a mermaid diagram
    """
    # represent as mermaid
    return format_mermaid_flowchart(model)
