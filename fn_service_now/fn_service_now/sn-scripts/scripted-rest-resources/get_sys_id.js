// Script that runs for the following endpoint:: 
// https://service-now-host.com/api/x_261673_resilient/api/get_sys_id

(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {

	var response_body = {};
  var query_params = request.queryParams;
		
	var record = new GlideRecord(query_params.sn_table_name);

	record.addQuery(query_params.sn_query_field, query_params.sn_query_value);
	record.query();
	record.next();
	response_body["sys_id"] = record.getValue("sys_id");

	response.setBody(response_body);
	
	return response;

})(request, response);