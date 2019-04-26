# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_pa_panorama"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_pa_panorama package"""
    reload_params = {"package": u"fn_pa_panorama",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "functions_params": [], 
                    "datatables": [], 
                    "message_destinations": [u"palo_alto_panorama"], 
                    "functions": [u"panorama_edit_address_group", u"panorama_get_address_groups"], 
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
    #   Message Destinations:
    #     palo_alto_panorama
    #   Functions:
    #     panorama_edit_address_group
    #     panorama_get_address_groups


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbXSwgImFjdGlvbnMiOiBbXSwgImxheW91
dHMiOiBbXSwgImV4cG9ydF9mb3JtYXRfdmVyc2lvbiI6IDIsICJpZCI6IDYzLCAiaW5kdXN0cmll
cyI6IG51bGwsICJwaGFzZXMiOiBbXSwgImFjdGlvbl9vcmRlciI6IFtdLCAiZ2VvcyI6IG51bGws
ICJsb2NhbGUiOiBudWxsLCAic2VydmVyX3ZlcnNpb24iOiB7Im1ham9yIjogMzEsICJ2ZXJzaW9u
IjogIjMxLjAuNDI1NCIsICJidWlsZF9udW1iZXIiOiA0MjU0LCAibWlub3IiOiAwfSwgInRpbWVm
cmFtZXMiOiBudWxsLCAid29ya3NwYWNlcyI6IFtdLCAiYXV0b21hdGljX3Rhc2tzIjogW10sICJm
dW5jdGlvbnMiOiBbeyJkaXNwbGF5X25hbWUiOiAiUGFub3JhbWEgRWRpdCBBZGRyZXNzIEdyb3Vw
IiwgImRlc2NyaXB0aW9uIjogeyJjb250ZW50IjogIiIsICJmb3JtYXQiOiAidGV4dCJ9LCAiY3Jl
YXRvciI6IHsiZGlzcGxheV9uYW1lIjogIlJlc2lsaWVudCBTeXNhZG1pbiIsICJ0eXBlIjogInVz
ZXIiLCAiaWQiOiAxLCAibmFtZSI6ICJhZG1pbkBjbzNzeXMuY29tIn0sICJ2aWV3X2l0ZW1zIjog
W10sICJleHBvcnRfa2V5IjogInBhbm9yYW1hX2VkaXRfYWRkcmVzc19ncm91cCIsICJ1dWlkIjog
ImM4MzM2YmQxLTFhNjMtNDY2Mi05YjA0LWViNzRlOWRlNzUxMCIsICJsYXN0X21vZGlmaWVkX2J5
IjogeyJkaXNwbGF5X25hbWUiOiAiUmVzaWxpZW50IFN5c2FkbWluIiwgInR5cGUiOiAidXNlciIs
ICJpZCI6IDEsICJuYW1lIjogImFkbWluQGNvM3N5cy5jb20ifSwgInZlcnNpb24iOiAxLCAid29y
a2Zsb3dzIjogW10sICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTU2MzAzNTY2NjIzLCAiZGVzdGlu
YXRpb25faGFuZGxlIjogInBhbG9fYWx0b19wYW5vcmFtYSIsICJpZCI6IDEwMiwgIm5hbWUiOiAi
cGFub3JhbWFfZWRpdF9hZGRyZXNzX2dyb3VwIn0sIHsiZGlzcGxheV9uYW1lIjogIlBhbm9yYW1h
IEdldCBBZGRyZXNzIEdyb3VwcyIsICJkZXNjcmlwdGlvbiI6IHsiY29udGVudCI6ICIiLCAiZm9y
bWF0IjogInRleHQifSwgImNyZWF0b3IiOiB7ImRpc3BsYXlfbmFtZSI6ICJSZXNpbGllbnQgU3lz
YWRtaW4iLCAidHlwZSI6ICJ1c2VyIiwgImlkIjogMSwgIm5hbWUiOiAiYWRtaW5AY28zc3lzLmNv
bSJ9LCAidmlld19pdGVtcyI6IFtdLCAiZXhwb3J0X2tleSI6ICJwYW5vcmFtYV9nZXRfYWRkcmVz
c19ncm91cHMiLCAidXVpZCI6ICI0YjIzMzE1My00MjZlLTQ1NmQtODNjZC1jMTMzYzZlMDU0Mjki
LCAibGFzdF9tb2RpZmllZF9ieSI6IHsiZGlzcGxheV9uYW1lIjogIlJlc2lsaWVudCBTeXNhZG1p
biIsICJ0eXBlIjogInVzZXIiLCAiaWQiOiAxLCAibmFtZSI6ICJhZG1pbkBjbzNzeXMuY29tIn0s
ICJ2ZXJzaW9uIjogMSwgIndvcmtmbG93cyI6IFtdLCAibGFzdF9tb2RpZmllZF90aW1lIjogMTU1
NjMwMjk5OTU3MSwgImRlc3RpbmF0aW9uX2hhbmRsZSI6ICJwYWxvX2FsdG9fcGFub3JhbWEiLCAi
aWQiOiAxMDEsICJuYW1lIjogInBhbm9yYW1hX2dldF9hZGRyZXNzX2dyb3VwcyJ9XSwgIm5vdGlm
aWNhdGlvbnMiOiBudWxsLCAicmVndWxhdG9ycyI6IG51bGwsICJpbmNpZGVudF90eXBlcyI6IFt7
ImNyZWF0ZV9kYXRlIjogMTU1NjMwNTUzNjQ3OCwgImRlc2NyaXB0aW9uIjogIkN1c3RvbWl6YXRp
b24gUGFja2FnZXMgKGludGVybmFsKSIsICJleHBvcnRfa2V5IjogIkN1c3RvbWl6YXRpb24gUGFj
a2FnZXMgKGludGVybmFsKSIsICJpZCI6IDAsICJuYW1lIjogIkN1c3RvbWl6YXRpb24gUGFja2Fn
ZXMgKGludGVybmFsKSIsICJ1cGRhdGVfZGF0ZSI6IDE1NTYzMDU1MzY0NzgsICJ1dWlkIjogImJm
ZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIsICJlbmFibGVkIjogZmFsc2UsICJz
eXN0ZW0iOiBmYWxzZSwgInBhcmVudF9pZCI6IG51bGwsICJoaWRkZW4iOiBmYWxzZX1dLCAic2Ny
aXB0cyI6IFtdLCAidHlwZXMiOiBbXSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW3sidXVpZCI6
ICIxNzY1ZGY1Yy0zN2E3LTRjZDktOTRlYy1iYWE2OGQ2NzMzMjkiLCAiZXhwb3J0X2tleSI6ICJw
YWxvX2FsdG9fcGFub3JhbWEiLCAibmFtZSI6ICJQYWxvIEFsdG8gUGFub3JhbWEiLCAiZGVzdGlu
YXRpb25fdHlwZSI6IDAsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJwYWxvX2FsdG9fcGFub3JhbWEi
LCAiZXhwZWN0X2FjayI6IHRydWUsICJ1c2VycyI6IFsiYWRtaW5AY28zc3lzLmNvbSJdfV0sICJp
bmNpZGVudF9hcnRpZmFjdF90eXBlcyI6IFtdLCAicm9sZXMiOiBbXSwgImZpZWxkcyI6IFt7Im9w
ZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAwLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ0ZXh0
IjogIlNpbXVsYXRpb24iLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiBudWxsLCAi
Y2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDM4LCAicmVhZF9vbmx5IjogdHJ1ZSwgInV1aWQiOiAi
YzNmMGUzZWQtMjFlMS00ZDUzLWFmZmItZmU1Y2EzMzA4Y2NhIiwgImNob3NlbiI6IGZhbHNlLCAi
aW5wdXRfdHlwZSI6ICJib29sZWFuIiwgInRvb2x0aXAiOiAiV2hldGhlciB0aGUgaW5jaWRlbnQg
aXMgYSBzaW11bGF0aW9uIG9yIGEgcmVndWxhciBpbmNpZGVudC4gIFRoaXMgZmllbGQgaXMgcmVh
ZC1vbmx5LiIsICJpbnRlcm5hbCI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0ZW1wbGF0
ZXMiOiBbXSwgImV4cG9ydF9rZXkiOiAiaW5jaWRlbnQvaW5jX3RyYWluaW5nIiwgImhpZGVfbm90
aWZpY2F0aW9uIjogZmFsc2UsICJuYW1lIjogImluY190cmFpbmluZyIsICJkZXByZWNhdGVkIjog
ZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZhbHVlcyI6IFtdfV0s
ICJvdmVycmlkZXMiOiBbXSwgImV4cG9ydF9kYXRlIjogMTU1NjMwNDgxNzI1MX0=
"""
    )