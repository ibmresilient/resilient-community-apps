""" Update incidents with results from a query """

import logging
import json
import copy
import os
import sys
import tempfile
import csv
import threading
from datetime import datetime
import resilient_circuits.template_functions as template_functions
from resilient import SimpleHTTPException
from .datatable import DataTable

LOG = logging.getLogger(__name__)

try:
    basestring
except NameError:
    LOG.info("Setting basestring to str for python 2/3 compatibility")
    basestring = str


def update_with_results(res_client, query_definition, event_message, response,
                        datatable_locks, context_token, additional_map_data=None):
    incident = event_message.get("incident", {})
    if response and "metadata" in response:
        # Some additional meta data about the search results, like a job ID
        metadata = response["metadata"]
    else:
        metadata = {}

    if query_definition.result_container:
        # The rows we care about are in this key of the query result object
        key_names = ", ".join(response.keys())
        for key in query_definition.result_container.split("."):
            if response:
                response = response.get(key)
        if not response:
            LOG.warn("No data returned from query in '%s' (top-level keys are: %s)", query_definition.result_container, key_names)
            return "Query returned no %s" % query_definition.result_container

    else:
        # We will use the entire query result object.  The mappings will need to manually
        # iterate over rows.
        pass

    if query_definition.attachment_mapping:
        _do_attach(query_definition, event_message, metadata, response, res_client,
                   context_token, additional_map_data=additional_map_data)

    if query_definition.incident_mapping:
        _do_incident_mapping(query_definition, event_message, metadata,
                             response, res_client, context_token,
                             additional_map_data=additional_map_data)

    if query_definition.artifact_mapping:
        _do_artifact_mapping(query_definition, event_message, metadata,
                             response, res_client, context_token,
                             additional_map_data=additional_map_data)

    if query_definition.data_table_mapping:
        for dtinfo in query_definition.data_table_mapping:
            _do_datatable_mapping(query_definition, dtinfo, event_message, metadata,
                                  response, datatable_locks, res_client, context_token,
                                  additional_map_data=additional_map_data)

    if query_definition.task_mapping:
        _do_task_mapping(query_definition, event_message, metadata, response, res_client,
                         context_token, additional_map_data=additional_map_data)

    if query_definition.note_mapping:
        _do_note_mapping(query_definition, event_message, metadata, response, res_client,
                         context_token, additional_map_data=additional_map_data)

    # TODO: add milestones

    if query_definition.iterate_per_result:
        _do_iterate_per_result(query_definition, event_message, metadata, response,
                               datatable_locks, res_client, context_token,
                               additional_map_data=additional_map_data)
# end update_with_results


def _update_incident(incident, mapping, incident_fields):
    """ used with get_put to update incident """
    LOG.info("Updating incident %s", incident["id"])
    LOG.debug("Fields: %s", json.dumps(mapping, indent=2))

    for key, value in mapping.items():
        if not value:
            LOG.info("Skipping update of field %s due to missing value", key)
            continue
        # Type coercion
        elif incident_fields.get(key, "") in ("datepicker", "datetimepicker", "number"):
            # Convert these fields to integers
            try:
                value = int(value)
            except ValueError as e:
                LOG.exception("Field %s should be numeric! %s", key, e)
                LOG.error("Mapping for field %s skipped due to invalid integer value", key)
                continue
        elif incident_fields.get(key, "") in ("multiselect", "multiselect_members"):
            # Convert the value to a list
            if not isinstance(value, list):
                value = [value]
        elif incident_fields.get(key, "") == "boolean":
            # Convert the value to True or False
            if value == "True":
                value = True
            elif value == "False":
                value = False
            elif not value:
                value = None
            else:
                raise ValueError("Field [%s] Value [%s] not valid boolean value", key, value)
            # Set the value
        if key in incident:
            incident[key] = value
        elif key in incident["properties"]:
            incident["properties"][key] = value
        else:
            LOG.error("Incident field %s not found! Field not updated.", key)
# end _update_incident


def _add_artifact(client, incident_id, artifact, context_token):
    """ Create resilient artifact """
    value = artifact.get("value")
    if isinstance(value, basestring) and value.lower() == "null":
        value = ""
    if not all((value, artifact.get("type"))):
        LOG.warn("Can't add artifact with missing value or type: %s",
                 json.dumps(artifact, indent=2))
        return
    try:
        LOG.info(u"Adding artifact to incident %s: %s", incident_id, artifact)
        client.post("/incidents/%s/artifacts" % incident_id, artifact, co3_context_token=context_token)
    except SimpleHTTPException as error:
        LOG.error("Failed to post new artifact. Status %s", str(error.response.status_code))
        LOG.exception("Failed to post artifact")
# end _add_artifact


post_attachment_lock = threading.RLock()


def post_attachment(rest_client, *args, **kwargs):
    """Synchronized method to post file attachments, to work around platform issue DE828"""
    with post_attachment_lock:
        return rest_client.post_attachment(*args, **kwargs)


def _get_csv_tempfile():
    if sys.version_info.major < 3:
        # Python 2.x: CSVWriter writes to a binary file, data is bytes
        return tempfile.NamedTemporaryFile(delete=False)
    else:
        # Python 3.x: CSVWriter writes to a text file, data is strings, but fix newline for Windows
        return tempfile.NamedTemporaryFile(mode='w', delete=False, newline='')


def _do_attach(query_definition, event_message, metadata,
               response, res_client, context_token, additional_map_data=None):
    """ Update incident with results as a CSV file attachment """
    # keys - options list of keys to extract from each result row
    incident = event_message.get("incident", {})
    incident_id = incident.get("id")
    parsable = True
    keys = query_definition.attachment_mapping.get("keys") or []

    if isinstance(response, dict):
        response = [response]
    elif not(hasattr(response, "__iter__")) or isinstance(response, basestring):
        # This isn't something we will try to parse, just write it to file
        parsable = False

    if not keys and parsable:
        for row in response:
            if len(keys) == 0:
                keys = list(row.keys())
            else:
                keys = list(keys) + list(set(row.keys()) - set(keys))

    with _get_csv_tempfile() as temp_file:
        temp_filename = temp_file.name
        if not parsable:
            temp_file.write(response)
        else:
            writer = csv.DictWriter(temp_file, fieldnames=keys,
                                    dialect='excel', extrasaction='ignore')

            key_dict = {}
            for key in keys:
                if sys.version_info.major < 3 and isinstance(key, unicode):
                    key_dict[key] = key.encode("utf-8")
                else:
                    key_dict[key] = key
            writer.writerow(key_dict)
            for row in response:
                writer.writerow(row)
            temp_file.flush()

    # Construct a filename based on attachment name (template) specified in the query definition
    filename = query_definition.attachment_mapping.get("name")
    if filename is None:
        searchname = query_definition.name
        searchtime = datetime.utcnow()
        attname = "{}-{}".format(searchname, searchtime.strftime("%Y%m%d%H%M%S"))
    else:
        attname = query_definition.render_value(filename)

    extension = query_definition.attachment_mapping.get("ext", "csv")
    contenttype = query_definition.attachment_mapping.get("content_type")
    attachment_name = "{}.{}".format(attname, extension)

    # Attach to the incident
    LOG.info("%s = %s", attachment_name, temp_filename)
    post_attachment(res_client,
                    "/incidents/{0}/attachments".format(incident_id),
                    temp_filename,
                    filename=attachment_name,
                    mimetype=contenttype,
                    co3_context_token=context_token)
    os.remove(temp_filename)
    return attachment_name
# end _do_attach


def _json(result):
    if not result:
        return result
    if isinstance(result, list):
        return [_json(v) for v in result]
    elif not isinstance(result, basestring):
        raise TypeError("_json expects list or str")
    try:
        # Don't want to convert values to numeric
        float(result)
        return result
    except:
        pass
    for n in range(1, 32):
        result = result.replace(chr(n), " ")
    try:
        value = json.loads(result)
    except:
        LOG.debug("Not JSON: %s", result)
        value = result
    return value


def _do_incident_mapping(query_definition, event_message, metadata,
                         response, res_client, context_token,
                         additional_map_data=None):
    """ Update incident with query results as defined in mapping """
    incident = event_message.get("incident", {})
    incident_id = incident.get("id")

    # Map for rendering starts with the event (incident, etc)
    mapdata = copy.deepcopy(event_message)
    if additional_map_data:
        mapdata.update(additional_map_data)
    # Add in any rendered vars
    mapdata.update(query_definition.vars)
    # Add in any query result metadata
    mapdata.update(metadata)
    # Add in the result data
    if query_definition.result_container:
        # We only use the first row returned to do incident updates.
        data = {"result": response[0]}
    else:
        data = response
    if data is not None:
        mapdata.update(data)

    # Render the mapping rules with the query results
    mapping = {}
    for key, value_template in query_definition.incident_mapping.items():
        # Note: each value uses 'render_json' so that we can produce text, lists, etc.
        # Values should generally be escaped with the '|json' filter.
        # If this doesn't work, just use the unescaped version.
        if isinstance(value_template, list):
            mapping[key] = [_json(template_functions.render(t, mapdata)) for t in value_template]
        else:
            mapping[key] = _json(template_functions.render(value_template, mapdata))
    # Update the incident (with awareness of field datatypes, if type coercion is needed)
    incident_fields = _get_incident_fields(res_client)
    try:
        res_client.get_put("/incidents/{0}".format(incident_id),
                           lambda incident: _update_incident(incident, mapping, incident_fields),
                           co3_context_token=context_token)
    except SimpleHTTPException:
        LOG.error("Failed to update incident with fields: %s", json.dumps(mapping, indent=2))
        raise
# end _do_incident_mapping


def _do_artifact_mapping(query_definition, event_message, metadata,
                         response, res_client, context_token,
                         additional_map_data=None):
    """ Map query results to new artifact and add to Resilient """
    incident = event_message.get("incident", {})
    incident_id = incident.get("id")

    if not response:
        return
    existing_artifacts = [_artifact_key(artifact) for artifact in _get_artifacts(incident_id, res_client)]
    LOG.debug(u"Existing Artifacts:\n%s", u"\n".join(existing_artifacts))

    if query_definition.result_container:
        # Create an artifact for each query result row
        for row in response:
            for artifact_template in query_definition.artifact_mapping:
                mapdata = {"result": row}
                # Add in any query result metadata
                mapdata.update(metadata)
                if additional_map_data:
                    mapdata.update(additional_map_data)
                artifact = template_functions.render_json(artifact_template,
                                                          mapdata)
                if artifact.get("value") and _unique_artifact(artifact, existing_artifacts):
                    _add_artifact(res_client, incident_id, artifact, context_token)
                    existing_artifacts.append(_artifact_key(artifact))
    else:
        # Create a single artifact from the query result
        for artifact_template in query_definition.artifact_mapping:
            artifact = template_functions.render_json(artifact_template, response)
            if artifact.get("value") and _unique_artifact(artifact, existing_artifacts):
                _add_artifact(res_client, incident_id, artifact, context_token)
                existing_artifacts.append(_artifact_key(artifact))
# end _do_artifact_mapping


def _unique_artifact(artifact, existing_artifacts):
    is_new = _artifact_key(artifact) not in existing_artifacts
    if not is_new:
        LOG.debug(u"Duplicate artifact %s", artifact.get("value", ""))
    return is_new


def _artifact_key(artifact):
    return u"{}{}".format(artifact.get("value", ""), artifact.get("type", ""))


def _get_artifacts(incident_id, res_client):
    try:
        artifacts = res_client.get("/incidents/%s/artifacts?handle_format=names" % incident_id)
        LOG.debug("Retrieved %d artifacts for incident %s", len(artifacts), str(incident_id))
        return artifacts
    except SimpleHTTPException as error:
        LOG.exception("Failed to get artifacts for incident %d", incident_id)
        return []
# end _get_artifacts


def _get_incident_fields(res_client):
    try:
        fields = res_client.get('/types/incident/fields')
        if fields:
            fields = {field["name"]: field["input_type"] for field in fields}
            return fields
        else:
            LOG.error("Failed to get incident fields from Resilient")
            raise Exception("Failed to get incident fields from Resilient")
    except SimpleHTTPException as error:
        LOG.exception("Failed to get incident fields from Resilient")
        raise


def _do_datatable_mapping(query_definition, dtinfo, event_message, metadata,
                          response, datatable_locks, res_client, context_token,
                          additional_map_data=None):
    """ Map query results to Resilient data table rows """
    incident = event_message.get("incident", {})
    incident_id = incident.get("id")
    if query_definition.result_container:
        rows = response
    else:
        rows = [response,]

    # Contains: "name", "key" (optional), "cells" (optional)
    dtname = dtinfo.get("name")
    dtkey = dtinfo.get("keys", [])
    dtrow_id = dtinfo.get("row_id", None)
    dtcells = dtinfo.get("cells", None)
    limit = dtinfo.get("limit", 0)

    # Get access to the data table
    if not datatable_locks[dtname].acquire(timeout=600):
        LOG.error("Couldn't acquire lock on table %s. No update done.", dtname)
        return
    try:
        datatable = DataTable(res_client, table_name=dtname)
        dtrows = []
        row_to_update = None

        if dtrow_id:
            # We are updating a single existing row
            row_to_update = datatable.find_row(incident['id'], dtrow_id)
            if not row_to_update:
                LOG.error("Row [%s] not found. No update done.", dtrow_id)
                return
        elif dtkey:
            # Read all the rows
            dtrows = datatable.rows(incident_id)

        # Map for rendering starts with the event (incident, etc)
        mapdata = copy.deepcopy(event_message)
        if additional_map_data:
            mapdata.update(additional_map_data)
        # Add in any rendered vars
        mapdata.update(query_definition.vars)
        # Add in any query result metadata
        mapdata.update(metadata)

        LOG.debug("Key columns: %s", dtkey)

        cells_template = json.dumps({"cells": dtcells}, indent=2)
        LOG.debug("Cells template: %s", cells_template)

        num_created = 0
        for result_row in rows:
            # If a key is specified, it's for upsert:
            # - Each row in the result should correspond to one row in the data table
            # - Render key with **the event_message and the result row**
            #   (because the key could be e.g. artifact.value, or task.id, or row.somevalue)
            # - It looks like {"cell":"value"} when rendered
            # - We expect a single row matching the key, or none
            #   (If multiple rows match the key, just pick the randomly-first one and carry on)
            # - Update it based on the response row, or insert
            mapdata["result"] = result_row

            # Render the result row to cells using the template provided in the query definition.
            cells_rendered = template_functions.render_json(cells_template, mapdata)
            datatable.update_cell_value_types(cells_rendered)

            dtrow = None
            if dtkey:
                LOG.debug("Find matching row to update!")
                key_dict = {key: cells_rendered["cells"].get(key, {}).get("value", None) for key in dtkey}
                matching_rows = datatable.match(dtrows, key_dict, limit=1)
                if matching_rows:
                    dtrow = matching_rows[0]
            elif row_to_update:
                dtrow = row_to_update
            if dtrow is None:
                # Insert a new row in the data table
                LOG.debug("Adding Row: %s", json.dumps(cells_rendered, indent=2))
                new_row = datatable.add_row(incident_id, cells_rendered)
                if new_row:
                    dtrows.append(new_row)
            else:
                # Update the row in the data table
                LOG.debug("Updating Row: %s", json.dumps(cells_rendered, indent=2))
                datatable.update(incident_id, dtrow, cells_rendered, co3_context_token=context_token)
            num_created = num_created + 1
            if num_created == limit:
                LOG.info("Limiting Datatable row creation to first %d results", limit)
                break
    finally:
        datatable_locks[dtname].release()
# end _do_datatable_mapping


def _do_task_mapping(query_definition, event_message, metadata,
                     response, res_client, context_token,
                     additional_map_data=None):
    """ Map query results to new task and add to Resilient """
    incident = event_message.get("incident", {})
    incident_id = incident.get("id")

    if not response:
        return

    def _add_task(client, incident_id, task):
        """ Create resilient task """
        try:
            LOG.info(u"Adding task to incident %s: %s", incident_id, task)
            client.post("/incidents/%s/tasks" % incident_id, task, co3_context_token=context_token)
        except SimpleHTTPException as error:
            LOG.error("Failed to post new task. Status %s", str(error.response.status_code))
            LOG.exception("Failed to post task")

    if query_definition.result_container:
        # Create a task for each query result row
        for row in response:
            for task_template in query_definition.task_mapping:
                mapdata = {"result": row}
                # Add in any query result metadata
                mapdata.update(metadata)
                if additional_map_data:
                    mapdata.update(additional_map_data)

                task = template_functions.render_json(task_template, mapdata)
                _add_task(res_client, incident_id, task)

    else:
        # Create a single task from the query result
        for task_template in query_definition.task_mapping:
            task = template_functions.render_json(task_template, response)
            _add_task(res_client, incident_id, task)
# end _do_task_mapping

def _do_iterate_per_result(query_definition, event_message, metadata,
                           response, datatable_locks, res_client, context_token,
                           additional_map_data=None):
    """Call additional mappings n times per result row"""

    for row in response:
        mapdata = {"result": row}
        mapdata.update(metadata)
        if additional_map_data:
            mapdata.update(additional_map_data)
        count = int(template_functions.render(query_definition.iterate_per_result.count_template, mapdata))
        for i in range(count):
            update_with_results(res_client,
                                query_definition.iterate_per_result,
                                event_message,
                                [row],
                                datatable_locks,
                                context_token,
                                additional_map_data={'i': i})
    # end _do_iterate_per_result

def _do_note_mapping(query_definition, event_message, metadata,
                     response, res_client, context_token,
                     additional_map_data=None):
    """ Map query results to new note and add to Resilient """
    incident = event_message.get("incident", {})
    incident_id = incident.get("id")

    if not response:
        return

    def _add_note(client, incident_id, note):
        """ Create resilient note """
        try:
            LOG.info(u"Adding note to incident %s: %s", incident_id, note)
            client.post("/incidents/%s/comments" % incident_id, note, co3_context_token=context_token)
        except SimpleHTTPException as error:
            LOG.error("Failed to post new note. Status %s", str(error.response.status_code))
            LOG.exception("Failed to post note")

    if query_definition.result_container:
        # Create a note for each query result row
        for row in response:
            mapdata = {"result": row}
            # Add in any query result metadata
            mapdata.update(metadata)
            if additional_map_data:
                mapdata.update(additional_map_data)

            for note_template in query_definition.note_mapping:
                note = template_functions.render_json(note_template, mapdata)
                _add_note(res_client, incident_id, note)
    else:
        # Create a single note from the query result
        for note_template in query_definition.note_mapping:
            note = template_functions.render_json(note_template, response)
            _add_note(res_client, incident_id, note)
# end _do_task_mapping
