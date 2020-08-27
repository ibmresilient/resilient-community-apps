// (c) Copyright IBM Corp. 2019. All Rights Reserved.

(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {
	
	//Declare global variables
	var snowHelper, params, tableName, record, responseBody, errMsg= null;
	
	//Instantiate new SNOWRESTHelper
	snowHelper = new SNOWRESTHelper();

	//Get the params from the request (because its a POST we use request body)
	params = request.body.data;

	//Get the tableName
	tableName = params.sn_table_name;

	//Function that creates and initializes a new GlideRecord
	function newRecord(tableName){
		var rec = new GlideRecord(tableName);
		rec.initialize();
		return rec;
	}

	//Function that generates the response body
	function generateResponseBody(record){
		return {
			"res_id": params.id,
			"sn_sys_id": record.getValue('sys_id'),
			"sn_ref_id": record.getValue('number'),
			"sn_state": record.state.getChoiceValue()
		};
	}
	
	//Function to set all common table column fields
	function setRecordRequiredFields(record, params, type, short_description, description){
		//Set custom table column fields
		record.setValue("x_ibmrt_resilient_ibm_resilient_reference_id", params.id);
		record.setValue("x_ibmrt_resilient_ibm_resilient_type", type);
		record.setValue("x_ibmrt_resilient_ibm_resilient_reference_link", params.link);
		
		//Set system table column fields
		record.short_description = short_description;
		record.description = description;
		
		//If an initial work note is defined, add it
		if(params.sn_init_work_note != null){
			record.work_notes = params.sn_init_work_note;
		}
		
		return record;
	}

	//Function that sets the optional_fields of the record
	function setRecordOptionalFields(record, fields, tableName){
		for (var i=0; i<fields.length; i++){
			var field = fields[i];
			if(record.isValidField(field.name)){
				record[field.name] = field.value;
				record.setValue(field.name, field.value);
			}
			else{
				gs.warning(field.name + " is not a valid field in the " + tableName + " table!");
			}
		}
	}
	
	//If the table is allowed to be accessed, continue
	if(snowHelper.tableIsAllowed(tableName)){
		//Initialize a new record
		record = newRecord(tableName);
		
		//Create a ServiceNow record in if it is a Resilient Task
		if(params.type == 'res_task'){	
			//Set the required fields of the record
			record = setRecordRequiredFields(record, params, 'Task', params.task_name, params.task_instructions);
		}
		else if (params.type == 'res_incident'){
			//Set the required fields of the record
			record = setRecordRequiredFields(record, params, 'Incident', params.incident_name, params.incident_description);
		}
		else {
			errMsg = 'The Resilient Type must be defined and valid. Either "res_task" or "res_incident". Current value: ' + params.type;
			return new sn_ws_err.BadRequestError(errMsg);
		}
		
		//Set the optional_fields that the user defines in the Resilient pre-process script
		if(params.sn_optional_fields){
			setRecordOptionalFields(record, params.sn_optional_fields, tableName);
		}

		//Insert the record
		record.insert();

		//Create the response body
		responseBody = generateResponseBody(record);
		response.setBody(responseBody);
		
		return response;
	}
	//Else return an error
	else{
		errMsg = "Do not have permission to access the table '"+tableName+"'. It needs to be included in the ServiceNowAllowedTables CSV list.";
		return new sn_ws_err.BadRequestError(errMsg);
	}

})(request, response);
