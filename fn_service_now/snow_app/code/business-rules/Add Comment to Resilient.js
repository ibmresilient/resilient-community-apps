// (c) Copyright IBM Corp. 2019. All Rights Reserved.

/////////////////
/// Condition ///
/////////////////
current.isValidField("x_ibmrt_resilient_ibm_resilient_reference_id") && current.getValue("x_ibmrt_resilient_ibm_resilient_reference_id") != null && gs.getProperty("x_ibmrt_resilient.ServiceNowUsername") != gs.getUserName() && gs.getUserName() != "system";

//////////////////
///   Script   ///
//////////////////
(function executeRule(current) {
	
	var workflowId = null;
	
	//Instantiate new Workflow object (use global. as in Scoped Application)	
	var wf = new global.Workflow();

	//Check if user has defined a custom workflow
	workflowId = wf.getWorkflowFromName("CUSTOM_RES_WF_AddComment");
	
	//If there is no custom workflow, run the default one
	if(workflowId == null){
		workflowId = wf.getWorkflowFromName("RES_WF_AddComment");
	}
	
	//Start the workflow, where 'current' is the current record the UI action was triggered from
	wf.startFlow(workflowId, current, null, null);

})(current);