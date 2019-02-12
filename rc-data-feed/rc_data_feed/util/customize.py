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
                    "message_destinations": [u"feed data"], 
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
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbXSwgImFjdGlvbnMiOiBbeyJsb2dpY190
eXBlIjogImFsbCIsICJuYW1lIjogIkRhdGEgRmVlZGVyOiBBcnRpZmFjdCIsICJ2aWV3X2l0ZW1z
IjogW10sICJ0eXBlIjogMCwgIndvcmtmbG93cyI6IFtdLCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZh
Y3QiLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ1dWlkIjogIjNjNjI3YWE4LTU4MTAtNDRh
NC1hMjVkLWU1YThkYjE5YjZhNiIsICJhdXRvbWF0aW9ucyI6IFtdLCAiZXhwb3J0X2tleSI6ICJE
YXRhIEZlZWRlcjogQXJ0aWZhY3QiLCAiY29uZGl0aW9ucyI6IFtdLCAiaWQiOiA1MCwgIm1lc3Nh
Z2VfZGVzdGluYXRpb25zIjogWyJmZWVkIGRhdGEiXX0sIHsibG9naWNfdHlwZSI6ICJhbGwiLCAi
bmFtZSI6ICJEYXRhIEZlZWRlcjogQXR0YWNobWVudCIsICJ2aWV3X2l0ZW1zIjogW10sICJ0eXBl
IjogMCwgIndvcmtmbG93cyI6IFtdLCAib2JqZWN0X3R5cGUiOiAiYXR0YWNobWVudCIsICJ0aW1l
b3V0X3NlY29uZHMiOiA4NjQwMCwgInV1aWQiOiAiMmI2MjhiOGMtMWI1Mi00ZTUxLWE1ZjMtYzMy
M2Q3ZmYwMzdlIiwgImF1dG9tYXRpb25zIjogW10sICJleHBvcnRfa2V5IjogIkRhdGEgRmVlZGVy
OiBBdHRhY2htZW50IiwgImNvbmRpdGlvbnMiOiBbXSwgImlkIjogNTEsICJtZXNzYWdlX2Rlc3Rp
bmF0aW9ucyI6IFsiZmVlZCBkYXRhIl19LCB7ImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm5hbWUiOiAi
RGF0YSBGZWVkZXI6IEluY2lkZW50IiwgInZpZXdfaXRlbXMiOiBbXSwgInR5cGUiOiAwLCAid29y
a2Zsb3dzIjogW10sICJvYmplY3RfdHlwZSI6ICJpbmNpZGVudCIsICJ0aW1lb3V0X3NlY29uZHMi
OiA4NjQwMCwgInV1aWQiOiAiNWJjMGI5OWItOGY4Ny00OGRlLTk3ZDktOTMzM2YxMTM5ZDVkIiwg
ImF1dG9tYXRpb25zIjogW10sICJleHBvcnRfa2V5IjogIkRhdGEgRmVlZGVyOiBJbmNpZGVudCIs
ICJjb25kaXRpb25zIjogW10sICJpZCI6IDQ2LCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbImZl
ZWQgZGF0YSJdfSwgeyJsb2dpY190eXBlIjogImFsbCIsICJuYW1lIjogIkRhdGEgRmVlZGVyOiBN
aWxlc3RvbmUiLCAidmlld19pdGVtcyI6IFtdLCAidHlwZSI6IDAsICJ3b3JrZmxvd3MiOiBbXSwg
Im9iamVjdF90eXBlIjogIm1pbGVzdG9uZSIsICJ0aW1lb3V0X3NlY29uZHMiOiA4NjQwMCwgInV1
aWQiOiAiYzdmY2FmNTAtNDQwMi00YzYyLTk1NTItYzI2ZGY2ZTViZTliIiwgImF1dG9tYXRpb25z
IjogW10sICJleHBvcnRfa2V5IjogIkRhdGEgRmVlZGVyOiBNaWxlc3RvbmUiLCAiY29uZGl0aW9u
cyI6IFtdLCAiaWQiOiA0OSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogWyJmZWVkIGRhdGEiXX0s
IHsibG9naWNfdHlwZSI6ICJhbGwiLCAibmFtZSI6ICJEYXRhIEZlZWRlcjogTm90ZSIsICJ2aWV3
X2l0ZW1zIjogW10sICJ0eXBlIjogMCwgIndvcmtmbG93cyI6IFtdLCAib2JqZWN0X3R5cGUiOiAi
bm90ZSIsICJ0aW1lb3V0X3NlY29uZHMiOiA4NjQwMCwgInV1aWQiOiAiNzgwZjJlYmUtOWFhYy00
MWU5LTk4YWItNzA2ODhhYzlhZjdhIiwgImF1dG9tYXRpb25zIjogW10sICJleHBvcnRfa2V5Ijog
IkRhdGEgRmVlZGVyOiBOb3RlIiwgImNvbmRpdGlvbnMiOiBbXSwgImlkIjogNDgsICJtZXNzYWdl
X2Rlc3RpbmF0aW9ucyI6IFsiZmVlZCBkYXRhIl19LCB7ImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm5h
bWUiOiAiRGF0YSBGZWVkZXI6IFRhc2siLCAidmlld19pdGVtcyI6IFtdLCAidHlwZSI6IDAsICJ3
b3JrZmxvd3MiOiBbXSwgIm9iamVjdF90eXBlIjogInRhc2siLCAidGltZW91dF9zZWNvbmRzIjog
ODY0MDAsICJ1dWlkIjogImVlMGQ5MmVlLWU1M2QtNGViZC1hMjhmLWRmOTU5ZTk0OWVkNyIsICJh
dXRvbWF0aW9ucyI6IFtdLCAiZXhwb3J0X2tleSI6ICJEYXRhIEZlZWRlcjogVGFzayIsICJjb25k
aXRpb25zIjogW10sICJpZCI6IDQ3LCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbImZlZWQgZGF0
YSJdfV0sICJsYXlvdXRzIjogW10sICJleHBvcnRfZm9ybWF0X3ZlcnNpb24iOiAyLCAiaWQiOiAx
LCAiaW5kdXN0cmllcyI6IG51bGwsICJwaGFzZXMiOiBbXSwgImFjdGlvbl9vcmRlciI6IFtdLCAi
Z2VvcyI6IG51bGwsICJsb2NhbGUiOiBudWxsLCAic2VydmVyX3ZlcnNpb24iOiB7Im1ham9yIjog
MzIsICJ2ZXJzaW9uIjogIjMyLjAuNDUwMiIsICJidWlsZF9udW1iZXIiOiA0NTAyLCAibWlub3Ii
OiAwfSwgInRpbWVmcmFtZXMiOiBudWxsLCAid29ya3NwYWNlcyI6IFtdLCAiYXV0b21hdGljX3Rh
c2tzIjogW10sICJmdW5jdGlvbnMiOiBbXSwgIm5vdGlmaWNhdGlvbnMiOiBudWxsLCAicmVndWxh
dG9ycyI6IG51bGwsICJpbmNpZGVudF90eXBlcyI6IFt7ImNyZWF0ZV9kYXRlIjogMTU1MDAwOTM3
MTI1OSwgImRlc2NyaXB0aW9uIjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIs
ICJleHBvcnRfa2V5IjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJpZCI6
IDAsICJuYW1lIjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJ1cGRhdGVf
ZGF0ZSI6IDE1NTAwMDkzNzEyNTksICJ1dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRh
MDAwNDA0NGFhMCIsICJlbmFibGVkIjogZmFsc2UsICJzeXN0ZW0iOiBmYWxzZSwgInBhcmVudF9p
ZCI6IG51bGwsICJoaWRkZW4iOiBmYWxzZX1dLCAic2NyaXB0cyI6IFtdLCAidHlwZXMiOiBbXSwg
Im1lc3NhZ2VfZGVzdGluYXRpb25zIjogW10sICJpbmNpZGVudF9hcnRpZmFjdF90eXBlcyI6IFtd
LCAicm9sZXMiOiBbXSwgImZpZWxkcyI6IFt7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAw
LCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ0ZXh0IjogIlNpbXVsYXRpb24iLCAiYmxhbmtfb3B0
aW9uIjogZmFsc2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDUx
LCAicmVhZF9vbmx5IjogdHJ1ZSwgInV1aWQiOiAiYzNmMGUzZWQtMjFlMS00ZDUzLWFmZmItZmU1
Y2EzMzA4Y2NhIiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJib29sZWFuIiwgInRv
b2x0aXAiOiAiV2hldGhlciB0aGUgaW5jaWRlbnQgaXMgYSBzaW11bGF0aW9uIG9yIGEgcmVndWxh
ciBpbmNpZGVudC4gIFRoaXMgZmllbGQgaXMgcmVhZC1vbmx5LiIsICJpbnRlcm5hbCI6IGZhbHNl
LCAicmljaF90ZXh0IjogZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgImV4cG9ydF9rZXkiOiAiaW5j
aWRlbnQvaW5jX3RyYWluaW5nIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJuYW1lIjog
ImluY190cmFpbmluZyIsICJkZXByZWNhdGVkIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9z
ZXJ2ZXIiOiBmYWxzZSwgInZhbHVlcyI6IFtdfV0sICJvdmVycmlkZXMiOiBbXSwgImV4cG9ydF9k
YXRlIjogMTU1MDAwOTI5MTk2MX0=
"""
    )