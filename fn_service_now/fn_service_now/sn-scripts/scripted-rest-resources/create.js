(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {
	
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
			"sn_action": record.getValue('x_261673_resilient_type') + ' Created'
		};
	}
	
	//Function to set all common table column fields
	function set_record_required_fields(record, request, type, short_description, description){
		//Set custom table column fields
		record.setValue("x_261673_resilient_reference_id", request.id);
		record.setValue("x_261673_resilient_type", type);
		record.setValue("x_261673_resilient_reference_link", request.link);
		//record.setValue("x_261673_resilient_track_changes", request.track_changes_in_resilient);
		
		//Set system table column fields
		record.short_description = short_description;
		record.description = description;
		
		//If an initial work note is defined, add it
		if(request.sn_init_work_note != null){
			record.work_notes = request.sn_init_work_note;
		}
		
		return record;
	}

	//Function that sets the optional_fields of the record
	function set_record_optional_fields(record, fields){
		for (var i=0; i<fields.length; i++){
			var field = fields[i];
			if(record.isValidField(field.name)){
				record[field.name] = field.value;
				record.setValue(field.name, field.value);
			}
		}
	}
	
	//Create a ServiceNow record in if it is a Resilient Task
	if(req.type == 'res_task'){	
				
		//Initialize a new record
		record = new_record(req.sn_table_name);
		
		//Set the required fields of the record
		record = set_record_required_fields(record, req, 'Task', req.task_name, req.task_instructions);
		
		//Set the optional_fields that the user defines in the Resilient pre-process script
		if(req.sn_optional_fields){
			set_record_optional_fields(record, req.sn_optional_fields);
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
		record = new_record(req.sn_table_name);
				
		//Set the required fields of the record
		record = set_record_required_fields(record, req, 'Incident', req.incident_name, req.incident_description);
		
		//Set the optional_fields that the user defines in the Resilient pre-process script
		if(req.sn_optional_fields){
			set_record_optional_fields(record, req.sn_optional_fields);
		}
		
		//Insert the record
		record.insert();
		
		//Create the response
		response_body = generate_response_body(record);
	}
	
	else{
		response.setError(new sn_ws_err.BadRequestError('The Resilient Type must be defined and valid. Either "res_task" or "res_incident". Current value: ' + req.type));
	}
	
	response.setBody(response_body);
	
	return response;

})(request, response);

