(function RES_WF_UpdateState(){
	
	var resHelper, stateToColorMap, res_reference_id, snTicketState, snTicketStateColor, resolutionNotes = null;

	try{
		//Instantiate new resHelper
		resHelper = new ResilientHelper();
		
		//Map ServiceNow state to a color
		//Colors accepted by resHelper.updateStateInResilient() = green/orange/yellow/red
		stateToColorMap = {
			"New": "green",
			"In Progress": "orange",
			"On Hold": "yellow",
			"Resolved": "red",
			"Closed": "red",
			"Canceled": "red"
		};
		
		//Get the required values
		res_reference_id = current.getValue("x_ibmrt_resilient_ibm_resilient_reference_id");
		snTicketState = current.state.getChoiceValue();
		snTicketStateColor = stateToColorMap[snTicketState];
		
		//Update that status in the res datatable
		resHelper.updateStateInResilient(res_reference_id, snTicketState, snTicketStateColor);
		
		//Get resolution notes if there are any
		resolutionNotes = current.getValue("close_notes");
		
		//Add a note to the resilient incident/task if there are resolution notes
		if(resolutionNotes){
			resHelper.addNote(res_reference_id, resolutionNotes);
		}
	}
	catch(errMsg){
		current.work_notes = "Failed to update state in IBM Resilient.\nReason: " + errMsg;
		gs.error(errMsg);
	}
})();