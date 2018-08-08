#
# Return data in this example
#   results.search_results.suspicious_observables: 
#     Suspicious observables related to this indicator. Used in the post-process script to create artifacts, 
#     if the type of the observable can be mapped to an default artifact type.
#
return_search = results.search

api_version = 2
try:
  if return_search.search_results["suspicious_observables"] is None:
    api_version = 1
except:
  api_version = 1
#
# Sample return json dict for v2.0
#
'''{
      "search": {
          "search_value_type": "DomainName", 
          "other_count": 1, 
          "search_results": {
          "suspicious_observables": [
                  {
                      "reference_count": 1, 
                      "timestamp": 1529421998, 
                      "type": "DomainName", 
                      "label": "mydomain.com"
                  }, 
                  {
                      "reference_count": 1, 
                      "timestamp": 1462407300, 
                      "type": "EmailContent", 
                      "label": "ccf2d5f4ab37650ccbb582f351aa6fdd:"
                  }, 
                  {
                      "reference_count": 1, 
                      "timestamp": 1462407300, 
                      "type": "File", 
                      "label": "ccf2d5f4ab37650ccbb582f351aa6fdd"
                  }, 
                  {
                      "reference_count": 1, 
                      "timestamp": 1463566500, 
                      "type": "IpAddress", 
                      "label": "190.104.198.116"
                  },
                  {
                      "reference_count": 1, 
                      "timestamp": 1463072400, 
                      "type": "Hash", 
                      "label": "51417677b5e7b17542d383f5b25e2b43"
                  }
          ], 
          "other_observables": [
              {
                  "reference_count": 1, 
                  "timestamp": 1529421998, 
                  "type": "DomainName", 
                  "label": "mydomain.com"
              }
          ]
      }, 
      "suspicious_count": 5, 
      "search_value": "mydomain.com", 
      "reference_count": 1, 
      "is_toxic": false}, 
      "whois": {
          "updated_date": "2015-09-15T23:25:25.000Z", 
          "contact_country": "Canada", 
          "registrar_name": "Domain.com, LLC", 
          "contact_email": "noreply@data-protected.net", 
          "created_date": "2000-06-22T04:00:00.000Z", 
          "contact_name": "Data Protected Data Protected", 
          "contact_type": "registrant", "contact_org": "Data Protected"
      }
      }
'''
#
# We ONLY create artifacts for those observables that can be mapped to 
# default Resilient artifacts. If customer has custom artifacts, and wants
# to map them as well, please modify the following mapping dict. 
#
mapping = {
  "DomainName":"DNS Name",
  "EmailContent":"Email Body",
  "File":"Malware MD5 Hash",        # File type is a hash value. So we map File to Malware MD5 Hash
  "IpAddress":"IP Address",
  "Hash":"Malware MD5 Hash"
}
#
# Note that in this example workflow, we only extract the suspicious_observables
#
if api_version == 2:
  #v2.0
  suspicious_observables = return_search.search_results.suspicious_observables
  
  new_artifact_count = 0
  summary_string = "This artifact is not a suspicious observable"
  
  for observable in suspicious_observables:
    #
    # We support only those defined in mapping dict above
    # 
    if observable.type in mapping:
      #
      # Note sometimes QRadar Advisor return the artifact itself as a suspicious observable. We don't want to
      # duplicate here.
      #
      if mapping[observable.type] != artifact.type or observable.label != artifact.value:
        new_artifact_count = new_artifact_count + 1
        incident.addArtifact(mapping[observable.type], observable.label, "Watson Search result")  
      else:
        #
        # The artifact itself is a suspicious observable. We don't create new (duplicated) artifact. But we show this info
        #
        summary_string = "This artifact is a suspicious observable"
  
  # Add a note about number of suspicious_observables
  note_string = "<h3>Watson Search Result Summary</h3><hr>"
  note_string = note_string + "<br><p><span style=\"font-weight:bold\">" + summary_string + "</span></p><br>"
  note_string = note_string + "<p>Search Value: " + return_search.search_value + "</p>"
  note_string = note_string + "<p>Search Type:  <span style=\"color:white; border-bottom-left-radius: 2.96667px;background-color:#808080\">&nbsp " + return_search.search_value_type + "&nbsp</span></p>"
  note_string = note_string + "<p style=\"color:#FF00FF;\">Suspicious observables: " + str(return_search.suspicious_count) + "</p>" 
  note_string = note_string + "<p style=\"color:red;\">New artifacts mapped from suspicious observables: " + str(new_artifact_count) + "</p>" 
  note_string = note_string + "<p>Other observables: " + str(return_search.other_count) + "</p>"
  html_note = helper.createRichText(note_string)
  incident.addNote(html_note)
else:
  #v1.0?
  new_artifact_count = 0
  toxic_count = 0
  non_toxic_count = 0
  summary_string = "This artifact is not a toxic observable"
  for result in return_search.search_results:
    value_type = result["type"]
    if value_type in mapping:
      #
      # We know what artifact type corresponds to this value type
      #
      for val in result["values"]:
        #
        # We care about the toxic ones only
        #
        if val["is_toxic"]:
          toxic_count = toxic_count + 1
          #
          # Note sometimes QRadar Advisor return the artifact itself as a suspicious observable. We don't want to
          # duplicate here.
          #
          if mapping[value_type] != artifact.type or val.label != artifact.value:
            new_artifact_count = new_artifact_count + 1
            incident.addArtifact(mapping[value_type], val.label, "Watson Search result")  
          else:
            #
            # The artifact itself is a suspicious observable. We don't create new (duplicated) artifact. But we show this info
            #
            summary_string = "This artifact is a toxic observable"
        else:
          non_toxic_count = non_toxic_count + 1
      
  # Add a note about number of suspicious_observables
  note_string = "<h3>Watson Search Result Summary</h3><hr>"
  note_string = note_string + "<br><p><span style=\"font-weight:bold\">" + summary_string + "</span></p><br>"
  note_string = note_string + "<p>Search Value: " + return_search.search_value + "</p>"
  note_string = note_string + "<p>Search Type:  <span style=\"color:white; border-bottom-left-radius: 2.96667px;background-color:#808080\">&nbsp " + return_search.search_value_type + "&nbsp</span></p>"
  note_string = note_string + "<p style=\"color:#FF00FF;\">Toxic observables: " + str(toxic_count) + "</p>" 
  note_string = note_string + "<p style=\"color:red;\">New artifacts mapped from toxic observables: " + str(new_artifact_count) + "</p>" 
  note_string = note_string + "<p>Non toxic observables: " + str(non_toxic_count) + "</p>"
  html_note = helper.createRichText(note_string)
  incident.addNote(html_note)    
   
        
      
