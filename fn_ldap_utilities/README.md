# Resilient LDAP Utilities v1.0.0

This Python Package is comprised of various Resilient Functions that allow you to manage users in your Directory Service, without having to leave the UI of Resilient

## ldap_utilities_set_password
* When using with **Microsoft Active Directory** server
  * Set the following in the **appconfig file**:
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
  * Set the following in the **appconfig file**:
    ```python
      [fn_ldap_utilities]
      ldap_is_active_directory=False
    ```