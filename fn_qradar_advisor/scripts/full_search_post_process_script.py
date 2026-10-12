import java.util.Date as Date

# Return data of function Watson Search with Local Context:
#   * results.observables: observables and their details, used here to be output to Data table.
#   * results.note: html representation of STIX data, used here to generate a Note.
#   * results.summary: used here to create a Task.
#   * results.stix: raw stix data (not used here), for any customized parsing.

# Check that we didn't get a status of 404 (no observables) for insights.
if "status_code" in results["stix"] and results["stix"]["status_code"] == 404:
    add_task = False
else:
    add_task  = True
# We publish a data table according to the stix if obserables found.
date_str = str(Date())
for observable in results.observables:
  qradar_obs = incident.addRow("qradar_advisor_observable_for_artifact")
  qradar_obs.qradar_advisor_toxicity = observable.toxicity 
  qradar_obs.qradar_advisor_relevance = observable.relevance
  qradar_obs.qradar_advisor_type = observable.type 
  qradar_obs.qradar_advisor_description = observable.description 
  qradar_obs.artifact_related = artifact.value
  qradar_obs.full_search_time = date_str
# Our STIX tree or error message
html = helper.createRichText(results.note)
incident.addNote(html)

if add_task:
    # Create a task
    incident.addTask("Review Watson Search with Local Context of artifact: " + artifact.value, "Initial", results.summary)