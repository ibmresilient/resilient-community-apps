# Old Implementation:
https://github.com/kathychurch/resilient-snow

# Notes:

# Pre-Reqs
* Create user in ServiceNow: 
  * Name: IBM Resilient
  * User ID: ibmresilient
  * Email: integrations@example.com (same email address as Resilient Orchestration Engine in app.config file)

* Create user in Resilient:
  * Name: SNOW Engine
  * Email: snow_engine@example.com
  ```
  $ sudo resutil newuser -org "ResOrg" -email snow_integration@example.com -password "ResDemo123" -first "SNOW" -last "Integration"
  ```

## Restarting MID Server
https://docs.servicenow.com/bundle/kingston-servicenow-platform/page/product/mid-server/concept/c_BasicMIDServerActions.html

## SN Utilities: Create in ServiceNow
* By default, sets `short_description` as Incident/Task title
* By default, sets `description` as `incident.description` or `task.instructions`
* By default, sets `work_notes` as `sn_init_work_note`


## Getting sn_record_state from ServiceNow
![screenshot](./screenshots/1.png)

## Getting sn_close_code from ServiceNow
![screenshot](./screenshots/2.png)


## ServiceNow Logs
* System Logs >> Application Logs
  * error (gs.error):
    * Logs events that might still allow the application to continue running. Setting the log level for an application to error generates error messages only, but does not generate warn, info, or debug messages.
  * warn (gs.warn):
    * Logs potentially harmful events. Setting the log level for an application to warn generates error and warn messages, but does not generate error or debug messages.
  * info (gs.info):
    * Logs informational messages that describe the progress of the application. Setting the log level for an application to info generates info, warn, and error messages, but does not generate debug messages.
  * debug (gs.debug):
    * Logs informational events that are useful for debugging an application. Setting the log level for an application to debug generates info, warn, error, and debug messages.

## Mid Server
* Make sure mid-server has IBMResilientAccess Capabilities
* RESTMessageV2 set MID Server by capability: https://community.servicenow.com/community?id=community_question&sys_id=17405329dbdcdbc01dcaf3231f96193c