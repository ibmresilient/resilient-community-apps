# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for rc_data_feed"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the rc_data_feed package"""
    reload_params = {"package": u"rc-data-feed",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "functions_params": [], 
                    "datatables": [], 
                    "message_destinations": [u"feed_data"],
                    "functions": [], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [], 
                    "workflows": [],
                    "actions": [u"Data Feeder: Artifact", u"Data Feeder: Attachment", u"Data Feeder: Incident", u"Data Feeder: Milestone", u"Data Feeder: Note", u"Data Feeder: Task"], 
                    "incident_artifact_types": [] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Message Destinations:
    #     feed data
    #   Rules:
    #     Data Feeder: Artifact
    #     Data Feeder: Attachment
    #     Data Feeder: Incident
    #     Data Feeder: Milestone
    #     Data Feeder: Note
    #     Data Feeder: Task


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbXSwgImFjdGlvbnMiOiBbeyJsb2dp
Y190eXBlIjogImFsbCIsICJuYW1lIjogIkRhdGEgRmVlZGVyOiBBcnRpZmFjdCIsICJ2aWV3
X2l0ZW1zIjogW10sICJ0eXBlIjogMCwgIndvcmtmbG93cyI6IFtdLCAib2JqZWN0X3R5cGUi
OiAiYXJ0aWZhY3QiLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ1dWlkIjogIjNjNjI3
YWE4LTU4MTAtNDRhNC1hMjVkLWU1YThkYjE5YjZhNiIsICJhdXRvbWF0aW9ucyI6IFtdLCAi
ZXhwb3J0X2tleSI6ICJEYXRhIEZlZWRlcjogQXJ0aWZhY3QiLCAiY29uZGl0aW9ucyI6IFtd
LCAiaWQiOiA1MCwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogWyJmZWVkX2RhdGEiXX0sIHsi
bG9naWNfdHlwZSI6ICJhbGwiLCAibmFtZSI6ICJEYXRhIEZlZWRlcjogQXR0YWNobWVudCIs
ICJ2aWV3X2l0ZW1zIjogW10sICJ0eXBlIjogMCwgIndvcmtmbG93cyI6IFtdLCAib2JqZWN0
X3R5cGUiOiAiYXR0YWNobWVudCIsICJ0aW1lb3V0X3NlY29uZHMiOiA4NjQwMCwgInV1aWQi
OiAiMmI2MjhiOGMtMWI1Mi00ZTUxLWE1ZjMtYzMyM2Q3ZmYwMzdlIiwgImF1dG9tYXRpb25z
IjogW10sICJleHBvcnRfa2V5IjogIkRhdGEgRmVlZGVyOiBBdHRhY2htZW50IiwgImNvbmRp
dGlvbnMiOiBbXSwgImlkIjogNTEsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFsiZmVlZF9k
YXRhIl19LCB7ImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm5hbWUiOiAiRGF0YSBGZWVkZXI6IElu
Y2lkZW50IiwgInZpZXdfaXRlbXMiOiBbXSwgInR5cGUiOiAwLCAid29ya2Zsb3dzIjogW10s
ICJvYmplY3RfdHlwZSI6ICJpbmNpZGVudCIsICJ0aW1lb3V0X3NlY29uZHMiOiA4NjQwMCwg
InV1aWQiOiAiNWJjMGI5OWItOGY4Ny00OGRlLTk3ZDktOTMzM2YxMTM5ZDVkIiwgImF1dG9t
YXRpb25zIjogW10sICJleHBvcnRfa2V5IjogIkRhdGEgRmVlZGVyOiBJbmNpZGVudCIsICJj
b25kaXRpb25zIjogW10sICJpZCI6IDQ2LCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbImZl
ZWRfZGF0YSJdfSwgeyJsb2dpY190eXBlIjogImFsbCIsICJuYW1lIjogIkRhdGEgRmVlZGVy
OiBNaWxlc3RvbmUiLCAidmlld19pdGVtcyI6IFtdLCAidHlwZSI6IDAsICJ3b3JrZmxvd3Mi
OiBbXSwgIm9iamVjdF90eXBlIjogIm1pbGVzdG9uZSIsICJ0aW1lb3V0X3NlY29uZHMiOiA4
NjQwMCwgInV1aWQiOiAiYzdmY2FmNTAtNDQwMi00YzYyLTk1NTItYzI2ZGY2ZTViZTliIiwg
ImF1dG9tYXRpb25zIjogW10sICJleHBvcnRfa2V5IjogIkRhdGEgRmVlZGVyOiBNaWxlc3Rv
bmUiLCAiY29uZGl0aW9ucyI6IFtdLCAiaWQiOiA0OSwgIm1lc3NhZ2VfZGVzdGluYXRpb25z
IjogWyJmZWVkX2RhdGEiXX0sIHsibG9naWNfdHlwZSI6ICJhbGwiLCAibmFtZSI6ICJEYXRh
IEZlZWRlcjogTm90ZSIsICJ2aWV3X2l0ZW1zIjogW10sICJ0eXBlIjogMCwgIndvcmtmbG93
cyI6IFtdLCAib2JqZWN0X3R5cGUiOiAibm90ZSIsICJ0aW1lb3V0X3NlY29uZHMiOiA4NjQw
MCwgInV1aWQiOiAiNzgwZjJlYmUtOWFhYy00MWU5LTk4YWItNzA2ODhhYzlhZjdhIiwgImF1
dG9tYXRpb25zIjogW10sICJleHBvcnRfa2V5IjogIkRhdGEgRmVlZGVyOiBOb3RlIiwgImNv
bmRpdGlvbnMiOiBbXSwgImlkIjogNDgsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFsiZmVl
ZF9kYXRhIl19LCB7ImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm5hbWUiOiAiRGF0YSBGZWVkZXI6
IFRhc2siLCAidmlld19pdGVtcyI6IFtdLCAidHlwZSI6IDAsICJ3b3JrZmxvd3MiOiBbXSwg
Im9iamVjdF90eXBlIjogInRhc2siLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ1dWlk
IjogImVlMGQ5MmVlLWU1M2QtNGViZC1hMjhmLWRmOTU5ZTk0OWVkNyIsICJhdXRvbWF0aW9u
cyI6IFtdLCAiZXhwb3J0X2tleSI6ICJEYXRhIEZlZWRlcjogVGFzayIsICJjb25kaXRpb25z
IjogW10sICJpZCI6IDQ3LCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbImZlZWRfZGF0YSJd
fV0sICJsYXlvdXRzIjogW10sICJleHBvcnRfZm9ybWF0X3ZlcnNpb24iOiAyLCAiaWQiOiAx
LCAiaW5kdXN0cmllcyI6IG51bGwsICJwaGFzZXMiOiBbXSwgImFjdGlvbl9vcmRlciI6IFtd
LCAiZ2VvcyI6IG51bGwsICJsb2NhbGUiOiBudWxsLCAic2VydmVyX3ZlcnNpb24iOiB7Im1h
am9yIjogMzAsICJ2ZXJzaW9uIjogIjMwLjAuNDI1NCIsICJidWlsZF9udW1iZXIiOiA0MjU0
LCAibWlub3IiOiAwfSwgInRpbWVmcmFtZXMiOiBudWxsLCAid29ya3NwYWNlcyI6IFtdLCAi
YXV0b21hdGljX3Rhc2tzIjogW10sICJmdW5jdGlvbnMiOiBbXSwgIm5vdGlmaWNhdGlvbnMi
OiBudWxsLCAicmVndWxhdG9ycyI6IG51bGwsICJpbmNpZGVudF90eXBlcyI6IFt7ImNyZWF0
ZV9kYXRlIjogMTU1MDAwOTM3MTI1OSwgImRlc2NyaXB0aW9uIjogIkN1c3RvbWl6YXRpb24g
UGFja2FnZXMgKGludGVybmFsKSIsICJleHBvcnRfa2V5IjogIkN1c3RvbWl6YXRpb24gUGFj
a2FnZXMgKGludGVybmFsKSIsICJpZCI6IDAsICJuYW1lIjogIkN1c3RvbWl6YXRpb24gUGFj
a2FnZXMgKGludGVybmFsKSIsICJ1cGRhdGVfZGF0ZSI6IDE1NTAwMDkzNzEyNTksICJ1dWlk
IjogImJmZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIsICJlbmFibGVkIjog
ZmFsc2UsICJzeXN0ZW0iOiBmYWxzZSwgInBhcmVudF9pZCI6IG51bGwsICJoaWRkZW4iOiBm
YWxzZX1dLCAic2NyaXB0cyI6IFtdLCAidHlwZXMiOiBbXSwgIm1lc3NhZ2VfZGVzdGluYXRp
b25zIjogW10sICJpbmNpZGVudF9hcnRpZmFjdF90eXBlcyI6IFtdLCAicm9sZXMiOiBbXSwg
ImZpZWxkcyI6IFt7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAwLCAib3BlcmF0aW9u
X3Blcm1zIjoge30sICJ0ZXh0IjogIlNpbXVsYXRpb24iLCAiYmxhbmtfb3B0aW9uIjogZmFs
c2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDUxLCAicmVh
ZF9vbmx5IjogdHJ1ZSwgInV1aWQiOiAiYzNmMGUzZWQtMjFlMS00ZDUzLWFmZmItZmU1Y2Ez
MzA4Y2NhIiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJib29sZWFuIiwgInRv
b2x0aXAiOiAiV2hldGhlciB0aGUgaW5jaWRlbnQgaXMgYSBzaW11bGF0aW9uIG9yIGEgcmVn
dWxhciBpbmNpZGVudC4gIFRoaXMgZmllbGQgaXMgcmVhZC1vbmx5LiIsICJpbnRlcm5hbCI6
IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgImV4cG9ydF9r
ZXkiOiAiaW5jaWRlbnQvaW5jX3RyYWluaW5nIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFs
c2UsICJuYW1lIjogImluY190cmFpbmluZyIsICJkZXByZWNhdGVkIjogZmFsc2UsICJkZWZh
dWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZhbHVlcyI6IFtdfV0sICJvdmVycmlk
ZXMiOiBbXSwgImV4cG9ydF9kYXRlIjogMTU1MDAwOTI5MTk2MX0K
"""
    )