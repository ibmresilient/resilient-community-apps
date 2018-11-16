(function resilientCreateTaskRunScript(){
	
	//Instantiate new helper
	var resHelper = new ResilientHelper();
	
	//Get the required info to createTask
	var record = current;
	var snRecordId = record.getValue("number");
	var incidentId = workflow.variables.u_ibm_resilient_incident_id;
	var taskName = "SN-[" + snRecordId + "]: " + record.getValue("short_description");
	var initSnNote = "Sent to IBM Resilient";
	
	//Set any optional fields
	var optionalFields = {};
		
	resHelper.createTask(record,
						  snRecordId,
						  incidentId,
						  taskName,
						  initSnNote,
						  optionalFields);
})();