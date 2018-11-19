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
	gs.addInfoMessage("Creating an Incident in Resilient from this record");
	
	//Instaniate new Workflow object (use global. as in Scoped Application)
	var wf = new global.Workflow();
	
	//Get the workflow_id from the workflow name
	var workflowId = wf.getWorkflowFromName("ResilientCreateIncident");
		
	//Start the workflow, where 'current' is the current record the UI action was triggered from
	wf.startFlow(workflowId, current, null, null);
})();