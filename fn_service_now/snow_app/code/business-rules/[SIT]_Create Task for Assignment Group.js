// (c) Copyright IBM Corp. 2022. All Rights Reserved.

/////////////////
/// Condition ///
/////////////////
current.isValidField("x_ibmrt_resilient_ibm_resilient_reference_id") && current.getValue("x_ibmrt_resilient_ibm_resilient_reference_id") == null

//////////////////
///   Script   ///
//////////////////
(function executeRule(current) {

	var resReferenceId, wfVars, wfId, wf, parent, resHelper = null;

	resHelper = new ResilientHelper();
	
	//This condition doesn't fit in the condition section so is checked here
	if (resHelper.assignGroupIsAllowed(current.getDisplayValue("assignment_group"))){

		parent = new GlideRecord("sn_si_incident");
		parent.get(current.getValue("parent"));

		resReferenceId = parent.getValue("x_ibmrt_resilient_ibm_resilient_reference_id");

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