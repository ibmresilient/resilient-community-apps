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
.gitignore
.icons
.travis.yml
CONTRIBUTING.md
LICENSE
README.md
fn_alienvault_otx
fn_ansible
fn_apility
fn_aws_utilities
fn_bigfix
fn_bluecoat_site_review
fn_calendar_invite
fn_cb_protection
fn_cisco_amp4ep
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
fn_floss
fn_geocoding
fn_google_cloud_dlp
fn_google_cloud_functions
fn_google_maps_directions
fn_grpc_interface
fn_grr_search
fn_hibp
fn_html2pdf
fn_icdx
fn_ioc_parser_v2
fn_ip_void
fn_ipinfo
fn_isitPhishing
fn_jira
fn_joe_sandbox_analysis
fn_ldap_utilities
fn_machine_learning
fn_mcafee_atd
fn_mcafee_epo
fn_mcafee_esm
fn_mcafee_opendxl
fn_mcafee_tie
fn_microsoft_security_graph
fn_misp
fn_mitre_integration
fn_mxtoolbox
fn_netdevice
fn_odbc_query
fn_pa_panorama
fn_pagerduty
fn_pastebin
fn_phish_ai
fn_phish_tank
fn_pipl
fn_qradar_advisor
fn_qradar_integration
fn_query_tor_network
fn_res_to_icd
fn_risk_fabric
fn_rsa_netwitness
fn_sep
fn_service_now
fn_slack
fn_spamhaus_query
fn_splunk_integration
fn_task_utils
fn_thug
fn_twilio
fn_twitter_most_popular
fn_url_void
fn_urlhaus
fn_urlscanio
fn_utilities
fn_virustotal
fn_vmray_analyzer
fn_watson_translate
fn_whois
fn_xforce
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
rc-data-feed
res_qraw_mitre
sc_email_parser
EOM

# Specify directories to exclude
while read line
do
    # Removes specific directories
    rm -rf ../$line
done <<EOM
fn_service_now/snow_app
EOM
