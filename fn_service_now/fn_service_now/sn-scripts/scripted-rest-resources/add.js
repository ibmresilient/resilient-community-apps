// (c) Copyright IBM Corp. 2019. All Rights Reserved.

// Script that runs for the following endpoint:: 
// https://service-now-host.com/api/x_ibmrt_resilient/api/add

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

	//Switch on the type: "comment", "attachment" or "artifact"
	switch(req.type){
		case "comment":
			var note_type = req.sn_note_type;
			var note_text = req.sn_note_text;
			if(note_type == "work_note"){
				record.work_notes = note_text;
			}
			else if(note_type == "additional_comment"){
				record.comments = note_text;
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