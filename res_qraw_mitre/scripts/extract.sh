resilient-circuits extract \
--workflow qradar_advisor_map_rule_to_tactic qradar_advisor_offense_analysis_mitre \
--rule "Map rule to MITRE tactic" "QRadar Advisor Offense Analysis with MITRE" \
--datatable mitre_attack_of_artifact mitre_attack_of_incident mitre_attack_techniques qradar_reference_set \
--exportfile export.res \
-o qraw_mitre.res

