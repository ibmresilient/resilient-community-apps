# Shell-Runner

This action processor responds to any custom action on its message destination,
locates a shell-script with the same name as the action,
runs the script and returns its output as a file attachment in the incident.

The behaviors to locate the script and to process the results are configurable
for specific actions if required.

Typical uses include
* Running network utilities such as dig, traceroute, nbtstat, ping,
* Using PowerShell or bash as a way to query databases or systems,
* Managing firewall and IPS rules (Snort examples are included),
* Integrating with existing systems that have a command-line interface.

For details, see the [setup documentation](https://github.com/ibmresilient/resilient-community-apps/blob/master/rc-shell-runner/docs/Shell_Actions_Setup.docx).
