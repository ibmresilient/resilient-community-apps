# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_utilities"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return u"""
[fn_utilities]

# For safety, shell_command parameter values are escaped - set to 'sh' (bash) or 'ps' (powershell)
shell_escaping=sh

# NOTE: For safety, you *must* enclose shell-param substitutions in double-quotes.
# The values of these parameters usually includes artifacts or other untrusted data
# that may contain spaces, dashes and other content.  

# accepted remote powershell extensions in a comma separated list, example: ps1, psm1, etc
remote_powershell_extensions=ps1

# remote auth transport one of [ntlm, basic]
remote_auth_transport=ntlm

# remote computers
remote_computer=(username:password@server)

# remote shell commands
remote_command=[remote path to script]

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

# directory of xml stylesheets to use for xml transformations
# xml_stylesheet_dir=

# Max Timer sleep timeThe input string is of format “time value” concatenated with a
# “time unit” character, where character is: ‘s’ for seconds, ‘m’ for minutes, ‘h’ for hours
# ‘d’ for days.  For example: '30s' = 30 seconds; '40m' = 40 minutes;
max_timer=30d
"""
