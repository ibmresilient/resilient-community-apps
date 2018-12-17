(function RES_WF_AddComment(){
	try{
		var res_helper = new ResilientHelper();
	
		var res_ref_id = current.getValue("x_261673_resilient_reference_id");
		var noteText = current.comments.getJournalEntry(1);
		
		res_helper.addNote(res_ref_id, noteText);
	}
	catch (errMsg){
		gs.error(errMsg);
	}
})();