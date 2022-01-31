#!/bin/bash

# Utility helper to move things around on the internal repo.
# Run from the `.scripts/` directory

# get the latest 'master'
git checkout master && git pull

# get onto a branch named 'public'
git checkout public && git pull

while read line
do
    # check out a specific directory from the master branch
    rm -rf ../$line
    git checkout master ../$line

    #array=( ${array[@]} $line )
    #echo ${array[@]}
done <<EOM
.github
.scripts/mirror-containers
CONTRIBUTING.md
LICENSE
README.md
app_host_files
base_input_types
fn_alienvault_otx
fn_anomali_staxx
fn_ansible
fn_ansible_tower
fn_apility
fn_aws_guardduty
fn_api_void
fn_aws_iam
fn_aws_utilities
fn_bigfix
fn_calendar_invite
fn_cb_protection
fn_cisco_amp4ep
fn_cisco_asa
fn_cisco_enforcement
fn_cisco_umbrella_inv
fn_clamav
fn_cloud_foundry
fn_create_webex_meeting
fn_create_zoom_meeting
fn_crowdstrike_falcon
fn_cve_search
fn_datatable_utils
fn_digital_shadows_search
fn_docker
fn_elasticsearch
fn_email_header_validation
fn_exchange
fn_exchange_online
fn_floss
fn_geocoding
fn_google_cloud_dlp
fn_google_cloud_functions
fn_google_maps_directions
fn_greynoise
fn_grpc_interface
fn_grr_search
fn_hibp
fn_html2pdf
fn_icdx
fn_incident_utils
fn_ioc_parser_v2
fn_ipinfo
fn_isitphishing
fn_jira
fn_joe_sandbox_analysis
fn_kafka
fn_ldap_utilities
fn_log_capture
fn_machine_learning
fn_machine_learning_nlp
fn_mcafee_atd
fn_mcafee_epo
fn_mcafee_esm
fn_mcafee_opendxl
fn_mcafee_tie
fn_microsoft_security_graph
fn_microsoft_sentinel
fn_misp
fn_mitre_integration
fn_mxtoolbox
fn_netdevice
fn_odbc_query
fn_outbound_email
fn_pa_panorama
fn_pagerduty
fn_pastebin
fn_phish_ai
fn_phish_tank
fn_pipl
fn_playbook_utils
fn_proofpoint_tap
fn_proofpoint_trap
fn_pulsedive
fn_qradar_advisor
fn_qradar_enhanced_data
fn_qradar_integration
fn_query_tor_network
fn_rsa_netwitness
fn_scheduler
fn_secureworks_ctp
fn_sentinelone
fn_sep
fn_service_now
fn_shodan
fn_slack
fn_spamhaus_query
fn_splunk_integration
fn_symantec_dlp
fn_task_utils
fn_teams
fn_thug
fn_twilio
fn_twitter_most_popular
fn_url_to_dns
fn_urlhaus
fn_urlscanio
fn_utilities
fn_virustotal
fn_vmray_analyzer
fn_watson_translate
fn_whois
fn_whois_rdap
fn_wiki
fn_xforce
fn_zia
older
rc-cts-abuseipdb
rc-cts-googlesafebrowsing
rc-cts-haveibeenpwned
rc-cts-mcafeetie
rc-cts-misp
rc-cts-passivetotal
rc-cts-shadowserver
rc-cts-urlscanio
rc-cts-yeti
rc_data_feed
rc-data-feed-plugin-elasticfeed
rc-data-feed-plugin-filefeed
rc-data-feed-plugin-kafkafeed
rc_data_feed_plugin_odbcfeed
rc-data-feed-plugin-resilientfeed
rc-data-feed-plugin-splunkfeed
res_qraw_mitre
sc_convert_json_to_rich_text
sc_email_parser
EOM

# Specify directories to exclude
while read line
do
    # Removes specific directories
    rm -rf ../$line
done <<EOM
.gitignore
.icons
.travis.yml
fn_service_now/snow_app
EOM
