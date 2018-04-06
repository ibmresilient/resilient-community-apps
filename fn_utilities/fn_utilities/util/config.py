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

# shell_command default commands (unix)
nslookup=nslookup "{{shell_param1}}"
dig=dig "{{shell_param1}}"
traceroute=traceroute -m20 "{{shell_param1}}"

# more shell_command examples:
# foo=bash $UTILBIN/foo "{{shell_param1}}"

# on windows, powershell example:
# psinfo=PsInfo.exe -accepteula -nobanner \\{{shell_param1}} | ConvertTo-Json

# more shell_command examples: Volatility.
#   First param is filename of the memory image, assuming $VOLATILITY_LOCATION is set
#   Second param is the profile ("Win7SP0x64" etc) 
# imageinfo=python $PYTHONBIN/vol.py -f "{{shell_param1}}" imageinfo --output=json
# kdbgscan=python $PYTHONBIN/vol.py -f "{{shell_param1}}" --profile={{shell_param2}} kdbgscan --output=json
# psscan=python $PYTHONBIN/vol.py -f "{{shell_param1}}" --profile={{shell_param2}} psscan --output=json
# dlllist=python $PYTHONBIN/vol.py -f "{{shell_param1}}" --profile={{shell_param2}} dlllist --output=json
# (etc)
        """