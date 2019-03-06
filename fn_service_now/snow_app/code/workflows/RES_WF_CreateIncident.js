(function RES_WF_CreateIncident(){
	
	var resHelper, record, snRecordId, caseName, options, resSeverityMap, res, noteText, workNotes, workNotesSplit = null;
	
	try{
		//Instantiate new ResilientHelper
		resHelper = new ResilientHelper();
		
		//Get the required parameters to create an Incident
		record = current;
		snRecordId = record.getValue("number");
		caseName = "SN: " + record.getValue("short_description") + " [" + snRecordId + "]";

		//Map ServiceNow severity in digits to Resilient strings
		//TIP: use the 'finfo' command on Resilient Integrations Server
		//to get Resilient field information
		resSeverityMap = {
			"1": "High",
			"2": "Medium",
			"3": "Low"
		};

		//Initialize options
		options = {
			initSnNote: "Incident created in IBM Resilient",
			optionalFields: {
				"description": record.getValue("description"),
				"severity_code": resSeverityMap[record.getValue("severity").toString()]
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
		current.work_notes = "Failed to create an Incident in IBM Resilient.\nReason: " + errMsg;
		gs.error(errMsg);
	}
})();