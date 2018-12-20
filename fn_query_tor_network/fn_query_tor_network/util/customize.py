# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_query_tor_network"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_query_tor_network package"""
    reload_params = {"package": u"fn_query_tor_network",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "function_params": [u"tor_search_data"], 
                    "datatables": [], 
                    "message_destinations": [u"fn_tor"], 
                    "functions": [u"fn_tor"], 
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
    #     tor_search_data
    #   Message Destinations:
    #     fn_tor
    #   Functions:
    #     fn_tor


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbXSwgImFjdGlvbnMiOiBbXSwgImxheW91
dHMiOiBbXSwgImV4cG9ydF9mb3JtYXRfdmVyc2lvbiI6IDIsICJpZCI6IDI1LCAiaW5kdXN0cmll
cyI6IG51bGwsICJwaGFzZXMiOiBbXSwgImFjdGlvbl9vcmRlciI6IFtdLCAiZ2VvcyI6IG51bGws
ICJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMCwgInZlcnNpb24iOiAiMzAuNC4yMzciLCAi
YnVpbGRfbnVtYmVyIjogMjM3LCAibWlub3IiOiA0fSwgInRpbWVmcmFtZXMiOiBudWxsLCAid29y
a3NwYWNlcyI6IFtdLCAiYXV0b21hdGljX3Rhc2tzIjogW10sICJmdW5jdGlvbnMiOiBbeyJkaXNw
bGF5X25hbWUiOiAiVE9SIiwgImRlc2NyaXB0aW9uIjogeyJjb250ZW50IjogIlRoaXMgVE9SIGZ1
bmN0aW9uIHNlYXJjaGVzIGZvciB0aGUgZ2l2ZW4gSVAgQWRkcmVzcyBvciBob3N0IG5hbWVzIGlu
IFRPUiBleGl0IG5vZGUgTmV0d29yayBieSB1c2luZyBSRVNUZnVsIEFQSSIsICJmb3JtYXQiOiAi
dGV4dCJ9LCAiY3JlYXRvciI6IHsiZGlzcGxheV9uYW1lIjogIk5pdGluIEthbmRoYXJlICIsICJ0
eXBlIjogInVzZXIiLCAiaWQiOiA2LCAibmFtZSI6ICJua2FuZGhhMUBpbi5pYm0uY29tIn0sICJ2
aWV3X2l0ZW1zIjogW3sic2hvd19pZiI6IG51bGwsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24i
LCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImNv
bnRlbnQiOiAiOWEyYWNlMTEtM2FkMC00YmI2LTkxZTMtZmQxMTcwNjk4YmZlIiwgInN0ZXBfbGFi
ZWwiOiBudWxsfV0sICJleHBvcnRfa2V5IjogImZuX3RvciIsICJ1dWlkIjogIjBiNDcyOTQyLWY3
MTgtNGEwYy04NTVlLWYxODBlMGZjNTViNiIsICJsYXN0X21vZGlmaWVkX2J5IjogeyJkaXNwbGF5
X25hbWUiOiAiTml0aW4gS2FuZGhhcmUgIiwgInR5cGUiOiAidXNlciIsICJpZCI6IDYsICJuYW1l
IjogIm5rYW5kaGExQGluLmlibS5jb20ifSwgInZlcnNpb24iOiA0LCAid29ya2Zsb3dzIjogW3si
ZGVzY3JpcHRpb24iOiBudWxsLCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZhY3QiLCAiYWN0aW9ucyI6
IFtdLCAibmFtZSI6ICJFeGFtcGxlOiBRdWVyeSBUT1IgTmV0d29yayIsICJ3b3JrZmxvd19pZCI6
IDI5LCAicHJvZ3JhbW1hdGljX25hbWUiOiAiZXhhbXBsZV9xdWVyeV90b3JfbmV0d29yayIsICJ1
dWlkIjogbnVsbH1dLCAibGFzdF9tb2RpZmllZF90aW1lIjogMTU0NTMxNzYyMTA1NiwgImRlc3Rp
bmF0aW9uX2hhbmRsZSI6ICJmbl90b3IiLCAiaWQiOiAyNywgIm5hbWUiOiAiZm5fdG9yIn1dLCAi
bm90aWZpY2F0aW9ucyI6IG51bGwsICJyZWd1bGF0b3JzIjogbnVsbCwgImluY2lkZW50X3R5cGVz
IjogW3siY3JlYXRlX2RhdGUiOiAxNTQ1MzE5MzMyNzA0LCAiZGVzY3JpcHRpb24iOiAiQ3VzdG9t
aXphdGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgImV4cG9ydF9rZXkiOiAiQ3VzdG9taXphdGlv
biBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgImlkIjogMCwgIm5hbWUiOiAiQ3VzdG9taXphdGlvbiBQ
YWNrYWdlcyAoaW50ZXJuYWwpIiwgInVwZGF0ZV9kYXRlIjogMTU0NTMxOTMzMjcwNCwgInV1aWQi
OiAiYmZlZWMyZDQtMzc3MC0xMWU4LWFkMzktNGEwMDA0MDQ0YWEwIiwgImVuYWJsZWQiOiBmYWxz
ZSwgInN5c3RlbSI6IGZhbHNlLCAicGFyZW50X2lkIjogbnVsbCwgImhpZGRlbiI6IGZhbHNlfV0s
ICJzY3JpcHRzIjogW10sICJ0eXBlcyI6IFtdLCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbeyJ1
dWlkIjogIjI3MjE5YzM5LWQ5MzYtNDEzNy05NjJkLTY3ZGJhYTYzMDdmZCIsICJleHBvcnRfa2V5
IjogImZuX3RvciIsICJuYW1lIjogImZuX3RvciIsICJkZXN0aW5hdGlvbl90eXBlIjogMCwgInBy
b2dyYW1tYXRpY19uYW1lIjogImZuX3RvciIsICJleHBlY3RfYWNrIjogdHJ1ZSwgInVzZXJzIjog
WyJua2FuZGhhMUBpbi5pYm0uY29tIl19XSwgImluY2lkZW50X2FydGlmYWN0X3R5cGVzIjogW10s
ICJyb2xlcyI6IFtdLCAiZmllbGRzIjogW3sib3BlcmF0aW9ucyI6IFtdLCAicmVhZF9vbmx5Ijog
dHJ1ZSwgIm5hbWUiOiAiaW5jX3RyYWluaW5nIiwgInRlbXBsYXRlcyI6IFtdLCAidHlwZV9pZCI6
IDAsICJjaG9zZW4iOiBmYWxzZSwgInRleHQiOiAiU2ltdWxhdGlvbiIsICJkZWZhdWx0X2Nob3Nl
bl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiaW5jaWRlbnQvaW5jX3RyYWluaW5n
IiwgInRvb2x0aXAiOiAiV2hldGhlciB0aGUgaW5jaWRlbnQgaXMgYSBzaW11bGF0aW9uIG9yIGEg
cmVndWxhciBpbmNpZGVudC4gIFRoaXMgZmllbGQgaXMgcmVhZC1vbmx5LiIsICJyaWNoX3RleHQi
OiBmYWxzZSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAicHJlZml4IjogbnVsbCwgImludGVybmFs
IjogZmFsc2UsICJ2YWx1ZXMiOiBbXSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiaW5wdXRfdHlw
ZSI6ICJib29sZWFuIiwgImNoYW5nZWFibGUiOiB0cnVlLCAiaGlkZV9ub3RpZmljYXRpb24iOiBm
YWxzZSwgImlkIjogNTEsICJ1dWlkIjogImMzZjBlM2VkLTIxZTEtNGQ1My1hZmZiLWZlNWNhMzMw
OGNjYSJ9LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAxMSwgIm9wZXJhdGlvbl9wZXJt
cyI6IHt9LCAidGV4dCI6ICJ0b3Jfc2VhcmNoX2RhdGEiLCAiYmxhbmtfb3B0aW9uIjogZmFsc2Us
ICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDE0MCwgInJlYWRfb25s
eSI6IGZhbHNlLCAidXVpZCI6ICI5YTJhY2UxMS0zYWQwLTRiYjYtOTFlMy1mZDExNzA2OThiZmUi
LCAiY2hvc2VuIjogZmFsc2UsICJpbnB1dF90eXBlIjogInRleHQiLCAidG9vbHRpcCI6ICIiLCAi
aW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJl
eHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vdG9yX3NlYXJjaF9kYXRhIiwgImhpZGVfbm90aWZpY2F0
aW9uIjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJ0b3Jfc2VhcmNoX2RhdGEi
LCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJ2YWx1ZXMiOiBbXX1dLCAib3Zl
cnJpZGVzIjogW10sICJleHBvcnRfZGF0ZSI6IDE1NDUzMTg4NjEzNjZ9
"""
    )