resilient-sdk codegen \
-p fn_qradar_enhanced_data \
-f qradar_top_events qradar_offense_summary \
-m fn_qradar_enhanced_data \
--field qradar_id qr_assigned qr_credibility qr_destination_ip_count qr_event_count qr_magnitude qr_offense_index_type qr_offense_index_value qr_offense_source qr_relevance  qr_severity qr_source_ip_count \
--workflow example_of_searching_qradar_top_events_using_offense_id qradar_offense_summary qradar_source_ips qradar_destination_ips qradar_categories qradar_triggered_rules qradar_assets_information \
--rule "QRadar Enhanced Data" "Create Artifact from Assets info" "Create artifact from Destination IP info" "Create Artifact from Events info" "Create artifact from Source IP info" \
--script "Create Artifact from Assets info" "Create Artifact from Destination IP info" "Create Artifact from Events info" "Create Artifact from Source IP info" \
--datatable qr_offense_top_events qr_top_destination_ips qr_top_source_ips qr_triggered_rules qr_categories qr_assets