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
if(typeof window == "undefined")
	createTaskNew();

function createTaskNew() {
	action.setRedirectURL(current);
	var incidentId = gs.getUser().getPreference("ibm_resilient_incident_id");
	
	var re = /^[0-9]*$/;
	var valid = re.test(incidentId);

	try{
		if(valid){
			var wf = new global.Workflow();
		
			vars = { "u_ibm_resilient_incident_id": incidentId };

			wf.startFlow(wf.getWorkflowFromName("ResilientCreateTask"), current, null, vars);
			
			gs.addInfoMessage("Creating a Task in Resilient on the Incident: " + incidentId);
		}
		else{
			gs.addErrorMessage(incidentId + " is not a VALID Resilient Incident ID");
		}
	}
	catch (ex){
		gs.addInfoMessage("Failed to Create Resilient Task: " + ex.toString());
		throw ex;
	}
}