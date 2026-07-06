
import sys
import pandas as pds
import numpy as np


if len(sys.argv) < 3:
    print("Usage check_predict csv_file_name predict_field_name")
    sys.exit()

filename = sys.argv[1]
predict = sys.argv[2]

print("Checking " + predict + " in " + filename)

dataf = pds.read_csv(filename,
                     sep=',',
                     usecols=[predict],
                     skipinitialspace=True,
                     quotechar='"')

predict_array = dataf[[predict]].values

print(predict_array)
print type(predict_array)

unique_list = []
count_dict = {}

for row in predict_array:
    val = row[0]
    print (val)
    print type(val)

    if not val:
        continue

    if val not in unique_list:
        unique_list.append(val)
        count_dict[val] = 1
    else:
        count_dict[val] = count_dict[val] + 1

print(str(count_dict))