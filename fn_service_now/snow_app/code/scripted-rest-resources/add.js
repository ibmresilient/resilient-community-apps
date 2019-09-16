// (c) Copyright IBM Corp. 2019. All Rights Reserved.

// Script that runs for the following endpoint:: 
// https://service-now-host.com/api/x_ibmrt_resilient/api/add

(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {

	//Declare global variables
	var snowHelper, params, tableName, record, responseBody, errMsg = null;
	
	//Instantiate new SNOWRESTHelper
	snowHelper = new SNOWRESTHelper();

	//Get the params from the request (because its a POST we use request body)
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

		//Switch on the type: "comment" or "attachment"
		switch(params.type){
			//Add a work_note or additional_comment
			case "comment":
				var note_type = params.sn_note_type;
				var note_text = params.sn_note_text;
				if(note_type == "work_note"){
					record.work_notes = note_text;
				}
				else if(note_type == "additional_comment"){
					record.comments = note_text;
				}
				break;
			
			//Add an attachment
			case "attachment":
				var sys_attachment = new GlideSysAttachment();
				responseBody["attachment_id"] = sys_attachment.writeBase64(record, params.attachment_name, params.attachment_content_type, params.attachment_base64);
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