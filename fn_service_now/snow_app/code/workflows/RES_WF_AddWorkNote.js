(function RES_WF_AddWorkNote(){
	
	var resHelper, res_reference_id, noteText = null;
	
	try{
		//Instantiate new ResilientHelper
		resHelper = new ResilientHelper();
	
		//Get resilient_reference_id
		res_reference_id = current.getValue("x_ibmrt_resilient_ibm_resilient_reference_id");
		
		//Set noteText to last additional comment added
		noteText = current.work_notes.getJournalEntry(1);
		
		//Add a note in Resilient
		resHelper.addNote(res_reference_id, noteText);
	}
	catch (errMsg){
		current.work_notes = "Failed to add a note in IBM Resilient.\nReason: " + errMsg;
		gs.error(errMsg);
	}
})();