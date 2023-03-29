Using the samples:

- Copy the sample template to your query definitions directory and set your app.config file to that directory.
- Create a queue message destination called "splunk".
- Create a menu item artifact rule called "Logged In Users" that writes to "splunk" queue.
  - Add condition to that rule so that it only applies to User Account type artifacts
- Create a menu item artifact rule called "Search History" that writes to "splunk" queue.
  - Add condition to that rule so that it only applies to User Account type artifacts
  - Add activity field to that rule with api name "days\_to_search" of type Number that is Always required.
- Create a custom incident text field called "splunk_system"
- Create a data table called "splunk\_user\_logins" with the following fields:
  - TEXT: username, splunk\_server, last\_time
  - NUMBER: login_count, total\_searches, distinct\_searches
- Add the custom field and data table to a tab so you can see it

- Create artifact corresponding to Splunk account names, like "admin".
- Log into Splunk a few times with that account and run some searches
- Run the Logged In Users action against the artifact and see the data table and field populated
- Run the Search History action against the artifact and see the other data table columns populated.
