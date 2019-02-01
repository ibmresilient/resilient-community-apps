# -*- coding: utf-8 -*-
incident_type_ids = [u'1001', u'Karick', u'14-12-2020', u'1$']
# # uni_list = [u'1001']
# print uni_list

# new_list = [x.encode('UTF8') for x in uni_list]
# print new_list

# print ", ".join(new_list)

# incident_types = "Incident Type: {0}".format(", ".join(new_list))

# for l in new_list:
#     incident_types.join(new_list)

# print incident_types

# incident_types = []
# for incident_type in incident_type_ids:
#     incident_types.append(incident_type.encode('UTF8'))



incident_types = [incident_type.encode('UTF8') for incident_type in incident_type_ids]


str = "Incident Type: {0}".format(", ".join(incident_types))


print str


# if len(incident_type_ids > 0):
#     str = "Incident Type: "

#     for incident_type in incident_type_ids:
#         str