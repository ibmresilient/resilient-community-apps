// (c) Copyright IBM Corp. 2022. All Rights Reserved.

/////////////////
/// Condition ///
/////////////////
(new ScriptConditionsHelper().sirAddCommentCheck(current)) == true

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