(function resilientUpdateStateWorkflow(){
	try{
		//Instantiate new resHelper
		var resHelper = new ResilientHelper();
		
		//A map of the ServiceNow record state to a related color
		var stateToColorMap = {
			"New": "green",
			"In Progress": "orange",
			"On Hold": "yellow",
			"Resolved": "red",
			"Closed": "red",
			"Canceled": "red"
		};
		
		//Get the required values
		var res_ref_id = current.getValue("x_261673_resilient_reference_id");
		var snTicketState = current.state.getChoiceValue();
		var snTicketStateColor = stateToColorMap[snTicketState];
		
		//Update that status in the res datatable
		resHelper.updateStateInResilient(res_ref_id, snTicketState, snTicketStateColor);
		
		//Get resolution notes if there are any
		var resolutionNotes = current.getValue("close_notes");
		
		//Add a note to the resilient incident/task if there are resolution notes
		if(resolutionNotes){
			resHelper.addNote(res_ref_id, resolutionNotes);
		}
	}
	catch(errMsg){
		gs.error(errMsg);
	}
	
})();