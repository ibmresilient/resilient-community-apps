/////////////////
/// Condition ///
/////////////////
current.isValidField("x_261673_resilient_reference_id") && current.getValue("x_261673_resilient_reference_id") == null

//////////////////
///   Script   ///
//////////////////
(function resActionCreateIncident(){
	//Stop redirect
	action.setRedirectURL(current);
	
	//Use the GlideSystem class (gs) to add a 'popup' message
	gs.addInfoMessage('Starting: Create IBM Resilient Incident Workflow');	
	
	//Instaniate new Workflow object (use global. as in Scoped Application)
	var wf = new global.Workflow();
	
	//Get the workflow_id from the workflow name
	var workflowId = wf.getWorkflowFromName("ResilientCreateIncident");
	
	//Set vars object which is JSON named-value pairs, where the name is the Column name of the workflow input
// 	var vars = {
// 		"u_test_workflow_input": 'test'
// 	};
	var vars = {};
		
	//Start the workflow, where 'current' is the current record the UI action was triggered from
	wf.startFlow(workflowId, current, null, vars);
})();