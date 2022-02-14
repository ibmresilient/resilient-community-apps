// (c) Copyright IBM Corp. 2022. All Rights Reserved.

//Use to convert JavaScript JSON Object to JSON String and back
var JSON_PARSER = new global.JSON();

var RES_DATATABLE_NAME = "sn_records_dt";
var RES_INTEGRATOR_ROLE = "x_ibmrt_resilient.integrator";

//Function to get Resilient Password so we don't have to set Variable in Memory
function getPassword(){
	return gs.getProperty("x_ibmrt_resilient.ResilientUserPassword");
}

//Function to get Resilient API Key Secret so we don't have to set Variable in Memory
function getAPISecret(){
	return gs.getProperty("x_ibmrt_resilient.ResilientAPISecret");
}

function validateMidServer(midServerName){
	var errMsg = null;
	var MID_SERVER_TABLE_NAME = "ecc_agent_capability_m2m";

	try{
		
		var gr = new GlideRecord(MID_SERVER_TABLE_NAME);
		gr.addQuery("agent.name", midServerName);
		gr.query();

		while(gr.next()) {
			if(gr.agent.status.toLowerCase() == "up" && gr.agent.validated == "true") {
				gs.debug("Mid-Server '"+midServerName+"' found and is valid.");
				return true;
			}
		}
	}
	catch (e){
		errMsg = "Failed to search for/find a MidServer " + e;
		throw errMsg;
	}

	errMsg = "No Active Mid-Server by the name of " + midServerName + " found that is Validated and Active";
	errMsg += "\nEnsure your Mid-Server is 'Up' and 'Validated'";
	throw errMsg;
}

function checkSnUserHasResilientIntegratorRole(snUsername) {

	//Find the sys_id of the RES_INTEGRATOR_ROLE in the sys_user_role table
	var roleTable = new GlideRecord("sys_user_role");
	roleTable.addQuery("name", RES_INTEGRATOR_ROLE);
	roleTable.query();

	//execute query for ibm integrator role sys_id
	if (roleTable.next()) {
		var sysIdResIntegratorRole = roleTable.sys_id;

		//Here have to query the sys_user_has_role table to know if the
		//user has the appropriate role
		var userRolesTable = new GlideRecord("sys_user_has_role");

		//filter on roles equal to target role
		userRolesTable.addQuery("role", sysIdResIntegratorRole);
		//filter on users with sys_id matching snUsername's id
		userRolesTable.addQuery("user.user_name", snUsername);
		
		userRolesTable.query(); //execute query

		if (userRolesTable.next()) {
			//the query had results - no issue
			return;
		} else {
			throw "ServiceNow Username '" + snUsername + "' does not have the " + RES_INTEGRATOR_ROLE + " role.";
		}
	} else {
		throw "ServiceNow Instance is no correctly configured. Could not find " + RES_INTEGRATOR_ROLE + " role.";
	}
}

//Function to execute a RESTMessage. Handles errors. Returns response if successful
function executeRESTMessage(rm, midServerName, restURL){
	var response, statusCode, responseBody, responseHeaders, errMsg = null;

	//Set timeout to 60s
	rm.setHttpTimeout(60000);

	try{
		response = rm.execute();

		// If using a mid-server, wait max 60s for response
		if(midServerName){
			response.waitForResponse(60);
		}
	}
	catch (e){
		if (e.message.indexOf("No response for ECC message request") !== -1){
			errMsg = "Timed out getting response.";
			if (midServerName){
				errMsg += "\nCheck Mid Server. Login to the machine hosting your '" +midServerName+ "' Mid-Server and ensure you can ping IBM SOAR at " + restURL;
			}
			else{
				errMsg += "\nEnsure you can access and login to IBM SOAR at " + restURL;
			}
		}
		else{
			errMsg = "Failed to execute REST message. Unhandled error. " + e;
		}
		throw errMsg;
	}

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
		errMsg = "SOAR API call FAILED\nStatus Code: " + statusCode + "\nReason: " + responseBody.message;
		throw errMsg;
	}
	else if (response.haveError()){
		var reason = response.getErrorMessage();
		if (reason.toLowerCase().indexOf("unknown host")){
			reason += "\nYour SOAR Host may be incorrect or not accessible.";
			reason += "\nCheck your SOAR Host is up and running.";
			if(midServerName){
				reason += "\nCheck your '" +midServerName+ "' Mid-Server is correctly configured";
			}
		}
		errMsg = "Reason: " + reason;
		throw errMsg;
	}
	else {
		errMsg = "Failed to call SOAR API: Unknown Error";
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
		errMsg = "JSESSIONID could not be parsed from the Cookie received from SOAR API\n" + e;
		throw errMsg;
	}
}

//Function to get the id of an org, handles errors
function getOrgId(orgs, orgName, resilientUser){
	var orgId, errMsg = null;
	
	try{
		//Loop the orgs
		for (var i = 0; i < orgs.length; i++){
			
			//Find org with same name as orgName
			if (orgs[i].name === orgName){

				orgId = orgs[i].id;

				//If user does not have permission throw error
				if (!orgs[i].enabled){
					errMsg = resilientUser + " does not have permission to access the SOAR Organization: " + orgName;
					throw errMsg;
				}
				break;
			}
		}
		//If no orgId found, throw error
		if (!orgId){
			errMsg = resilientUser + " is not a member of specified of the SOAR Organization: " + orgName;
			throw errMsg;
		}

		return orgId;
	}

	//Throw a custom error if anything fails
	catch (e){
		errMsg = "Error trying to find the SOAR Organization: " + orgName + ".\n" + e;
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
		
		var hostName, orgName, resAPIId, resAPISecret, userEmail, userPassword, snUsername, midServerName, errMsg, APIKeysEnabled, restEndpointCP4S = null;
		
		//Ensure all the required System Properties are available before continuing
		try{
			hostName = gs.getProperty("x_ibmrt_resilient.ResilientHost");
			orgName = gs.getProperty("x_ibmrt_resilient.ResilientOrgName");
			resAPIId = gs.getProperty("x_ibmrt_resilient.ResilientAPIId");
			resAPISecret = gs.getProperty("x_ibmrt_resilient.ResilientAPISecret");
			userEmail = gs.getProperty("x_ibmrt_resilient.ResilientUserEmail");
			userPassword = gs.getProperty("x_ibmrt_resilient.ResilientUserPassword");
			snUsername = gs.getProperty("x_ibmrt_resilient.ServiceNowUsername");
			midServerName = gs.getProperty("x_ibmrt_resilient.ServiceNowMidServerName");
			restEndpointCP4S = gs.getProperty("x_ibmrt_resilient.ResilientCP4SRestHost");
			if (gs.getProperty("x_ibmrt_resilient.ResilientIsCP4S").toLowerCase() == "yes") {
				this.isCP4S = true;
			} else {
				this.isCP4S = false;
			}
		}
		catch (e){
			errMsg = "Failed getting SOAR Configuration Properties. Check your Properties for IBM SOAR\n" + e;
			throw errMsg;
		}

		errMsg = " property cannot be null. Please update your IBM SOAR Properties";
		if (!hostName) {throw "SOAR Host" + errMsg;}
		if (!orgName) {throw "SOAR Organization" + errMsg;}
		if (!snUsername) {throw "ServiceNow Username" + errMsg;}
		if (this.isCP4S && !restEndpointCP4S) {throw "CP4S URL" + errMsg;}

		//Check that either the API Key details or the email/pass details are present
		//One of the two sets must be provided
		if (!resAPIId || !resAPISecret) {
			errMsgStart = "API Key details are missing. ";
			errMsgEnd = " is required if not authenticating with API Key. Please update your IBM SOAR Properties";

			if (!userEmail) {throw errMsgStart + "SOAR Email" + errMsgEnd;}
			if (!userPassword) {throw errMsgStart + "SOAR Password" + errMsgEnd;}

			APIKeysEnabled = false;
		} else {
			APIKeysEnabled = true;
		}

		//Check snUsername's permissions - will throw appropriate error if
		//snUsername doesn't have RES_INTEGRATOR_ROLE role or if can't find the role
		checkSnUserHasResilientIntegratorRole(snUsername);

		//Setup MID Server
		midServerName = midServerName.trim();
		if (midServerName.length == 0){
			midServerName = null;
		}
		this.midServerName = midServerName;

		//Set Resilient Configuration Settings
		if (this.isCP4S) {
			this.restURL = "https://" + restEndpointCP4S;
		} else {
			this.restURL = "https://" + hostName;
		}
		this.baseURL = "https://" + hostName;
		this.resAPIId = resAPIId;
		this.orgName = orgName;
		this.userEmail = userEmail;
		this.APIKeysEnabled = APIKeysEnabled;

		//Initialise other class variables that will be set in the connect() method
		this.XSESSID = null;
		this.csrfToken = null;
		this.JSESSIONID = null;
		this.orgId = null;

		try{
			this.connect();
		}
		catch (e){
			errMsg = "Failed to connect to IBM SOAR Host at " + this.restURL + ".\n" + e;
			throw errMsg;
		}
	},
	
	connect: function(){
		
		var rm, authData, requestBody, res = null;

		//Instantiate new REST Message
		rm = new sn_ws.RESTMessageV2();

		//Set authData for the request
		//If not using API key, set the email/pass and that will
		//be used to get a JSESSIONID and csrfToken. If using API key, 
		//that info is provided to each request
		if (!this.APIKeysEnabled) {
			authData = { "email": this.userEmail, "password": getPassword() };
		
			//Set Request Body
			requestBody = JSON_PARSER.encode(authData);

			rm.setHttpMethod("post");
			rm.setRequestBody(requestBody);
		} else {
			//Auth with API key uses GET on session rather than POST
			//and provides the API key details in a header
			rm.setHttpMethod("get");
			rm.setBasicAuth(this.resAPIId, getAPISecret());
		}

		rm.setEndpoint(this.restURL + "/rest/session");
		rm.setRequestHeader("content-type", "application/json");

		//If a mid server has been specified, check it is up and validated, then set it in the RESTMessage
		if (this.midServerName){
			validateMidServer(this.midServerName); //will throw an error if not valid
			rm.setMIDServer(this.midServerName);
			rm.setEccParameter("skip_sensor", true);
		}

		//Execute and get response
		res = executeRESTMessage(rm, this.midServerName, this.restURL);

		//Get csrfToken and JSESSIONID if authenticating with email
		if (!this.APIKeysEnabled) {
			this.csrfToken = res.body.csrf_token;
			this.JSESSIONID = parseJSESSIONID(res.headers["Set-Cookie"]);
		}

		//Get the orgId
		this.orgId = getOrgId(res.body.orgs, this.orgName);
	},
	
	request: function(method, endpoint, dataAsJSONobj, headers){
		
		//If headers is null, set to empty object
		if(!headers){ headers = {}; }
		
		var url = this.restURL + "/rest" + endpoint;
		
		//Instantiate new REST Message
		var rm = new sn_ws.RESTMessageV2();
		
		//If using a midServer, set it
		if (this.midServerName){ 
			validateMidServer(this.midServerName); //will throw an error if not valid
			rm.setMIDServer(this.midServerName);
			rm.setEccParameter("skip_sensor", true);
		}
		
		//Set the method 'get', 'post', 'delete'
		rm.setHttpMethod(method);
		
		//Set the endpoint
		rm.setEndpoint(url);
		
		//Set the headers
		headers["content-type"] = "application/json";

		//Figure out how authentication will happen
		//If using API key, set the ID and secret in header
		//otherwise use session info that was retrieved
		//using email/pass when connect() was called in init
		if (this.APIKeysEnabled) {
			rm.setBasicAuth(this.resAPIId, getAPISecret());
		} else {
			headers["X-sess-id"] = this.csrfToken;
			headers["Cookie"] = "JSESSIONID=" + this.JSESSIONID + ";";
		}

		rm = setHeaders(rm, headers);
		
		//If data, set the body
		if (dataAsJSONobj){
			rm.setRequestBody(JSON_PARSER.encode(dataAsJSONobj));
		}
		
		//Execute the request
		var res = executeRESTMessage(rm, this.midServerName, this.restURL);
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
		var link = null;
		if (this.isCP4S){
			link = this.baseURL + "/app/respond/#cases/" + String(incident_id);
		} else {
			link = this.baseURL + "/#incidents/" + String(incident_id);
		}
		
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