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
			"res_id": req.id,
			"sn_sys_id": record.getValue('sys_id'),
			"sn_ref_id": record.getValue('number'),
			"sn_record_link": record.getLink(false),
			"sn_status": 'New',
			"sn_action": record.getValue('x_261673_resilient_type') + ' Created'
		};
	}
	
	//Function to set all common table column fields
	function set_record_values(record, request, type, caller_display_name,
								short_description, description, work_note){
		//Set custom table column fields
		record.setValue("x_261673_resilient_reference_id", request.id);
		record.setValue("x_261673_resilient_type", type);
		record.setValue("x_261673_resilient_reference_link", request.link);
		record.setValue("x_261673_resilient_track_changes", request.track_changes_in_resilient);
		
		//Set system table column fields
 		record.caller_id.setDisplayValue(caller_display_name);	//Caller has to be a ServiceNow user to display correctly
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
		
		/* IBM Resilient 'Create Task in ServiceNow Request' Payload Example
		{
		  "id": "RES-2131-2254750",
		  "type": "res_task",
		  "link": "https://192.168.57.3/#incidents/2131?task_id=2254750",
		  "sn_init_work_note": "This record was created by Admin User [admin@example.com] using our IBM Resilient Systems IR Platform",
		  "track_changes_in_resilient": true,
		  "incident_id": 2131,
		  "task_id": 2254750,
		  "task_creator": {"name": "Tom Smith", "email": "tomsmith@example.com"},
		  "task_instructions": "Call the local Police to see if any mobile device has been handed in",
		  "task_owner": { "name": "Jane Smith", "email": "janesmith@example.com"},
		  "task_name": "Check with local Police",
		  "extra_info": {
			  "assignment_group": "IT Security",
			  "state": "In Progress"
		  }
	   } */
		
		//Initialize a new record
		record = new_record(TABLE_NAME_TO_INSERT);
		
		//Set the common values of the record
		record = set_record_values(record, req, 'Task', req.task_creator.name,
								   req.task_name, req.task_instructions, req.sn_init_work_note);
		
		//Set extra_info values
		//TODO

		//Insert the record
		record.insert();
		
		//Create the response
		response_body = generate_response_body(record);
		response_body.res_task_id = req.task_id;
	}
	
	//If it is a Resilient Incident
	else if(req.type == 'res_incident'){
		
		/*
		{
		  "id": "RES-2131",
		  "type": "res_incident",
		  "link": "https://192.168.57.3/#incidents/2131",
		  "sn_init_work_note": "This record was created by Admin User [admin@res.com] using our IBM Resilient Systems IR Platform",
		  "track_changes_in_resilient": true,
		  "incident_id": 2131,
		  "incident_creator": { "name": "Angela Valdes", "email": "angela@res.com"},
		  "incident_name": "James lost his laptop bag in Dublin",
		  "incident_description": "James was visiting a client and left his laptop bag in the taxi at the \\nairport in Dublin",
		  "incident_severity": 1,
		  "incident_date_created": 1533809472000,
		  "extra_info": {
			"assignment_group": "IT Security",
			"state": "In Progress"
		  }
		}
		*/
		
		//Initialize a new record
		record = new_record(TABLE_NAME_TO_INSERT);
		
		//Set the common values of the record
		record = set_record_values(record, req, 'Incident', req.incident_creator.name,
								   req.incident_name, req.incident_description,
								   req.sn_init_work_note);
		
		//Set custom required values for an Incident
		record.setValue('severity', req.incident_severity);
		
		//Set extra_info values
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