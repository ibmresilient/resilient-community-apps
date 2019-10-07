// (c) Copyright IBM Corp. 2019. All Rights Reserved.

// Script that runs for the following endpoint:: 
// https://service-now-host.com/api/x_ibmrt_resilient/api/update


(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {
	
	//Declare global variables
	var snowHelper, params, tableName, record, responseBody, i, fields, field, errMsg = null;
	
	//Instantiate new SNOWRESTHelper
	snowHelper = new SNOWRESTHelper();

	//Get the params from the request (because its a PATCH we use request body)
	params = request.body.data;

	//Initialize responseBody to empty object
	responseBody = {};

	//Get the tableName
	tableName = params.sn_table_name;

	//If the table is allowed to be accessed, continue
	if(snowHelper.tableIsAllowed(tableName)){

		//Initialize a new record
		record = new GlideRecord(tableName);

		//Get the record using sn_ref_id
		record.addQuery("number", params.sn_ref_id);
		record.query();
		record.next();

		// If record not found, return an error
		if(!record.isValid()){
			errMsg = "Could not find a ServiceNow Record with Number: " + params.sn_ref_id + " in table: " + tableName;
			return new sn_ws_err.BadRequestError(errMsg);
		}

		//Get the fields to update
		fields = params.sn_update_fields;

		//Loop the fields. Each field has a 'name' and 'value' key
		for (i = 0 ; i < fields.length; i++){
			field = fields[i];

			//If the field is valid, update its value
			if(record.isValidField(field.name)){
				record[field.name] = field.value;
				record.setValue(field.name, field.value);
			}
			else{
				gs.warning(field.name + " is not a valid field in the " + tableName + " table!");
			}
		}

		//Update the record
		record.update();
		
		//Set and return the response
		responseBody["sn_ref_id"] = params.sn_ref_id;	
		response.setBody(responseBody);
		return response;
	}
	else{
		errMsg = "Do not have permission to access the table '"+tableName+"'. It needs to be included in the ServiceNowAllowedTables CSV list.";
		return new sn_ws_err.BadRequestError(errMsg);
	}

})(request, response);
