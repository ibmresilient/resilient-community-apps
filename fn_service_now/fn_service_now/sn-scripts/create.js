// Script that runs for the following endpoint:: 
// https://service-now-host.com/api/x_261673_resilient/api/create

(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {
	
	//Declare CONSTANTS
	var TABLE_NAME_TO_INSERT = 'incident';
	
	//Declare variables
	var record = null;
    var req = request.body.data;
	var response_body = {};
	
	//Function that creates and initializes new GlideRecord
	function newRecord(table_name){
		var rec = new GlideRecord(table_name);
		rec.initialize();
		return rec;
	}

	//Create a ServiceNow record in if it is a Resilient Task
	if(req.type == 'res_task'){	
		
		/* IBM Resilient 'Create Task Request' Payload Example
			req = {
				"type": "res_task",
				"id": "RES-1001-2002"
				"link": "https://192.168.0.2/#incidents/1001?task_id=2002"
				"incident_id": 1001,
				"task_id": 2002,
				"task_name": "Change device/application passwords",
				"task_creator": {"name": "John Smith", "email": "johnsmith@example.com"},
				"task_owner": {"name": "Jane Smith", "email": "jamesmith@example.com"},
				"task_date_initiated": 1534932076553,
				"task_instructions": "Immediately change any associated app or device passwords to company directory services.",
				"sn_init_work_note": "This Incident has been created by Resilient Systems user seanmurphy@example.com",
				"optional_fields": {"task_due_date": null}
			} */
		
		//Initialize a new record
		record = newRecord(TABLE_NAME_TO_INSERT);
		
		//Set custom table column fields
		record.setValue("x_261673_resilient_reference_id", req.id);
		record.setValue("x_261673_resilient_type", 'Task');
		record.setValue("x_261673_resilient_reference_link", req.link);
		
		//Set system table column fields
		record.caller_id.setDisplayValue(req.task_creator.name);
		record.short_description = req.task_name;
		record.description = req.task_instructions;
		
		//If an initial work note is defined, add it
		if(req.sn_init_work_note != null){
			record.work_notes = req.sn_init_work_note;
		}
		
		//Insert the record
		record.insert();
		
		//Create the response
		response_body.res_incident_id = req.incident_id;
		response_body.res_task_id = req.task_id;
		response_body.sn_sys_id = record.getValue('sys_id');
		response_body.sn_id = record.getValue('number');
		response_body.sn_record_link = record.getLink(false);
	}
	
	//If it is a Resilient Incident
	else if(req.type == 'res_incident'){
		//Initialize a new record
		record = newRecord(TABLE_NAME_TO_INSERT);
		
		//Set custom table column fields
		record.setValue("x_261673_resilient_reference_id", req.id);
		record.setValue("x_261673_resilient_type", 'Incident');
		record.setValue("x_261673_resilient_reference_link", req.link);
		
		//Set system table column fields
		record.caller_id.setDisplayValue(req.incident_creator.name);
		record.short_description = req.incident_name;
		record.description = req.incident_description;

		//If an initial work note is defined, add it
		if(req.sn_init_work_note != null){
			record.work_notes = req.sn_init_work_note;
		}

		//Insert the record
		record.insert();
		
		//Create the response
		response_body.res_incident_id = req.incident_id;
		response_body.sn_sys_id = record.getValue('sys_id');
		response_body.sn_id = record.getValue('number');
		response_body.sn_record_link = record.getLink(false);
	}
	
	else{
		response.setError(new sn_ws_err.BadRequestError('The Resilient Type must be defined and valid. Either "res_task" or "res_incident". Current value: ' + req.type));
	}
	
	response.setBody(response_body);
	
// 	See this for creating response object
// 	https://docs.servicenow.com/bundle/kingston-application-development/page/app-store/dev_portal/API_reference/ScriptableServiceResponseBuilder/concept/c_ScriptableServiceResponseBuilder.html
	return response;

})(request, response);