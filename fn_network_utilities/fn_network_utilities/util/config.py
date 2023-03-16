# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_network_utilities"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_network_utilities when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_network_utilities]
# For safety when using local shell commands and for selftest to determine which machine to test, shell_command parameter values are escaped - set to 'sh' (bash) or 'ps' (powershell)
shell_escaping=sh
# NOTE: For safety, you *must* enclose shell-param substitutions in double-quotes.
# The values of these parameters usually includes artifacts or other untrusted data
# that may contain spaces, dashes and other content.  
# accepted remote powershell extensions in a comma separated list, example: ps1, psm1, etc
remote_powershell_extensions=ps1
# remote auth transport one of [ntlm, basic]
remote_auth_transport=ntlm
# remote computers
remote_computer=username:password@server
# remote shell commands
remote_command_powershell= powershell command or path to powershell script
remote_command_linux= bash command or path to bash script
# local shell_command default commands (unix)
nslookup=nslookup "{{shell_param1}}"
dig=dig "{{shell_param1}}"
traceroute=traceroute -m 15 "{{shell_param1}}"
whois=whois "{{shell_param1}}"
# more shell_command examples:
# foo=bash $UTILBIN/foo "{{shell_param1}}"
# on windows, powershell example:
# psinfo=PsInfo.exe -accepteula -nobanner \\{{shell_param1}} | ConvertTo-Json
# more shell_command examples: Volatility.
#   First param is filename of the memory image, assuming $VOLATILITY_LOCATION is set
#   Second param is the profile ("Win7SP0x64" etc) 
# imageinfo=python /path/to/vol.py -f "{{shell_param1}}" imageinfo --output=json
# kdbgscan=python /path/to/vol.py -f "{{shell_param1}}" "--profile={{shell_param2}}" kdbgscan --output=json
# psscan=python /path/to/vol.py -f "{{shell_param1}}" "--profile={{shell_param2}}" psscan --output=json
# dlllist=python /path/to/vol.py -f "{{shell_param1}}" "--profile={{shell_param2}}" dlllist --output=json
# (etc)

# Timeout in seconds, default is 20
#timeout_linux=20
#timeout_windows=20
"""
    return config_data