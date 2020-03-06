// (c) Copyright IBM Corp. 2019. All Rights Reserved.

/////////////////
/// Condition ///
/////////////////
current.isValidField("x_ibmrt_resilient_ibm_resilient_reference_id") && current.getValue("x_ibmrt_resilient_ibm_resilient_reference_id") == null && gs.hasRole('x_ibmrt_resilient.user')

//////////////////
///   Script   ///
//////////////////
function promptForResilientIncidentId(){
	
	var incidentId, re, ga = null;
	
	//Regex for numbers only
	re = /^[0-9]*$/;
	
	//Prompt user to enter incidentId
	incidentId = prompt("Enter Resilient Incident ID to add task to:");

	// IncidentId will be null if the user clicks cancel
	if(incidentId != null){

		//Validate incidentId
		if(!re.test(incidentId)){
			alert("ERROR: "+incidentId+" is NOT a valid Resilient Incident ID");
		}
		
		else{
			//Create new GlideAjax on our CreateTask Script Include
			ga = new GlideAjax("CreateTask");

			//Set the name of the function we want to call
			ga.addParam("sysparm_name", "createTask");

			//Set the variables 
			ga.addParam("sysparm_snTableName", g_form.getTableName());
			ga.addParam("sysparm_recordSysId", g_form.getUniqueValue());
			ga.addParam("sysparm_incidentId", incidentId);
			
			//Call the function createTask()
			ga.getXML();

			//Call this UI Action and skip the "onclick" function 
			gsftSubmit(null, g_form.getFormElement(), "create_new_ibm_resilient_task");
		}
	}
}

if(typeof window == "undefined"){
	//This is called from line 45 gsftSubmit... because Action Name == create_new_ibm_resilient_task
	action.setRedirectURL(current);
	gs.addInfoMessage("Creating a Task in Resilient from this record");
}
