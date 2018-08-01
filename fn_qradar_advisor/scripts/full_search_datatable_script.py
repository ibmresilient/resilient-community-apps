#
# We create artifacts for those observables according to how they can be mapped to 
# Resilient default artifacts. If user has custom artifacts, and wants
# to map them as well, please modify the following mapping dict. 
#
# All the other observables will be created as String type artifacts
#
mapping = {
  "domain-name":"DNS Name",
  "EmailContent":"Email Body",
  "ipv4-addr":"IP Address",
  "malware":"Malware MD5 Hash",
  "url":"URL"
}

artifact_description = "Watson Search with Local Context observable"
type = row.qradar_advisor_type
if type in mapping:
  incident.addArtifact(mapping[type], row.qradar_advisor_description, artifact_description)
else:
  #
  # if the type is "file", the description could be MD5 hash, SHA-256 hash. Distinguish them according to the length
  #
  bcreated = False
  if type == "file":
    if len(row.qradar_advisor_description) == 32:
      incident.addArtifact("Malware MD5 Hash", row.qradar_advisor_description, artifact_description)
      bcreated = True
    elif len(row.qradar_advisor_description) == 64:
      incident.addArtifact("Malware SHA-256 Hash", row.qradar_advisor_description, artifact_description)
      bcreated = True
  else:
    bcreated = False
  # We don't know what type this observable should be mapped to. Just create a String type
  if not bcreated:
    incident.addArtifact("String", row.qradar_advisor_description, artifact_description)
