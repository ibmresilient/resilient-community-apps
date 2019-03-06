// (c) Copyright IBM Corp. 2019. All Rights Reserved.

// Script that runs for the following endpoint:: 
// https://service-now-host.com/api/x_ibmrt_resilient/api/update


(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {
	
	//Declare global variables
	var record, field, fields = null;
	var response_body = {};
	var req = request.body.data;
	
	record = new GlideRecord(req.sn_table_name);

	//Get the record using sn_ref_id
	record.addQuery("number", req.sn_ref_id);
	record.query();
	record.next();

	// If record not found, respond with error
	if(!record.isValid()){
		response.setError(new sn_ws_err.BadRequestError("Could not find a ServiceNow Record with Number: " + req.sn_ref_id + " in table: " + req.sn_table_name));
		return response;
	}

	fields = req.sn_update_fields;

	for (var i=0; i<fields.length; i++){
		field = fields[i];
		if(record.isValidField(field.name)){
			record[field.name] = field.value;
			record.setValue(field.name, field.value);
		}
		else{
			gs.warning(field.name + " is not a valid field in the " + sn_table_name + " table!");
		}
	}

	//Update the record
	record.update();
	
	response_body["sn_ref_id"] = req.sn_ref_id;
	
	response.setBody(response_body);
	
	return response;

})(request, response);
