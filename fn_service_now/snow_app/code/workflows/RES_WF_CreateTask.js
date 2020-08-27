(function RES_WF_CreateTask(){
	
	var resHelper, record, snRecordId, caseName, incidentId, options, res, noteText, workNotes, workNotesSplit = null;

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
			initSnNote: "Task created in IBM Resilient",
			incidentId: incidentId,
			optionalFields: {
				"instr_text": record.getValue("description")
			}
		};
			
		// Call helper to create the Incident in Resilient
		res = resHelper.create(record, snRecordId, caseName, options);
		
		if (res){
			// Create the initial RES Note
			noteText = "<br>This " + res.res_reference_type + " has been sent from <b>ServiceNow</b>";
			noteText += "<br><b>ServiceNow ID:</b> " + snRecordId;
			noteText += '<br><b>ServiceNow Link:</b> <a href="'+res.snLink+'">'+res.snLink+'</a></div>';
			resHelper.addNote(res.res_reference_id, noteText, "html");
			
			// Get all Work Notes. Returns as a string where each entry is delimited by '\n\n'
			workNotes = current.work_notes.getJournalEntry(-1);

			//Split the Work Notes on '\n\n'
			workNotesSplit = workNotes.split("\n\n");

			//Loop each Work Note and add a Resilient Note
			for (var i = 0; i < workNotesSplit.length; i++){
				noteText = workNotesSplit[i];
				if(noteText && noteText.length > 0){
					resHelper.addNote(res.res_reference_id, workNotesSplit[i]);
				}
			}
		}
	}
	catch (errMsg){
		current.work_notes = "Failed to create a Task in IBM Resilient for Incident "+incidentId+".\nReason: " + errMsg;
		gs.error(errMsg);
	}
})();