resilient-circuits codegen \
-p fn_qradar_integration \
-f qradar_add_reference_set_item qradar_delete_reference_set_item qradar_find_reference_set_item qradar_search qradar_find_reference_sets \
-m fn_qradar_integration \
--workflow qradar_add_reference_set_item qradar_delete_reference_set_item qradar_find_reference_set_item qradar_search_event_offense qradar_move_item_to_different_ref_set \
qradar_find_reference_sets_artifact \
--rule "QRadar Add to Reference Set" "Delete from QRadar Reference Set" "Find in QRadar Reference Set" "Search QRadar for offense id" "QRadar Move from suspect to blocked" \
"Find QRadar Reference Sets" \
--datatable qradar_offense_event qradar_reference_set \
--exportfile export.res
