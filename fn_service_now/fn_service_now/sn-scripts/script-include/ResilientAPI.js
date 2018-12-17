//Use to convert JavaScript JSON Object to JSON String and back
var JSON_PARSER = new global.JSON();

var RES_DATATABLE_NAME = "sn_external_ticket_status";

//Function to get Resilient Password so we don't have to set Variable in Memory
function getPassword(){
	return gs.getProperty("x_261673_resilient.ResilientUserPassword");
}

//Function to get the name of the MidServer that has IBMResilientAccess Capabilities and is Running
function getMidServer(){
	var errMsg = null;
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
		errMsg = "Failed to search for/find a MidServer " + e;
		throw errMsg;
	}

	errMsg = "No Active Mid-Server with " + MID_SERVER_CAPABILITY + " Capabilities found.";
	errMsg += "\nEnsure your Mid-Server is 'Up' and has " + MID_SERVER_CAPABILITY + "Capabilities";
	throw errMsg;
}

//Function to execute a RESTMessage. Handles errors. Returns response if successful
function executeRESTMessage(rm){
	var response, statusCode, responseBody, responseHeaders, errMsg = null;
		response = rm.execute();
		statusCode = response.getStatusCode();
		
		if(statusCode == 200){
			responseBody = JSON_PARSER.decode(response.getBody());
			responseHeaders = response.getHeaders();
			return {
				body: responseBody,
				headers: responseHeaders
			};
		}
		else if (statusCode >= 400){
			responseBody = JSON_PARSER.decode(response.getBody());
			errMsg = "Resilient API call FAILED\nStatus Code: " + statusCode + "\nReason: " + responseBody.message;
			throw errMsg;
		}
		else if (response.haveError()){
			var reason = response.getErrorMessage();
			if (reason.toLowerCase().indexOf("unknown host")){
				reason += "\n(Hint: Your Resilient Host may be incorrect or not accessible.";
				reason += "\nCheck your Resilient Host is correct and Mid-Server is correctly configured)";
			}
			errMsg = "Reason: " + reason;
			throw errMsg;
		}
		else {
			errMsg = "Failed to call Resilient API: Unknown Error";
			throw errMsg;
		}
}

//Function to parse the JSESSIONID from a cookie
function parseJSESSIONID(cookie){
	var errMsg = null;

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
			errMsg = "No JSESSIONID found in the cookie: " + cookie;
			throw errMsg;
		}		
	}
	//Throw a custom error if anything fails
	catch (e){
		errMsg = "JSESSIONID could not be parsed from the Cookie received from ResilientAPI\n" + e;
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
					throw errMsg;
				}
				break;
			}
		}
		//If no orgId found, throw error
		if (!orgId){
			errMsg = "Resilient user is not a member of specified org: " + orgName;
			throw errMsg;
		}

		return orgId;
	}

	//Throw a custom error if anything fails
	catch (e){
		errMsg = "OrgId could not be found for: " + orgName + "\nReason: " + e;
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
		
		var hostName, orgName, userEmail, userPassword, usingMidServer, errMsg = null;
		
		//Ensure all the required System Properties are available before continuing
		try{
			hostName = gs.getProperty("x_261673_resilient.ResilientHost");
			orgName = gs.getProperty("x_261673_resilient.ResilientOrgName");
			userEmail = gs.getProperty("x_261673_resilient.ResilientUserEmail");
			userPassword = gs.getProperty("x_261673_resilient.ResilientUserPassword");
			usingMidServer = gs.getProperty("x_261673_resilient.UseMidServer");
		}
		catch (e){
			errMsg = "Failed getting Resilient Configuration Properties. Check the System Properties\n" + e;
			throw errMsg;
		}

		if (!hostName) {throw "Resilient Host cannot be null";}
		if (!orgName) {throw "Resilient Organization cannot be null";}
		if (!userEmail) {throw "Resilient Email Address cannot be null";}
		if (!userPassword) {throw "Resilient Password cannot be null";}

		//Set Resilient Configuration Settings
		this.baseURL = "https://" + hostName;
		this.orgName = orgName;
		this.userEmail = userEmail;
		this.usingMidServer = usingMidServer;

		//Initialise other class variables that will be set in the connect() method
		this.midServerName = null;
		this.XSESSID = null;
		this.csrfToken = null;
		this.JSESSIONID = null;
		this.orgId = null;
		
		try{
			this.connect();
		}
		catch (e){
			errMsg = "Failed to connect to Resilient\n" + e;
			throw errMsg;
		}
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

		// If we're using a Mid-Server, get its name
		if(!this.midServerName && this.usingMidServer){
			//Check if there is an Active Mid-Server with IBMResilientAccess Capabilities
			this.midServerName = getMidServer();
		}
		//If its valid, set it
		if (this.midServerName){
			rm.setMIDServer(this.midServerName);
		}
		
		//Execute and get response
		var res = executeRESTMessage(rm);
		
		//Get csrfToken and JSESSIONID
		this.csrfToken = res.body.csrf_token;
		this.JSESSIONID = parseJSESSIONID(res.headers["Set-Cookie"]);
		
		//Get the orgId
		this.orgId = getOrgId(res.body.orgs, this.orgName);
	},
	
	request: function(method, endpoint, dataAsJSONobj, headers){
		
		//If headers is null, set to empty object
		if(!headers){ headers = {}; }
		
		var url = this.baseURL + "/rest" + endpoint;
		
		//Instaniate new REST Message
		var rm = new sn_ws.RESTMessageV2();
		
		//If using a midServer, set it
		if (this.midServerName){ rm.setMIDServer(this.midServerName);}
		
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
		var res = executeRESTMessage(rm);
		return res.body;
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
	
	addNote: function(incidentId, taskId, noteText, noteFormat){
		var endpoint = null;
		if(taskId){
			endpoint = "/orgs/" + this.orgId + "/tasks/" + taskId + "/comments";
		}
		else{
			endpoint = "/orgs/" + this.orgId + "/incidents/" + incidentId + "/comments";
		}

		if (!noteFormat){
			noteFormat = "text";
		}

		var data = {
			"text": {
				"format": noteFormat,
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
	},

	generateSNlink: function(record){
		var snLink = record.getLink();
		var instanceName = gs.getProperty("instance_name");
		return "https://" + instanceName + ".service-now.com/" + snLink;
	}
};