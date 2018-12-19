# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_query_tar_network"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_query_tar_network package"""
    reload_params = {"package": u"fn_query_tar_network",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "function_params": [u"search_data"], 
                    "datatables": [], 
                    "message_destinations": [u"fn_querytar_network"], 
                    "functions": [u"query_tor_network"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [], 
                    "workflows": [],
                    "actions": [] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     search_data
    #   Message Destinations:
    #     fn_querytar_network
    #   Functions:
    #     query_tor_network


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbXSwgImFjdGlvbnMiOiBbXSwgImxheW91
dHMiOiBbXSwgImV4cG9ydF9mb3JtYXRfdmVyc2lvbiI6IDIsICJpZCI6IDIyLCAiaW5kdXN0cmll
cyI6IG51bGwsICJwaGFzZXMiOiBbXSwgImFjdGlvbl9vcmRlciI6IFtdLCAiZ2VvcyI6IG51bGws
ICJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMCwgInZlcnNpb24iOiAiMzAuNC4yMzciLCAi
YnVpbGRfbnVtYmVyIjogMjM3LCAibWlub3IiOiA0fSwgInRpbWVmcmFtZXMiOiBudWxsLCAid29y
a3NwYWNlcyI6IFtdLCAiYXV0b21hdGljX3Rhc2tzIjogW10sICJmdW5jdGlvbnMiOiBbeyJkaXNw
bGF5X25hbWUiOiAiUXVlcnkgVE9SIE5ldHdvcmsiLCAiZGVzY3JpcHRpb24iOiB7ImNvbnRlbnQi
OiAiVGhpcyBGdW5jdGlvbiB0byBTZWFyY2ggZm9yIEdpdmVuIFBhcmFtZXRlciBpbiBUT1IgUmVs
YXkgRXhpdCBOb2RlIiwgImZvcm1hdCI6ICJ0ZXh0In0sICJjcmVhdG9yIjogeyJkaXNwbGF5X25h
bWUiOiAiTml0aW4gS2FuZGhhcmUgIiwgInR5cGUiOiAidXNlciIsICJpZCI6IDYsICJuYW1lIjog
Im5rYW5kaGExQGluLmlibS5jb20ifSwgInZpZXdfaXRlbXMiOiBbeyJzaG93X2lmIjogbnVsbCwg
ImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJl
bGVtZW50IjogImZpZWxkX3V1aWQiLCAiY29udGVudCI6ICJmZjEyYzg1MC1mNDFkLTQwNGEtOTEz
OC01ZTk4Y2MzN2JiMGMiLCAic3RlcF9sYWJlbCI6IG51bGx9XSwgImV4cG9ydF9rZXkiOiAicXVl
cnlfdG9yX25ldHdvcmsiLCAidXVpZCI6ICI0YmE1YTVlNy1lMGExLTQ4ZWEtOWJhMC0xZGNiZWE2
MWJkZGMiLCAibGFzdF9tb2RpZmllZF9ieSI6IHsiZGlzcGxheV9uYW1lIjogIk5pdGluIEthbmRo
YXJlICIsICJ0eXBlIjogInVzZXIiLCAiaWQiOiA2LCAibmFtZSI6ICJua2FuZGhhMUBpbi5pYm0u
Y29tIn0sICJ2ZXJzaW9uIjogMywgIndvcmtmbG93cyI6IFt7ImRlc2NyaXB0aW9uIjogbnVsbCwg
Im9iamVjdF90eXBlIjogImFydGlmYWN0IiwgImFjdGlvbnMiOiBbXSwgIm5hbWUiOiAiRXhhbXBs
ZTogUXVlcnkgVE9SIE5ldHdvcmsiLCAid29ya2Zsb3dfaWQiOiAyOCwgInByb2dyYW1tYXRpY19u
YW1lIjogImV4YW1wbGVfcXVlcnlfdG9yX25ldHdvcmsiLCAidXVpZCI6IG51bGx9XSwgImxhc3Rf
bW9kaWZpZWRfdGltZSI6IDE1NDUxNTMwNDQyOTYsICJkZXN0aW5hdGlvbl9oYW5kbGUiOiAiZm5f
cXVlcnl0YXJfbmV0d29yayIsICJpZCI6IDI2LCAibmFtZSI6ICJxdWVyeV90b3JfbmV0d29yayJ9
XSwgIm5vdGlmaWNhdGlvbnMiOiBudWxsLCAicmVndWxhdG9ycyI6IG51bGwsICJpbmNpZGVudF90
eXBlcyI6IFt7ImNyZWF0ZV9kYXRlIjogMTU0NTIxOTc2ODE2NywgImRlc2NyaXB0aW9uIjogIkN1
c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJleHBvcnRfa2V5IjogIkN1c3RvbWl6
YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJpZCI6IDAsICJuYW1lIjogIkN1c3RvbWl6YXRp
b24gUGFja2FnZXMgKGludGVybmFsKSIsICJ1cGRhdGVfZGF0ZSI6IDE1NDUyMTk3NjgxNjcsICJ1
dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIsICJlbmFibGVkIjog
ZmFsc2UsICJzeXN0ZW0iOiBmYWxzZSwgInBhcmVudF9pZCI6IG51bGwsICJoaWRkZW4iOiBmYWxz
ZX1dLCAic2NyaXB0cyI6IFtdLCAidHlwZXMiOiBbXSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjog
W3sidXVpZCI6ICJhNjM0MTQ5OC1hYTg5LTQ2MWUtYTg4Ny0wYzliYmI3YTZiNjQiLCAiZXhwb3J0
X2tleSI6ICJmbl9xdWVyeXRhcl9uZXR3b3JrIiwgIm5hbWUiOiAiZm5fcXVlcnl0YXJfbmV0d29y
ayIsICJkZXN0aW5hdGlvbl90eXBlIjogMCwgInByb2dyYW1tYXRpY19uYW1lIjogImZuX3F1ZXJ5
dGFyX25ldHdvcmsiLCAiZXhwZWN0X2FjayI6IHRydWUsICJ1c2VycyI6IFsibmthbmRoYTFAaW4u
aWJtLmNvbSJdfV0sICJpbmNpZGVudF9hcnRpZmFjdF90eXBlcyI6IFtdLCAicm9sZXMiOiBbXSwg
ImZpZWxkcyI6IFt7Im9wZXJhdGlvbnMiOiBbXSwgInJlYWRfb25seSI6IHRydWUsICJuYW1lIjog
ImluY190cmFpbmluZyIsICJ0ZW1wbGF0ZXMiOiBbXSwgInR5cGVfaWQiOiAwLCAiY2hvc2VuIjog
ZmFsc2UsICJ0ZXh0IjogIlNpbXVsYXRpb24iLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjog
ZmFsc2UsICJleHBvcnRfa2V5IjogImluY2lkZW50L2luY190cmFpbmluZyIsICJ0b29sdGlwIjog
IldoZXRoZXIgdGhlIGluY2lkZW50IGlzIGEgc2ltdWxhdGlvbiBvciBhIHJlZ3VsYXIgaW5jaWRl
bnQuICBUaGlzIGZpZWxkIGlzIHJlYWQtb25seS4iLCAicmljaF90ZXh0IjogZmFsc2UsICJvcGVy
YXRpb25fcGVybXMiOiB7fSwgInByZWZpeCI6IG51bGwsICJpbnRlcm5hbCI6IGZhbHNlLCAidmFs
dWVzIjogW10sICJibGFua19vcHRpb24iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAiYm9vbGVhbiIs
ICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDUx
LCAidXVpZCI6ICJjM2YwZTNlZC0yMWUxLTRkNTMtYWZmYi1mZTVjYTMzMDhjY2EifSwgeyJvcGVy
YXRpb25zIjogW10sICJ0eXBlX2lkIjogMTEsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQi
OiAic2VhcmNoX2RhdGEiLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiBudWxsLCAi
Y2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDEzOSwgInJlYWRfb25seSI6IGZhbHNlLCAidXVpZCI6
ICJmZjEyYzg1MC1mNDFkLTQwNGEtOTEzOC01ZTk4Y2MzN2JiMGMiLCAiY2hvc2VuIjogZmFsc2Us
ICJpbnB1dF90eXBlIjogInRleHQiLCAidG9vbHRpcCI6ICIiLCAiaW50ZXJuYWwiOiBmYWxzZSwg
InJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJleHBvcnRfa2V5IjogIl9fZnVu
Y3Rpb24vc2VhcmNoX2RhdGEiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgInBsYWNlaG9s
ZGVyIjogIiIsICJuYW1lIjogInNlYXJjaF9kYXRhIiwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZl
ciI6IGZhbHNlLCAidmFsdWVzIjogW119XSwgIm92ZXJyaWRlcyI6IFtdLCAiZXhwb3J0X2RhdGUi
OiAxNTQ1MjEyMjU4NjI3fQ==
"""
    )