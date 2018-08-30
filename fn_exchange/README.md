# Exchange Functions

This IBM Resilient Function package can be used to access Exchange email and meeting capabilities.
The functions provided have the following capabilities:

* Querying emails
* Deleting queried emails
* Moving queried emails
* Moving the contents of a folder to another folder then deleting the original folder
* Sending emails
* Creating meetings
* Getting mailbox info for a specified user

## To install in *development mode*:

    pip install -e ./fn_exchange/

After installation, the package will be loaded by `resilient-circuits run`.


## To uninstall:

    pip uninstall fn_exchange


## To package for distribution:

    python ./fn_exchange/setup.py sdist

## The resulting .tar.gz file can be installed using:

    pip install <filename>.tar.gz

## Add Exchange configuration details to the config file:
    
    resilient-circuits config -u
    
Set the following values in the config file (`app.config`) under the `[fn_exchange]` section:

```
verify_cert=[True|False]
server=example.com
username=domain\username
email=admin@example.com
password=password
default_folder_path=Some folder path after root i.e. Top of Information Store/Inbox. Multiple folderpaths must be separated by commas.
```

## How to use the function
Please note that version 31 of Resilient is required to use the example workflows.

1. Import the necessary customization data into the Resilient platform:
                
        resilient-circuits customize
                
    This creates the following customization components:
    * Action fields and Function inputs: 
        *   `exchange_destination_folder_path`
        *   `exchange_email`
        *   `exchange_email_ids`
        *    `exchange_emails`
        *    `exchange_end_date`
        *    `exchange_folder_path`
        *    `exchange_get_email`
        *    `exchange_has_attachments`
        *    `exchange_meeting_body`
        *    `exchange_meeting_end_time`
        *    `exchange_meeting_start_time`
        *    `exchange_meeting_subject`
        *    `exchange_message_body`
        *    `exchange_message_subject`
        *    `exchange_num_emails`
        *    `exchange_optional_attendees`
        *    `exchange_order_by_recency`
        *    `exchange_required_attendees`
        *    `exchange_search_subfolders`
        *    `exchange_sender`
        *    `exchange_start_date`
    * Message Destination: `fn_exchange`
    * Functions: 
        * `exchange_create_meeting`
        * `exchange_delete_emails`
        * `exchange_find_emails`
        * `exchange_get_mailbox_info`
        * `exchange_move_and_delete_folder`
        * `exchange_move_emails`
        * `exchange_send_email`
    * Workflows:
        * `example_of_exchange_create_meeting`
        * `example_of_exchange_delete_emails`
        * `example_of_exchange_find_emails`
        * `example_of_exchange_get_mailbox_info`
        * `example_of_exchange_move_emails`
        * `example_of_exchange_send_email`
        * `exchange_move_and_delete_folder`
    * Rules [Artifact]:
        * `Exchange Create Meeting`
        * `Exchange Delete Emails`
        * `Exchange Find Emails`
        * `Exchange Get Mailbox Info`
        * `Exchange Move and Delete Folder`
        * `Exchange Move Emails`
        * `Exchange Send Email`
          
2. Update and edit `app.config`:
                
        resilient-circuits config -u
                
3. Start Resilient Circuits:

        resilient-circuits run

4. Trigger the rule
