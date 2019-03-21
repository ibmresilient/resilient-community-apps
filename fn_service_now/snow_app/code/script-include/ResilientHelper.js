// (c) Copyright IBM Corp. 2019. All Rights Reserved.

var JSON_PARSER = new global.JSON();

var ResilientHelper = Class.create();
ResilientHelper.prototype = {
	type: 'ResilientHelper',
	
	initialize: function() {
		this.res_api = new ResilientAPI();
	},
	
	parseRefId: function(res_reference_id){
		var incidentId, taskId = null;
		var ids = res_reference_id.split("-");

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
			errMsg = "ResilientHelper.create(): 'snRecordId' parameter must be a defined String object";
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

		// Generate the snLink for the Resilient Data Table Entry
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

			// Check if custom field object, properties has been defined in optionalFields
			if (!caseData.properties){
				caseData.properties = {};
			}

			// Set our two required custom fields
			caseData.properties["sn_snow_record_link"] = "<a href='"+snLink+"'>Link</a>";
			caseData.properties["sn_snow_record_id"] = snRecordId;

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
			//Get record name
			var record_name = record.getValue("short_description");

			//Set required values on SN record
			record.setValue("x_ibmrt_resilient_ibm_resilient_reference_id", res_reference_id);
			record.setValue("x_ibmrt_resilient_ibm_resilient_type", res_reference_type);
			record.setValue("x_ibmrt_resilient_ibm_resilient_reference_link", res_reference_link);

			//If user specifies initial ServiceNow note, add it
			if(initSnNote){
				record.work_notes = initSnNote;
			}

			//Add a new row to the Resilient Data Table
			this.addNewRowToRESDatatable(record_name, res_reference_type, res_reference_id, snRecordId, res_reference_link, snLink);

			returnValue = {
				res_reference_id: res_reference_id,
				res_reference_link: res_reference_link,
				res_reference_type: res_reference_type,
				snLink: snLink
			};
		}

		return returnValue;
	},

	addNewRowToRESDatatable: function(record_name, res_type, res_reference_id, sn_ref_id, res_link, sn_link){
		var colors = {
			"green": "#00b33c",
			"orange": "#ff9900",
			"yellow": "#e6e600",
			"red": "#e60000"
		};

		try{
				var ids = this.parseRefId(res_reference_id);
				var gdt = new GlideDateTime();
				var now = gdt.getNumericValue();

				var links = '<a target="_blank" href="'+res_link+'">RES</a> <a href="'+sn_link+'">SN</a>';

				var resTicketStateRichText = '<div style="color:' + colors["green"] +'">Active</div>';
				var snTicketStateRichText = '<div style="color:' + colors["green"] +'">Sent to Resilient</div>';

				var cells = [
					["sn_records_dt_time", now],
					["sn_records_dt_name", record_name],
					["sn_records_dt_type", res_type],
					["sn_records_dt_res_id", res_reference_id],
					["sn_records_dt_sn_ref_id", sn_ref_id],
					["sn_records_dt_res_status", resTicketStateRichText],
					["sn_records_dt_snow_status", snTicketStateRichText],
					["sn_records_dt_links", links]
				];

				var formattedCells = {};
				
				for (var j=0; j<cells.length; j++){
					formattedCells[cells[j][0]] = {"value": cells[j][1]};
				}
				formattedCells = {"cells": formattedCells};
				
				this.res_api.addDatatableRow(ids.incidentId, formattedCells);
			}
		catch(e){
			var errMsg = "Failed to send add row in Resilient Datatable for " + res_reference_id;
			gs.error(errMsg);
			throw e;
		}
	},
	
	updateStateInResilient: function(res_reference_id, snTicketState, snTicketStateColor){
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
			var ids = this.parseRefId(res_reference_id);

			var dt = this.res_api.getDatatable(ids.incidentId);
			var rows = dt.rows;
			var rowToUpdate = null;
			
			for (var i=0; i<rows.length; i++){
				if(rows[i].cells.sn_records_dt_res_id.value == res_reference_id){
					rowToUpdate = rows[i];
					break;
				}
			}
			
			if (rowToUpdate == null){
				throw "Could not find row in Resilient Datatable for " + res_reference_id;
			}

			else{
				var rowId = rowToUpdate.id;
				var gdt = new GlideDateTime();
				var now = gdt.getNumericValue();

				var snTicketStateRichText = '<div style="color:' + colors[snTicketStateColor] +'">' + snTicketState + '</div>';

				var cells = [
					["sn_records_dt_time", now],
					["sn_records_dt_name", rowToUpdate.cells.sn_records_dt_name.value],
					["sn_records_dt_type", rowToUpdate.cells.sn_records_dt_type.value],
					["sn_records_dt_res_id", rowToUpdate.cells.sn_records_dt_res_id.value],
					["sn_records_dt_sn_ref_id", rowToUpdate.cells.sn_records_dt_sn_ref_id.value],
					["sn_records_dt_res_status", rowToUpdate.cells.sn_records_dt_res_status.value],
					["sn_records_dt_snow_status", snTicketStateRichText],
					["sn_records_dt_links", rowToUpdate.cells.sn_records_dt_links.value]
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
			var errMsg = "Failed to update SNOW Status column in data table in Resilient to " + snTicketState;
			gs.error(errMsg);
			throw e;
		}
	},
	
	addNote: function(res_reference_id, noteText, noteFormat){
		try{
			if(!noteFormat){
				noteFormat = "text";
			}
			var ids = this.parseRefId(res_reference_id);
			this.res_api.addNote(ids.incidentId, ids.taskId, noteText, noteFormat);
		}

		catch(e){
			var errMsg = "Failed to send note to IBM Resilient";
			gs.error(errMsg);
			throw e;
		}
	}
};