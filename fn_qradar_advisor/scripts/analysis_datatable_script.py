#
# We create artifacts for those observables according to how they can be mapped to 
# Resilient default artifacts. If user has custom artifacts, and wants
# to map them as well, please modify the following mapping dict. 
#
# All the other observables without direct mapping, try to make decision depending
# on the qradar_advisor_description of them. If not decision can be made, then 
# a String type artifact will be created.
#
mapping = {
  "domain-name":"DNS Name",
  "domain":"DNS Name",
  "EmailContent":"Email Body",
  "ipv4-addr":"IP Address",
  "malware":"Malware Family/Variant",
  "url":"URL"
}

artifact_description = "QRadar Advisor Analysis observable"
type = row.qradar_advisor_type
if type in mapping:
  incident.addArtifact(mapping[type], row.qradar_advisor_description, artifact_description)
else:
  artifact_type = "String"
  #
  # if the type is "file", the description could be MD5 hash, SHA-256 hash, SHA-1. 
  # Distinguish them according to the lengthself.
  #
  # Anything else is considered "File Name"
  #
  if type == "file":
    if len(row.qradar_advisor_description) == 32:
      artifact_type = "Malware MD5 Hash"
    elif len(row.qradar_advisor_description) == 64:
      artifact_type = "Malware SHA-256 Hash"
    elif len(row.qradar_advisor_description) == 40:
      artifact_type = "Malware SHA-1 Hash"
    else:
      artifact_type = "File Name"
      
  incident.addArtifact(artifact_type, row.qradar_advisor_description, artifact_description)
