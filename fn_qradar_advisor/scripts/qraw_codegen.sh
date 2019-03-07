resilient-circuits codegen \
-p fn_qradar_advisor \
-f qradar_advisor_offense_analysis qradar_advisor_quick_search qradar_advisor_full_search qradar_advisor_map_rule \
-m fn_qradar_advisor \
--field mitre_tactic_name qradar_rule \
--workflow qradar_advisor_offense_analysis qradar_advisor_quick_search qradar_advisor_full_search qradar_advisor_map_rule \
--rule "QRadar Advisor Offense Analysis" "Watson Search" "Watson Search with Local Context" "Create Artifact (QRadar Advisor Analysis)" \
"Create Artifact (Watson Search with Local Context)" "Map QRadar rule" \
--script "Create Artifact for QRadar Advisor Analysis Observable" "Create Artifact for Watson Search with Local Context" \
--datatable qradar_advisor_observable qradar_advisor_observable_for_artifact \
--exportfile export.res
