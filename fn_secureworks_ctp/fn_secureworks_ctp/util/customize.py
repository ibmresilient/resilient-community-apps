# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_secureworks_ctp"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_secureworks_ctp package"""
    reload_params = {"package": u"fn_secureworks_ctp",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "functions_params": [], 
                    "datatables": [], 
                    "message_destinations": [u"fn_secureworks_ctp"], 
                    "functions": [u"secureworks_ctp_close_ticket"], 
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
    #     fn_secureworks_ctp
    #   Functions:
    #     secureworks_ctp_close_ticket


    yield ImportDefinition(u"""
eyJncm91cHMiOiBudWxsLCAibG9jYWxlIjogbnVsbCwgIndvcmtmbG93cyI6IFtdLCAiYWN0aW9u
cyI6IFtdLCAibGF5b3V0cyI6IFtdLCAiZXhwb3J0X2Zvcm1hdF92ZXJzaW9uIjogMiwgImlkIjog
MiwgImluZHVzdHJpZXMiOiBudWxsLCAiZnVuY3Rpb25zIjogW3siZGlzcGxheV9uYW1lIjogIlNl
Y3VyZXdvcmtzIENUUDogQ2xvc2UgVGlja2V0IiwgImRlc2NyaXB0aW9uIjogeyJjb250ZW50Ijog
IkNsb3NlIGEgU2VjdXJld29ya3MgQ1RQIFRpY2tldCB3aGVuIHRoZSBhc3NvY2lhdGVkIFJlc2ls
aWVudCBJbmNpZGVudCBpcyBjbG9zZWQuIiwgImZvcm1hdCI6ICJ0ZXh0In0sICJjcmVhdG9yIjog
eyJ0eXBlIjogInVzZXIiLCAiZGlzcGxheV9uYW1lIjogIlJlc2lsaWVudCBTeXNhZG1pbiIsICJp
ZCI6IDMsICJuYW1lIjogImFAYS5jb20ifSwgInZpZXdfaXRlbXMiOiBbXSwgInRhZ3MiOiBbXSwg
ImV4cG9ydF9rZXkiOiAic2VjdXJld29ya3NfY3RwX2Nsb3NlX3RpY2tldCIsICJ1dWlkIjogIjkw
NWRiZGFiLTI1YTQtNDMyNC04ZWQyLWQ2M2IyMzViNjhhYiIsICJsYXN0X21vZGlmaWVkX2J5Ijog
eyJ0eXBlIjogInVzZXIiLCAiZGlzcGxheV9uYW1lIjogIlJlc2lsaWVudCBTeXNhZG1pbiIsICJp
ZCI6IDMsICJuYW1lIjogImFAYS5jb20ifSwgInZlcnNpb24iOiAxLCAid29ya2Zsb3dzIjogW10s
ICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTgyODMyNjc2Nzg1LCAiZGVzdGluYXRpb25faGFuZGxl
IjogImZuX3NlY3VyZXdvcmtzX2N0cCIsICJpZCI6IDE4LCAibmFtZSI6ICJzZWN1cmV3b3Jrc19j
dHBfY2xvc2VfdGlja2V0In1dLCAiYWN0aW9uX29yZGVyIjogW10sICJnZW9zIjogbnVsbCwgInRh
Z3MiOiBbXSwgInRhc2tfb3JkZXIiOiBbXSwgInR5cGVzIjogW10sICJ0aW1lZnJhbWVzIjogbnVs
bCwgIndvcmtzcGFjZXMiOiBbXSwgImluYm91bmRfbWFpbGJveGVzIjogbnVsbCwgImF1dG9tYXRp
Y190YXNrcyI6IFtdLCAicGhhc2VzIjogW10sICJub3RpZmljYXRpb25zIjogbnVsbCwgInJlZ3Vs
YXRvcnMiOiBudWxsLCAiaW5jaWRlbnRfdHlwZXMiOiBbeyJjcmVhdGVfZGF0ZSI6IDE1ODI4MzMw
ODAxMTMsICJkZXNjcmlwdGlvbiI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCki
LCAiZXhwb3J0X2tleSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiaWQi
OiAwLCAibmFtZSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAidXBkYXRl
X2RhdGUiOiAxNTgyODMzMDgwMTEzLCAidXVpZCI6ICJiZmVlYzJkNC0zNzcwLTExZTgtYWQzOS00
YTAwMDQwNDRhYTAiLCAiZW5hYmxlZCI6IGZhbHNlLCAic3lzdGVtIjogZmFsc2UsICJwYXJlbnRf
aWQiOiBudWxsLCAiaGlkZGVuIjogZmFsc2V9XSwgInNjcmlwdHMiOiBbXSwgInNlcnZlcl92ZXJz
aW9uIjogeyJtYWpvciI6IDM1LCAidmVyc2lvbiI6ICIzNS4yLjMyIiwgImJ1aWxkX251bWJlciI6
IDMyLCAibWlub3IiOiAyfSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW3sicHJvZ3JhbW1hdGlj
X25hbWUiOiAiZm5fc2VjdXJld29ya3NfY3RwIiwgInRhZ3MiOiBbXSwgImV4cG9ydF9rZXkiOiAi
Zm5fc2VjdXJld29ya3NfY3RwIiwgInV1aWQiOiAiNDQxOTFlNzctNGIzNi00NGU3LThjNjUtMWQ3
YWMxMDc1Mjc5IiwgImV4cGVjdF9hY2siOiB0cnVlLCAiZGVzdGluYXRpb25fdHlwZSI6IDAsICJ1
c2VycyI6IFtdLCAiYXBpX2tleXMiOiBbXSwgIm5hbWUiOiAiZm5fc2VjdXJld29ya3NfY3RwIn1d
LCAiaW5jaWRlbnRfYXJ0aWZhY3RfdHlwZXMiOiBbXSwgInJvbGVzIjogW10sICJmaWVsZHMiOiBb
eyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogMCwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAi
dGV4dCI6ICJTaW11bGF0aW9uIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4IjogbnVs
bCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiA2MiwgInJlYWRfb25seSI6IHRydWUsICJ1dWlk
IjogImMzZjBlM2VkLTIxZTEtNGQ1My1hZmZiLWZlNWNhMzMwOGNjYSIsICJjaG9zZW4iOiBmYWxz
ZSwgImlucHV0X3R5cGUiOiAiYm9vbGVhbiIsICJ0b29sdGlwIjogIldoZXRoZXIgdGhlIGluY2lk
ZW50IGlzIGEgc2ltdWxhdGlvbiBvciBhIHJlZ3VsYXIgaW5jaWRlbnQuIFRoaXMgZmllbGQgaXMg
cmVhZC1vbmx5LiIsICJpbnRlcm5hbCI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0ZW1w
bGF0ZXMiOiBbXSwgInRhZ3MiOiBbXSwgImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImV4
cG9ydF9rZXkiOiAiaW5jaWRlbnQvaW5jX3RyYWluaW5nIiwgImhpZGVfbm90aWZpY2F0aW9uIjog
ZmFsc2UsICJuYW1lIjogImluY190cmFpbmluZyIsICJpc190cmFja2VkIjogZmFsc2UsICJkZXBy
ZWNhdGVkIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJ2YWx1ZXMiOiBbXSwgImRlZmF1
bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlfV0sICJvdmVycmlkZXMiOiBbXSwgImV4cG9ydF9k
YXRlIjogMTU4MjgzMzA3NjAwNn0=
"""
    )