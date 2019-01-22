// (c) Copyright IBM Corp. 2019. All Rights Reserved.

/////////////////
/// Condition ///
/////////////////
current.isValidField("x_261673_resilient_reference_id") && current.getValue("x_261673_resilient_reference_id") == null

//////////////////
///   Script   ///
//////////////////
function promptForResilientIncidentId(){
	
	//Get the last entered incidentId
	var lastIncidentId = getPreference("ibm_resilient_incident_id");
	
	//Create and open the dialog form
	var incidentId = prompt("Enter Resilient Incident ID to add task to:", lastIncidentId);
	
	if (incidentId){
		if (lastIncidentId != incidentId){
			setPreference("ibm_resilient_incident_id", incidentId);
		}

		//Call the UI Action and skip the "onclick" function
		gsftSubmit(null, g_form.getFormElement(), "create_new_ibm_resilient_task");
	}
}

//Code that runs without "onclick"
//Ensure call to server-side function with no browser errors
if(typeof window == "undefined"){
	createTaskNew();
}

function createTaskNew() {
	action.setRedirectURL(current);
	var incidentId = gs.getUser().getPreference("ibm_resilient_incident_id");
	
	var re = /^[0-9]*$/;
	var valid = re.test(incidentId);

	try{
		if(valid){
			gs.addInfoMessage("Creating a Task in Resilient from this record in the Resilient Incident: " + incidentId);
			
			var workflowId, workflowVars = null;
			
			//Instantiate new Workflow object (use global. as in Scoped Application)
			var wf = new global.Workflow();
		
			workflowVars = { 
				"u_ibm_resilient_incident_id": incidentId 
			};

			//Check if user has defined a custom workflow
			workflowId = wf.getWorkflowFromName("CUSTOM_RES_WF_CreateTask");

			//If there is no custom workflow, run the default one
			if(workflowId == null){
				workflowId = wf.getWorkflowFromName("RES_WF_CreateTask");
			}
	
			wf.startFlow(workflowId, current, null, workflowVars);

		}
		else{
			gs.addErrorMessage(incidentId + " is NOT a valid Resilient Incident ID");
		}
	}
	catch (err){
		gs.addInfoMessage("Failed to Create Resilient Task: " + err);
		throw err;
	}
}