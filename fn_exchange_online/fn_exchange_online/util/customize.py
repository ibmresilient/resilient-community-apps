# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_exchange_online"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_exchange_online package"""
    reload_params = {"package": u"fn_exchange_online",
                    "incident_fields": [], 
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


    yield ImportDefinition(u"""
eyJhY3Rpb25fb3JkZXIiOiBbXSwgImFjdGlvbnMiOiBbXSwgImF1dG9tYXRpY190YXNrcyI6IFtd
LCAiZXhwb3J0X2RhdGUiOiAxNTc0MTU4Mjk0ODgzLCAiZXhwb3J0X2Zvcm1hdF92ZXJzaW9uIjog
MiwgImZpZWxkcyI6IFt7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlv
biI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9z
ZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRl
ZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJpbmNpZGVudC9pbmNfdHJhaW5pbmciLCAiaGlkZV9u
b3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogNjEsICJpbnB1dF90eXBlIjogImJvb2xlYW4iLCAi
aW50ZXJuYWwiOiBmYWxzZSwgIm5hbWUiOiAiaW5jX3RyYWluaW5nIiwgIm9wZXJhdGlvbl9wZXJt
cyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicHJlZml4IjogbnVsbCwgInJlYWRfb25seSI6IHRy
dWUsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbXSwgInRlbXBsYXRlcyI6IFtdLCAidGV4
dCI6ICJTaW11bGF0aW9uIiwgInRvb2x0aXAiOiAiV2hldGhlciB0aGUgaW5jaWRlbnQgaXMgYSBz
aW11bGF0aW9uIG9yIGEgcmVndWxhciBpbmNpZGVudC4gVGhpcyBmaWVsZCBpcyByZWFkLW9ubHku
IiwgInR5cGVfaWQiOiAwLCAidXVpZCI6ICJjM2YwZTNlZC0yMWUxLTRkNTMtYWZmYi1mZTVjYTMz
MDhjY2EiLCAidmFsdWVzIjogW119XSwgImZ1bmN0aW9ucyI6IFtdLCAiZ2VvcyI6IG51bGwsICJn
cm91cHMiOiBudWxsLCAiaWQiOiAxLCAiaW5ib3VuZF9tYWlsYm94ZXMiOiBudWxsLCAiaW5jaWRl
bnRfYXJ0aWZhY3RfdHlwZXMiOiBbXSwgImluY2lkZW50X3R5cGVzIjogW3sidXBkYXRlX2RhdGUi
OiAxNTc0MTc2Mjk4MzM1LCAiY3JlYXRlX2RhdGUiOiAxNTc0MTc2Mjk4MzM1LCAidXVpZCI6ICJi
ZmVlYzJkNC0zNzcwLTExZTgtYWQzOS00YTAwMDQwNDRhYTAiLCAiZGVzY3JpcHRpb24iOiAiQ3Vz
dG9taXphdGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgImV4cG9ydF9rZXkiOiAiQ3VzdG9taXph
dGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgIm5hbWUiOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdl
cyAoaW50ZXJuYWwpIiwgImVuYWJsZWQiOiBmYWxzZSwgInN5c3RlbSI6IGZhbHNlLCAicGFyZW50
X2lkIjogbnVsbCwgImhpZGRlbiI6IGZhbHNlLCAiaWQiOiAwfV0sICJpbmR1c3RyaWVzIjogbnVs
bCwgImxheW91dHMiOiBbXSwgImxvY2FsZSI6IG51bGwsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6
IFtdLCAibm90aWZpY2F0aW9ucyI6IG51bGwsICJvdmVycmlkZXMiOiBbXSwgInBoYXNlcyI6IFtd
LCAicmVndWxhdG9ycyI6IG51bGwsICJyb2xlcyI6IFtdLCAic2NyaXB0cyI6IFtdLCAic2VydmVy
X3ZlcnNpb24iOiB7ImJ1aWxkX251bWJlciI6IDUxMTIsICJtYWpvciI6IDMzLCAibWlub3IiOiAw
LCAidmVyc2lvbiI6ICIzMy4wLjUxMTIifSwgInRhZ3MiOiBbXSwgInRhc2tfb3JkZXIiOiBbXSwg
InRpbWVmcmFtZXMiOiBudWxsLCAidHlwZXMiOiBbXSwgIndvcmtmbG93cyI6IFtdLCAid29ya3Nw
YWNlcyI6IFtdfQ==
"""
    )