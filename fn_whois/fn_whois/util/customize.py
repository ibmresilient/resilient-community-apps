# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.

"""Generate the Resilient customizations required for fn_whois"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_whois package"""
    reload_params = {"package": u"fn_whois",
        "incident_fields": [],
        "action_fields": [],
        "function_params": [u"whois_query"],
        "datatables": [],
        "message_destinations": [u"fn_whois"],
        "functions": [u"whois_query"],
        "phases": [],
            "automatic_tasks": [],
            "scripts": [],
            "workflows": [u"example_whois_query_against_artifact"],
            "actions": [u"Run Whois Query Against Artifact"]
            }
    return reload_params



def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     whois_query
    #   Message Destinations:
    #     fn_whois
    #   Functions:
    #     whois_query
    #   Workflows:
    #     example_whois_query_against_artifact
    #   Rules:
    #     Run Whois Query Against Artifact


    yield ImportDefinition(u"""
        eyJpZCI6IDExLCAiZmllbGRzIjogW3siY2hvc2VuIjogZmFsc2UsICJpbnRlcm5hbCI6IGZhbHNl
        LCAidXVpZCI6ICJjM2YwZTNlZC0yMWUxLTRkNTMtYWZmYi1mZTVjYTMzMDhjY2EiLCAib3BlcmF0
        aW9ucyI6IFtdLCAidmFsdWVzIjogW10sICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMzgsICJu
        YW1lIjogImluY190cmFpbmluZyIsICJ0ZXh0IjogIlNpbXVsYXRpb24iLCAicHJlZml4IjogbnVs
        bCwgInR5cGVfaWQiOiAwLCAidG9vbHRpcCI6ICJXaGV0aGVyIHRoZSBpbmNpZGVudCBpcyBhIHNp
        bXVsYXRpb24gb3IgYSByZWd1bGFyIGluY2lkZW50LiAgVGhpcyBmaWVsZCBpcyByZWFkLW9ubHku
        IiwgImlucHV0X3R5cGUiOiAiYm9vbGVhbiIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAi
        ZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwg
        Im9wZXJhdGlvbl9wZXJtcyI6IHt9LCAicmVhZF9vbmx5IjogdHJ1ZSwgInJpY2hfdGV4dCI6IGZh
        bHNlLCAiZXhwb3J0X2tleSI6ICJpbmNpZGVudC9pbmNfdHJhaW5pbmciLCAidGVtcGxhdGVzIjog
        W119LCB7ImNob3NlbiI6IGZhbHNlLCAiaW50ZXJuYWwiOiBmYWxzZSwgInV1aWQiOiAiODU4NGFk
        ZjQtYWJhNy00MTQ5LTg0YzQtYWY5ZTE1ZjdiZDBmIiwgIm9wZXJhdGlvbnMiOiBbXSwgInZhbHVl
        cyI6IFtdLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDExNSwgIm5hbWUiOiAid2hvaXNfcXVl
        cnkiLCAidGV4dCI6ICJ3aG9pc19xdWVyeSIsICJwcmVmaXgiOiBudWxsLCAidHlwZV9pZCI6IDEx
        LCAidG9vbHRpcCI6ICJBIFVSTCBvciBJUCB2YWx1ZSB3aGljaCB3aWxsIGJlIHF1ZXJpZWQgYWdh
        aW5zdCBhIFdIT0lTIHNlcnZlci4iLCAicGxhY2Vob2xkZXIiOiAiZ29vZ2xlLmNvbSIsICJpbnB1
        dF90eXBlIjogInRleHQiLCAicmVxdWlyZWQiOiAiYWx3YXlzIiwgImhpZGVfbm90aWZpY2F0aW9u
        IjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImJsYW5rX29wdGlv
        biI6IGZhbHNlLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJyZWFkX29ubHkiOiBmYWxzZSwgInJp
        Y2hfdGV4dCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL3dob2lzX3F1ZXJ5Iiwg
        InRlbXBsYXRlcyI6IFtdfV0sICJwaGFzZXMiOiBbXSwgIm92ZXJyaWRlcyI6IFtdLCAiYWN0aW9u
        cyI6IFt7ImlkIjogMzgsICJuYW1lIjogIlJ1biBXaG9pcyBRdWVyeSBBZ2FpbnN0IEFydGlmYWN0
        IiwgInR5cGUiOiAxLCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZhY3QiLCAiY29uZGl0aW9ucyI6IFt7
        Im1ldGhvZCI6ICJpbiIsICJmaWVsZF9uYW1lIjogImFydGlmYWN0LnR5cGUiLCAidmFsdWUiOiBb
        IlVSTCJdLCAidHlwZSI6IG51bGwsICJldmFsdWF0aW9uX2lkIjogbnVsbH1dLCAiYXV0b21hdGlv
        bnMiOiBbXSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW10sICJ3b3JrZmxvd3MiOiBbImV4YW1w
        bGVfd2hvaXNfcXVlcnlfYWdhaW5zdF9hcnRpZmFjdCJdLCAidmlld19pdGVtcyI6IFtdLCAidGlt
        ZW91dF9zZWNvbmRzIjogODY0MDAsICJ1dWlkIjogIjBkYTA1MjExLWM4YzMtNGM1OC1hYmJkLTk5
        MjdjNDVhOWYwNiIsICJleHBvcnRfa2V5IjogIlJ1biBXaG9pcyBRdWVyeSBBZ2FpbnN0IEFydGlm
        YWN0IiwgImxvZ2ljX3R5cGUiOiAiYWxsIn1dLCAibGF5b3V0cyI6IFtdLCAibm90aWZpY2F0aW9u
        cyI6IG51bGwsICJ0aW1lZnJhbWVzIjogbnVsbCwgImluZHVzdHJpZXMiOiBudWxsLCAicmVndWxh
        dG9ycyI6IG51bGwsICJnZW9zIjogbnVsbCwgImZ1bmN0aW9ucyI6IFt7ImlkIjogMjMsICJuYW1l
        IjogIndob2lzX3F1ZXJ5IiwgImRlc2NyaXB0aW9uIjogeyJmb3JtYXQiOiAidGV4dCIsICJjb250
        ZW50IjogIlVzZWQgdG8gc2VuZCBhIHF1ZXJ5IGRpcmVjdGx5IHRvIGEgV0hPSVMgc2VydmVyIHRv
        IGdhdGhlciBpbmZvcm1hdGlvbiBhYm91dCBhbiBJUCBPciBVUkwgdGFrZW4gYXMgYW4gaW5wdXQu
        In0sICJ1dWlkIjogIjZlMmUyY2ZiLWU1MGEtNGQ0OC04NWE5LWViODBkOTY1ZjU1ZCIsICJ2ZXJz
        aW9uIjogMCwgImNyZWF0b3IiOiB7ImlkIjogMiwgInR5cGUiOiAidXNlciIsICJuYW1lIjogImFA
        YS5jb20iLCAiZGlzcGxheV9uYW1lIjogIlJlc2lsaWVudCBTeXNhZG1pbiJ9LCAid29ya2Zsb3dz
        IjogW3siZGVzY3JpcHRpb24iOiBudWxsLCAidXVpZCI6IG51bGwsICJ3b3JrZmxvd19pZCI6IDIw
        LCAibmFtZSI6ICJFeGFtcGxlOiBXaG9pcyBRdWVyeSBBZ2FpbnN0IEFydGlmYWN0IiwgInByb2dy
        YW1tYXRpY19uYW1lIjogImV4YW1wbGVfd2hvaXNfcXVlcnlfYWdhaW5zdF9hcnRpZmFjdCIsICJv
        YmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJhY3Rpb25zIjogW119XSwgImRpc3BsYXlfbmFtZSI6
        ICJXaG9pczogUXVlcnkiLCAiZGVzdGluYXRpb25faGFuZGxlIjogImZuX3dob2lzIiwgImV4cG9y
        dF9rZXkiOiAid2hvaXNfcXVlcnkiLCAibGFzdF9tb2RpZmllZF9ieSI6IHsiaWQiOiAyLCAidHlw
        ZSI6ICJ1c2VyIiwgIm5hbWUiOiAiYUBhLmNvbSIsICJkaXNwbGF5X25hbWUiOiAiUmVzaWxpZW50
        IFN5c2FkbWluIn0sICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTQxMDAzMjk2MjY1LCAidmlld19p
        dGVtcyI6IFt7InN0ZXBfbGFiZWwiOiBudWxsLCAic2hvd19pZiI6IG51bGwsICJlbGVtZW50Ijog
        ImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgImNvbnRlbnQiOiAiODU4
        NGFkZjQtYWJhNy00MTQ5LTg0YzQtYWY5ZTE1ZjdiZDBmIiwgInNob3dfbGlua19oZWFkZXIiOiBm
        YWxzZX1dfV0sICJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMCwgIm1pbm9yIjogMCwgImJ1
        aWxkX251bWJlciI6IDM0NzYsICJ2ZXJzaW9uIjogIjMwLjAuMzQ3NiJ9LCAiZXhwb3J0X2Zvcm1h
        dF92ZXJzaW9uIjogMiwgImV4cG9ydF9kYXRlIjogMTU0MTYxMjcxMTQ5NSwgImluY2lkZW50X3R5
        cGVzIjogW3sidXBkYXRlX2RhdGUiOiAxNTQxNjEyODgwODMyLCAiY3JlYXRlX2RhdGUiOiAxNTQx
        NjEyODgwODMyLCAidXVpZCI6ICJiZmVlYzJkNC0zNzcwLTExZTgtYWQzOS00YTAwMDQwNDRhYTAi
        LCAiZGVzY3JpcHRpb24iOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgImV4
        cG9ydF9rZXkiOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgIm5hbWUiOiAi
        Q3VzdG9taXphdGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgImVuYWJsZWQiOiBmYWxzZSwgInN5
        c3RlbSI6IGZhbHNlLCAicGFyZW50X2lkIjogbnVsbCwgImhpZGRlbiI6IGZhbHNlLCAiaWQiOiAw
        fV0sICJhdXRvbWF0aWNfdGFza3MiOiBbXSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW3sibmFt
        ZSI6ICJXaG9pcyBNZXNzYWdlIERlc3RpbmF0aW9uIiwgInByb2dyYW1tYXRpY19uYW1lIjogImZu
        X3dob2lzIiwgImRlc3RpbmF0aW9uX3R5cGUiOiAwLCAiZXhwZWN0X2FjayI6IHRydWUsICJ1c2Vy
        cyI6IFsiYUBhLmNvbSJdLCAidXVpZCI6ICI0ZWY1MDcwMi02ZTA1LTQ2NzMtOWFmZi02NTMxMzMx
        MTc2ZDIiLCAiZXhwb3J0X2tleSI6ICJmbl93aG9pcyJ9XSwgInRhc2tfb3JkZXIiOiBbXSwgImFj
        dGlvbl9vcmRlciI6IFtdLCAidHlwZXMiOiBbXSwgInNjcmlwdHMiOiBbXSwgImluY2lkZW50X2Fy
        dGlmYWN0X3R5cGVzIjogW10sICJ3b3JrZmxvd3MiOiBbeyJkZXNjcmlwdGlvbiI6ICJBbiBleGFt
        cGxlIHdvcmtmbG93IHdoaWNoIGlzIHJhbiBvbiBhbiBhcnRpZmFjdC4gVGFrZXMgaW4gdGhlIGFy
        dGlmYWN0cyB2YWx1ZSBpcyBhbiBpbnB1dCBhbmQgc3VibWl0cyBhIFdIT0lTIHF1ZXJ5IGFnYWlu
        c3QgdGhpcyBpbnB1dC4gUmVzdWx0cyBhcmUgcmV0dXJuZWQgaW4gdGhlIGZvcm0gb2YgYSBub3Rl
        LiIsICJ1dWlkIjogIjA0NDg0ZjZkLTNhMDMtNDk5Mi1hNzgxLTdlYjlkYTAzODM0MyIsICJ3b3Jr
        Zmxvd19pZCI6IDIwLCAibmFtZSI6ICJFeGFtcGxlOiBXaG9pcyBRdWVyeSBBZ2FpbnN0IEFydGlm
        YWN0IiwgInByb2dyYW1tYXRpY19uYW1lIjogImV4YW1wbGVfd2hvaXNfcXVlcnlfYWdhaW5zdF9h
        cnRpZmFjdCIsICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJjcmVhdG9yX2lkIjogImFAYS5j
        b20iLCAibGFzdF9tb2RpZmllZF9ieSI6ICJhQGEuY29tIiwgImxhc3RfbW9kaWZpZWRfdGltZSI6
        IDE1NDEwMTU1OTE5NDAsICJleHBvcnRfa2V5IjogImV4YW1wbGVfd2hvaXNfcXVlcnlfYWdhaW5z
        dF9hcnRpZmFjdCIsICJjb250ZW50IjogeyJ4bWwiOiAiPD94bWwgdmVyc2lvbj1cIjEuMFwiIGVu
        Y29kaW5nPVwiVVRGLThcIj8+PGRlZmluaXRpb25zIHhtbG5zPVwiaHR0cDovL3d3dy5vbWcub3Jn
        L3NwZWMvQlBNTi8yMDEwMDUyNC9NT0RFTFwiIHhtbG5zOmJwbW5kaT1cImh0dHA6Ly93d3cub21n
        Lm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvRElcIiB4bWxuczpvbWdkYz1cImh0dHA6Ly93d3cub21n
        Lm9yZy9zcGVjL0RELzIwMTAwNTI0L0RDXCIgeG1sbnM6b21nZGk9XCJodHRwOi8vd3d3Lm9tZy5v
        cmcvc3BlYy9ERC8yMDEwMDUyNC9ESVwiIHhtbG5zOnJlc2lsaWVudD1cImh0dHA6Ly9yZXNpbGll
        bnQuaWJtLmNvbS9icG1uXCIgeG1sbnM6eHNkPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxT
        Y2hlbWFcIiB4bWxuczp4c2k9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0
        YW5jZVwiIHRhcmdldE5hbWVzcGFjZT1cImh0dHA6Ly93d3cuY2FtdW5kYS5vcmcvdGVzdFwiPjxw
        cm9jZXNzIGlkPVwiZXhhbXBsZV93aG9pc19xdWVyeV9hZ2FpbnN0X2FydGlmYWN0XCIgaXNFeGVj
        dXRhYmxlPVwidHJ1ZVwiIG5hbWU9XCJFeGFtcGxlOiBXaG9pcyBRdWVyeSBBZ2FpbnN0IEFydGlm
        YWN0XCI+PGRvY3VtZW50YXRpb24+QW4gZXhhbXBsZSB3b3JrZmxvdyB3aGljaCBpcyByYW4gb24g
        YW4gYXJ0aWZhY3QuIFRha2VzIGluIHRoZSBhcnRpZmFjdHMgdmFsdWUgaXMgYW4gaW5wdXQgYW5k
        IHN1Ym1pdHMgYSBXSE9JUyBxdWVyeSBhZ2FpbnN0IHRoaXMgaW5wdXQuIFJlc3VsdHMgYXJlIHJl
        dHVybmVkIGluIHRoZSBmb3JtIG9mIGEgbm90ZS48L2RvY3VtZW50YXRpb24+PHN0YXJ0RXZlbnQg
        aWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIj48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzF5bzlqMG88
        L291dGdvaW5nPjwvc3RhcnRFdmVudD48c2VydmljZVRhc2sgaWQ9XCJTZXJ2aWNlVGFza18wOGVy
        YTVkXCIgbmFtZT1cIldob2lzOiBRdWVyeVwiIHJlc2lsaWVudDp0eXBlPVwiZnVuY3Rpb25cIj48
        ZXh0ZW5zaW9uRWxlbWVudHM+PHJlc2lsaWVudDpmdW5jdGlvbiB1dWlkPVwiNmUyZTJjZmItZTUw
        YS00ZDQ4LTg1YTktZWI4MGQ5NjVmNTVkXCI+e1wiaW5wdXRzXCI6e30sXCJwcmVfcHJvY2Vzc2lu
        Z19zY3JpcHRcIjpcImlucHV0cy53aG9pc19xdWVyeSA9IGFydGlmYWN0LnZhbHVlXCIsXCJyZXN1
        bHRfbmFtZVwiOlwiXCIsXCJwb3N0X3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCJcXG5cXG5pZiByZXN1
        bHRzW1xcXCJzdWNjZXNzXFxcIl06XFxuICAjIFdlIGhhdmUgcmVzdWx0c1xcbiAgbm90ZVRleHQg
        PSB1XFxcIlxcXCJcXFwiV2hvaXMgUXVlcnkgcmFuIGFnYWluc3QgaW5wdXQgJmx0O2ImZ3Q7ezB9
        Jmx0Oy9iJmd0OyZsdDticiZndDsgUmVzdWx0cyBmb3VuZDogJmx0O2JyJmd0O1xcXCJcXFwiXFxc
        Ii5mb3JtYXQocmVzdWx0cy5pbnB1dHNbXFxcIndob2lzX3F1ZXJ5XFxcIl0pXFxuICBcXFwiXFxc
        IlxcXCJcXG4gIGZvciBrZXksIHZhbCBpbiByZXN1bHRzLmRvbWFpbl9kZXRhaWxzLml0ZW1zKCk6
        XFxuICAgIG5vdGVUZXh0ICs9IHUnJycmbHQ7YiZndDsgezB9IDogezF9JycnLmZvcm1hdChrZXks
        dmFsKVxcbiAgXFxcIlxcXCJcXFwiXFxuICBmb3Iga2V5dmFsIGluIHppcChyZXN1bHRzLmRvbWFp
        bl9kZXRhaWxzX2tleXMscmVzdWx0cy5kb21haW5fZGV0YWlsc192YWx1ZXMpOlxcbiAgICBub3Rl
        VGV4dCArPSB1XFxcIlxcXCJcXFwiJmx0O2JyJmd0OyZsdDtiJmd0OyB7MH0mbHQ7L2ImZ3Q7IDog
        ezF9IFxcXCJcXFwiXFxcIi5mb3JtYXQoa2V5dmFsWzBdLmNhcGl0YWxpemUoKSxrZXl2YWxbMV0p
        XFxuZWxzZTpcXG4gIG5vdGVUZXh0ID0gdVxcXCJcXFwiXFxcIldob2lzIFF1ZXJ5IHJhbiBhZ2Fp
        bnN0IGlucHV0ICZsdDtiJmd0O3swfSZsdDsvYiZndDsmbHQ7YnImZ3Q7IE5vIHJlc3VsdHMgZm91
        bmRcXFwiXFxcIlxcXCIuZm9ybWF0KHJlc3VsdHMuaW5wdXRzW1xcXCJ3aG9pc19xdWVyeVxcXCJd
        KVxcbmluY2lkZW50LmFkZE5vdGUoaGVscGVyLmNyZWF0ZVJpY2hUZXh0KG5vdGVUZXh0KSlcXG4g
        ICAgXCJ9PC9yZXNpbGllbnQ6ZnVuY3Rpb24+PC9leHRlbnNpb25FbGVtZW50cz48aW5jb21pbmc+
        U2VxdWVuY2VGbG93XzF5bzlqMG88L2luY29taW5nPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMXRo
        ODNqYTwvb3V0Z29pbmc+PC9zZXJ2aWNlVGFzaz48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VG
        bG93XzF5bzlqMG9cIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0YXJnZXRSZWY9
        XCJTZXJ2aWNlVGFza18wOGVyYTVkXCIvPjxlbmRFdmVudCBpZD1cIkVuZEV2ZW50XzFlOWx5ZjRc
        Ij48aW5jb21pbmc+U2VxdWVuY2VGbG93XzF0aDgzamE8L2luY29taW5nPjwvZW5kRXZlbnQ+PHNl
        cXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18xdGg4M2phXCIgc291cmNlUmVmPVwiU2Vydmlj
        ZVRhc2tfMDhlcmE1ZFwiIHRhcmdldFJlZj1cIkVuZEV2ZW50XzFlOWx5ZjRcIi8+PHRleHRBbm5v
        dGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiPjx0ZXh0PlN0YXJ0IHlvdXIgd29y
        a2Zsb3cgaGVyZTwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29j
        aWF0aW9uXzFzZXVqNDhcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0YXJnZXRS
        ZWY9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIvPjwvcHJvY2Vzcz48YnBtbmRpOkJQTU5EaWFn
        cmFtIGlkPVwiQlBNTkRpYWdyYW1fMVwiPjxicG1uZGk6QlBNTlBsYW5lIGJwbW5FbGVtZW50PVwi
        dW5kZWZpbmVkXCIgaWQ9XCJCUE1OUGxhbmVfMVwiPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVt
        ZW50PVwiU3RhcnRFdmVudF8xNTVhc3htXCIgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1fZGlcIj48
        b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCIxNjJcIiB5PVwiMTg4
        XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMFwiIHdpZHRoPVwi
        OTBcIiB4PVwiMTU3XCIgeT1cIjIyM1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBN
        TlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25fMWt4
        eGl5dFwiIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVp
        Z2h0PVwiMzBcIiB3aWR0aD1cIjEwMFwiIHg9XCI5OVwiIHk9XCIyNTRcIi8+PC9icG1uZGk6QlBN
        TlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4
        XCIgaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxNjlc
        IiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIyMFwiLz48b21nZGk6d2F5cG9pbnQgeD1c
        IjE1M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5F
        ZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU2VydmljZVRhc2tfMDhlcmE1ZFwi
        IGlkPVwiU2VydmljZVRhc2tfMDhlcmE1ZF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiODBc
        IiB3aWR0aD1cIjEwMFwiIHg9XCIzNDNcIiB5PVwiMTY2XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48
        YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzF5bzlqMG9cIiBpZD1c
        IlNlcXVlbmNlRmxvd18xeW85ajBvX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxOThcIiB4c2k6
        dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjM0M1wi
        IHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxv
        bWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiMjcwLjVcIiB5PVwiMTg0
        XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFw
        ZSBicG1uRWxlbWVudD1cIkVuZEV2ZW50XzFlOWx5ZjRcIiBpZD1cIkVuZEV2ZW50XzFlOWx5ZjRf
        ZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCI1NjlcIiB5
        PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3
        aWR0aD1cIjBcIiB4PVwiNTg3XCIgeT1cIjIyN1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1u
        ZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1ZW5jZUZsb3df
        MXRoODNqYVwiIGlkPVwiU2VxdWVuY2VGbG93XzF0aDgzamFfZGlcIj48b21nZGk6d2F5cG9pbnQg
        eD1cIjQ0M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxvbWdkaTp3YXlw
        b2ludCB4PVwiNTY5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PGJwbW5k
        aTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI1
        MDZcIiB5PVwiMTg0XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48L2Jw
        bW5kaTpCUE1OUGxhbmU+PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9ucz4iLCAidmVy
        c2lvbiI6IDEyLCAid29ya2Zsb3dfaWQiOiAiZXhhbXBsZV93aG9pc19xdWVyeV9hZ2FpbnN0X2Fy
        dGlmYWN0In0sICJhY3Rpb25zIjogW119XSwgInJvbGVzIjogW10sICJ3b3Jrc3BhY2VzIjogW119
        """
                           )
