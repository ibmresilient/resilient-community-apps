# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_symantec_dlp"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_symantec_dlp package"""
    reload_params = {"package": u"fn_symantec_dlp",
                    "incident_fields": [u"sdlp_incident_id", u"sdlp_incident_url"], 
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
    #     sdlp_incident_url
    #   Message Destinations:
    #     fn_symantec_dlp
    #   Functions:
    #     fn_symantec_dlp_update_incident


    yield ImportDefinition(u"""
eyJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMSwgIm1pbm9yIjogMCwgImJ1aWxkX251bWJl
ciI6IDQyMzUsICJ2ZXJzaW9uIjogIjMxLjAuNDIzNSJ9LCAiZXhwb3J0X2Zvcm1hdF92ZXJzaW9u
IjogMiwgImlkIjogMTUsICJleHBvcnRfZGF0ZSI6IDE1NjcxNzY2Njk5NjgsICJmaWVsZHMiOiBb
eyJpZCI6IDQzOCwgIm5hbWUiOiAic2RscF9pbmNpZGVudF91cmwiLCAidGV4dCI6ICJTeW1hbnRl
YyBETFAgSW5jaWRlbnQgVVJMICIsICJwcmVmaXgiOiAicHJvcGVydGllcyIsICJ0eXBlX2lkIjog
MCwgInRvb2x0aXAiOiAiIiwgInBsYWNlaG9sZGVyIjogIiIsICJpbnB1dF90eXBlIjogInRleHRh
cmVhIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1
bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJpbnRl
cm5hbCI6IGZhbHNlLCAidXVpZCI6ICI0OTU5ODY5My0yYWMzLTQzYWYtYTI2Yi0wMTFjZGJlN2Jk
NGEiLCAib3BlcmF0aW9ucyI6IFtdLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ2YWx1ZXMiOiBb
XSwgInJlYWRfb25seSI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJyaWNoX3RleHQiOiB0
cnVlLCAiZXhwb3J0X2tleSI6ICJpbmNpZGVudC9zZGxwX2luY2lkZW50X3VybCIsICJ0ZW1wbGF0
ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBmYWxzZX0sIHsiaWQiOiA0MzcsICJuYW1lIjogInNkbHBf
aW5jaWRlbnRfaWQiLCAidGV4dCI6ICJTeW1hbnRlYyBETFAgSW5jaWRlbnQgSUQiLCAicHJlZml4
IjogInByb3BlcnRpZXMiLCAidHlwZV9pZCI6IDAsICJ0b29sdGlwIjogIlRoZSBJRCBvZiBhIFN5
bWFudGVjIERMUCBJbmNpZGVudCIsICJwbGFjZWhvbGRlciI6ICIiLCAiaW5wdXRfdHlwZSI6ICJu
dW1iZXIiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImNob3NlbiI6IGZhbHNlLCAiZGVm
YXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImlu
dGVybmFsIjogZmFsc2UsICJ1dWlkIjogIjU1ZjM1ZTIyLTE2MTAtNDJiMC1hY2NjLWY2NTk3NGU4
NmU0ZSIsICJvcGVyYXRpb25zIjogW10sICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInZhbHVlcyI6
IFtdLCAicmVhZF9vbmx5IjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgInJpY2hfdGV4dCI6
IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJpbmNpZGVudC9zZGxwX2luY2lkZW50X2lkIiwgInRlbXBs
YXRlcyI6IFtdLCAiZGVwcmVjYXRlZCI6IGZhbHNlfV0sICJpbmNpZGVudF90eXBlcyI6IFt7InVw
ZGF0ZV9kYXRlIjogMTU2NzE3NjY3MTY3NywgImNyZWF0ZV9kYXRlIjogMTU2NzE3NjY3MTY3Nywg
InV1aWQiOiAiYmZlZWMyZDQtMzc3MC0xMWU4LWFkMzktNGEwMDA0MDQ0YWEwIiwgImRlc2NyaXB0
aW9uIjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJleHBvcnRfa2V5Ijog
IkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJuYW1lIjogIkN1c3RvbWl6YXRp
b24gUGFja2FnZXMgKGludGVybmFsKSIsICJlbmFibGVkIjogZmFsc2UsICJzeXN0ZW0iOiBmYWxz
ZSwgInBhcmVudF9pZCI6IG51bGwsICJoaWRkZW4iOiBmYWxzZSwgImlkIjogMH1dLCAicGhhc2Vz
IjogW10sICJhdXRvbWF0aWNfdGFza3MiOiBbXSwgIm92ZXJyaWRlcyI6IFtdLCAibWVzc2FnZV9k
ZXN0aW5hdGlvbnMiOiBbeyJuYW1lIjogIlN5bWFudGVjIERMUCBNZXNzYWdlIERlc3RpbmF0aW9u
IiwgInByb2dyYW1tYXRpY19uYW1lIjogImZuX3N5bWFudGVjX2RscCIsICJkZXN0aW5hdGlvbl90
eXBlIjogMCwgImV4cGVjdF9hY2siOiB0cnVlLCAidXNlcnMiOiBbImludGVncmF0aW9uLXNlcnZl
ci5hbGZyZWRAd2F5bmVjb3JwLmNvbSJdLCAidXVpZCI6ICJkNzVjODU2MC02NGQyLTQ0Y2EtODdj
ZS00ZGI1MTBhM2M1ZDEiLCAiZXhwb3J0X2tleSI6ICJmbl9zeW1hbnRlY19kbHAifV0sICJhY3Rp
b25zIjogW10sICJsYXlvdXRzIjogW10sICJub3RpZmljYXRpb25zIjogbnVsbCwgInRpbWVmcmFt
ZXMiOiBudWxsLCAibG9jYWxlIjogbnVsbCwgImluZHVzdHJpZXMiOiBudWxsLCAicmVndWxhdG9y
cyI6IG51bGwsICJnZW9zIjogbnVsbCwgInRhc2tfb3JkZXIiOiBbXSwgImFjdGlvbl9vcmRlciI6
IFtdLCAidHlwZXMiOiBbXSwgInNjcmlwdHMiOiBbXSwgImluY2lkZW50X2FydGlmYWN0X3R5cGVz
IjogW10sICJ3b3JrZmxvd3MiOiBbXSwgInJvbGVzIjogW10sICJ3b3Jrc3BhY2VzIjogW10sICJm
dW5jdGlvbnMiOiBbeyJpZCI6IDQzLCAibmFtZSI6ICJmbl9zeW1hbnRlY19kbHBfdXBkYXRlX2lu
Y2lkZW50IiwgImRpc3BsYXlfbmFtZSI6ICJTeW1hbnRlYyBETFA6IFVwZGF0ZSBJbmNpZGVudCIs
ICJkZXNjcmlwdGlvbiI6IHsiZm9ybWF0IjogInRleHQiLCAiY29udGVudCI6ICIifSwgImRlc3Rp
bmF0aW9uX2hhbmRsZSI6ICJmbl9zeW1hbnRlY19kbHAiLCAiZXhwb3J0X2tleSI6ICJmbl9zeW1h
bnRlY19kbHBfdXBkYXRlX2luY2lkZW50IiwgInV1aWQiOiAiODk2MmY3MTUtNjExNC00ZThmLWEy
NDctMjljNDA2MjNiOThjIiwgInZlcnNpb24iOiAyLCAiY3JlYXRvciI6IHsiaWQiOiA0MCwgInR5
cGUiOiAidXNlciIsICJuYW1lIjogImludGVncmF0aW9uLXNlcnZlci5hbGZyZWRAd2F5bmVjb3Jw
LmNvbSIsICJkaXNwbGF5X25hbWUiOiAiSW50ZWdyYXRpb25zIFNlcnZlciBBIn0sICJsYXN0X21v
ZGlmaWVkX2J5IjogeyJpZCI6IDQwLCAidHlwZSI6ICJ1c2VyIiwgIm5hbWUiOiAiaW50ZWdyYXRp
b24tc2VydmVyLmFsZnJlZEB3YXluZWNvcnAuY29tIiwgImRpc3BsYXlfbmFtZSI6ICJJbnRlZ3Jh
dGlvbnMgU2VydmVyIEEifSwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE1NjYzMjA1MjgxNjksICJ2
aWV3X2l0ZW1zIjogW10sICJ3b3JrZmxvd3MiOiBbXX1dfQ==
"""
    )