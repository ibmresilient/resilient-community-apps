// (c) Copyright IBM Corp. 2022. All Rights Reserved.

/////////////////
/// Condition ///
/////////////////
gs.getProperty("x_ibmrt_resilient.ServiceNowUsername") != gs.getUserName() && gs.getUserName() != "system" && (new ScriptConditionsHelper().sitCreateOnAssignCheck(current) == true);

//////////////////
///   Script   ///
//////////////////
(function executeRule(current) {

	var resReferenceId, wfVars, wfId, wf, resHelper, snowHelper = null;

	resHelper = new ResilientHelper();
	snowHelper = new SNOWRESTHelper();

	//Get the res ID to properly link this new task to a resilient incident
	resReferenceId = snowHelper.getResReferenceIdFromTaskParent(current, "sn_si_incident");

	//Instantiate new Workflow object (use global. as in Scoped Application)
	wf = new global.Workflow();

	//Set workflow variable
	wfVars = { 
		"u_ibm_resilient_incident_id": resHelper.parseRefId(resReferenceId).incidentId
	};

	//Check if user has defined a custom workflow
	wfId = wf.getWorkflowFromName("CUSTOM_RES_WF_CreateTask");

	//If there is no custom workflow, run the default one
	if(wfId == null){
		wfId = wf.getWorkflowFromName("RES_WF_CreateTask");
	}

	//Start the workflow
	wf.startFlow(wfId, current, null, wfVars);

})(current);