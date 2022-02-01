// (c) Copyright IBM Corp. 2022. All Rights Reserved.

var SIR_RES_ID = "x_ibmrt_resilient_ibm_soar_reference_id";
var INC_RES_ID = "x_ibmrt_resilient_ibm_resilient_reference_id";
var SN_RES_USERNAME = "x_ibmrt_resilient.ServiceNowUsername";

var SN_SI_INCIDENT_TABLE_NAME = "sn_si_incident";
var SN_SI_TASK_TABLE_NAME = "sn_si_task";

/////////////////////////////////////
// Business Rule Condition Helpers //
/////////////////////////////////////

function checkUser() {
	//Global user check
	return gs.getProperty(SN_RES_USERNAME) != gs.getUserName() && gs.getUserName() != "system";
}

//
//INC TABLES
//

function isIncidentTable(current) {
	//Only incident tables have this field
	return current.isValidField(INC_RES_ID);
}

function incIsNotLinkedToRes(current) {
	//Check if the current INC record is NOT already linked to Resilient
	//NOTE: this should be run *after* calling "isIncidentTable"
	return current.isValidField(INC_RES_ID) && current.getValue(INC_RES_ID) != null;
}

//
//SIR TABLES
//

function isSirTable(current) {
	//Check that the current table doesn't have the ..._resilient_... column
	//i.e. a general check for sn_si... related tables.
	//See the isSnSi... functions for more specific checks
	return !current.isValidField(INC_RES_ID);
}

function isSnSiIncidentTable(current) {
	//Check specifically if this is sn_si_incident table
	return current.getTableName() == SN_SI_INCIDENT_TABLE_NAME;
}

function isSnSiTaskTable(current) {
	//Check specifically if this is sn_si_task table
	return current.getTableName() == SN_SI_TASK_TABLE_NAME;
}

function sirIsLinkedToRes(current) {
	//Check if the current SIR record IS already linked to Resilient
	//NOTE: this should be run *after* calling "isSirTable"
	return current.isValidField(SIR_RES_ID) && current.getValue(SIR_RES_ID) != null;
}

function sirIsNotLinkedToRes(current) {
	//Check if the current SIR record is NOT already linked to Resilient
	//NOTE: this should be run *after* calling "isSirTable"
	return current.isValidField(SIR_RES_ID) && current.getValue(SIR_RES_ID) == null;
}

var ScriptConditionsHelper = Class.create();
ScriptConditionsHelper.prototype = {
	type: 'ScriptConditionsHelper',

	initialize: function() {},

	sirAddCommentCheck: function(current) {
		return isSirTable(current) && sirIsLinkedToRes(current) && checkUser();
	},

	sirAddWorkNoteCheck: function(current) {
		return isSirTable(current) && sirIsLinkedToRes(current) && checkUser();
	},

	sirUpdateStateCheck: function(current) {
		return isSirTable(current) && sirIsLinkedToRes(current) && checkUser();
	},

	sirCreateOnAssignCheck: function(current) {
		var condition = isSirTable(current) && sirIsNotLinkedToRes(current) && isSnSiIncidentTable(current) && checkUser();

		var resHelper = new ResilientHelper();
		var checkGroupAllowed = resHelper.assignGroupIsAllowed(current.getDisplayValue("assignment_group").trim().toLowerCase());

		return condition && checkGroupAllowed;
	},

	sitCreateonAssignCheck: function(current) {
		var condition = isSirTable(current) && sirIsNotLinkedToRes(current) && isSnSiTaskTable(current) && checkUser();

		var resHelper = new ResilientHelper();
		var checkGroupAllowed = resHelper.assignGroupIsAllowed(current.getDisplayValue("assignment_group").trim().toLowerCase());

		return condition && checkGroupAllowed;
	}

};
