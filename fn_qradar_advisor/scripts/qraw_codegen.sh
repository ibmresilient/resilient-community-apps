resilient-circuits codegen \
-p fn_qradar_advisor \
-f qradar_advisor_offense_analysis qradar_advisor_quick_search qradar_advisor_full_search qradar_advisor_map_rule \
-m fn_qradar_advisor \
--workflow qradar_advisor_offense_analysis qradar_advisor_quick_search qradar_advisor_full_search qradar_advisor_map_rule_to_tactic \
--rule "QRadar Advisor Offense Analysis" "Watson Search" "Watson Search with Local Context" "Create Artifact (QRadar Advisor Analysis)" \
"Create Artifact (Watson Search with Local Context)" "Map rule to MITRE tactic" \
--script "Create Artifact for QRadar Advisor Analysis Observable" "Create Artifact for Watson Search with Local Context" \
--datatable qradar_advisor_observable qradar_advisor_observable_for_artifact mitre_attack_of_artifact mitre_attack_of_incident mitre_attack_techniques qradar_reference_set \
--exportfile export.res
