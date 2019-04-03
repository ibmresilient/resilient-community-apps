// (c) Copyright IBM Corp. 2019. All Rights Reserved.

var CreateTask = Class.create();
CreateTask.prototype = Object.extendsObject(global.AbstractAjaxProcessor, {
    type: "CreateTask",
	
	createTask: function(){
		
		var snTableName, recordSysId, incidentId, record, wfVars, wfId, wf = null;
		
		//Get parameters from Ajax Client call
		snTableName = this.getParameter("sysparm_snTableName");
		recordSysId = this.getParameter("sysparm_recordSysId");
		incidentId = this.getParameter("sysparm_incidentId");
		
		//Get the GlideRecord using Table Name and sys_id
		record = new GlideRecord(snTableName);
		record.addQuery("sys_id", recordSysId);
		record.query();
		record.next();
					
		//Instantiate new Workflow object (use global. as in Scoped Application)
		wf = new global.Workflow();

		//Set workflow variable
		wfVars = { 
			"u_ibm_resilient_incident_id": incidentId 
		};

		//Check if user has defined a custom workflow
		wfId = wf.getWorkflowFromName("CUSTOM_RES_WF_CreateTask");

		//If there is no custom workflow, run the default one
		if(wfId == null){
			wfId = wf.getWorkflowFromName("RES_WF_CreateTask");
		}

		//Start the workflow
		wf.startFlow(wfId, record, null, wfVars);
	}
});