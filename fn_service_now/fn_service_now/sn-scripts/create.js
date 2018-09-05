// Script that runs for the following endpoint:: 
// https://service-now-host.com/api/x_261673_resilient/api/create

(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {
	
	//Declare CONSTANTS
	var TABLE_NAME_TO_INSERT = 'incident';
	
	//Declare global variables
	var record, response_body = null;
    var req = request.body.data;
	
	//Function that converts miliseconds to a GlideDateTime Object
	function ms_to_glideDateTime(ms){
		var gdt = new GlideDateTime();
		gdt.subtract(gdt.getNumericValue()); // sets the date to 0 
		gdt.add(ms); //Set to ms you want
		return gdt;
	}
	
	//Function that creates and initializes a new GlideRecord
	function new_record(table_name){
		var rec = new GlideRecord(table_name);
		rec.initialize();
		return rec;
	}

	//Function that generates the response body
	function generate_response_body(record){
		return {
			"res_incident_id": req.incident_id,
			"sn_sys_id": record.getValue('sys_id'),
			"sn_id": record.getValue('number'),
			"sn_record_link": record.getLink(false)
		};
	}
	
	//Function to set all common table column fields
	function set_record_values(record, request, type, caller_display_name,
								short_description, description, work_note){
		//Set custom table column fields
		record.setValue("x_261673_resilient_reference_id", request.id);
		record.setValue("x_261673_resilient_type", type);
		record.setValue("x_261673_resilient_reference_link", request.link);
		
		//Set system table column fields
 		record.caller_id.setDisplayValue(caller_display_name);	
		record.short_description = short_description;
		record.description = description;
		
		//If an initial work note is defined, add it
		if(work_note != null){
			record.work_notes = work_note;
		}
		
		return record;
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
		record = new_record(TABLE_NAME_TO_INSERT);
		
		//Set the common values of the record
		record = set_record_values(record, req, 'Task', req.task_creator.name,
								   req.task_name, req.task_instructions, req.sn_init_work_note);
		
		//Set custom optional values for a Task
		if(req.optional_fields.task_due_date != null){
			record.setValue("due_date", ms_to_glideDateTime(req.optional_fields.task_due_date));
		}

		//Insert the record
		record.insert();
		
		//Create the response
		response_body = generate_response_body(record);
		response_body.res_task_id = req.task_id;
	}
	
	//If it is a Resilient Incident
	else if(req.type == 'res_incident'){
		//Initialize a new record
		record = new_record(TABLE_NAME_TO_INSERT);
		
		//Set the common values of the record
		record = set_record_values(record, req, 'Incident', req.incident_creator.name,
								   req.incident_name, req.incident_description,
								   req.sn_init_work_note);
		
		//Set custom required values for an Incident
		record.setValue('severity', req.incident_severity);
		
		//Set custom optional values for an Incident
		//TODO

		//Insert the record
		record.insert();
		
		//Create the response
		response_body = generate_response_body(record);
	}
	
	else{
		response.setError(new sn_ws_err.BadRequestError('The Resilient Type must be defined and valid. Either "res_task" or "res_incident". Current value: ' + req.type));
	}
	
	response.setBody(response_body);
	
// 	See this for creating response object
// 	https://docs.servicenow.com/bundle/kingston-application-development/page/app-store/dev_portal/API_reference/ScriptableServiceResponseBuilder/concept/c_ScriptableServiceResponseBuilder.html
	return response;

})(request, response);