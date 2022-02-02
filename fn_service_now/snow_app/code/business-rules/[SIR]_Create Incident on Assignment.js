// (c) Copyright IBM Corp. 2022. All Rights Reserved.

/////////////////
/// Condition ///
/////////////////
gs.getProperty("x_ibmrt_resilient.ServiceNowUsername") != gs.getUserName() && gs.getUserName() != "system" && (new ScriptConditionsHelper().sirCreateOnAssignCheck(current) == true);

//////////////////
///   Script   ///
//////////////////
(function resActionCreateIncident(current){

	var workflowId, wf = null;

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

})(current);