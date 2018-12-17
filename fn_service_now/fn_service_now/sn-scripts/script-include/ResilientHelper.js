var JSON_PARSER = new global.JSON();

var ResilientHelper = Class.create();
ResilientHelper.prototype = {
	type: 'ResilientHelper',
	
	initialize: function() {
			this.res_api = new ResilientAPI();
	},
	
	parseRefId: function(res_ref_id){
		var incidentId, taskId = null;
		var ids = res_ref_id.split("-");

		//RES-1234-56789
		incidentId = ids[1];
		if(ids.length == 3){
			taskId = ids[2];
		}
		
		return {"incidentId": incidentId, "taskId": taskId};
	},
	
	create: function(record, snRecordId, caseName, options){
		var caseData = {};
		var snLink, res, res_reference_id, res_reference_type, res_reference_link, returnValue, errMsg = null;
		var VALID_OPTIONS = ["incidentId", "initSnNote", "optionalFields"];

		//Validate required parameters
		if(!record || record instanceof GlideRecord == false){
			errMsg = "ResilientHelper.create(): 'record' parameter must be a GlideRecord object";
			throw errMsg;
		}

		if(!snRecordId || typeof snRecordId !== "string"){
			errMsg = "ResilientHelper.create(): 'snRecord' parameter must be a defined String object";
			throw errMsg;
		}

		if(!caseName || typeof caseName !== "string"){
			errMsg = "ResilientHelper.create(): 'caseName' parameter must be a defined String object";
			throw errMsg;
		}

		//Validate options
		if(options){
			for (var optionName in options){
				if (options.hasOwnProperty(optionName) && VALID_OPTIONS.indexOf(optionName) == -1) {
					errMsg = "Invalid option for ResilientHelper.create()";
					errMsg += "\n" + optionName + " is an invalid option";
					errMsg += "\n Valid options are: " + VALID_OPTIONS.join(","); 
					throw errMsg;
				}
			}
		}

		//Get vars in options
		var incidentId = options["incidentId"];
		var initSnNote = options["initSnNote"];
		var optionalFields = options["optionalFields"];

		//Set name of the incident/task
		caseData["name"] = caseName;

		//Handle optional fields
		if(optionalFields){
			for (var fieldName in optionalFields){
				if (optionalFields.hasOwnProperty(fieldName)) {
					var fieldValue = optionalFields[fieldName];
					caseData[fieldName] = fieldValue;
				}
			}
		}

		// Generate the snLink for the Resilient Datatable Entry
		snLink = this.res_api.generateSNlink(record);

		//If no incidentId, we are creating an Incident
		if (!incidentId){

			//Set the type
			res_reference_type = "Incident";

			//Get discoveredDate
			var gdt = new GlideDateTime();
			var discoveredDate = gdt.getNumericValue();

			//Set the discovered_date, which is mandatory to create an incident
			caseData["discovered_date"] = discoveredDate;

			//Create the incident and get response
			res = this.res_api.createIncident(caseData);

			//Get res_reference_id and link
			res_reference_id = this.res_api.generateRESid(res.id);
			res_reference_link = this.res_api.generateRESlink(res.id);
		}
		//Else we are creating a Task on the given incidentId
		else{
			//Set the type
			res_reference_type = "Task";

			//Create the task
			res = this.res_api.createTask(incidentId, caseData);
			
			//Get res_reference_id and link
			res_reference_id = this.res_api.generateRESid(incidentId, res.id);
			res_reference_link = this.res_api.generateRESlink(incidentId, res.id);
		}

		if(res){
			//Set required values on SN record
			record.setValue("x_261673_resilient_reference_id", res_reference_id);
			record.setValue("x_261673_resilient_type", res_reference_type);
			record.setValue("x_261673_resilient_reference_link", res_reference_link);

			//If user specifies initial ServiceNow note, add it
			if(initSnNote){
				record.work_notes = initSnNote;
			}

			//Add a new row to the Resilient Datatable
			this.addNewRowToRESDatatable(res_reference_id, snRecordId, res_reference_link, snLink);

			returnValue = {
				res_reference_id: res_reference_id,
				res_reference_link: res_reference_link,
				res_reference_type: res_reference_type,
				snLink: snLink
			}
		}

		return returnValue;
	},

	formatChange: function(type, field){

		var returnValue = {
			"field": field.api_name,
			"new_value": {},
			"old_value": {}
		};
		
		switch (type){
			case "textarea":
				var format = (field.rich_text) ? "html" : "text";
				
				//resolution_summary has unique format if null
				if (field.api_name == "resolution_summary" && field.old_value == null){
					returnValue.old_value = {"textarea":field.old_value};
					returnValue.new_value = {"textarea":{"format":format,"content":field.new_value}};
				}
				else{
					returnValue.old_value = {"textarea":{"format": format,"content":field.old_value}};
					returnValue.new_value = {"textarea":{"format": format,"content":field.new_value}};
				}
				break;
				
			case "text":
				returnValue.old_value = {"text": field.old_value};
				returnValue.new_value = {"text": field.new_value};
				break;

			case "number":
				returnValue.old_value = {"object": field.old_value};
				returnValue.new_value = {"object": field.new_value};
				break;

			case "boolean":
				returnValue.old_value = {"boolean": field.old_value};
				returnValue.new_value = {"boolean": field.new_value};
				break;
			
			case "multiselect":
				returnValue.old_value = {"ids": field.old_value};
				returnValue.new_value = {"ids": field.new_value};
				break;
			
			case "select":
				returnValue.old_value = {"id": field.old_value};
				returnValue.new_value = {"id": field.new_value};
				break;

			case "datetimepicker":
			case "datepicker":
				returnValue.old_value = {"date": field.old_value};
				returnValue.new_value = {"date": field.new_value};
				break;
		}
		
		return returnValue;
	},
	
	close: function(record, roc_fields){
		var res_ref_id = record.getValue("x_261673_resilient_reference_id");
		var errMsg = null;
		var resTicket = null;
		var resTicketType = null;
		var fieldsToUpdate = {};
		var requestData = [];

		//Get and parse the resilient_reference_ids [RES-incidentId-taskId]
		var ids = this.parseRefId(res_ref_id);
				
		if(ids.taskId){
			try{
				resTicket = this.res_api.getTask(ids.taskId);
				resTicketType = "task";
			}
			catch (e){
				errMsg = "Could not retrieve Task from Resilient: " + ids.taskId;
				gs.error(errMsg);
				throw e;
			}
		}
		else{
			try{
				resTicket = this.res_api.getIncident(ids.incidentId);
				resTicketType = "incident";
			}
			catch (e){
				errMsg = "Could not retrieve Incident from Resilient: " + ids.incidentId;
				gs.error(errMsg);
				throw e;
			}
		}

		//Loop the supplied roc_fields
		for (var name in roc_fields) {
			if (roc_fields.hasOwnProperty(name)) {
				var fieldValue = roc_fields[name];
				
				//Extend the fieldsToUpdate obj with this field
				fieldsToUpdate[name] = {
					"field": name,
					"old_value": null,
					"new_value": fieldValue,
					"is_custom_field": false
				};

				//Get its old_value if it is a default field
				if(resTicket.hasOwnProperty(name)){
					fieldsToUpdate[name].old_value = resTicket[name];
				}
				//Get its old_value if it is a custom field
				else if(resTicket["properties"].hasOwnProperty(name)){
					fieldsToUpdate[name].old_value = resTicket["properties"][name];
					fieldsToUpdate[name].is_custom_field = true;
				}
				else{
					errMsg = name + " could not be found as a required-on-close field";
					gs.error(errMsg);
					throw errMsg;
				}
			}
		}
		
		//Loop fieldsToUpdate
		for (var fieldName in fieldsToUpdate) {
		
			if (fieldsToUpdate.hasOwnProperty(fieldName)) {
			
				var change = fieldsToUpdate[fieldName];
				var res = null;

				try{
					//Get the field info from resilient. Need field_type and field_rich_text values
					res = this.res_api.getField(change.field, resTicketType, change.is_custom_field);
				}
		
				catch(e){
					errMsg = "Failed get Resilient Field Information for " + fieldName;
					gs.error(errMsg);
					throw e;
				}
				
				var field = {
					"api_name": fieldName,
					"old_value": fieldsToUpdate[fieldName].old_value,
					"new_value": fieldsToUpdate[fieldName].new_value,
					"rich_text": res.rich_text
				};

				//format the change, depending on its type
				requestData.push(this.formatChange(res.input_type, field));
			}
		}

		//Push the required plan_status to the requestData
		var plan_status = {
			"api_name": "plan_status",
			"old_value": "A",
			"new_value": "C"
		};
		
		requestData.push(this.formatChange("text", plan_status));
		
		if(ids.taskId){
// 			resTicket = this.res_api.getTask(ids.taskId);
// 			resTicketType = "task";
		}
		else{
			try{
				//TODO:: if error code is 400 and message contains: "The following fields are required",
				//Show dialog error outlining what inputs are missing
				this.res_api.closeIncident(ids.incidentId, {"changes": requestData});
			}
			catch(e){
				errMsg = "Failed to close the Resilient " + resTicketType + ": " + res_ref_id;
				gs.error(errMsg);
				throw e;
			}
		}
	},
	
	addNewRowToRESDatatable: function(res_ref_id, sn_ref_id, res_link, sn_link){
		var colors = {
			"green": "#00b33c",
			"orange": "#ff9900",
			"yellow": "#e6e600",
			"red": "#e60000"
		};

		try{
				var ids = this.parseRefId(res_ref_id);
				var gdt = new GlideDateTime();
				var now = gdt.getNumericValue();

				var links = '<a target="_blank" href="'+res_link+'">RES</a> <a href="'+sn_link+'">SN</a>';

				var resTicketStateRichText = '<div style="color:' + colors["green"] +'">Active</div>';
				var snTicketStateRichText = '<div style="color:' + colors["green"] +'">Sent to Resilient</div>';

				var cells = [
					["time", now],
					["res_id", res_ref_id],
					["sn_ref_id", sn_ref_id],
					["resilient_status", resTicketStateRichText],
					["servicenow_status", snTicketStateRichText],
					["link", links]
				];
				
				var formattedCells = {};
				
				for (var j=0; j<cells.length; j++){
					formattedCells[cells[j][0]] = {"value": cells[j][1]};
				}
				formattedCells = {"cells": formattedCells};
				
				this.res_api.addDatatableRow(ids.incidentId, formattedCells);
			}
		catch(e){
			var errMsg = "Failed to send add row in Resilient Datatable for " + res_ref_id;
			gs.error(errMsg);
			throw e;
		}
	},
	
	updateStateInResilient: function(res_ref_id, snTicketState, snTicketStateColor){
		var colors = {
			"green": "#00b33c",
			"orange": "#ff9900",
			"yellow": "#e6e600",
			"red": "#e60000"
		};

		if (!snTicketStateColor){
			snTicketStateColor = "green";
		}

		try{
			var ids = this.parseRefId(res_ref_id);

			var dt = this.res_api.getDatatable(ids.incidentId);
			var rows = dt.rows;
			var rowToUpdate = null;
			
			for (var i=0; i<rows.length; i++){
				if(rows[i].cells.res_id.value == res_ref_id){
					rowToUpdate = rows[i];
					break;
				}
			}
			
			if (rowToUpdate == null){
				throw "Could not find row in Resilient Datatable for " + res_ref_id;
			}

			else{
				var rowId = rowToUpdate.id;
				var gdt = new GlideDateTime();
				var now = gdt.getNumericValue();

				var snTicketStateRichText = '<div style="color:' + colors[snTicketStateColor] +'">' + snTicketState + '</div>';

				var cells = [
					["time", now],
					["res_id", rowToUpdate.cells.res_id.value],
					["sn_ref_id", rowToUpdate.cells.sn_ref_id.value],
					["resilient_status", rowToUpdate.cells.resilient_status.value],
					["servicenow_status", snTicketStateRichText],
					["link", rowToUpdate.cells.link.value]
				];
				
				var formattedCells = {};
				
				for (var j=0; j<cells.length; j++){
					formattedCells[cells[j][0]] = {"value": cells[j][1]};
				}
				formattedCells = {"cells": formattedCells};

				this.res_api.udpateDatatableRow(ids.incidentId, rowId, formattedCells);
			}
		}
		catch(e){
			var errMsg = "Failed to send updateStateInResilient to " + snTicketState;
			gs.error(errMsg);
			throw e;
		}
	},
	
	addNote: function(res_ref_id, noteText, noteFormat){
		try{
			if(!noteFormat){
				noteFormat = "text";
			}
			var ids = this.parseRefId(res_ref_id);
			this.res_api.addNote(ids.incidentId, ids.taskId, noteText, noteFormat);
		}

		catch(e){
			var errMsg = "Failed to send note to IBM Resilient";
			gs.error(errMsg);
			throw e;
		}
	}
};