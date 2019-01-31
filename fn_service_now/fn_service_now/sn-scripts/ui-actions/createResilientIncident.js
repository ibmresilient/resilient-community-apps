// (c) Copyright IBM Corp. 2019. All Rights Reserved.

/////////////////
/// Condition ///
/////////////////
current.isValidField("x_261673_resilient_reference_id") && current.getValue("x_261673_resilient_reference_id") == null && gs.hasRole('x_261673_resilient.user')

//////////////////
///   Script   ///
//////////////////
(function resActionCreateIncident(){
	//Stop redirect
	action.setRedirectURL(current);
	
	//Use the GlideSystem class (gs) to add a 'popup' message
	gs.addInfoMessage("Creating an Incident in Resilient from this record");

	var workflowId = null;
	
	//Instantiate new Workflow object (use global. as in Scoped Application)
	var wf = new global.Workflow();
	
	//Check if user has defined a custom workflow
	workflowId = wf.getWorkflowFromName("CUSTOM_RES_WF_CreateIncident");

	//If there is no custom workflow, run the default one
	if(workflowId == null){
		workflowId = wf.getWorkflowFromName("RES_WF_CreateIncident");
	}
	
	//Start the workflow, where 'current' is the current record the UI action was triggered from
	wf.startFlow(workflowId, current, null, null);
})();