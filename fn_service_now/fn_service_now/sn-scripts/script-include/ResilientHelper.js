var ResilientHelper = Class.create();
ResilientHelper.prototype = {
	type: 'ResilientHelper',
	
	initialize: function() {
		try{
			this.res_api = new ResilientAPI();
		}
		catch (e){
			throw (e);
		}
    },
	
	createIncident: function(record, res_init_note, res_optional_fields){
		try{
			
			// Set required fields
			var recordNumber = record.getValue("number");
			var recordNamePrefix = "SN-[" + recordNumber + "]: ";
			var recordName = recordNamePrefix + record.getValue("short_description");
			
			var gdt = new GlideDateTime();
			var discovered_date = gdt.getNumericValue();
			
			var incData = {
				"name": recordName,
				"discovered_date": discovered_date
			};

			//If an initial note is defined, add it to incData as a comment
			if(res_init_note){
				incData["comments"] = [{"text":{"format": "text", "content": res_init_note}}];
			}
			
			var inc = this.res_api.createIncident(incData);

			record.setValue("x_261673_resilient_reference_id", this.res_api.generateRESid(inc.id));
			record.setValue("x_261673_resilient_type", "Incident");
			record.setValue("x_261673_resilient_reference_link", this.res_api.generateRESlink(inc.id));
			
			record.work_notes = "Sent to IBM Resilient";
			
			record.update();
		}
		catch(e){
			var errMsg = "Failed to Create the Incident in IBM Resilient";
			gs.error(errMsg);
			throw e;
		}
	},
	
	addNote: function(res_ref_id, noteText){
		try{
			var incidentId, taskId = null;
			var ids = res_ref_id.split("-");

			//RES-1234-56789
			incidentId = ids[1];
			if(ids.length == 3){
				taskId = ids[2];
			}
			
			this.res_api.addNote(incidentId, taskId, noteText);
		}

		catch(e){
			var errMsg = "Failed to send note to IBM Resilient";
			gs.error(errMsg);
			throw e;
		}
	}
};