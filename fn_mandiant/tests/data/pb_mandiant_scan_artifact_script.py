def compile_section_by_dtype(value, name):
    """
    Complies received information into HIT Cards. The information can have varied datatype. This function
    automatically detects the data type and formats the information suitable for a SOAR artifact. The result
    is returned as a dictionary representing the subsection with its name, data type, and converted
    value (if applicable).

    Args:
    ----
        value (str): The value to be categorized into a specific data type.
        name  (str): The name or identifier for the subsection.

    Returns:
    -------
        dict: A dictionary representing the subsection with the following keys:
            - "name"  : The name or identifier passed as the 'name' parameter.
            - "type"  : The determined data type of the 'value' (either "string," "uri," or "number").
            - "value" : The 'value' converted to the appropriate data type (int for numbers).
    """
    info_type = "string"

    # if "http" found, the string is classified as an URL
    if "http" in value:
        info_type = "uri"

    # detects if the given string is a number
    elif value.isdigit():
        info_type = "number"
        value = int(value)

    # format required for a HIT card to compile within an artifact
    subsection = {
        "name"  : name,
        "type"  : info_type,
        "value" : value
    }
    return subsection


def dedup_section(section):
    """
    An HIT card exclusively accommodates distinct entries and cannot exhibit information in a nested
    structure. Consequently, data is condensed and organized within the HIT card. To prevent 
    redundancies, this function is employed to attach an index number to the names of recurring
    entries, ensuring their uniqueness

    Args:
    ----
        section (dict): The section to be de-duplicated

    Returns:
    -------
        dict : Similar dictionary with de-duplicated "name" value
    """
    unique_keys = {}
    for idx, each_item in enumerate(section):
        if each_item["name"] not in unique_keys:
            unique_keys[each_item["name"]] = 0
        else:
            unique_keys[each_item["name"]] += 1
            section[idx]["name"] = section[idx]["name"] + str(unique_keys[each_item["name"]])
    return section


def dedup_verdict_section(section):
    """
    Verdict is a special section that contains the result of multiple analysis. Each analysis has
    its own "name", "response_count", "source_count", "benign_count", "confidence", and "malicious_count".
    As these values are being repeated, this function finds the appropriate analysis being performed using
    the name parameter, and appends that to the appropriate fields, there by eliminating duplicates.
    
    Example:
    -------
        Input : Bulletproof Hosting, response_count, source_count, benign_count, malicious_count
        Output: Bulletproof Hosting response_count, Bulletproof Hosting source_count, Bulletproof
                Hosting benign_count, Bulletproof Hosting malicious_count

    Args:
    ----
        section (dict): Verdict section of the response

    Returns:
        dict :  Similar dictionary with "name" values modified with their appropriate analysis type.
    """
    verdict_name = ""

    for each_item in section:
        # Saving the analysis name for subsequent fields
        if each_item["name"] == "name":
            verdict_name = each_item["value"]

        # Appending analysis name to fields that belong to the analysis
        if verdict_name:
            each_item["name"] = f"{verdict_name} {each_item['name']}"
    return section


def compile_hits_section(gathered_info, compiled_section:list) -> list:
    """ 
    The purpose of this function is to flatten and organize data from the `gathered_info`
    dictionary and append it to the `compiled_section` list. The function can also handle
    recursive calls when it encounters nested dictionaries or lists.

    Here's a breakdown of its functionality:
        1. It iterates through the keys of the `gathered_info` dictionary.
        2. If a key corresponds to a dictionary, it recursively calls itself with the nested
            dictionary, aiming to flatten it, and appends the results to the `compiled_section`.
        3. If the `gathered_info` is not a list and the value associated with the current key
            is a dictionary, it also recursively calls itself to flatten the nested dictionary.
        4. If the current key is not a list, and the value is a list, it iterates through the
            list and checks if the elements are dictionaries or lists. If so, it recursively
            calls itself on each element and appends the results to the `compiled_section`.
        5. If neither of the above conditions is met (i.e., the key or value is not a list or
            dictionary), it formats the key and value into a subsection using a function called
            `compile_section_by_dtype`. It then appends this subsection to the `compiled_section`.
        6. Finally, it returns the `compiled_section` containing the flattened and organized data.

    Args:
    ----
        gathered_info   (dict or list) : Could either be a dictionary or a list that requires
                                            flattening.
        compiled_section        (list) : Final flattened result. Contains a list of dictionaries.
                                            The function starts of with an empty list.

    Returns:
    -------
        list: compiled_section
    """
    for each_key in gathered_info:

        # This function has been designed with recursion in mind. This means that
        # gathered_info can be a dict and at times even a list. And therefore 

        # If gathered_info is a list and each_key is a dict is found within the section,
        # this function is recursively called with the newly found dict while passing
        # the previous output list. This is done to flatten the newly found dict and
        # append its contents to the existing section.
        if isinstance(each_key, dict):
            compile_hits_section(each_key, compiled_section)

        # If gathered_info is not a list and the current value of the gathered_info is a dict
        # the function is called recursively to flatten the newly found dict.
        elif not isinstance(gathered_info, list) and isinstance(gathered_info[each_key], dict):
            compile_hits_section(gathered_info[each_key], compiled_section)

        # Similarly if a list is found for the current value or key, it is then iterated further
        # and flattened out.
        elif not isinstance(each_key, list) and isinstance(gathered_info[each_key], list):
            for each_entity in gathered_info[each_key]:
                if isinstance(each_entity, dict) or isinstance(each_entity, list):
                    subsection = compile_hits_section(each_entity, compiled_section)
                    # compiled_section.append(subsection)

        # Finally, if the key or value is not a list or dict, then it's classified based on
        # it's datatype and formatted into a section.
        else:
            subsection = compile_section_by_dtype(str(gathered_info[each_key]), each_key)
            compiled_section.append(subsection)

    return compiled_section


def add_response_as_hits(response):
    """
    Here the HIT cards are created for artifacts. Depending on the response, 2 or more cards can
    be created. The primary/top level of the response is created into a HIT card by itself. Every
    other nested item within the response is created into a standalone section.

    Args:
    ----
        response (dict): response from the function that contains information that is to be displayed
                            as HITS.
    Returns:
    -------
        None
    """
    # Extract information found in the top level of the response and create a standalone HIT card
    # for those values. This usually has information related to MScore. Other sections are created
    # into separate HIT cards.
    main_section , other_sections = {}, {}
    for section in response:
        if isinstance(response[section], list) or isinstance(response[section], dict):
            other_sections[section] = response[section]
        else:
            main_section[section ] = response[section]

    # Each of the other sections are create into separate HIT cards, with special processing done
    # for Verdict to accommodate various analysis results. Each section is then deduplicated to
    # avoid any conflicts.
    for each_section in other_sections:
        section = compile_hits_section(other_sections[each_section], [])
        if each_section == "verdict":
            section = dedup_verdict_section(section)
        section = dedup_section(section)
        artifact.addHit(f"Mandiant Threat intelligence: {each_section.title()}", section)
    
    section = compile_hits_section(main_section, [])
    section = dedup_section(section)
    artifact.addHit("Mandiant Threat intelligence: MScore", section)