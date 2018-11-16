//Use to convert JavaScript JSON Object to JSON String and back
var JSON_PARSER = new global.JSON();

var RES_DATATABLE_NAME = "sn_external_ticket_status";

//Function to get Resilient Password so we don't have to set Variable in Memory
function getPassword(){
	return gs.getProperty("x_261673_resilient.ResilientUserPassword");
}

//Function to get the name of the MidServer that has IBMResilientAccess Capabilities and is Running
function getMidServer(){
	var MID_SERVER_TABLE_NAME = "ecc_agent_capability_m2m";
	var MID_SERVER_CAPABILITY = "IBMResilientAccess";
	
	try{
		var gr = new GlideRecord(MID_SERVER_TABLE_NAME);
		gr.addQuery("capability.capability", MID_SERVER_CAPABILITY);
		gr.query();

		while(gr.next()) {
			if(gr.agent.status == "Up") {
				return gr.agent.name;
			 }
		}
	}
	catch (e){
		var errMsg = "Failed to search for/find a MidServer with IBMResilientAccess Capabilities.";
		gs.error(errMsg);
		throw errMsg;
	}

	return null;
}

//Function to execute a RESTMessage. Handles errors. Returns response if successful
function executeRESTMessage(rm){
	var response, status, responseBody = null;
	
	try{
		//Execute RESTMessage, get body and status
		response = rm.execute();
		responseBody = response.getBody();
		status = response.getStatusCode();

		//Parse the body
		if (responseBody){
			responseBody = JSON_PARSER.decode(responseBody);
		}

		//Check for errors
		if(response.haveError()){
			var errMsg = response.getErrorMessage() + " :: " + responseBody.message;
			gs.error(errMsg);
			throw errMsg;
		}
		//Return the response if all good
		else{
			return response;
		}
	}
	catch (e){
		var errMsg = "Failed to execute a RESTMessage to the ResilientAPI. (Status: " + status + ").";
		if(status == 0){ errMsg += " Cannot connect to Resilient. Check connection"; }
		gs.error(errMsg);
		throw e;
	}
}

//Function to parse the JSESSIONID from a cookie
function parseJSESSIONID(cookie){
	//Create Regex and search the cookie for the regex
	var regex = new RegExp('JSESSIONID=[A-Z0-9]+;');
	var jsessionFound = cookie.match(regex);
	
	try{
		//If something was found, try get the JSESSIONID
		if(jsessionFound){
			var str = jsessionFound[0];
			return str.slice(str.indexOf("=") + 1, str.length - 1);
		}
		//else throw an error
		else{
			var errMsg = "No JSESSIONID found in the cookie: " + cookie;
			gs.error(errMsg);
			throw errMsg;
		}		
	}
	//Throw a custom error if anything fails
	catch (e){
		var errMsg = "JSESSIONID could not be parsed from the Cookie recieved from ResilientAPI";
		gs.error(errMsg);
		throw errMsg;
	}	
}

//Function to get the id of an org, handles errors
function getOrgId(orgs, orgName){
	var orgId, errMsg = null;
	
	try{
		//Loop the orgs
		for (var i = 0; i < orgs.length; i++){
			
			//Find org with same name as specified in System Properties
			if (orgs[i].name === orgName){

				orgId = orgs[i].id;

				//If user does not have permission throw error
				if (!orgs[i].enabled){
					errMsg = "Resilient user does not have permission to access org: " + orgName;
					gs.error(errMsg);
					throw errMsg;
				}
				break;
			}
		}
		//If no orgId found, throw error
		if (!orgId){
			errMsg = "Resilient user is not a member of specified org: " + orgName;
			gs.error(errMsg);
			throw errMsg;
		}

		return orgId;
	}

	//Throw a custom error if anything fails
	catch (e){
		var errMsg = "OrgId could not be found for: " + orgName;
		gs.error(errMsg);
		throw errMsg;
	}	
}

//Function to set the Headers of a RESTMessage
function setHeaders(rm, headers){
	for(var h in headers){
		if(headers.hasOwnProperty(h)){
			rm.setRequestHeader(h, headers[h]);
		}
	}
	return rm;
}

var ResilientAPI = Class.create();
ResilientAPI.prototype = {
	type: 'ResilientAPI',
	
		initialize: function() {
		
		var hostName, orgName, userEmail, userPassword = null;
		
		//Ensure all the required System Properties are available before continuing
		try{
			hostName = gs.getProperty("x_261673_resilient.ResilientHost");
			orgName = gs.getProperty("x_261673_resilient.ResilientOrgName");
			userEmail = gs.getProperty("x_261673_resilient.ResilientUserEmail");
			userPassword = gs.getProperty("x_261673_resilient.ResilientUserPassword");
		}
		catch (e){
			var errMsg = "Failed getting Resilient Configuration Properties. Check the System Properties";
			gs.error(errMsg);
			throw errMsg;
		}

		//Set Resilient Configuration Settings
		this.baseURL = "https://" + hostName;
		this.orgName = orgName;
		this.userEmail = userEmail;
		
		//Initialise other class variables that will be set in the connect() method
		this.midServer=null;
		this.XSESSID = null;
		this.csrfToken = null;
		this.JSESSIONID=null;
		this.orgId = null; 
		
		this.connect();
		},
	
	connect: function(){
		
		//Instaniate new REST Message
		var rm = new sn_ws.RESTMessageV2();
		rm.setHttpMethod("post");
		rm.setEndpoint(this.baseURL + "/rest/session");
		rm.setRequestHeader("content-type", "application/json");

		//Set authData for the request
		var authData = { "email": this.userEmail, "password": getPassword() };
		
		//Set Request Body
		var requestBody = JSON_PARSER.encode(authData);
		rm.setRequestBody(requestBody);

		//If this.midServer is null (it may already be set if we are 're-authenticating)
		if(!this.midServer){
			//Check if there is a MidServer with IBMResilientAccess Capabilities
			this.midServer = getMidServer();
		}
		//If its valid, set it
		if (this.midServer){
			rm.setMIDServer(this.midServer);
		}
		
		//Execute and get response
		var response = executeRESTMessage(rm);
		var responseBody = response.getBody();
		
		if (responseBody){
			//Parse the body
			responseBody = JSON_PARSER.decode(responseBody);
					
			//Get csrfToken and JSESSIONID
			this.csrfToken = responseBody.csrf_token;
			var cookie = response.getHeader("Set-Cookie");
			this.JSESSIONID = parseJSESSIONID(cookie);
			
			//Get the orgId
			this.orgId = getOrgId(responseBody.orgs, this.orgName);
		}
		
		else{
			var errMsg = "No body in the response from the ResilientAPI";
			gs.error(errMsg);
			throw errMsg;
		}
	},
	
	request: function(method, endpoint, dataAsJSONobj, headers){
		
		//If headers is null, set to empty object
		if(!headers){ headers = {}; }
		
		var url = this.baseURL + "/rest" + endpoint;
		
		//Instaniate new REST Message
		var rm = new sn_ws.RESTMessageV2();
		
		//If using a midServer, set it
		if (this.midServer){ rm.setMIDServer(this.midServer);}
		
		//Set the method 'get', 'post', 'delete'
		rm.setHttpMethod(method);
		
		//Set the endpoint
		rm.setEndpoint(url);
		
		//Set the headers
		headers["content-type"] = "application/json";
		headers["X-sess-id"] = this.csrfToken;
		headers["Cookie"] = "JSESSIONID=" + this.JSESSIONID + ";";
		rm = setHeaders(rm, headers);
		
		//If data, set the body
		if (dataAsJSONobj){
			rm.setRequestBody(JSON_PARSER.encode(dataAsJSONobj));
		}
		
		//Execute the request
		var response = executeRESTMessage(rm);
		var responseBody = response.getBody();
	
		if(responseBody){
			gs.info("Request Status Code:: " + response.getStatusCode());
			return JSON_PARSER.decode(responseBody);
		}
		else{
			var errMsg = "No body in the response from the ResilientAPI";
			gs.error(errMsg);
			throw errMsg;
		}
	},
	
	disconnect: function(){
		this.request("delete", "/session", {}, null);
	},
	
	createIncident: function(data){
		var method = "post";
		var endpoint = "/orgs/" + this.orgId + "/incidents";
		var headers = {"handle_format": "names"};
		return this.request(method, endpoint, data, headers);
	},
	
	createTask: function(incidentId, data){
		var method = "post";
		var endpoint = "/orgs/" + this.orgId + "/incidents/" + incidentId + "/tasks";
		var headers = null;
		return this.request(method, endpoint, data, headers);
	},
	
	getIncident: function(incidentId){
		var method = "get";
		var endpoint = "/orgs/" + this.orgId + "/incidents/" + incidentId;
		var headers = {"handle_format": "names"};
		return this.request(method, endpoint, null, headers);
	},
	
	closeIncident: function(incidentId, data){
		var method = "patch";
		var endpoint = "/orgs/" + this.orgId + "/incidents/" + incidentId;
		var headers = {"handle_format": "names"};
		return this.request(method, endpoint, data, headers);
	},
	
	getField: function(fieldAPIName, type, isCustomField){
		fieldAPIName = (isCustomField) ? "properties."+fieldAPIName : fieldAPIName;
		var method = "get";
		var endpoint = "/orgs/" + this.orgId + "/types/" + type + "/fields/" + fieldAPIName;
		var headers = {"handle_format": "names"};
		return this.request(method, endpoint, null, headers);
	},
	
	getDatatable: function(incidentId){
		var method = "get";
		var endpoint = "/orgs/" + this.orgId + "/incidents/" + incidentId + "/table_data/" + RES_DATATABLE_NAME;
		var headers = {"handle_format": "names"};
		return this.request(method, endpoint, null, headers);
	},

	addDatatableRow: function(incidentId, formattedCells){
		var method = "post";
		var endpoint = "/orgs/" + this.orgId + "/incidents/" + incidentId + "/table_data/" + RES_DATATABLE_NAME + "/row_data/";
		var headers = {"handle_format": "names"};
		return this.request(method, endpoint, formattedCells, headers);
	},
	
	udpateDatatableRow: function(incidentId, rowId, formattedCells){
		var method = "put";
		var endpoint = "/orgs/" + this.orgId + "/incidents/" + incidentId + "/table_data/" + RES_DATATABLE_NAME + "/row_data/" + rowId;
		var headers = {"handle_format": "names"};
		return this.request(method, endpoint, formattedCells, headers);
	},
	
	addNote: function(incidentId, taskId, noteText){
		var endpoint = null;
		if(taskId){
			endpoint = "/orgs/" + this.orgId + "/tasks/" + taskId + "/comments";
		}
		else{
			endpoint = "/orgs/" + this.orgId + "/incidents/" + incidentId + "/comments";
		}

		var data = {
			"text": {
				"format": "text",
				"content": noteText
			}
		};
		var method = "post";
		return this.request(method, endpoint, data);
	},
	
	generateRESid: function(incident_id, task_id){
		var id = "RES-" + String(incident_id);
		
		if(task_id){
			id += "-" + String(task_id);
		}
		
		return id;
	},
	
	generateRESlink: function(incident_id, task_id){
		var link = this.baseURL + "/#incidents/" + String(incident_id);
		
		if(task_id){
			link += "?task_id=" + String(task_id);
		}
		
		return link;
	}
};