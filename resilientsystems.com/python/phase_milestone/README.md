Phase Milestone
===============

As an incident progresses, the Phase changes to reflect the task progress.

Resilient automatically advances the phase.  The "current phase" is the first
phase that has tasks, where not all tasks are completed.  So, if users
complete all the tasks in a phase, the phase will advance.  And if a task
is reopened, the phase will regress.

It's easy, and a very useful metric, to report on the current Phase of your
incidents.  But it is more difficult to report on the phase progression over
time, for example to see a visual chart of each phase's time.

This custom action adds a Milestone to each incident whenever the phase changes.
The Timeline view of each incident then shows these phase milestones
alongside other events in the incident.


## Environment and Installation

This integration is provided as
* A component for a "resilient circuits" framework
* A fragment of a configuration file.

Copy the .py file into your `components` directory, where it will be
loaded automatically when your application starts.

Copy the configuration file fragment into your application's configuration
file and edit the settings appropriately.


## Resilient server setup

You must configure the following customizations to the Resilient server.
Open the Administrator Settings --> Actions, then:


## Message Destination

Create a Queue message destination with programmatic name `phase_milestone`.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.


## Automatic Action

Create an automatic action named 'AutoPhase', associated with object type
"Incident".  Choose `phase_milestone` as the message destination.
Add condition: "Phase is changed".

