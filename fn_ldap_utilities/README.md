# Resilient LDAP Utilities v1.0.0

This Python Package is comprised of various Resilient Functions that allow you to manage users in your Directory Service, without having to leave the UI of Resilient

## ldap_utilities_set_password
* When using with **Microsoft Active Directory** server
  * Set the following in the **app.config file**:
    ```python
      [fn_ldap_utilities]
      ldap_port=636
      ldap_use_ssl=True
      ldap_is_active_directory=True
    ```
  * Must use a secure connection
  * Microsoft does not allow you to change an user's password unless using a secure connection
  * Microsoft have their own ldap3 function to change the password of an entry in the Active Directory [see here](https://ldap3.readthedocs.io/microsoft.html)

* For other directory services using LDAP (i.e. **OpenLDAP**)
  * Set the following in the **app.config file**:
    ```python
      [fn_ldap_utilities]
      ldap_is_active_directory=False
    ```

## ldap_utilities_update
* Takes the name of the attribute you want to update and an array of values to update that attribute with
* The function input `ldap_attribute_values` must be a **string repersenation of an array**
  ```python
  inputs.ldap_attribute_values = "['stringValue1', 1234, 'stringValue2']"
  ```
* Uses **MODIFY_REPLACE** as documented [here](https://ldap3.readthedocs.io/modify.html)
  * _"Replace all existing values of the specified attribute with the new values listed"_ 
  * _"Creates the attribute if it does not already exist"_
  * _"It is ignored if the attribute does not exist"_

## ldap_utilities_toggle_access
* Supports only **Active Directory**. Set the following in the **app.config file**:
    ```python
      [fn_ldap_utilities]
      ldap_port=636
      ldap_use_ssl=True
      ldap_is_active_directory=True
    ```
* Enables or Disables an **Active Directory** user
* Requires the DN of the user you wish to toggle access for
* Example shows how to use with **LDAP Utilities: Search Function** to toggle access for a user using their email address