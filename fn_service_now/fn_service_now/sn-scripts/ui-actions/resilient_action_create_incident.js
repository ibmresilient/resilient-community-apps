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
// 		"u_test_workflow_input": 'YessAii'
// 	};
	var vars = {};
	
// 	//Use the GlideSystem class to print a debug message to System Logs >> Application Logs
// 	gs.info('Starting Workflow: test_workflow');
	
// 	var gdw = new GlideDialogWindow('show_list');
// 	gdw.setTitle('Test');
// 	gdw.setSize(750,300);
// 	gdw.adjustBodySize();
// 	gdw.render();
	
	//Start the workflow, where 'current' is the current record the UI action was triggered from
	wf.startFlow(workflowId, current, null, vars);
})();