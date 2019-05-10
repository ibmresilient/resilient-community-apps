HA_REST_API_URLS = {
    "submit_file": ("{}/submit/file", "post"),
    "submit_url": ("{}/submit/url-for-analysis", "post"),
    "get_state": ("{}/report/{}/state", "get"),
    "get_summary": ("{}/report/{}/summary", "get"),
}
HA_SUBMIT_URL_CONTENT_TYPE = 'application/x-www-form-urlencoded'
HA_COMPLETED_STATUSES = ["ERROR", "SUCCESS"]
HA_AVAILABLE_ENVS = {
                    "Android Static Analysis": "200",
                    "Linux (Ubuntu 16.04, 64 bit)": "300",
                    "Windows 7 32 bit": "100",
                    "Windows 7 32 bit (HWP Support)": "110",
                    "Windows 7 64 bit": "120"
                }
HA_AVAILABLE_RUNTIME_ACTION_SCRIPTS = {
    "Default analysis": "default.au3",
    "Heavy Anti-Evasion": "default_maxantievasion.au3",
    "Random desktop files": "default_randomfiles.au3",
    "Random desktop theme": "default_randomtheme.au3",
    "Open Internet Explorer": "default_openie.au3",
    "Default browser analysis": "default_browser.au3"
}
# List of runtime resilient function parameters for Submit File function 
HA_LIST_OF_RUNTIME_PARAMS_SUBMIT_FILE = [
    "falcon_sandbox_environment_id",
    "falcon_sandbox_action_script",
    "falcon_sandbox_no_share_third_party",
    "falcon_sandbox_allow_community_access",
    "falcon_sandbox_comment",
    "falcon_sandbox_priority",
    "falcon_sandbox_environment_variable",
    "falcon_sandbox_custom_run_time",
    "falcon_sandbox_submit_name",
    "falcon_sandbox_custom_date_time",
    "falcon_sandbox_document_password",
    "falcon_sandbox_tor_enabled_analysis",
]
# List of runtime resilient function parameters for Submit File function 
HA_LIST_OF_RUNTIME_PARAMS_SUBMIT_URL = [
    "falcon_sandbox_environment_id",
    "falcon_sandbox_action_script",
    "falcon_sandbox_no_share_third_party",
    "falcon_sandbox_allow_community_access",
    "falcon_sandbox_comment",
    "falcon_sandbox_priority",
    "falcon_sandbox_environment_variable",
    "falcon_sandbox_custom_run_time",
    "falcon_sandbox_submit_name",
    "falcon_sandbox_custom_date_time",
    "falcon_sandbox_tor_enabled_analysis",
]