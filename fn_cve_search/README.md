#About This Package

This Common Vulnerability Exposures function provides a way to search vulnerabilities from CVE Database, 
     function offers below mentioned ways to search for vulnerabilities.

* Browse
* Search
* Specific CVE ID
* Last 30 CVE's
* Database Information
 
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
    max_results_display = 5
    
Edit the [fn_cve_search] properties as follows:
    
   1. max_results_display : The Vulnerabilities to display on the resilient tables from search results.

#Using the CVE Function
Below are details of the input fields and outputs results of the function.

##Function Inputs Fields:
   1. CVE Search Criteria       - Vulnerabilities search options
   2. Vendor                    - Name of the Vendor
   3. Product                   - Name of the Product
   4. CVE ID                    - specific Vulnerability ID
   5. CVE Published Date From   - Date Range to filter search data
   6. CVE Published Date To     - Date Range to filter search data
 
 CVE Function offers below search configurations to query vulnerabilities from DB
 
 1. Browse : 
    
    * Select Browse and all other inputs are empty results all the vendor list from Database
    * Select Browse with vendor name given returns all the products associated with the vendor
    * Select Browse with Vendor, Product name given returns all the vulnerabilities associated with 
        given vendor's product, and no of results returned will be limited by given date range and 
        `max_results_display` flag.
 
 2. Search :
    * Select Search with all other inputs are empty results all the vendor list from Database
    * Select Search with Vendor name given returns all the vulnerabilities associated with 
        given vendor and no of results returned will be limited by given date range and 
        `max_results_display` flag.
    * Select Search with Product name given returns all the vulnerabilities associated with 
        given product and no of results returned will be limited by given date range and 
        `max_results_display` flag.
    * Select Search with Vendor, Product name given returns all the vulnerabilities associated with 
        given vendor's product, and no of results returned will be limited by given date range and 
        `max_results_display` flag.
        
 3. Specific CVE ID
    * Select Specific CVE ID Option from CVE Search Criteria with CVE ID of Vulnerability, returns
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
    By default browse and db api call type data is displayed on incident Notes, and other type data displayed 
    on the CVE Table

    
    
    