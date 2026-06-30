# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for components_app_host"""

try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition


def codegen_reload_data():
    """
    Parameters required reload codegen for the components_app_host package
    """
    return {
        "package": u"components_app_host",
        "message_destinations": [],
        "functions": [],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    Contents:
    """

    yield ImportDefinition(u"""
eyJhY3Rpb25fb3JkZXIiOiBbXSwgImFjdGlvbnMiOiBbXSwgImF1dG9tYXRpY190YXNrcyI6IFtd
LCAiZXhwb3J0X2RhdGUiOiAxNTk0MTM0OTE5MTAwLCAiZXhwb3J0X2Zvcm1hdF92ZXJzaW9uIjog
MiwgImZpZWxkcyI6IFt7ImV4cG9ydF9rZXkiOiAiaW5jaWRlbnQvaW50ZXJuYWxfY3VzdG9taXph
dGlvbnNfZmllbGQiLCAiaWQiOiAwLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjog
dHJ1ZSwgIm5hbWUiOiAiaW50ZXJuYWxfY3VzdG9taXphdGlvbnNfZmllbGQiLCAicmVhZF9vbmx5
IjogdHJ1ZSwgInRleHQiOiAiQ3VzdG9taXphdGlvbnMgRmllbGQgKGludGVybmFsKSIsICJ0eXBl
X2lkIjogMCwgInV1aWQiOiAiYmZlZWMyZDQtMzc3MC0xMWU4LWFkMzktNGEwMDA0MDQ0YWExIn1d
LCAiZnVuY3Rpb25zIjogW10sICJnZW9zIjogbnVsbCwgImdyb3VwcyI6IG51bGwsICJpZCI6IDUs
ICJpbmJvdW5kX21haWxib3hlcyI6IG51bGwsICJpbmNpZGVudF9hcnRpZmFjdF90eXBlcyI6IFtd
LCAiaW5jaWRlbnRfdHlwZXMiOiBbeyJ1cGRhdGVfZGF0ZSI6IDE1OTQxMzQ5MTcxODcsICJjcmVh
dGVfZGF0ZSI6IDE1OTQxMzQ5MTcxODcsICJ1dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFlOC1hZDM5
LTRhMDAwNDA0NGFhMCIsICJkZXNjcmlwdGlvbiI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChp
bnRlcm5hbCkiLCAiZXhwb3J0X2tleSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5h
bCkiLCAibmFtZSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZW5hYmxl
ZCI6IGZhbHNlLCAic3lzdGVtIjogZmFsc2UsICJwYXJlbnRfaWQiOiBudWxsLCAiaGlkZGVuIjog
ZmFsc2UsICJpZCI6IDB9XSwgImluZHVzdHJpZXMiOiBudWxsLCAibGF5b3V0cyI6IFtdLCAibG9j
YWxlIjogbnVsbCwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW10sICJub3RpZmljYXRpb25zIjog
bnVsbCwgIm92ZXJyaWRlcyI6IFtdLCAicGhhc2VzIjogW10sICJyZWd1bGF0b3JzIjogbnVsbCwg
InJvbGVzIjogW10sICJzY3JpcHRzIjogW10sICJzZXJ2ZXJfdmVyc2lvbiI6IHsiYnVpbGRfbnVt
YmVyIjogMzIsICJtYWpvciI6IDM1LCAibWlub3IiOiAyLCAidmVyc2lvbiI6ICIzNS4yLjMyIn0s
ICJ0YWdzIjogW10sICJ0YXNrX29yZGVyIjogW10sICJ0aW1lZnJhbWVzIjogbnVsbCwgInR5cGVz
IjogW10sICJ3b3JrZmxvd3MiOiBbXSwgIndvcmtzcGFjZXMiOiBbXX0=
""")
