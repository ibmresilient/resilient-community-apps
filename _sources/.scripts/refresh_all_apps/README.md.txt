# Utility scripts for automatic app refreshment

## Overview

### customize_and_reload.sh

Script to run 'resilient-circuits customize' to import the app into
the SOAR server set in the app.config file in the same directory as
this script. Then reload the export.res using resilient-sdk and reset
the Dockerfile to the new template.

### inventory_apps_server_version.py

This Python script invertories all the SOAR apps under a given root directory.
It displays the server version of each SOAR app. In addition, it calculates the number of apps with the
server versions above the threshold value and the number of apps with the server versions below 
the threshold value

### REBUILD_IMAGE_NAMES.txt

Uncomment the app names that will be rebuilt

## Steps to rebuild apps using the app refreshment utility scripts

* List the SOAR apps that are still under server version 40

```
(env_3.11_refresh_apps) Macbook Pro resilient-community-apps % python3 .scripts/refresh_all_apps/inventory_apps_server_version.py
fn_cisco_enforcement                        30.0.0
fn_thug                                     30.0.0
fn_twitter_most_popular                  30.0.3476
fn_google_maps_directions                30.0.3476
fn_cisco_umbrella_inv                       30.0.0
fn_machine_learning                      30.0.3471
fn_google_cloud_functions                30.0.3476
fn_floss                                 30.0.3439
fn_email_header_validation                  30.0.0
fn_grr_search                             30.4.237
fn_apility                                30.4.237
fn_digital_shadows_search                31.0.4254
fn_threatminer                           31.0.4254
fn_cb_protection                         31.0.4254
fn_mcafee_atd                            31.0.4254
fn_crowdstrike_falcon                    31.0.4254
fn_mcafee_esm                            31.0.4254
fn_phish_tank                            31.0.4254
fn_query_tor_network                     31.0.4254
fn_docker                                31.0.4235
fn_proofpoint_trap                       32.0.4502
fn_machine_learning_nlp                  35.2.4502
fn_mitre_integration                       32.3.12
fn_twilio                                33.0.5087
fn_log_capture                           33.0.5087
fn_hibp                                  34.0.5261
fn_urlhaus                                  35.0.0
fn_pastebin                                 35.0.0
fn_spamhaus_query                           35.0.0
fn_shodan                                   35.0.0
fn_mxtoolbox                             35.0.5445
fn_vmray_analyzer                           35.0.0
fn_secureworks_ctp                       35.0.5445
fn_mcafee_opendxl                           35.0.0
fn_urlscanio                             35.0.5343
fn_whois                                   35.2.32
fn_anomali_staxx                           35.2.32
fn_components                              35.2.32
fn_ipinfo                                  35.2.32
fn_alienvault_otx                          35.2.32
fn_ioc_parser_v2                           35.2.32
fn_cve_search                              35.2.32
fn_geocoding                               35.2.32
fn_whois_rdap                              35.2.32
fn_ansible_tower                         36.0.5634
fn_calendar_invite                       36.0.5634
fn_task_utils                            36.0.5634
fn_greynoise                             36.0.5634
fn_pulsedive                             36.0.5634
fn_icdx                                     36.0.0
fn_url_to_dns                            36.0.5634
fn_mcafee_tie                            36.0.5634
fn_phish_ai                              36.0.5634
fn_wiki                                  36.0.5634
fn_isitphishing                          36.0.5634
fn_cloud_foundry                           36.2.76
fn_watson_translate                      39.0.6328
fn_html2pdf                              40.0.6554
fn_create_webex_meeting                     40.0.0
fn_netdevice                             40.0.6554
fn_aws_utilities                         41.0.6783
fn_clamav                                41.0.6783
fn_utilities                             42.0.7058
fn_elasticsearch                            43.0.0
fn_passivetotal                            43.1.49
fn_googlesafebrowsing                      43.1.49
fn_yeti                                    43.1.49
fn_timer                                   43.1.49
fn_ocr                                     43.1.49
fn_abuseipdb                               43.1.49
fn_google_cloud_scc                        43.1.49
fn_shadowserver                            43.1.49
fn_webex                                   43.1.49
fn_joe_sandbox_analysis                  44.0.7585
fn_create_zoom_meeting                   45.0.7899
fn_playbook_maker                           45.0.0
fn_trusteer_ppd                          45.0.7899
fn_github                                45.0.7899
fn_soar_utils                            45.0.7899
fn_darktrace                             45.0.7899
fn_teams                                 45.0.7899
fn_bmc_helix                             45.0.7899
fn_xforce                                45.0.7899
fn_randori                               45.0.7899
fn_salesforce                            46.0.8131
fn_incident_utils                        46.0.8131
fn_grpc_interface                        46.0.8131
fn_sep                                   46.0.8131
fn_network_utilities                     46.0.8131
fn_playbook_utils                        46.0.8131
fn_maas360                               46.0.8131
fn_reaqta                                46.0.8131
fn_slack                                 46.0.8131
fn_google_cloud_dlp                      46.0.8131
fn_exchange                              46.0.8131
fn_cisco_asa                             46.0.8131
fn_proofpoint_tap                        46.0.8131
fn_datatable_utils                       46.0.8131
fn_bigfix                                46.0.8131
fn_api_void                              46.0.8131
fn_pipl                                  46.0.8131
fn_extrahop                              46.0.8131
fn_scheduler                             46.0.8131
fn_relations                                48.0.0
fn_azure_automation_utilities               48.0.0
fn_splunk_integration                      48.2.16
fn_rest_api                                48.2.16
fn_sentinelone                             48.2.16
fn_mandiant                                48.2.16
fn_snapshot_url                            48.2.45
fn_parse_utilities                         48.2.16
fn_rapid7_insight_idr                       49.0.0
fn_aws_guardduty                         49.0.8803
fn_jira                                  49.0.8803
fn_mcafee_epo                            49.0.8803
fn_misp                                  49.0.8803
fn_ldap_utilities                        49.0.8803
fn_virustotal                            50.0.9097
fn_microsoft_sentinel                    50.0.9097
fn_wiz                                   50.0.9097
fn_qradar_enhanced_data                  50.0.9097
fn_axonius                                  50.0.0
fn_vmware_cbc                               50.0.0
fn_outbound_email                        50.0.9097
fn_cisco_amp4ep                          50.0.9097
fn_qradar_integration                    50.0.9097
fn_kafka                                 50.0.9097
fn_ansible                               50.0.9097
fn_pa_panorama                           50.0.9097
fn_rsa_netwitness                          50.2.42
fn_exchange_online                         50.2.42
fn_microsoft_defender                51.0.0.0.9340
fn_qradar_advisor                    51.0.0.0.9340
fn_aws_iam                           51.0.0.0.9340
fn_guardium_insights_integration     51.0.0.0.9340
fn_zia                               51.0.0.0.9340
fn_service_now                       51.0.0.0.9340
fn_odbc_query                        51.0.0.0.9340
fn_microsoft_security_graph          51.0.0.0.9340
fn_pagerduty                         51.0.0.0.9340
fn_guardium_integration              51.0.0.0.9340
fn_symantec_dlp                      51.0.0.0.9340
fn_siemplify                         51.0.0.0.9340
fn_remedy                            51.0.0.0.9340
Found 144 total apps; 87 apps are above v40.0.0; 57 apps are below v40.0.0
```

* Install pyenv on your local machine, please refer to https://github.com/pyenv/pyenv

For Mac
```
brew install pyenv
```

*  Create pyenv virtualenv that matches the value set for PYENV_VIRTUALENV_NAME

ex:
```
pyenv virtualenv 3.11.5 env_3.11_refresh_apps
```

* Check that you have a virtual environment created under $HOME/.pyenv/versions successfully

* Update the app.config in this folder to point to a SOAR with version 40

* Run this script to create branches, perform reloads, update version, git commit and git push
```
bash .scripts/refresh_all_apps/customize_and_reload.sh
```

* If the script runs successfully, you should see github branches for the apps that have been uncommented in REBUILD_IMAGE_NAMEs.txt

 ![screenshot: github_branches](./doc/screenshots/github_branches.png)