// (c) Copyright IBM Corp. 2019. All Rights Reserved.

// Script that runs for the following endpoint:: 
// https://service-now-host.com/api/x_ibmrt_resilient/api/get_sys_id

(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {

	var snowHelper, params, tableName, record, errMsg = null;

	//Instantiate new SNOWRESTHelper
	snowHelper = new SNOWRESTHelper();

	//Get the params from the request
	params = request.queryParams;

	//Get the tableName
	tableName = params.sn_table_name;

	//If the table is allowed to be accessed, continue
	if(snowHelper.tableIsAllowed(tableName)){
		record = new GlideRecord(tableName);
		record.addQuery(params.sn_query_field, params.sn_query_value);
		record.query();
		record.next();
	
		response.setBody({
			"sys_id": record.getValue("sys_id")
		});

		return response;
	}
	//Else return an error
	else{
		errMsg = "Do not have permission to access the table '"+tableName+"'. It needs to be included in the ServiceNowAllowedTables CSV list.";
		return new sn_ws_err.BadRequestError(errMsg);
	}

})(request, response);