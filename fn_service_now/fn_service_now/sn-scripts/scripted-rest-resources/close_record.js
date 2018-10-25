// Script that runs for the following endpoint:: 
// https://service-now-host.com/api/x_261673_resilient/api/close_record

(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {
	
	//Declare global variables
	var record = null;
	var response_body = {};
    var req = request.body.data;
	
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
		
		//Update the record
		record.update();
		
		response_body["sn_ref_id"] = req.sn_ref_id;
		response.setBody(response_body);
	
	}
	else{
		err_msg = req.sn_ref_id + " state is already " + record.state + ". Cannot update the record.";
		return new sn_ws_err.BadRequestError(err_msg);
	}

	return response;

})(request, response);