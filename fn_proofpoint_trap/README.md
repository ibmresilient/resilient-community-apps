Proofpoint TRAP Integration


Before running this integration, ensure that your app.config has the [fn_proofpoint_trap] section populated.

- Base URL of Proofpoint TRAP API
  + base_url=
- API Key for Proofpoint TRAP
  + api_key=
-  Interval to poll TRAP in Minutes
   + polling_interval=2
- Initial Import Look-back Interval (default: 2 weeks)
   + startup_interval=20160
-  State of Incidents to Query
   + state=open


This integration will pull incidents created from Proofpoint TRAP and populate incidents within resilient.
