(function resilientCreateIncidentRunScript(){
	//Instantiate new helper
	var resHelper = new ResilientHelper();
	
	//Get the required info to createIncident
	var record = current;
	var snRecordId = record.getValue("number");
	var incidentName = "SN-[" + snRecordId + "]: " + record.getValue("short_description");
	var initSnNote = "Sent to IBM Resilient";
	
	//Map ServiceNow severity in digits to Resilient strings
	//TIP: use the 'finfo' command on Resilient Integrations Server
	//to get Resilient field information
	var resSeverityMap = {
		"1": "High",
		"2": "Medium",
		"3": "Low"
	};

	//Set any optional fields
	var optionalFields = {
		"severity_code": resSeverityMap[record.getValue("severity").toString()]
	};
		
	// Call helper to create the Incident in Resilient
	resHelper.createIncident(record,
							snRecordId,
							incidentName,
							initSnNote,
							optionalFields);
})();