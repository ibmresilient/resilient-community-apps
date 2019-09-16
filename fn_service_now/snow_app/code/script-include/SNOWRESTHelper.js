// (c) Copyright IBM Corp. 2019. All Rights Reserved.

function getAllowedTables(){
	
	var tableNamesCSV, tableNamesArray, i, errMsg = null;
	
	// Get the ServiceNowAllowedTables system property
	try{
		tableNamesCSV = gs.getProperty("x_ibmrt_resilient.ServiceNowAllowedTables");
	}
	catch (e){
		errMsg = "Failed getting x_ibmrt_resilient.ServiceNowAllowedTables Property.\n" + e;
		throw errMsg;
	}
	
	if (!tableNamesCSV) {
		throw "ServiceNowAllowedTables property cannot be null. It must be a comma separated list of ServiceNow Table Names";
	}

	try{
		// Split them on comma
		tableNamesArray = tableNamesCSV.split(",");

		// Trim whitespace off each table name
		for(i = 0; i < tableNamesArray.length; i++){
			tableNamesArray[i] = tableNamesArray[i].trim();
		}
	}
	catch (e){
		errMsg = "Error parsing x_ibmrt_resilient.ServiceNowAllowedTables. Ensure in correct CSV format.\n" + e;
		throw errMsg;
	}

	return tableNamesArray;
}

var SNOWRESTHelper = Class.create();
SNOWRESTHelper.prototype = {
	type: 'SNOWRESTHelper',

	initialize: function() {

	},

	isValidSnUsername: function(snUsername){
		var gr = new GlideRecord("sys_user");

		gr.addQuery("user_name", snUsername);
		gr.query();

		if(gr.next()){
			return true;
		}
		else{
			return false;
		}
	},

	allowedTablesAreValid: function() {

		var tableNamesArray, incidentTableFound, i, t, gr, errMsg = null;

		gs.debug("Validating x_ibmrt_resilient.ServiceNowAllowedTables");
		
		// Get array of allowed table names
		tableNamesArray = getAllowedTables();

		gs.debug("tableNames array " + tableNamesArray);

		// Bool to track if incident table is included in the list
		incidentTableFound = false;

		// For loop to check each table name is a valid table
		for(i = 0; i < tableNamesArray.length; i++){

			t = tableNamesArray[i];

			if (t == "incident"){
				incidentTableFound = true;
			}

			gs.debug("Validating " + t);

			gr = new GlideRecord(t);

			if(!gr.isValid()){
				errMsg = "'" + t + "' is not a valid Table in this ServiceNow Instance";
				throw errMsg;
			}

			gs.debug(t + " is valid");

		}

		if (!incidentTableFound){
			throw "The table 'incident' must be included in the ServiceNowAllowedTables CSV list";
		}

		gs.debug("x_ibmrt_resilient.ServiceNowAllowedTables are all valid");

		return true;
	},

	tableIsAllowed: function(tableName){

		var allowedTables, i = null;

		allowedTables = getAllowedTables();
	
		for(i = 0; i < allowedTables.length; i++){
			if(allowedTables[i] == tableName){
				return true;
			}
		}

		gs.debug("'"+tableName+"' is not in the ServiceNowAllowedTables CSV list");

		return false;
	}
};