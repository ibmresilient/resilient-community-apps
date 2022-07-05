// (c) Copyright IBM Corp. 2022. All Rights Reserved.

var SIR_RES_ID = "x_ibmrt_resilient_ibm_soar_reference_id";
var INC_RES_ID = "x_ibmrt_resilient_ibm_resilient_reference_id";

var SN_SI_INCIDENT_TABLE_NAME = "sn_si_incident";
var SN_SI_TASK_TABLE_NAME = "sn_si_task";

/////////////////////////////////////
// Business Rule Condition Helpers //
/////////////////////////////////////

//
//SIR TABLES
//

function isSirTable(current, snowHelper) {
	return snowHelper.tableIsAllowed(current.getTableName()) && !current.isValidField(INC_RES_ID) && current.isValidField(SIR_RES_ID);
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
	return current.getValue(SIR_RES_ID) != null;
}

var ScriptConditionsHelper = Class.create();
ScriptConditionsHelper.prototype = {
	type: 'ScriptConditionsHelper',

	initialize: function() {
		this.snowHelper = new SNOWRESTHelper();
	},

	uiCreateIncidentCheck: function(current) {
		return isSirTable(current, this.snowHelper) && !sirIsLinkedToRes(current);
	},

	uiCreateTaskCheck: function(current) {
		return isSirTable(current, this.snowHelper) && !sirIsLinkedToRes(current);
	},

	sirAddCommentCheck: function(current) {
		return isSirTable(current, this.snowHelper) && sirIsLinkedToRes(current);
	},

	sirAddWorkNoteCheck: function(current) {
		return isSirTable(current, this.snowHelper) && sirIsLinkedToRes(current);
	},

	sirUpdateStateCheck: function(current) {
		return isSirTable(current, this.snowHelper) && sirIsLinkedToRes(current);
	},

	sirCreateOnAssignCheck: function(current) {
		var condition = isSirTable(current, this.snowHelper) && !sirIsLinkedToRes(current) && isSnSiIncidentTable(current);

		if (!condition) {
			return condition;
		}

		var resHelper = new ResilientHelper();
		var checkGroupAllowed = resHelper.assignGroupIsAllowed(current.getDisplayValue("assignment_group").trim().toLowerCase());

		return condition && checkGroupAllowed;
	},

	sitCreateOnAssignCheck: function(current) {
		var condition = isSirTable(current, this.snowHelper) && !sirIsLinkedToRes(current) && isSnSiTaskTable(current);

		if (!condition) {
			return condition;
		}

		var resHelper = new ResilientHelper();
		var checkGroupAllowed = resHelper.assignGroupIsAllowed(current.getDisplayValue("assignment_group").trim().toLowerCase());

		return condition && checkGroupAllowed;
	}

};
