(function resilientCreateIncidentRunScript(){
	var res_helper = new ResilientHelper();
	
	//Do some mapping, pass current and extra info to createIncident
	var res_init_note = "This was created by ServiceNow";
	
	var res_optional_fields = {};
	
	res_helper.createIncident(current, res_init_note, res_optional_fields);
})();