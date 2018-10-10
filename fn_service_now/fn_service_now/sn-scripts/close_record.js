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

	//Set note why its resolved and set the state to closed 
	//[this number is defined in Resilient as changes client to client]
	record.close_notes = req.sn_close_notes;
	record.close_code = req.sn_close_code;
	record.state = req.sn_record_state;
	
	//Update the record
	record.update();
	
	response_body["sn_ref_id"] = req.sn_ref_id;
	
	response.setBody(response_body);
	
	return response;

})(request, response);