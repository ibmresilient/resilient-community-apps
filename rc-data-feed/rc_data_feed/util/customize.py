# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for rc_data_feed"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the rc_data_feed package"""
    reload_params = {"package": u"rc_data_feed",
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
                    "actions": [u"Data Feeder: Artifact", u"Data Feeder: Attachment", u"Data Feeder: Incident", u"Data Feeder: Milestone", u"Data Feeder: Note", u"Data Feeder: Task"] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Message Destinations:
    #     feed_data
    #   Rules:
    #     Data Feeder: Artifact
    #     Data Feeder: Attachment
    #     Data Feeder: Incident
    #     Data Feeder: Milestone
    #     Data Feeder: Note
    #     Data Feeder: Task


    yield ImportDefinition(u"""
eyJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMSwgIm1pbm9yIjogMCwgImJ1aWxkX251bWJl
ciI6IDQyNTQsICJ2ZXJzaW9uIjogIjMxLjAuNDI1NCJ9LCAiZXhwb3J0X2Zvcm1hdF92ZXJzaW9u
IjogMiwgImlkIjogMjcsICJleHBvcnRfZGF0ZSI6IDE1NTM2Mjg4Njk2MzMsICJmaWVsZHMiOiBb
eyJpZCI6IDUxLCAibmFtZSI6ICJpbmNfdHJhaW5pbmciLCAidGV4dCI6ICJTaW11bGF0aW9uIiwg
InByZWZpeCI6IG51bGwsICJ0eXBlX2lkIjogMCwgInRvb2x0aXAiOiAiV2hldGhlciB0aGUgaW5j
aWRlbnQgaXMgYSBzaW11bGF0aW9uIG9yIGEgcmVndWxhciBpbmNpZGVudC4gIFRoaXMgZmllbGQg
aXMgcmVhZC1vbmx5LiIsICJpbnB1dF90eXBlIjogImJvb2xlYW4iLCAiaGlkZV9ub3RpZmljYXRp
b24iOiBmYWxzZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjog
ZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImludGVybmFsIjogZmFsc2UsICJ1dWlkIjog
ImMzZjBlM2VkLTIxZTEtNGQ1My1hZmZiLWZlNWNhMzMwOGNjYSIsICJvcGVyYXRpb25zIjogW10s
ICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInZhbHVlcyI6IFtdLCAicmVhZF9vbmx5IjogdHJ1ZSwg
ImNoYW5nZWFibGUiOiB0cnVlLCAicmljaF90ZXh0IjogZmFsc2UsICJleHBvcnRfa2V5IjogImlu
Y2lkZW50L2luY190cmFpbmluZyIsICJ0ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBmYWxz
ZX1dLCAiaW5jaWRlbnRfdHlwZXMiOiBbeyJ1cGRhdGVfZGF0ZSI6IDE1NTM4ODE0NjE2ODAsICJj
cmVhdGVfZGF0ZSI6IDE1NTM4ODE0NjE2ODAsICJ1dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFlOC1h
ZDM5LTRhMDAwNDA0NGFhMCIsICJkZXNjcmlwdGlvbiI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2Vz
IChpbnRlcm5hbCkiLCAiZXhwb3J0X2tleSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRl
cm5hbCkiLCAibmFtZSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZW5h
YmxlZCI6IGZhbHNlLCAic3lzdGVtIjogZmFsc2UsICJwYXJlbnRfaWQiOiBudWxsLCAiaGlkZGVu
IjogZmFsc2UsICJpZCI6IDB9XSwgInBoYXNlcyI6IFtdLCAiYXV0b21hdGljX3Rhc2tzIjogW10s
ICJvdmVycmlkZXMiOiBbXSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW3sibmFtZSI6ICJmZWVk
X2RhdGEiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiZmVlZF9kYXRhIiwgImRlc3RpbmF0aW9uX3R5
cGUiOiAwLCAiZXhwZWN0X2FjayI6IHRydWUsICJ1c2VycyI6IFsiYUBleGFtcGxlLmNvbSJdLCAi
dXVpZCI6ICJlMDUyODJmYi02Y2ZjLTQ3MDktYWY4NC1jZDcxNDM4NTgxYzgiLCAiZXhwb3J0X2tl
eSI6ICJmZWVkX2RhdGEifV0sICJhY3Rpb25zIjogW3siaWQiOiA0MywgIm5hbWUiOiAiRGF0YSBG
ZWVkZXI6IEFydGlmYWN0IiwgInR5cGUiOiAwLCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZhY3QiLCAi
Y29uZGl0aW9ucyI6IFtdLCAiYXV0b21hdGlvbnMiOiBbXSwgIm1lc3NhZ2VfZGVzdGluYXRpb25z
IjogWyJmZWVkX2RhdGEiXSwgIndvcmtmbG93cyI6IFtdLCAidmlld19pdGVtcyI6IFtdLCAidGlt
ZW91dF9zZWNvbmRzIjogODY0MDAsICJ1dWlkIjogIjNjNjI3YWE4LTU4MTAtNDRhNC1hMjVkLWU1
YThkYjE5YjZhNiIsICJleHBvcnRfa2V5IjogIkRhdGEgRmVlZGVyOiBBcnRpZmFjdCIsICJsb2dp
Y190eXBlIjogImFsbCJ9LCB7ImlkIjogNDQsICJuYW1lIjogIkRhdGEgRmVlZGVyOiBBdHRhY2ht
ZW50IiwgInR5cGUiOiAwLCAib2JqZWN0X3R5cGUiOiAiYXR0YWNobWVudCIsICJjb25kaXRpb25z
IjogW10sICJhdXRvbWF0aW9ucyI6IFtdLCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbImZlZWRf
ZGF0YSJdLCAid29ya2Zsb3dzIjogW10sICJ2aWV3X2l0ZW1zIjogW10sICJ0aW1lb3V0X3NlY29u
ZHMiOiA4NjQwMCwgInV1aWQiOiAiMmI2MjhiOGMtMWI1Mi00ZTUxLWE1ZjMtYzMyM2Q3ZmYwMzdl
IiwgImV4cG9ydF9rZXkiOiAiRGF0YSBGZWVkZXI6IEF0dGFjaG1lbnQiLCAibG9naWNfdHlwZSI6
ICJhbGwifSwgeyJpZCI6IDQ1LCAibmFtZSI6ICJEYXRhIEZlZWRlcjogSW5jaWRlbnQiLCAidHlw
ZSI6IDAsICJvYmplY3RfdHlwZSI6ICJpbmNpZGVudCIsICJjb25kaXRpb25zIjogW10sICJhdXRv
bWF0aW9ucyI6IFtdLCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbImZlZWRfZGF0YSJdLCAid29y
a2Zsb3dzIjogW10sICJ2aWV3X2l0ZW1zIjogW10sICJ0aW1lb3V0X3NlY29uZHMiOiA4NjQwMCwg
InV1aWQiOiAiNWJjMGI5OWItOGY4Ny00OGRlLTk3ZDktOTMzM2YxMTM5ZDVkIiwgImV4cG9ydF9r
ZXkiOiAiRGF0YSBGZWVkZXI6IEluY2lkZW50IiwgImxvZ2ljX3R5cGUiOiAiYWxsIn0sIHsiaWQi
OiA0NiwgIm5hbWUiOiAiRGF0YSBGZWVkZXI6IE1pbGVzdG9uZSIsICJ0eXBlIjogMCwgIm9iamVj
dF90eXBlIjogIm1pbGVzdG9uZSIsICJjb25kaXRpb25zIjogW10sICJhdXRvbWF0aW9ucyI6IFtd
LCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbImZlZWRfZGF0YSJdLCAid29ya2Zsb3dzIjogW10s
ICJ2aWV3X2l0ZW1zIjogW10sICJ0aW1lb3V0X3NlY29uZHMiOiA4NjQwMCwgInV1aWQiOiAiYzdm
Y2FmNTAtNDQwMi00YzYyLTk1NTItYzI2ZGY2ZTViZTliIiwgImV4cG9ydF9rZXkiOiAiRGF0YSBG
ZWVkZXI6IE1pbGVzdG9uZSIsICJsb2dpY190eXBlIjogImFsbCJ9LCB7ImlkIjogNDcsICJuYW1l
IjogIkRhdGEgRmVlZGVyOiBOb3RlIiwgInR5cGUiOiAwLCAib2JqZWN0X3R5cGUiOiAibm90ZSIs
ICJjb25kaXRpb25zIjogW10sICJhdXRvbWF0aW9ucyI6IFtdLCAibWVzc2FnZV9kZXN0aW5hdGlv
bnMiOiBbImZlZWRfZGF0YSJdLCAid29ya2Zsb3dzIjogW10sICJ2aWV3X2l0ZW1zIjogW10sICJ0
aW1lb3V0X3NlY29uZHMiOiA4NjQwMCwgInV1aWQiOiAiNzgwZjJlYmUtOWFhYy00MWU5LTk4YWIt
NzA2ODhhYzlhZjdhIiwgImV4cG9ydF9rZXkiOiAiRGF0YSBGZWVkZXI6IE5vdGUiLCAibG9naWNf
dHlwZSI6ICJhbGwifSwgeyJpZCI6IDQ4LCAibmFtZSI6ICJEYXRhIEZlZWRlcjogVGFzayIsICJ0
eXBlIjogMCwgIm9iamVjdF90eXBlIjogInRhc2siLCAiY29uZGl0aW9ucyI6IFtdLCAiYXV0b21h
dGlvbnMiOiBbXSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogWyJmZWVkX2RhdGEiXSwgIndvcmtm
bG93cyI6IFtdLCAidmlld19pdGVtcyI6IFtdLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ1
dWlkIjogImVlMGQ5MmVlLWU1M2QtNGViZC1hMjhmLWRmOTU5ZTk0OWVkNyIsICJleHBvcnRfa2V5
IjogIkRhdGEgRmVlZGVyOiBUYXNrIiwgImxvZ2ljX3R5cGUiOiAiYWxsIn1dLCAibGF5b3V0cyI6
IFtdLCAibm90aWZpY2F0aW9ucyI6IG51bGwsICJ0aW1lZnJhbWVzIjogbnVsbCwgImxvY2FsZSI6
IG51bGwsICJpbmR1c3RyaWVzIjogbnVsbCwgInJlZ3VsYXRvcnMiOiBudWxsLCAiZ2VvcyI6IG51
bGwsICJ0YXNrX29yZGVyIjogW10sICJhY3Rpb25fb3JkZXIiOiBbXSwgInR5cGVzIjogW10sICJz
Y3JpcHRzIjogW10sICJpbmNpZGVudF9hcnRpZmFjdF90eXBlcyI6IFtdLCAid29ya2Zsb3dzIjog
W10sICJyb2xlcyI6IFtdLCAid29ya3NwYWNlcyI6IFtdLCAiZnVuY3Rpb25zIjogW119
"""
    )