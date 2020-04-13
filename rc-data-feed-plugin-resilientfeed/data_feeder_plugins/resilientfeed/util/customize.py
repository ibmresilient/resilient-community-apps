# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for rc-data-feed-plugin-resilientfeed"""

from __future__ import print_function
from resilient import ImportDefinition

def codegen_reload_data():
    """Parameters to codegen used to generate the rc-data-feed-plugin-resilientfeed package"""
    reload_params = {"package": u"rc-data-feed-plugin-resilientfeed",
                     "incident_fields": [u"df_inc_id", u"df_org_id"],
                     "action_fields": [],
                     "functions_params": [],
                     "datatables": [],
                     "message_destinations": [],
                     "functions": [],
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
    #     df_inc_id
    #     df_org_id


    yield ImportDefinition(u"""
eyJhY3Rpb25fb3JkZXIiOiBbXSwgImFjdGlvbnMiOiBbXSwgImF1dG9tYXRpY190YXNrcyI6IFtd
LCAiZXhwb3J0X2RhdGUiOiAxNTg0MDMxODExOTA5LCAiZXhwb3J0X2Zvcm1hdF92ZXJzaW9uIjog
MiwgImZpZWxkcyI6IFt7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlv
biI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9z
ZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRl
ZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJpbmNpZGVudC9kZl9vcmdfaWQiLCAiaGlkZV9ub3Rp
ZmljYXRpb24iOiBmYWxzZSwgImlkIjogMTQ0OSwgImlucHV0X3R5cGUiOiAibnVtYmVyIiwgImlu
dGVybmFsIjogZmFsc2UsICJuYW1lIjogImRmX29yZ19pZCIsICJvcGVyYXRpb25fcGVybXMiOiB7
fSwgIm9wZXJhdGlvbnMiOiBbXSwgInBsYWNlaG9sZGVyIjogIiIsICJwcmVmaXgiOiAicHJvcGVy
dGllcyIsICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFtd
LCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogIkRhdGEgRmVlZGVyIFN5bmMgT3JnIElkIiwgInRv
b2x0aXAiOiAiRGF0YSBGZWVkZXIgU3luYyBPcmlnaW5hdGluZyBPcmcgSWQiLCAidHlwZV9pZCI6
IDAsICJ1dWlkIjogImFiNjJhZTdlLTdjZjItNDdiNC04OTQwLWYwZTFlMTNhNTgzNCIsICJ2YWx1
ZXMiOiBbXX0sIHsiYWxsb3dfZGVmYXVsdF92YWx1ZSI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjog
ZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImNob3NlbiI6
IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJkZXByZWNhdGVkIjog
ZmFsc2UsICJleHBvcnRfa2V5IjogImluY2lkZW50L2RmX2luY19pZCIsICJoaWRlX25vdGlmaWNh
dGlvbiI6IGZhbHNlLCAiaWQiOiAxNDUwLCAiaW5wdXRfdHlwZSI6ICJudW1iZXIiLCAiaW50ZXJu
YWwiOiBmYWxzZSwgIm5hbWUiOiAiZGZfaW5jX2lkIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAi
b3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6ICJwcm9wZXJ0aWVz
IiwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0YWdzIjogW10sICJ0
ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAiRGF0YSBGZWVkZXIgU3luYyBJbmNpZGVudCBJZCIsICJ0
b29sdGlwIjogIkRhdGEgRmVlZGVyIFN5bmMgT3JpZ2luYXRpbmcgSW5jaWRlbnQgSWQiLCAidHlw
ZV9pZCI6IDAsICJ1dWlkIjogImE1ZjdhNjM3LTBkMjMtNDYzYS1iOGMyLTlhMzdjYWI0Njc4NyIs
ICJ2YWx1ZXMiOiBbXX1dLCAiZnVuY3Rpb25zIjogW10sICJnZW9zIjogbnVsbCwgImdyb3VwcyI6
IG51bGwsICJpZCI6IDY1LCAiaW5ib3VuZF9tYWlsYm94ZXMiOiBudWxsLCAiaW5jaWRlbnRfYXJ0
aWZhY3RfdHlwZXMiOiBbXSwgImluY2lkZW50X3R5cGVzIjogW3sidXBkYXRlX2RhdGUiOiAxNTg0
MDMxODIwOTg2LCAiY3JlYXRlX2RhdGUiOiAxNTg0MDMxODIwOTg2LCAidXVpZCI6ICJiZmVlYzJk
NC0zNzcwLTExZTgtYWQzOS00YTAwMDQwNDRhYTAiLCAiZGVzY3JpcHRpb24iOiAiQ3VzdG9taXph
dGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgImV4cG9ydF9rZXkiOiAiQ3VzdG9taXphdGlvbiBQ
YWNrYWdlcyAoaW50ZXJuYWwpIiwgIm5hbWUiOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdlcyAoaW50
ZXJuYWwpIiwgImVuYWJsZWQiOiBmYWxzZSwgInN5c3RlbSI6IGZhbHNlLCAicGFyZW50X2lkIjog
bnVsbCwgImhpZGRlbiI6IGZhbHNlLCAiaWQiOiAwfV0sICJpbmR1c3RyaWVzIjogbnVsbCwgImxh
eW91dHMiOiBbXSwgImxvY2FsZSI6IG51bGwsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFtdLCAi
bm90aWZpY2F0aW9ucyI6IG51bGwsICJvdmVycmlkZXMiOiBbXSwgInBoYXNlcyI6IFtdLCAicmVn
dWxhdG9ycyI6IG51bGwsICJyb2xlcyI6IFtdLCAic2NyaXB0cyI6IFtdLCAic2VydmVyX3ZlcnNp
b24iOiB7ImJ1aWxkX251bWJlciI6IDUwODcsICJtYWpvciI6IDMzLCAibWlub3IiOiAwLCAidmVy
c2lvbiI6ICIzMy4wLjUwODcifSwgInRhZ3MiOiBbXSwgInRhc2tfb3JkZXIiOiBbXSwgInRpbWVm
cmFtZXMiOiBudWxsLCAidHlwZXMiOiBbXSwgIndvcmtmbG93cyI6IFtdLCAid29ya3NwYWNlcyI6
IFtdfQ==
"""
)