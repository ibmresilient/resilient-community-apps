resilient-circuits codegen \
-p fn_mitre_integration \
-f mitre_tactic_information mitre_technique_information \
-m fn_mitre_integration \
--field mitre_tactic_name mitre_technique_name \
--workflow mitre_technique_task mitre_get_tactic_information mitre_get_technique_information \
--rule "Create Task For Technique" "Get MITRE technique information" "Get MITRE tactic information" \
--datatable mitre_attack_of_incident mitre_attack_of_incident \
--exportfile export.res
