# Installation Guide for ServiceNow Integration

---
## Table of Contents
  - [Prerequisites](#prerequisites)
  - [Step 1: *Create a User on the Resilient Appliance*](#step-1-create-a-user-on-the-resilient-appliance)
  - [Step 2: *Install ServiceNow IBM Resilient App*](#step-2-install-servicenow-ibm-resilient-app)
  - [Step 3: *Create a User in ServiceNow and assign it the correct Role*](#step-3-create-a-user-in-servicenow-and-assign-it-the-correct-role)
  - [Step 4: *Enter IBM Resilient Configurations*](#step-4-enter-ibm-resilient-configurations)
  - [Step 5: *Download & Install fn_service_now Integration*](#step-5-download--install-fnservicenow-integration)
  - [Step 6: *Install and Configure ServiceNow Mid-Server (if needed)*](#step-6-install-and-configure-servicenow-mid-server-if-needed)
  - [Step 7: *Give your ServiceNow users the correct Role*](#step-7-give-your-servicenow-users-the-correct-role)
  - [Step 8: *Test*](#step-8-test)
  - [Step 9: *How to Import Updates in ServiceNow*](#step-9-how-to-import-updates-in-servicenow)
---

## Prerequisites 
* ServiceNow Instance running >= `Kingston` release
* Access to the `Incident Table` in ServiceNow
* A user in ServiceNow with an `admin` role
* IBM Resilient >= `v31.0.0`
* An Integrations Server running `resilient-circuits >= v31.0.0`
* If IBM Resilient is not publicly accessible (behind a firewall) a `ServiceNow MID Server` is required

---

## Step 1: *Create a User on the Resilient Appliance*
* Get the Resilient Organization name you want to use this integration with.
* SSH into your Resilient Appliance.
* Insert your Organization name in the command below and run it:
  ```
  $ sudo resutil newuser -org "<org-name>" -email snow_integration@example.com -first "SNOW" -last "Integration"
  ```
* You can use any email address you desire
* This creates a new user in that Organization with the following attributes:
  * **First Name:** SNOW
  * **Last Name:** Integration
  * **Email:** snow_integration@example.com
--- 

## Step 2: *Install ServiceNow IBM Resilient App*
* Go to the [ServiceNow Store](https://store.servicenow.com/)
* Login with your **ServiceNow HI Credentials**.
* Search for **IBM Resilient**.
* Click **more,** a new page opens.
* On the top-right click **Get** and follow the on screen instructions to install the app on your ServiceNow instance.
* Log in to your ServiceNow instance with a user that has an **admin** role.
* Look for the **IBM Resilient** menu in the navigation panel.
 ![screenshot](./screenshots/8.png)
* If you see it, the app installed successfully.
---

## Step 3: *Create a User in ServiceNow and assign it the correct Role*
* In ServiceNow, go to the **Users Table** and click **New**
 ![screenshot](./screenshots/9.png)
* Enter the following:
  * **User ID:** ibmresilient
  * **First Name:** IBM
  * **Last Name:** Resilient
  * **Password:** #########
  * **Email:** ibm_resilient_integration@example.com
* Set the **Timezone** to the same timezone of your Resilient Integrations Server.
 ![screenshot](./screenshots/10.png)
* Click **Submit.**
* Still in the users table, search and open the user you just created.
 ![screenshot](./screenshots/11.png)
* Scroll down. Under **Roles**, click **Edit**
* Give the user the `x_ibmrt_resilient.integrator` role.
 ![screenshot](./screenshots/12.png)
* Click **Save.**
---

## Step 4: *Enter IBM Resilient Configurations*
* In ServiceNow, look for the **IBM Resilient** menu in the navigation panel.
 ![screenshot](./screenshots/8.png)
* Click **Properties.** A new tab opens.
  ![screenshot](./screenshots/7.png)
* Enter your configurations:
  * **Resilient Host:** this is the Hostname or IP address of your Resilient Appliance, **relative to your ServiceNow Instance**, but **if you use a Mid-Server, it is relative to the Mid-Server** *(See  Step 6 on setting up your Mid-Server).*
  * **Resilient Organization:** this is the Org Name you used in **Step 1.**
  * **Email Address:** this is the Email Address you used in **Step 1.**
  * **Password:** this is the Password you used in **Step 1.**
  * **ServiceNow Username:** this is the **User ID** you entered in **Step 3.**
  * **ServiceNow MID Server Name:** enter the name of the MID Server to use with this Integration or leave blank if not using a MID Server
  * **ServiceNowAllowedTableNames:** is a CSV list of all the **Table Names** in ServiceNow IBM Resilient is allowed to integrate with. *Out-of-the-box this integration requires access to the `incident`, `sys_user` and `sys_user_group` tables.*
  * **Logging Verbosity:** set this to **error**. Can be changed to **debug** if needed later.
  * **Logging Destination:** set this to **db** (which will print any error logs to the Application Logs Table). Can be changed to **file** if needed later.
* Click **Save.** You should see a **Properties updated** banner at the top of the page if the save was successful.
* **Close** the tab.
---

## Step 5: *Download & Install fn_service_now Integration*
* Source the `.tar.gz` package internally.
* Copy the package to your Integrations Server and SSH into it.
* **Install** the package:
  ```
  $ pip install fn_service_now-x.x.x.tar.gz
  ```
* Import the **configurations** into your app.config file:
  ```
  $ resilient-circuits config -u
  ```
* Import the fn-service-now **customizations** into the Resilient Appliance:
  ```
  $ resilient-circuits customize -y -l fn-service-now
  ```
* Open the config file, scroll to the bottom and **edit your ServiceNow credentials**:
  ```
  $ nano ~/.resilient/app.config
  ```
  * **sn_host:** this is the host you use to access your ServiceNow Instance.
    ![screenshot](./screenshots/14.png)
  * **sn_api_uri:** generally left as its default setting. This is the URL for the custom APIs that get installed with the app. If you decide to implement your own endpoints, you would change this URL.
  * **sn_table_name:** this is the name of the Table in ServiceNow to Integrate with. It is where any Incidents/Tasks from Resilient will be created and synced
    >**NOTE:** currently this version (v1.0.0) only supports the **incident table in ServiceNow**
  * **sn_username:** the **User ID** from **Step 3.**
  * **sn_password:** the **Password** from **Step 3.**
* **Save** and **Close** the app.config file.
* **Test** your Connection to ServiceNow:
  ```
  $ resilient-circuits selftest -l fn-service-now
  ```
    ![screenshot](./screenshots/15.png)

* **Run** resilient-circuits:
  ```
  $ resilient-circuits run
  ```
* **Login** to the Resilient Appliance and select the Organization used in Step 1
* Go to **Customization Settings** > **Layouts** > **Incident Tabs** > **Summary Section**
* Under **Fields**, search for **snow**
* Drag the two **SNOW Fields** into the **Summary Section** as per the screenshot below
  ![screenshot](./screenshots/31.png)
* Click **Save**
* In the same view, click **Add Tab**
* In the popup modal, enter **ServiceNow** and click **Add**
  ![screenshot](./screenshots/32.png)
* Click the **ServiceNow** tab, drag in the **ServiceNow Records** Data Table and click **Save**
  ![screenshot](./screenshots/33.png)
--- 

## Step 6: *Install and Configure ServiceNow Mid-Server (if needed)*
A ServiceNow Mid-Server is needed if your Resilient instance is not directly accessible from your ServiceNow instance. If using a Mid-Server, verify the following:
  * The ServiceNow Mid-Server must be setup on the same network as your Resilient Appliance.
  * The Resilient Host Address you input in **Step 4** must be relevant to your Mid Server.

If not already installed:
* Type **mid-server** into your ServiceNow search box and click **Installation Instructions.**
  ![screenshot](./screenshots/16.png)

Once **installed** and **validated:**
* In ServiceNow, go to your List of Mid Servers.
  ![screenshot](./screenshots/17.png)
* Copy the **Name** of the Mid Server you will be using with IBM Resilient.
* In the Navigation Panel, open **IBM Resilient Properties**.
  ![screenshot](./screenshots/36.png)
* Paste the name into the **ServiceNow MID Server Name** field.
* Click **Save.**
--- 

## Step 7: *Give your ServiceNow users the correct Role*
* For a ServiceNow user to have the permission to escalate an Incident to IBM Resilient, they must be explicitly given the correct role
* In ServiceNow, go to the **Users Table** and open the user you want to give the permissions to
* Scroll down. Under **Roles**, click **Edit**
 ![screenshot](./screenshots/34.png)
* Give the user the `x_ibmrt_resilient.user` role
 ![screenshot](./screenshots/35.png)
* Click **Save**
---

## Step 8: *Test*
* In ServiceNow, in the navigation panel, go to **IBM Resilient > Test Connection**
* A **new tab** opens
* Click the green **Test Connection** button and wait until you see a page banner
* The **page banner** will inform you if your Test was successful or not and print any errors you may have
  ![screenshot](./screenshots/29.png)
* If your test was successful, we can now do a **real test!**
* **Login** to ServiceNow with a user that has the `x_ibmrt_resilient.admin` or `x_ibmrt_resilient.user` role
* Go to the **Incident Table**
  ![screenshot](./screenshots/20.png)
* Create a **New Incident** and **Save** it
* Open the incident you just created and **scroll to the bottom**
* Click **Create Resilient Incident**
  ![screenshot](./screenshots/21.png)
* Click the **IBM Resilient** tab
  ![screenshot](./screenshots/22.png)
* Once the incident has been created in Resilient, these fields will be populated
  >**NOTE:** this can take up to 20 seconds. If nothing appears after that time, **view the logs**
  > 
  > To view the Application Logs in ServiceNow:
  > * In the navigation panel, go to **System Logs > System Log > Application Logs**
  >  ![screenshot](./screenshots/28.png)
  > * If you are using a Mid-Server but there is a log: "No Mid-Server being used", either your Mid-Server is not "Up" or it does not have the **IBMResilientAccess Capability,** *see **Step 6***

* Sign into your Resilient Appliance and see if it created successfully
* Open the incident that was created
* Send the **default task** to ServiceNow by clicking the Action Status button:
  ![screenshot](./screenshots/23.png)
* Then fill out the Activity Inputs and click **Execute**:
  ![screenshot](./screenshots/24.png)
* If successful, a **Note** was added to the Task
  ![screenshot](./screenshots/25.png)
---
