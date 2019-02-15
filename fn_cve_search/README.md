#About This Package

This Common Vulnerability Exposures function provides a way to search for vulnerabilities from CVE Database, 
     function offers below mentioned ways to search for vulnerabilities.

* Browse
* Search
* Specific CVE ID
* Last 30 CVE's
* CVE Database Information
 
For More Information see https://www.circl.lu/services/cve-search/

#Prerequisites:

* resilient version 31 or later
* resilient_circuits version 30 or later
    
#Resilient Installation

This package requires that it is installed on a RHEL or CentOS platform and uses the resilient-circuits framework.
Install this package with 'pip', such as:

`pip install fn_cve_search-<version>.tar.gz`

To import the function and example rule and workflows into Resilient, run the following command:

`resilient-circuits customize`

Answer the prompts for the package to import.


To uninstall,

    pip uninstall fn_cve_search
    
#Resilient Configuration
    
Run the following command to generate the cve configuration section in the app.config file:

    resilient-circuits config [-u | -c]     

The following gRPC configuration data is added:
                    
    [fn_cve_search]
    # Flag display maximum CVE Entries on the resilient table
    max_results_display = 50
    # Base URL of Common Vulnerability Exposures Data Base.
    cve_base_url = https://cve.circl.lu/api

    
Edit the [fn_cve_search] properties as follows:
    
   1. max_results_display : Max Vulnerabilities to display on the resilient `CVE searched Data` table from search results.

#Using the CVE Function

There are two functions a) Example: CVE Browse  b) Example: CVE Search

Example CVE Browse : 

   This function can be accessed on the incidents. which offers the capabilities to browse for vendors and products,
    current CVE  data base information.
    
Example: CVE Search : 

   This function can be accessed on the artifacts. which offers the capabilities to search for product & vendor 
    vulnerabilities, search for specific CVE's data, latest vulnerabilities added to databases.
     
Below are details of the input fields and outputs results of the function.

##Function Inputs Fields:
   1. CVE Search Criteria       - Vulnerabilities search options
   2. Vendor                    - Name of the vendor
   3. Product                   - Name of the product
   4. CVE ID                    - Specific vulnerability ID
   5. CVE Published Date From   - Date range to filter searched vulnerability data
   6. CVE Published Date To     - Date range to filter searched vulnerability data
 
 CVE Function offers below search configurations to query vulnerabilities from DB
 
 1. Browse : 
    
    * Select Browse and all other inputs are empty results all the vendor list from Database
    * Select Browse with vendor name given returns all the products associated with the vendor
    
 2. Search :
    * Select Search with all other inputs are empty results all the vendor list from Database
    * Select Search with vendor name given returns all the vulnerabilities associated with 
        given vendor and no of results returned will be limited by given date range and 
        `max_results_display` flag.
    * Select Search with product name given returns all the vulnerabilities associated with 
        given product and no of results returned will be limited by given date range and 
        `max_results_display` flag.
    * Select Search with vendor, product name given returns all the vulnerabilities associated with 
        given vendor's product, and no of results returned will be limited by given date range and 
        `max_results_display` flag.
        
 3. Specific CVE ID
    * Select Specific CVE ID option from CVE Search Criteria with CVE ID of Vulnerability, returns
      data related to specific CVE ID & populates into CVE table.
      
 4. Last 30 CVES
    * Returns last 30 latest Vulnerabilities from Database no of results returned controlled by 
       `max_results_display` flag.
     
 5. CVE DB Info
    * To get more information about the current databases in use and when it was updated 
        
     
##Function Payload Data Format

  The Payload from the function will be always in the JSON format sample out format is given.
  Basically `api_call` key is used to segregate the data.
  
    {
       "content": [list of Retruned JSON Object],
       "api_call": last/browse/search/cve/db
    }
    
##Function Post-Process Script
   It can be parsed within the post-process script as `results.get("content")`. Based on the api_call type 
   the data can be represented as user needs.
   
   By default `Example: CVE Browse` function data is displayed on incident Notes, 
    and `Example: CVE Search` function data displayed on the `CVE searched Data` Table.

    
    
