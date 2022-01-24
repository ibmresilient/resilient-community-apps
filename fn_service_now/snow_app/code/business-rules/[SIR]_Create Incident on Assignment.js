// (c) Copyright IBM Corp. 2022. All Rights Reserved.

/////////////////
/// Condition ///
/////////////////
current.isValidField("x_ibmrt_resilient_ibm_resilient_reference_id") && current.getValue("x_ibmrt_resilient_ibm_resilient_reference_id") == null

//////////////////
///   Script   ///
//////////////////
(function resActionCreateIncident(current){

	var resHelper, workflowId, wf = null;

	resHelper = new ResilientHelper();

	//This condition doesn't fit in the condition section so is checked here
	//Check that the new assignment group is in the list of groups to auto-sync on
	if (resHelper.assignGroupIsAllowed(current.getDisplayValue("assignment_group").trim().toLowerCase())) {

		workflowId = null;

		//Instantiate new Workflow object (use global. as in Scoped Application)
		wf = new global.Workflow();
		
		//Check if user has defined a custom workflow
		workflowId = wf.getWorkflowFromName("CUSTOM_RES_WF_CreateIncident");

		//If there is no custom workflow, run the default one
		if(workflowId == null){
			workflowId = wf.getWorkflowFromName("RES_WF_CreateIncident");
		}
		
		//Start the workflow, where 'current' is the current record the UI action was triggered from
		wf.startFlow(workflowId, current, null, null);
	}
})(current);