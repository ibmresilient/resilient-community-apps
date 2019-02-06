
## About Ansible

  

**You can use Ansible to automate three types of tasks:**

  

- Provisioning: Set up the various servers you need in your infrastructure.

- **Configuration management: Change the configuration of an application, OS, or device; start and stop services; install or update applications; implement a security policy; or perform a wide variety of other configuration tasks.**

- Application deployment: Make DevOps easier by automating the deployment of internally developed applications to your production systems.

  
  
  
  

## Using the Ansible Function

Make sure that you have ansible v2.7 installed in your system(control machine). 
One Function and one Workflow added as example we encourage you to explore that for better understanding.
If you are using ansible-vault please provide full path of your password file( Recommended format below: ) -
> vault_password.yml

    ---
    vault_pass: <your-password>
  
  

## Environment

To install in "development mode", run

`pip install -e ./fn_ansible/`

The distribution file can be installed using

`pip install fn_ansible-<version>.tar.gz`

Import the package into Resilient by running `resilient-circuits customize`

  

To configure the Ansible parameters, run `resilient-circuits config [-u | -c]`.

Then edit the `[fn_ansible]` template with the URL and basic authentication settings.

  

Run with: `resilient-circuits run`.

  

To uninstall, run: `pip uninstall fn_ansible`

## Resilient Configuration

Follow the steps to add a fn_ansible section to your `app.config` file by running `resilient-circuits config [-u | -c]` and updating the fields:

  

```
[fn_ansible]
playbook_dir=</full/path/to/your/playbook/directory>
user_name=<USERNAME-OF-HOSTS>
root_password=<PASSWORD-OF-HOSTS>
hosts_path=</full/path/of/your/inventory/file>
playbook_become_method=<SUPER-USER-METHOD e.g. sudo>
playbook_become_user=<NAME-OF-ROOT-USER e.g. root>
vault_password_file=<OPTIONAL: /full/path/of/password/file>
connection_type=<OPTIONAL: e.g. local, smart etc.>
control_machine_username=<OPTIONAL: for user, REQUIRED: for developers and testers>
control_machine_password=<OPTIONAL: for user, REQUIRED: for developers and testers>