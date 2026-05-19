#
# Sample return from function
# 
# results = {"mitre_tactics":[
#   {
#     "tactic_name": "Execution",
#     "tactic_id": "TA0002",
#     "tactic_ref": "https://attack.mitre.org/tactics/TA0002/",
#     "techs": []
#   }
#]
#
#

# Read result from QRAW to get confidence information
insights = workflow.properties.qraw_offense_insights.insights
mitre_tactics = insights["tactics"]

tactic_confidence = {}
if mitre_tactics is not None:
  for tactic in mitre_tactics:
    tactic_confidence[tactic["tactic_id"]] = tactic["confidence"]


tactics = results.mitre_tactics

for tactic in tactics:
  #
  # MITRE ATTACK of Incident Datatable
  #
  tactic_row = incident.addRow("mitre_attack_of_incident")
  tactic_row["attack_tactic"] = tactic["tactic_name"]
  tactic_row["tactic_code"] = tactic["tactic_id"]
  url_html = '<a href="' + tactic["tactic_ref"] + '">' + tactic["tactic_ref"] + '</a><br>'
  tactic_row["reference"] = helper.createRichText(url_html)
  tactic_row["confidence"] = str(tactic_confidence.get(tactic["tactic_name"], ""))
  #
  # MITRE ATT&CK techniques Datatable
  #
  techs = tactic["techs"]
  for att_tech in techs:
    tech_row = incident.addRow("mitre_attack_techniques")
    tech_row["tactic"] = tactic["tactic_name"]

    tech_row["technique_name"] = att_tech["name"]
    tech_row["tech_description"] = att_tech["description"]
    refs = att_tech["external_references"]
    ref_html = ""
    for ref in refs:
      ref_html = ref_html + '<a href="' + ref["url"] + '">' + ref["url"] + '</a><br>'
    tech_row["references"] = helper.createRichText(ref_html)
    tech_row["detection"] = att_tech["x_mitre_detection"]
    tech_row["technique_id"] = att_tech["mitre_tech_id"]

