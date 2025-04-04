# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_network_utilities"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_network_utilities when called by `resilient-circuits config [-c|-u]`
    """

    return """[fn_network_utilities]
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
# If using ssh_key_auth then remote_computer can be username@server
# If not using ssh_key_auth then remote_computer must be username:password@server
# For multiple remote_computers, specify another setting and reference in 'network_utilities_shell_command' function input
remote_computer=username:password@server
# Either a path to the ssh key auth file or an app secret variable that contains the private ssh key auth in PEM format.
# This setting can be any name as to support multiple ssh keys.
# The setting name is asked for in the function network_utilities_linux_shell_command.
#ssh_key_auth=$id_rsa
# If the private key is encrypted, provide the password for the private key. 
# Use the pattern '<id>_passphrase' when specifying multiple ssh keys.
#ssh_key_auth_passphrase=$passphrase
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
# New to 1.1.0
# make shell commands directly on remove computers without being specified in this configuration.
# Note: This capability is very powerful and a potential security risk to run any command
allow_ad_hoc_execution = False

# Timeout in seconds, default is 20
#timeout_linux=20
"""
