// Script that runs for the following endpoint:: 
// https://service-now-host.com/api/x_261673_resilient/api/add

(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {
	
	//Declare CONSTANTS
	var TABLE_NAME_TO_ADD = 'incident';
	
	//Declare global variables
	var record = null;
	var response_body = {};
    var req = request.body.data;
	
	record = new GlideRecord(TABLE_NAME_TO_ADD);

	//Get the record using sn_ref_id
	record.addQuery("number", req.sn_ref_id);
	record.query();
	record.next();

	//Switch on the type: "comment", "attachment" or "artifact"
	switch(req.type){
		case "comment":
			var comment_type = req.sn_comment_type;
			var comment_text = req.sn_comment_text;
			if(comment_type == "work_note"){
				record.work_notes = comment_text;
			}
			else if(comment_type == "additional_comment"){
				record.comments = comment_text;
			}
			break;
		
		case "attachment":
			var sys_attachment = new GlideSysAttachment();
			response_body["attachment_id"] = sys_attachment.writeBase64(record, req.attachment_name, req.attachment_content_type, req.attachment_base64);
	}

	//Update the record
	record.update();
	
	response_body["sn_ref_id"] = req.sn_ref_id;
	
	response.setBody(response_body);
	return response;

})(request, response);