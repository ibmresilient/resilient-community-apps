"""
Template for formatting incident data in a structured, readable format.
Converted from FreeMarker template to Python string template.
"""

INCIDENT_TEMPLATE = """# Incident {inc_id}: {inc_name}

Organization: {org_name}
Workspace: {workspace_name} (ID: {workspace_id})

Name: {inc_name}
Severity: {severity_code}
Incident Types: {incident_types}
Incident enabled: {inc_enabled}
Incident disposition: {inc_disposition}

Description:
<incident_description>
{inc_description}
</incident_description>
{training_line}
### Address:

- Street address: {inc_address}
- City: {inc_city}
- State: {inc_state}
- Zip code: {inc_zip}

### Timeline
{timeline}

### Incident Members

{members}

### Artifacts

{artifacts_section}

### Last 10 playbook executions

{playbook_executions}

### Tasks

Tasks that have a status of "Closed" have been completed, and are considered finished.

{tasks_section}

{custom_properties_section}
"""
def format_incident_data(incident_data: dict) -> str:
    """
    Format incident data using the template.
    
    Args:
        incident_data: Dictionary containing all incident information
        
    Returns:
        Formatted string with incident details
    """
    return INCIDENT_TEMPLATE.format(**incident_data)

