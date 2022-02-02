(function RES_WF_AddWorkNote(){
	
	var resHelper, res_reference_id, noteText = null;
	
	try{
		//Instantiate new ResilientHelper
		resHelper = new ResilientHelper();
	
		//Get resilient_reference_id depending on what Table the record is in
		res_reference_id = resHelper.getResilientReferenceId(current);
		
		//Set noteText to last additional comment added
		noteText = current.work_notes.getJournalEntry(1);
		
		//Add a note in Resilient
		resHelper.addNote(res_reference_id, noteText);
	}
	catch (errMsg){
		current.work_notes = "Failed to add a note in IBM SOAR.\nReason: " + errMsg;
		gs.error(errMsg);
	}
})();