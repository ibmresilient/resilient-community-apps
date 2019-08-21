# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_symantec_dlp"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_symantec_dlp package"""
    reload_params = {"package": u"fn_symantec_dlp",
                    "incident_fields": [u"sdlp_incident_id"], 
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
    #   Incident fields:
    #     sdlp_incident_id
    #   Message Destinations:
    #     fn_symantec_dlp
    #   Functions:
    #     fn_symantec_dlp_update_incident


    yield ImportDefinition(u"""
eyJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMSwgIm1pbm9yIjogMCwgImJ1aWxkX251bWJl
ciI6IDQyMzUsICJ2ZXJzaW9uIjogIjMxLjAuNDIzNSJ9LCAiZXhwb3J0X2Zvcm1hdF92ZXJzaW9u
IjogMiwgImlkIjogMTQsICJleHBvcnRfZGF0ZSI6IDE1NjYzMjA0OTkxMTgsICJmaWVsZHMiOiBb
eyJpZCI6IDQzNywgIm5hbWUiOiAic2RscF9pbmNpZGVudF9pZCIsICJ0ZXh0IjogInNkbHBfaW5j
aWRlbnRfaWQiLCAicHJlZml4IjogInByb3BlcnRpZXMiLCAidHlwZV9pZCI6IDAsICJ0b29sdGlw
IjogIlRoZSBJRCBvZiBhIFN5bWFudGVjIERMUCBJbmNpZGVudCIsICJwbGFjZWhvbGRlciI6ICIi
LCAiaW5wdXRfdHlwZSI6ICJudW1iZXIiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImNo
b3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJibGFua19v
cHRpb24iOiBmYWxzZSwgImludGVybmFsIjogZmFsc2UsICJ1dWlkIjogIjU1ZjM1ZTIyLTE2MTAt
NDJiMC1hY2NjLWY2NTk3NGU4NmU0ZSIsICJvcGVyYXRpb25zIjogW10sICJvcGVyYXRpb25fcGVy
bXMiOiB7fSwgInZhbHVlcyI6IFtdLCAicmVhZF9vbmx5IjogZmFsc2UsICJjaGFuZ2VhYmxlIjog
dHJ1ZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJpbmNpZGVudC9zZGxwX2lu
Y2lkZW50X2lkIiwgInRlbXBsYXRlcyI6IFtdLCAiZGVwcmVjYXRlZCI6IGZhbHNlfV0sICJpbmNp
ZGVudF90eXBlcyI6IFt7InVwZGF0ZV9kYXRlIjogMTU2NjM4MjExOTQ1OSwgImNyZWF0ZV9kYXRl
IjogMTU2NjM4MjExOTQ1OSwgInV1aWQiOiAiYmZlZWMyZDQtMzc3MC0xMWU4LWFkMzktNGEwMDA0
MDQ0YWEwIiwgImRlc2NyaXB0aW9uIjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFs
KSIsICJleHBvcnRfa2V5IjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJu
YW1lIjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJlbmFibGVkIjogZmFs
c2UsICJzeXN0ZW0iOiBmYWxzZSwgInBhcmVudF9pZCI6IG51bGwsICJoaWRkZW4iOiBmYWxzZSwg
ImlkIjogMH1dLCAicGhhc2VzIjogW10sICJhdXRvbWF0aWNfdGFza3MiOiBbXSwgIm92ZXJyaWRl
cyI6IFtdLCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbeyJuYW1lIjogIlN5bWFudGVjIERMUCBN
ZXNzYWdlIERlc3RpbmF0aW9uIiwgInByb2dyYW1tYXRpY19uYW1lIjogImZuX3N5bWFudGVjX2Rs
cCIsICJkZXN0aW5hdGlvbl90eXBlIjogMCwgImV4cGVjdF9hY2siOiB0cnVlLCAidXNlcnMiOiBb
ImludGVncmF0aW9uLXNlcnZlci5hbGZyZWRAd2F5bmVjb3JwLmNvbSJdLCAidXVpZCI6ICJkNzVj
ODU2MC02NGQyLTQ0Y2EtODdjZS00ZGI1MTBhM2M1ZDEiLCAiZXhwb3J0X2tleSI6ICJmbl9zeW1h
bnRlY19kbHAifV0sICJhY3Rpb25zIjogW10sICJsYXlvdXRzIjogW10sICJub3RpZmljYXRpb25z
IjogbnVsbCwgInRpbWVmcmFtZXMiOiBudWxsLCAibG9jYWxlIjogbnVsbCwgImluZHVzdHJpZXMi
OiBudWxsLCAicmVndWxhdG9ycyI6IG51bGwsICJnZW9zIjogbnVsbCwgInRhc2tfb3JkZXIiOiBb
XSwgImFjdGlvbl9vcmRlciI6IFtdLCAidHlwZXMiOiBbXSwgInNjcmlwdHMiOiBbXSwgImluY2lk
ZW50X2FydGlmYWN0X3R5cGVzIjogW10sICJ3b3JrZmxvd3MiOiBbXSwgInJvbGVzIjogW10sICJ3
b3Jrc3BhY2VzIjogW10sICJmdW5jdGlvbnMiOiBbeyJpZCI6IDQzLCAibmFtZSI6ICJmbl9zeW1h
bnRlY19kbHBfdXBkYXRlX2luY2lkZW50IiwgImRpc3BsYXlfbmFtZSI6ICJTeW1hbnRlYyBETFA6
IFVwZGF0ZSBJbmNpZGVudCIsICJkZXNjcmlwdGlvbiI6IHsiZm9ybWF0IjogInRleHQiLCAiY29u
dGVudCI6ICIifSwgImRlc3RpbmF0aW9uX2hhbmRsZSI6ICJmbl9zeW1hbnRlY19kbHAiLCAiZXhw
b3J0X2tleSI6ICJmbl9zeW1hbnRlY19kbHBfdXBkYXRlX2luY2lkZW50IiwgInV1aWQiOiAiODk2
MmY3MTUtNjExNC00ZThmLWEyNDctMjljNDA2MjNiOThjIiwgInZlcnNpb24iOiAxLCAiY3JlYXRv
ciI6IHsiaWQiOiA0MCwgInR5cGUiOiAidXNlciIsICJuYW1lIjogImludGVncmF0aW9uLXNlcnZl
ci5hbGZyZWRAd2F5bmVjb3JwLmNvbSIsICJkaXNwbGF5X25hbWUiOiAiSW50ZWdyYXRpb25zIFNl
cnZlciBBIn0sICJsYXN0X21vZGlmaWVkX2J5IjogeyJpZCI6IDQwLCAidHlwZSI6ICJ1c2VyIiwg
Im5hbWUiOiAiaW50ZWdyYXRpb24tc2VydmVyLmFsZnJlZEB3YXluZWNvcnAuY29tIiwgImRpc3Bs
YXlfbmFtZSI6ICJJbnRlZ3JhdGlvbnMgU2VydmVyIEEifSwgImxhc3RfbW9kaWZpZWRfdGltZSI6
IDE1NjYzMjA0ODI5MjcsICJ2aWV3X2l0ZW1zIjogW10sICJ3b3JrZmxvd3MiOiBbXX1dfQ==
"""
    )