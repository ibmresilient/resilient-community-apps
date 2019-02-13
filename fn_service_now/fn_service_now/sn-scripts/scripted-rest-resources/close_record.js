// (c) Copyright IBM Corp. 2019. All Rights Reserved.

// Script that runs for the following endpoint:: 
// https://service-now-host.com/api/x_261673_resilient/api/close_record

(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {
	
	//Declare global variables
	var record = null;
	var req = request.body.data;
	
	//Function that generates the response body
	function generate_response_body(record){
		return {
			"sn_ref_id": req.sn_ref_id,
			"sn_state": record.state.getChoiceValue()
		};
	}
	
	record = new GlideRecord(req.sn_table_name);

	//Get the record using sn_ref_id
	record.addQuery("number", req.sn_ref_id);
	record.query();
	record.next();

	//Only update if the sn_record_state is different to the records current state
	if(req.sn_record_state != record.state){
		
		//Set the attributes required to close a record
		record.close_notes = req.sn_close_notes;
		record.close_code = req.sn_close_code;
		record.state = req.sn_record_state;

		//If a close work note is defined, add it
		if(req.sn_close_work_note != null){
			record.work_notes = req.sn_close_work_note;
		}

		//Update the record
		record.update();
		
		//Set the response body
		response.setBody(generate_response_body(record));

		return response;
	
	}
	else{
		err_msg = req.sn_ref_id + " state is already " + record.state + ". Cannot update the record.";
		return new sn_ws_err.BadRequestError(err_msg);
	}

})(request, response);