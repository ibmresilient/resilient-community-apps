(function RES_WF_AddComment(){
	
	var resHelper, res_reference_id, noteText = null;
	
	try{
		//Instantiate new ResilientHelper
		resHelper = new ResilientHelper();
	
		//Get resilient_reference_id
		//Note the helper method for getting the Resilient Ref ID
		//There are also: getResilientReferenceLink and getResilientType available
		res_reference_id = resHelper.getResilientReferenceId(current);
		
		//Set noteText to last additional comment added
		noteText = current.comments.getJournalEntry(1);
		
		//Add a note in Resilient
		resHelper.addNote(res_reference_id, noteText);
	}
	catch (errMsg){
		current.work_notes = "Failed to add a note in IBM SOAR.\nReason: " + errMsg;
		gs.error(errMsg);
	}
})();