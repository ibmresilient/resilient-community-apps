
## Function McAfee Tagging ePO Asset

To install in "development mode"

    pip install -e ./fn_mcafee_epo/

After installation, the package will be loaded by `resilient-circuits run`.


To uninstall,

    pip uninstall fn_mcafee_epo


To package for distribution,

    python ./fn_mcafee_epo/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz

Add ePO configuration details

    resilient-circuits configure -u

Set the following values in `app.config` under the `[fn_mcafee_epo]` section.
    
    epo_url=https://<your_epo_server>:<port>
    epo_username=<your_epo_username>
    epo_password=<your_epo_password>
    epo_trust_cert=true/false
    
### How to use the function

1. Start Resilient Circuits with `resilient-circuits run`

2. Create a workflow and add a the function `McAfee Tag an epo asset` to it

3. Edit the Function from the Workflow view and determine how to set the two input parameters `mcafee_epo_systems` and `mcafee_epo_tag`

4. Create a rule which will kick off the Workflow created above.

5. Trigger the rule.