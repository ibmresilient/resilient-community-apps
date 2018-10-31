/////////////////
/// Condition ///
/////////////////
current.isValidField("x_261673_resilient_reference_id") && current.getValue("x_261673_resilient_reference_id") != null && gs.getProperty("x_261673_resilient.ServiceNowUsername") != gs.getUserName()

//////////////////
///   Script   ///
//////////////////
(function executeRule(current, previous) {
	
	//Instaniate new Workflow object (use global. as in Scoped Application)
	var wf = new global.Workflow();
	
	//Get the workflow_id from the workflow name
	var workflowId = wf.getWorkflowFromName("ResilientAddWorkNote");
			
	//Start the workflow, where 'current' is the current record the UI action was triggered from
	wf.startFlow(workflowId, current, null, null);

})(current, previous);