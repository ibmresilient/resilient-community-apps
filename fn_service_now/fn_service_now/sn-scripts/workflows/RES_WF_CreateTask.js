(function RES_WF_CreateTask(){
	
	var resHelper, record, snRecordId, caseName, incidentId, options, res, noteText = null;

	try{
		//Instantiate new ResilientHelper
		resHelper = new ResilientHelper();
		
		//Get the required parameters to create a Task
		record = current;
		snRecordId = record.getValue("number");
		caseName = "SN: " + record.getValue("short_description") + " [" + snRecordId + "]";
		incidentId = workflow.variables.u_ibm_resilient_incident_id;
		
		//Initialize options
		options = {
			initSnNote: "Sent to IBM Resilient",
			incidentId: incidentId,
			optionalFields: {
				"instr_text": record.getValue("description")
			}
		};
			
		// Call helper to create the Incident in Resilient
		res = resHelper.create(record, snRecordId, caseName, options);
		
		if (res){
			// Create the RES Note
			noteText = "<br>This " + res.res_reference_type + " has been sent from <b>ServiceNow</b>";
			noteText += "<br><b>ServiceNow ID:</b> " + snRecordId;
			noteText += '<br><b>ServiceNow Link:</b> <a href="'+res.snLink+'">'+res.snLink+'</a></div>';
			resHelper.addNote(res.res_reference_id, noteText, "html");
		}
	}
	catch (errMsg){
		gs.error(errMsg);
	}
})();