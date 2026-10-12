#
# Result retured by the QRadar Advisor Offense Analysis function:
#   * results.observables: observables and their details, used here to be output to Data table.
#   * results.note: html representation of STIX data, used here to generate a Note.
#   * results.insights: used here to create a Task.
#   * results.stix: raw stix data, preserved for any customized parsing.
#
#   Note: results.insights can have a status code e.g. 404
#
# We publish a data table according to the stix

# Check that we didn't get a status of 404 (no observables) for insights.
if "status_code" in results["insights"] and results["insights"]["status_code"] == 404:
    process_insights = False
else:
    process_insights = True

for observable in results.observables:
  qradar_obs = incident.addRow("qradar_advisor_observable")
  qradar_obs.qradar_advisor_toxicity = observable.toxicity
  qradar_obs.qradar_advisor_relevance = observable.relevance
  qradar_obs.qradar_advisor_type = observable.type
  qradar_obs.qradar_advisor_description = observable.description

# Pass insights data (with MITRE ATTACK tactics information) to following function
# using workflow.properties.qraw_offense_insights. Refer to the Output tab please

# Our STIX tree or error status.
html = helper.createRichText(results.note)
incident.addNote(html)

if process_insights:
    # If we didn't get a 404 (no observables) status process for insights.
    # Task
    task_title = "Review QRadar Advisor Analysis for Offense " + str(incident.properties.qradar_id)
    task_summary = results.insights.insights + "\n\n" + results.insights.stage3_insights
    incident.addTask(task_title, "Initial", task_summary)

    #
    # MITRE tactic information
    #
    tactics = results.insights["tactics"]

    mitre_tactic_names = []
    if tactics is not None:
      for tactic in tactics:
        #
        # Note, even though QRAW calls it tactic_id, it is more a tactic name
        #
        mitre_tactic_names.append(tactic["tactic_id"])
    #
    # QRadar Advisor might return more than one tactics for a given offense. Include them inputs
    # a comma separated string
    #
    incident.properties.mitre_tactic_name = ", ".join(mitre_tactic_names)

# Note that results.stix is the raw stix return from QRadar Advisor in stix 2 (json) format
# Users can add their customize codes to handle the stix data here
#