// (c) Copyright IBM Corp. 2022. All Rights Reserved.

/////////////////
/// Condition ///
/////////////////
current.isValidField("x_ibmrt_resilient_ibm_soar_reference_id") && current.getValue("x_ibmrt_resilient_ibm_soar_reference_id") == null && !current.isValidField("x_ibmrt_resilient_ibm_resilient_reference_id") && current.getTableName() == "sn_si_task"

//////////////////
///   Script   ///
//////////////////
(function executeRule(current) {

	var resReferenceId, wfVars, wfId, wf, resHelper, snowHelper = null;

	resHelper = new ResilientHelper();
	snowHelper = new SNOWRESTHelper();

	//This condition doesn't fit in the condition section so is checked here
	//Check that the new assignment group is in the list of groups to auto-sync on
	if (resHelper.assignGroupIsAllowed(current.getDisplayValue("assignment_group").trim().toLowerCase())){

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
	}

})(current);