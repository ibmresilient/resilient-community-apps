(function RES_WF_AddWorkNote(){
	try{
		var res_helper = new ResilientHelper();
	
		var res_ref_id = current.getValue("x_261673_resilient_reference_id");
		var noteText = current.work_notes.getJournalEntry(1);
		
		res_helper.addNote(res_ref_id, noteText);
	}
	catch (errMsg){
		gs.error(errMsg);
	}
})();