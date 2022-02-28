// (c) Copyright IBM Corp. 2022. All Rights Reserved.

var INC_RES_ID = "x_ibmrt_resilient_ibm_resilient_reference_id";
var SIR_RES_ID = "x_ibmrt_resilient_ibm_soar_reference_id";
var TABLE_NAME_INC = "incident";
var TABLE_NAME_SIR = "sn_si_incident";

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
	
	gs.debug("Table Names found: " + tableNamesArray);

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

		var tableNamesArray, validTableFound, i, t, gr, errMsg = null;

		gs.debug("Validating x_ibmrt_resilient.ServiceNowAllowedTables");
		
		// Get array of allowed table names
		tableNamesArray = getAllowedTables();

		// Bool to track if TABLE_NAME_INC or TABLE_NAME_SIR is included in the list
		validTableFound = false;

		// For loop to check each table name is a valid table
		for(i = 0; i < tableNamesArray.length; i++){

			t = tableNamesArray[i];

			if (t == TABLE_NAME_INC || t == TABLE_NAME_SIR){
				validTableFound = true;
			}

			gs.debug("Validating " + t);

			gr = new GlideRecord(t);

			if(!gr.isValid()){
				errMsg = "'" + t + "' is not a valid Table in this ServiceNow Instance";
				throw errMsg;
			}

			gs.debug(t + " is valid");

		}

		if (!validTableFound){
			throw "The table '" + TABLE_NAME_INC +"' and/or '" + TABLE_NAME_SIR +"' must be included in the ServiceNowAllowedTables CSV list";
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
	},

	getResReferenceIdFromTaskParent: function(current, parentTableName){

		var parent, refID = null;

		//Get the task's parent record so we can grab the res ID
		//to properly link this new task with the resilient incident
		parent = new GlideRecord(parentTableName);
		parent.get(current.getValue("parent"));

		//Return the value stored in the parent table, if found
		if (parent.isValidField(INC_RES_ID)){
			refID = parent.getValue(INC_RES_ID);
		}
		else{
			refID = parent.getValue(SIR_RES_ID);
		}

		if (!refID){
			gs.warn("Task's parent SOAR Reference ID not found for Task: '" + current.getValue("number") + "'");
		}

		return refID;
	}
};