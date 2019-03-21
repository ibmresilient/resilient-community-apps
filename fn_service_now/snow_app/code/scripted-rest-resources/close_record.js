// (c) Copyright IBM Corp. 2019. All Rights Reserved.

// Script that runs for the following endpoint:: 
// https://service-now-host.com/api/x_ibmrt_resilient/api/close_record

(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {

	//Declare global variables
	var snowHelper, params, tableName, record, responseBody, errMsg = null;

	//Function that generates the response body
	function generateResponseBody(record){
		return {
			"sn_ref_id": params.sn_ref_id,
			"sn_state": record.state.getChoiceValue()
		};
	}

	//Instantiate new SNOWRESTHelper
	snowHelper = new SNOWRESTHelper();

	//Get the params from the request (because its a POST we use request body)
	params = request.body.data;

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

		//Only update if the sn_record_state is different to the records current state
		if(params.sn_record_state != record.state){
			
			//Set the attributes required to close a record
			record.close_notes = params.sn_close_notes;
			record.close_code = params.sn_close_code;
			record.state = params.sn_record_state;

			//If a close work_note is defined, add it
			if(params.sn_close_work_note != null){
				record.work_notes = params.sn_close_work_note;
			}

			//Update the record
			record.update();
			
			//Set and return the response
			response.setBody(generateResponseBody(record));
			return response;

		}
		else{
			errMsg = params.sn_ref_id + " state is already " + record.state + ". Cannot update the record.";
			return new sn_ws_err.BadRequestError(errMsg);
		}
	}
	else{
		errMsg = "Do not have permission to access the table '"+tableName+"'. It needs to be included in the ServiceNowAllowedTables CSV list.";
		return new sn_ws_err.BadRequestError(errMsg);
	}

})(request, response);