# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_ipinfo"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_ipinfo package"""
    reload_params = {"package": u"fn_ipinfo",
        "incident_fields": [],
        "action_fields": [],
        "function_params": [u"ipinfo_query_ip"],
        "datatables": [],
        "message_destinations": [u"fn_ipinfo"],
        "functions": [u"fn_ipinfo_query_ip_address"],
        "phases": [],
            "automatic_tasks": [],
            "scripts": [],
            "workflows": [u"example_query_ip_artifact_with_ipinfo"],
            "actions": [u"Query Artifact with IP Info"]
            }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
        that should be installed by `resilient-circuits customize`
        """
    
    # This import data contains:
    #   Function inputs:
    #     ipinfo_query_ip
    #   Message Destinations:
    #     fn_ipinfo
    #   Functions:
    #     fn_ipinfo_query_ip_address
    #   Workflows:
    #     example_query_ip_artifact_with_ipinfo
    #   Rules:
    #     Query Artifact with IP Info
    
    
    yield ImportDefinition(u"""
        eyJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMSwgIm1pbm9yIjogMCwgImJ1aWxkX251bWJl
        ciI6IDQyMzUsICJ2ZXJzaW9uIjogIjMxLjAuNDIzNSJ9LCAiZXhwb3J0X2Zvcm1hdF92ZXJzaW9u
        IjogMiwgImlkIjogNCwgImV4cG9ydF9kYXRlIjogMTU0NDAwNzY3NDY2MCwgImZpZWxkcyI6IFt7
        ImlkIjogMjIzLCAibmFtZSI6ICJpbmNfdHJhaW5pbmciLCAidGV4dCI6ICJTaW11bGF0aW9uIiwg
        InByZWZpeCI6IG51bGwsICJ0eXBlX2lkIjogMCwgInRvb2x0aXAiOiAiV2hldGhlciB0aGUgaW5j
        aWRlbnQgaXMgYSBzaW11bGF0aW9uIG9yIGEgcmVndWxhciBpbmNpZGVudC4gVGhpcyBmaWVsZCBp
        cyByZWFkLW9ubHkuIiwgImlucHV0X3R5cGUiOiAiYm9vbGVhbiIsICJoaWRlX25vdGlmaWNhdGlv
        biI6IGZhbHNlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBm
        YWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiaW50ZXJuYWwiOiBmYWxzZSwgInV1aWQiOiAi
        YzNmMGUzZWQtMjFlMS00ZDUzLWFmZmItZmU1Y2EzMzA4Y2NhIiwgIm9wZXJhdGlvbnMiOiBbXSwg
        Im9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidmFsdWVzIjogW10sICJyZWFkX29ubHkiOiB0cnVlLCAi
        Y2hhbmdlYWJsZSI6IHRydWUsICJyaWNoX3RleHQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiaW5j
        aWRlbnQvaW5jX3RyYWluaW5nIiwgInRlbXBsYXRlcyI6IFtdLCAiZGVwcmVjYXRlZCI6IGZhbHNl
        fSwgeyJpZCI6IDI5NywgIm5hbWUiOiAiaXBpbmZvX3F1ZXJ5X2lwIiwgInRleHQiOiAiaXBpbmZv
        X3F1ZXJ5X2lwIiwgInByZWZpeCI6IG51bGwsICJ0eXBlX2lkIjogMTEsICJ0b29sdGlwIjogIkFu
        IElQIGFkZHJlc3MgaW4gZWl0aGVyIElQVjQgb2YgSVBWNiBmb3JtYXQuIiwgInBsYWNlaG9sZGVy
        IjogIjguOC44LjgiLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInJlcXVpcmVkIjogImFsd2F5cyIs
        ICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2No
        b3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiaW50ZXJuYWwi
        OiBmYWxzZSwgInV1aWQiOiAiNGZhOGM1ODEtMjRmNC00YzIzLWEyYmMtMjE5MjM1NmEzZGNmIiwg
        Im9wZXJhdGlvbnMiOiBbXSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidmFsdWVzIjogW10sICJy
        ZWFkX29ubHkiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAicmljaF90ZXh0IjogZmFsc2Us
        ICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vaXBpbmZvX3F1ZXJ5X2lwIiwgInRlbXBsYXRlcyI6
        IFtdLCAiZGVwcmVjYXRlZCI6IGZhbHNlfV0sICJpbmNpZGVudF90eXBlcyI6IFt7InVwZGF0ZV9k
        YXRlIjogMTU0NDAwNzcxNzc2NCwgImNyZWF0ZV9kYXRlIjogMTU0NDAwNzcxNzc2NCwgInV1aWQi
        OiAiYmZlZWMyZDQtMzc3MC0xMWU4LWFkMzktNGEwMDA0MDQ0YWEwIiwgImRlc2NyaXB0aW9uIjog
        IkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJleHBvcnRfa2V5IjogIkN1c3Rv
        bWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJuYW1lIjogIkN1c3RvbWl6YXRpb24gUGFj
        a2FnZXMgKGludGVybmFsKSIsICJlbmFibGVkIjogZmFsc2UsICJzeXN0ZW0iOiBmYWxzZSwgInBh
        cmVudF9pZCI6IG51bGwsICJoaWRkZW4iOiBmYWxzZSwgImlkIjogMH1dLCAicGhhc2VzIjogW10s
        ICJhdXRvbWF0aWNfdGFza3MiOiBbXSwgIm92ZXJyaWRlcyI6IFtdLCAibWVzc2FnZV9kZXN0aW5h
        dGlvbnMiOiBbeyJuYW1lIjogIklwSW5mbyBEZXN0aW5hdGlvbiIsICJwcm9ncmFtbWF0aWNfbmFt
        ZSI6ICJmbl9pcGluZm8iLCAiZGVzdGluYXRpb25fdHlwZSI6IDAsICJleHBlY3RfYWNrIjogdHJ1
        ZSwgInVzZXJzIjogWyJhbGZyZWRAd2F5bmVjb3JwLmNvbSIsICJpbnRlZ3JhdGlvbi1zZXJ2ZXIu
        YWxmcmVkQHdheW5lY29ycC5jb20iXSwgInV1aWQiOiAiYjZhZDNjZDgtZWMwZC00ZGRmLThmODUt
        YTBkY2RlNGY2ZDg5IiwgImV4cG9ydF9rZXkiOiAiZm5faXBpbmZvIn1dLCAiYWN0aW9ucyI6IFt7
        ImlkIjogMjcsICJuYW1lIjogIlF1ZXJ5IEFydGlmYWN0IHdpdGggSVAgSW5mbyIsICJ0eXBlIjog
        MSwgIm9iamVjdF90eXBlIjogImFydGlmYWN0IiwgImNvbmRpdGlvbnMiOiBbeyJtZXRob2QiOiAi
        aGFzX2FfdmFsdWUiLCAiZmllbGRfbmFtZSI6ICJhcnRpZmFjdC52YWx1ZSIsICJ2YWx1ZSI6IG51
        bGwsICJ0eXBlIjogbnVsbCwgImV2YWx1YXRpb25faWQiOiBudWxsfSwgeyJtZXRob2QiOiAiZXF1
        YWxzIiwgImZpZWxkX25hbWUiOiAiYXJ0aWZhY3QudHlwZSIsICJ2YWx1ZSI6ICJJUCBBZGRyZXNz
        IiwgInR5cGUiOiBudWxsLCAiZXZhbHVhdGlvbl9pZCI6IG51bGx9XSwgImF1dG9tYXRpb25zIjog
        W10sICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFtdLCAid29ya2Zsb3dzIjogWyJleGFtcGxlX3F1
        ZXJ5X2lwX2FydGlmYWN0X3dpdGhfaXBpbmZvIl0sICJ2aWV3X2l0ZW1zIjogW10sICJ0aW1lb3V0
        X3NlY29uZHMiOiA4NjQwMCwgInV1aWQiOiAiZWIxMzY3ZWUtYmZmZC00MTI3LTk1N2UtMWEyMTdj
        MjY5MjMyIiwgImV4cG9ydF9rZXkiOiAiUXVlcnkgQXJ0aWZhY3Qgd2l0aCBJUCBJbmZvIiwgImxv
        Z2ljX3R5cGUiOiAiYWxsIn1dLCAibGF5b3V0cyI6IFtdLCAibm90aWZpY2F0aW9ucyI6IG51bGws
        ICJ0aW1lZnJhbWVzIjogbnVsbCwgImxvY2FsZSI6IG51bGwsICJpbmR1c3RyaWVzIjogbnVsbCwg
        InJlZ3VsYXRvcnMiOiBudWxsLCAiZ2VvcyI6IG51bGwsICJ0YXNrX29yZGVyIjogW10sICJhY3Rp
        b25fb3JkZXIiOiBbXSwgInR5cGVzIjogW10sICJzY3JpcHRzIjogW10sICJpbmNpZGVudF9hcnRp
        ZmFjdF90eXBlcyI6IFtdLCAid29ya2Zsb3dzIjogW3sid29ya2Zsb3dfaWQiOiAzLCAibmFtZSI6
        ICJFeGFtcGxlOiBRdWVyeSBJUCBBcnRpZmFjdCBXaXRoIElwSW5mbyIsICJwcm9ncmFtbWF0aWNf
        bmFtZSI6ICJleGFtcGxlX3F1ZXJ5X2lwX2FydGlmYWN0X3dpdGhfaXBpbmZvIiwgIm9iamVjdF90
        eXBlIjogImFydGlmYWN0IiwgImRlc2NyaXB0aW9uIjogIkFuIGV4YW1wbGUgd29ya2Zsb3cgd2hp
        Y2ggaXMgaW50ZW5kZWQgdG8gYmUgcmFuIG9uIGFuIGFydGlmYWN0IG9mIHR5cGUgSVAgQWRkcmVz
        cy4gVGFrZXMgdGhlIElQIGlucHV0IGFuZCBzdWJtaXRzIGEgcXVlcnkgdG8gdGhlIElQSW5mbyBS
        RVNUIEFQSSBpbiBhbiBhdHRlbXB0IHRvIHJldHVybiBlbnJpY2htZW50IGluZm8gZm9yIHRoZSBJ
        UCBhZGRyZXNzLlxuUmVzdWx0cyBhcmUgc2F2ZWQgYXMgYSByaWNoIHRleHQgbm90ZSIsICJjcmVh
        dG9yX2lkIjogImFsZnJlZEB3YXluZWNvcnAuY29tIiwgImxhc3RfbW9kaWZpZWRfYnkiOiAiYWxm
        cmVkQHdheW5lY29ycC5jb20iLCAibGFzdF9tb2RpZmllZF90aW1lIjogMTU0NDAwNzA0MzczNSwg
        ImV4cG9ydF9rZXkiOiAiZXhhbXBsZV9xdWVyeV9pcF9hcnRpZmFjdF93aXRoX2lwaW5mbyIsICJ1
        dWlkIjogIjkzZDFjOTA5LTRmYWUtNGYzZS05Zjk5LWZmMDU4Yjk3Y2VhNiIsICJjb250ZW50Ijog
        eyJ3b3JrZmxvd19pZCI6ICJleGFtcGxlX3F1ZXJ5X2lwX2FydGlmYWN0X3dpdGhfaXBpbmZvIiwg
        InhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVmaW5p
        dGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01PREVM
        XCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9E
        SVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRENc
        IiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJXCIg
        eG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxuczp4
        c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0dHA6
        Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNlPVwi
        aHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJleGFtcGxlX3F1ZXJ5
        X2lwX2FydGlmYWN0X3dpdGhfaXBpbmZvXCIgaXNFeGVjdXRhYmxlPVwidHJ1ZVwiIG5hbWU9XCJF
        eGFtcGxlOiBRdWVyeSBJUCBBcnRpZmFjdCBXaXRoIElwSW5mb1wiPjxkb2N1bWVudGF0aW9uPjwh
        W0NEQVRBW0FuIGV4YW1wbGUgd29ya2Zsb3cgd2hpY2ggaXMgaW50ZW5kZWQgdG8gYmUgcmFuIG9u
        IGFuIGFydGlmYWN0IG9mIHR5cGUgSVAgQWRkcmVzcy4gVGFrZXMgdGhlIElQIGlucHV0IGFuZCBz
        dWJtaXRzIGEgcXVlcnkgdG8gdGhlIElQSW5mbyBSRVNUIEFQSSBpbiBhbiBhdHRlbXB0IHRvIHJl
        dHVybiBlbnJpY2htZW50IGluZm8gZm9yIHRoZSBJUCBhZGRyZXNzLlxuUmVzdWx0cyBhcmUgc2F2
        ZWQgYXMgYSByaWNoIHRleHQgbm90ZV1dPjwvZG9jdW1lbnRhdGlvbj48c3RhcnRFdmVudCBpZD1c
        IlN0YXJ0RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMGhza3NibDwvb3V0
        Z29pbmc+PC9zdGFydEV2ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNrXzFnamRvemRc
        IiBuYW1lPVwiSXBJbmZvOiBRdWVyeSBJUCBBZGRyZXNzXCIgcmVzaWxpZW50OnR5cGU9XCJmdW5j
        dGlvblwiPjxleHRlbnNpb25FbGVtZW50cz48cmVzaWxpZW50OmZ1bmN0aW9uIHV1aWQ9XCJmMTJk
        NWIxYS00NTdjLTQzOWEtOTc5YS0wOGU3NDFmNWJmZTlcIj57XCJpbnB1dHNcIjp7fSxcInBvc3Rf
        cHJvY2Vzc2luZ19zY3JpcHRcIjpcIlxcXCJcXFwiXFxcIlxcbkV4YW1wbGUgb3V0cHV0IGZyb20g
        SVAgSW5mbyBcXG5cXG57XFxuJ3N1Y2Nlc3MnOiBUcnVlLCBcXG4naW5wdXRzJzogXFxuICAgIHsn
        aXBpbmZvX3F1ZXJ5X2lwJzogJzguOC44LjgnfSwgXFxuJ3F1ZXJ5X3Jlc3VsdCc6IFxcbiAgICB7
        J2lwJzogJzguOC44LjgnLCBcXG4gICAgJ2hvc3RuYW1lJzogXFxuICAgICdnb29nbGUtcHVibGlj
        LWRucy1hLmdvb2dsZS5jb20nLCBcXG4gICAgJ2NpdHknOiAnTW91bnRhaW4gVmlldycsIFxcbiAg
        ICAncmVnaW9uJzogJ0NhbGlmb3JuaWEnLCBcXG4gICAgJ2NvdW50cnknOiAnVVMnLCBcXG4gICAg
        J2xvYyc6ICczNy4zODYwLC0xMjIuMDg0MCcsIFxcbiAgICAncG9zdGFsJzogJzk0MDM1JywgXFxu
        ICAgICdwaG9uZSc6ICc2NTAnLCBcXG4gICAgJ29yZyc6ICdBUzE1MTY5IEdvb2dsZSBMTEMnLCBc
        XG4gICAgJ2NvdW50cnlfbmFtZSc6ICdVbml0ZWQgU3RhdGVzJywgXFxuICAgICdsYXRpdHVkZSc6
        ICczNy4zODYwJywgXFxuICAgICdsb25naXR1ZGUnOiAnLTEyMi4wODQwJ319XFxuXFxcIlxcXCJc
        XFwiXFxuXFxuaWYgcmVzdWx0cy5xdWVyeV9yZXN1bHQgIT0gTm9uZTpcXG4gIG5vdGVUZXh0ID0g
        XFxcIlxcXCJcXFwiSVAgSW5mbyBBbmFseXNpcyByYW4gYWdhaW5zdCBpbnB1dCAmbHQ7YiZndDt7
        MH0mbHQ7L2ImZ3Q7ICZsdDticiZndDsmbHQ7YnImZ3Q7IEhvc3RuYW1lIDogJmx0O2ImZ3Q7ezF9
        Jmx0Oy9iJmd0OyAmbHQ7YnImZ3Q7IENvdW50cnkgJmx0O2ImZ3Q7ezJ9Jmx0Oy9iJmd0OyAmbHQ7
        YnImZ3Q7IEdlb0xvY2F0aW9uIDombHQ7YiZndDt7M30mbHQ7L2ImZ3Q7XFxcIlxcXCJcXFwiLmZv
        cm1hdChyZXN1bHRzLmlucHV0c1tcXFwiaXBpbmZvX3F1ZXJ5X2lwXFxcIl0sIHJlc3VsdHMucXVl
        cnlfcmVzdWx0Wydob3N0bmFtZSddLCByZXN1bHRzLnF1ZXJ5X3Jlc3VsdFsnY291bnRyeSddLCBy
        ZXN1bHRzLnF1ZXJ5X3Jlc3VsdFsnbG9jJ10pXFxuICBpbmNpZGVudC5hZGROb3RlKGhlbHBlci5j
        cmVhdGVSaWNoVGV4dChub3RlVGV4dCkpXCIsXCJwcmVfcHJvY2Vzc2luZ19zY3JpcHRcIjpcImlu
        cHV0cy5pcGluZm9fcXVlcnlfaXAgPSBhcnRpZmFjdC52YWx1ZVxcblxcblwifTwvcmVzaWxpZW50
        OmZ1bmN0aW9uPjwvZXh0ZW5zaW9uRWxlbWVudHM+PGluY29taW5nPlNlcXVlbmNlRmxvd18waHNr
        c2JsPC9pbmNvbWluZz48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzBldXQ0d2k8L291dGdvaW5nPjwv
        c2VydmljZVRhc2s+PGVuZEV2ZW50IGlkPVwiRW5kRXZlbnRfMDVhdGFqelwiPjxpbmNvbWluZz5T
        ZXF1ZW5jZUZsb3dfMGV1dDR3aTwvaW5jb21pbmc+PC9lbmRFdmVudD48c2VxdWVuY2VGbG93IGlk
        PVwiU2VxdWVuY2VGbG93XzBldXQ0d2lcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18xZ2pkb3pk
        XCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRfMDVhdGFqelwiLz48c2VxdWVuY2VGbG93IGlkPVwiU2Vx
        dWVuY2VGbG93XzBoc2tzYmxcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0YXJn
        ZXRSZWY9XCJTZXJ2aWNlVGFza18xZ2pkb3pkXCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRB
        bm5vdGF0aW9uXzFreHhpeXRcIj48dGV4dD5TdGFydCB5b3VyIHdvcmtmbG93IGhlcmU8L3RleHQ+
        PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIg
        c291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90YXRp
        b25fMWt4eGl5dFwiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xcWRpZTBu
        XCI+PHRleHQ+VGFrZXMgYW4gSVAgQWRkcmVzcyBhcnRpZmFjdHMgdmFsdWUgYXMgaXRzIG9ubHkg
        aW5wdXQ8L3RleHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlv
        bl8wcGszZW9xXCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMWdqZG96ZFwiIHRhcmdldFJlZj1c
        IlRleHRBbm5vdGF0aW9uXzFxZGllMG5cIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90
        YXRpb25fMGtydGhjdFwiPjx0ZXh0Pk91dHB1dHMgZW5yaWNobWVudCBpbmZvcm1hdGlvbiBmb3Ig
        dGhlIGdpdmVuIElQPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNz
        b2NpYXRpb25fMDVmM2VyMVwiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzFnamRvemRcIiB0YXJn
        ZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8wa3J0aGN0XCIvPjwvcHJvY2Vzcz48YnBtbmRpOkJQTU5E
        aWFncmFtIGlkPVwiQlBNTkRpYWdyYW1fMVwiPjxicG1uZGk6QlBNTlBsYW5lIGJwbW5FbGVtZW50
        PVwidW5kZWZpbmVkXCIgaWQ9XCJCUE1OUGxhbmVfMVwiPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5F
        bGVtZW50PVwiU3RhcnRFdmVudF8xNTVhc3htXCIgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1fZGlc
        Ij48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCIxNjJcIiB5PVwi
        MTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMFwiIHdpZHRo
        PVwiOTBcIiB4PVwiMTU3XCIgeT1cIjIyM1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6
        QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25f
        MWt4eGl5dFwiIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dF9kaVwiPjxvbWdkYzpCb3VuZHMg
        aGVpZ2h0PVwiMzBcIiB3aWR0aD1cIjEwMFwiIHg9XCI5OVwiIHk9XCIyNTRcIi8+PC9icG1uZGk6
        QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8xc2V1
        ajQ4XCIgaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIx
        NjlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIyMFwiLz48b21nZGk6d2F5cG9pbnQg
        eD1cIjE1M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQ
        TU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU2VydmljZVRhc2tfMWdqZG96
        ZFwiIGlkPVwiU2VydmljZVRhc2tfMWdqZG96ZF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwi
        ODBcIiB3aWR0aD1cIjEwMFwiIHg9XCIzODBcIiB5PVwiMTY2XCIvPjwvYnBtbmRpOkJQTU5TaGFw
        ZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIkVuZEV2ZW50XzA1YXRhanpcIiBpZD1c
        IkVuZEV2ZW50XzA1YXRhanpfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9
        XCIzNlwiIHg9XCI2NzFcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3Vu
        ZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNjg5XCIgeT1cIjIyN1wiLz48L2JwbW5k
        aTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1l
        bnQ9XCJTZXF1ZW5jZUZsb3dfMGV1dDR3aVwiIGlkPVwiU2VxdWVuY2VGbG93XzBldXQ0d2lfZGlc
        Ij48b21nZGk6d2F5cG9pbnQgeD1cIjQ4MFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwi
        MjA2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNjcxXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwi
        IHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wi
        IHdpZHRoPVwiMFwiIHg9XCI1NzUuNVwiIHk9XCIxODQuNVwiLz48L2JwbW5kaTpCUE1OTGFiZWw+
        PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNl
        Rmxvd18waHNrc2JsXCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMGhza3NibF9kaVwiPjxvbWdkaTp3YXlw
        b2ludCB4PVwiMTk4XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2Rp
        OndheXBvaW50IHg9XCIzODBcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48
        YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIg
        eD1cIjI4OVwiIHk9XCIxODQuNVwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVk
        Z2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8xcWRpZTBu
        XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xcWRpZTBuX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9
        XCI3NlwiIHdpZHRoPVwiMTU2XCIgeD1cIjIxN1wiIHk9XCI3M1wiLz48L2JwbW5kaTpCUE1OU2hh
        cGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzBwazNlb3FcIiBp
        ZD1cIkFzc29jaWF0aW9uXzBwazNlb3FfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjM4M1wiIHhz
        aTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTczXCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMzQ5
        XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIxNDlcIi8+PC9icG1uZGk6QlBNTkVkZ2U+
        PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8wa3J0aGN0XCIg
        aWQ9XCJUZXh0QW5ub3RhdGlvbl8wa3J0aGN0X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI3
        MVwiIHdpZHRoPVwiMTQwXCIgeD1cIjUyM1wiIHk9XCI3NVwiLz48L2JwbW5kaTpCUE1OU2hhcGU+
        PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzA1ZjNlcjFcIiBpZD1c
        IkFzc29jaWF0aW9uXzA1ZjNlcjFfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjQ4MFwiIHhzaTp0
        eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTc3XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNTMzXCIg
        eHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIxNDZcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PC9i
        cG1uZGk6QlBNTlBsYW5lPjwvYnBtbmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+IiwgInZl
        cnNpb24iOiA0fSwgImFjdGlvbnMiOiBbXX1dLCAicm9sZXMiOiBbXSwgIndvcmtzcGFjZXMiOiBb
        XSwgImZ1bmN0aW9ucyI6IFt7ImlkIjogMzQsICJuYW1lIjogImZuX2lwaW5mb19xdWVyeV9pcF9h
        ZGRyZXNzIiwgImRpc3BsYXlfbmFtZSI6ICJJcEluZm86IFF1ZXJ5IElQIEFkZHJlc3MiLCAiZGVz
        Y3JpcHRpb24iOiB7ImZvcm1hdCI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiU3VibWl0cyBhIHF1ZXJ5
        IHRvIElQIEluZm8gZm9yIGVucmljaG1lbnQgaW5mb3JtYXRpb24gb24gYSBnaXZlbiBJUCBhZGRy
        ZXNzLlxuVGFrZXMgaW4gYSBTdHJpbmcgaW5wdXQgcmVwcmVzZW50aW5nIGFuIElQIEFkZHJlc3Mu
        In0sICJkZXN0aW5hdGlvbl9oYW5kbGUiOiAiZm5faXBpbmZvIiwgImV4cG9ydF9rZXkiOiAiZm5f
        aXBpbmZvX3F1ZXJ5X2lwX2FkZHJlc3MiLCAidXVpZCI6ICJmMTJkNWIxYS00NTdjLTQzOWEtOTc5
        YS0wOGU3NDFmNWJmZTkiLCAidmVyc2lvbiI6IDEsICJjcmVhdG9yIjogeyJpZCI6IDM5LCAidHlw
        ZSI6ICJ1c2VyIiwgIm5hbWUiOiAiYWxmcmVkQHdheW5lY29ycC5jb20iLCAiZGlzcGxheV9uYW1l
        IjogIkFsZnJlZCBQZW5ueXdvcnRoIn0sICJsYXN0X21vZGlmaWVkX2J5IjogeyJpZCI6IDM5LCAi
        dHlwZSI6ICJ1c2VyIiwgIm5hbWUiOiAiYWxmcmVkQHdheW5lY29ycC5jb20iLCAiZGlzcGxheV9u
        YW1lIjogIkFsZnJlZCBQZW5ueXdvcnRoIn0sICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTQyOTAy
        NTM5NzE5LCAidmlld19pdGVtcyI6IFt7InN0ZXBfbGFiZWwiOiBudWxsLCAic2hvd19pZiI6IG51
        bGwsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwg
        ImNvbnRlbnQiOiAiNGZhOGM1ODEtMjRmNC00YzIzLWEyYmMtMjE5MjM1NmEzZGNmIiwgInNob3df
        bGlua19oZWFkZXIiOiBmYWxzZX1dLCAid29ya2Zsb3dzIjogW3sid29ya2Zsb3dfaWQiOiAzLCAi
        bmFtZSI6ICJFeGFtcGxlOiBRdWVyeSBJUCBBcnRpZmFjdCBXaXRoIElwSW5mbyIsICJwcm9ncmFt
        bWF0aWNfbmFtZSI6ICJleGFtcGxlX3F1ZXJ5X2lwX2FydGlmYWN0X3dpdGhfaXBpbmZvIiwgIm9i
        amVjdF90eXBlIjogImFydGlmYWN0IiwgImRlc2NyaXB0aW9uIjogbnVsbCwgInV1aWQiOiBudWxs
        LCAiYWN0aW9ucyI6IFtdfSwgeyJ3b3JrZmxvd19pZCI6IDIsICJuYW1lIjogIlF1ZXJ5IElQIEFy
        dGlmYWN0IHdpdGggSVBJbmZvIiwgInByb2dyYW1tYXRpY19uYW1lIjogInF1ZXJ5X2lwX2FydGlm
        YWN0X3dpdGhfaXBpbmZvIiwgIm9iamVjdF90eXBlIjogImFydGlmYWN0IiwgImRlc2NyaXB0aW9u
        IjogbnVsbCwgInV1aWQiOiBudWxsLCAiYWN0aW9ucyI6IFtdfSwgeyJ3b3JrZmxvd19pZCI6IDEs
        ICJuYW1lIjogIlRlc3QgSXAgSW5mbyIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJ0ZXN0X2lwX2lu
        Zm8iLCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZhY3QiLCAiZGVzY3JpcHRpb24iOiBudWxsLCAidXVp
        ZCI6IG51bGwsICJhY3Rpb25zIjogW119XX1dfQ==
        """
                           )
