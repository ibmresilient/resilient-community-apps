# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
"""Generate the Resilient customizations required for fn_symantec_dlp"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_symantec_dlp package"""
    reload_params = {"package": u"fn_symantec_dlp",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "functions_params": [], 
                    "datatables": [], 
                    "message_destinations": [u"fn_symantec_dlp"], 
                    "functions": [u"fn_symantec_dlp_update_incident"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [], 
                    "workflows": [],
                    "actions": [],
                    "incident_artifact_types": [] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Message Destinations:
    #     fn_symantec_dlp
    #   Functions:
    #     fn_symantec_dlp_update_incident


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbXSwgImFjdGlvbnMiOiBbXSwgImxheW91
dHMiOiBbXSwgImV4cG9ydF9mb3JtYXRfdmVyc2lvbiI6IDIsICJpZCI6IDksICJpbmR1c3RyaWVz
IjogbnVsbCwgInBoYXNlcyI6IFtdLCAiYWN0aW9uX29yZGVyIjogW10sICJnZW9zIjogbnVsbCwg
ImxvY2FsZSI6IG51bGwsICJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMSwgInZlcnNpb24i
OiAiMzEuMC40MjM1IiwgImJ1aWxkX251bWJlciI6IDQyMzUsICJtaW5vciI6IDB9LCAidGltZWZy
YW1lcyI6IG51bGwsICJ3b3Jrc3BhY2VzIjogW10sICJhdXRvbWF0aWNfdGFza3MiOiBbXSwgImZ1
bmN0aW9ucyI6IFt7ImRpc3BsYXlfbmFtZSI6ICJTeW1hbnRlYyBETFA6IFVwZGF0ZSBJbmNpZGVu
dCIsICJkZXNjcmlwdGlvbiI6IHsiY29udGVudCI6ICIiLCAiZm9ybWF0IjogInRleHQifSwgImNy
ZWF0b3IiOiB7ImRpc3BsYXlfbmFtZSI6ICJBZG1pbiBVc2VyIiwgInR5cGUiOiAidXNlciIsICJp
ZCI6IDQzLCAibmFtZSI6ICJhZG1pbkBleGFtcGxlLm9yZyJ9LCAidmlld19pdGVtcyI6IFtdLCAi
ZXhwb3J0X2tleSI6ICJmbl9zeW1hbnRlY19kbHBfdXBkYXRlX2luY2lkZW50IiwgInV1aWQiOiAi
ODk2MmY3MTUtNjExNC00ZThmLWEyNDctMjljNDA2MjNiOThjIiwgImxhc3RfbW9kaWZpZWRfYnki
OiB7ImRpc3BsYXlfbmFtZSI6ICJBZG1pbiBVc2VyIiwgInR5cGUiOiAidXNlciIsICJpZCI6IDQz
LCAibmFtZSI6ICJhZG1pbkBleGFtcGxlLm9yZyJ9LCAidmVyc2lvbiI6IDIsICJ3b3JrZmxvd3Mi
OiBbXSwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE1NjQzOTM0MzY5OTMsICJkZXN0aW5hdGlvbl9o
YW5kbGUiOiAiZm5fc3ltYW50ZWNfZGxwIiwgImlkIjogMzQsICJuYW1lIjogImZuX3N5bWFudGVj
X2RscF91cGRhdGVfaW5jaWRlbnQifV0sICJub3RpZmljYXRpb25zIjogbnVsbCwgInJlZ3VsYXRv
cnMiOiBudWxsLCAiaW5jaWRlbnRfdHlwZXMiOiBbeyJjcmVhdGVfZGF0ZSI6IDE1NjQzOTQyMTEw
MjAsICJkZXNjcmlwdGlvbiI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAi
ZXhwb3J0X2tleSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiaWQiOiAw
LCAibmFtZSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAidXBkYXRlX2Rh
dGUiOiAxNTY0Mzk0MjExMDIwLCAidXVpZCI6ICJiZmVlYzJkNC0zNzcwLTExZTgtYWQzOS00YTAw
MDQwNDRhYTAiLCAiZW5hYmxlZCI6IGZhbHNlLCAic3lzdGVtIjogZmFsc2UsICJwYXJlbnRfaWQi
OiBudWxsLCAiaGlkZGVuIjogZmFsc2V9XSwgInNjcmlwdHMiOiBbXSwgInR5cGVzIjogW10sICJt
ZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFt7InV1aWQiOiAiZDc1Yzg1NjAtNjRkMi00NGNhLTg3Y2Ut
NGRiNTEwYTNjNWQxIiwgImV4cG9ydF9rZXkiOiAiZm5fc3ltYW50ZWNfZGxwIiwgIm5hbWUiOiAi
U3ltYW50ZWMgRExQIE1lc3NhZ2UgRGVzdGluYXRpb24iLCAiZGVzdGluYXRpb25fdHlwZSI6IDAs
ICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJmbl9zeW1hbnRlY19kbHAiLCAiZXhwZWN0X2FjayI6IHRy
dWUsICJ1c2VycyI6IFsiYWRtaW5AZXhhbXBsZS5vcmciLCAiYWRtaW5AcmVzaWxpZW50LmNvbSJd
fV0sICJpbmNpZGVudF9hcnRpZmFjdF90eXBlcyI6IFtdLCAicm9sZXMiOiBbXSwgImZpZWxkcyI6
IFt7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAwLCAib3BlcmF0aW9uX3Blcm1zIjoge30s
ICJ0ZXh0IjogIlNpbXVsYXRpb24iLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiBu
dWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDM0NywgInJlYWRfb25seSI6IHRydWUsICJ1
dWlkIjogImMzZjBlM2VkLTIxZTEtNGQ1My1hZmZiLWZlNWNhMzMwOGNjYSIsICJjaG9zZW4iOiBm
YWxzZSwgImlucHV0X3R5cGUiOiAiYm9vbGVhbiIsICJ0b29sdGlwIjogIldoZXRoZXIgdGhlIGlu
Y2lkZW50IGlzIGEgc2ltdWxhdGlvbiBvciBhIHJlZ3VsYXIgaW5jaWRlbnQuICBUaGlzIGZpZWxk
IGlzIHJlYWQtb25seS4iLCAiaW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAi
dGVtcGxhdGVzIjogW10sICJleHBvcnRfa2V5IjogImluY2lkZW50L2luY190cmFpbmluZyIsICJo
aWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAibmFtZSI6ICJpbmNfdHJhaW5pbmciLCAiZGVwcmVj
YXRlZCI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJ2YWx1ZXMi
OiBbXX1dLCAib3ZlcnJpZGVzIjogW10sICJleHBvcnRfZGF0ZSI6IDE1NjQzOTQwMzQxMjJ9
"""
    )