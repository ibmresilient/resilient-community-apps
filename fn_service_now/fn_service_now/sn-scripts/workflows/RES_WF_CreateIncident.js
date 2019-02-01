(function RES_WF_CreateIncident(){
	
	var resHelper, record, snRecordId, caseName, options, resSeverityMap, res, noteText = null;
	
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
			initSnNote: "Sent to IBM Resilient",
			optionalFields: {
				"severity_code": resSeverityMap[record.getValue("severity").toString()]
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
		current.work_notes = "Failed to create in IBM Resilient.\nReason: " + errMsg;
		gs.error(errMsg);
	}
})();