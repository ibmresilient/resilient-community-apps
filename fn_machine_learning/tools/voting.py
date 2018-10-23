# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#

# We are following the tutorial here
# http://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_probas.html
#
import numpy as ny
import pandas as pds
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC


from fn_machine_learning.lib.multi_id_binarizer import MultiIdBinarizer
from fn_machine_learning.lib.model_utils import analyze

# Read CSV file using pandas
field = "is_significant"
all_fields = ["incident_type_ids", "confirmed", "negative_pr_likely", "nist_attack_vectors", field]

dataf = pds.read_csv("full.csv",
                     sep=',',
                     usecols=all_fields,
                     dtype={field: object},
                     skipinitialspace=True,
                     quotechar='"',
                     error_bad_lines=True)
#
#   Print out value counts before we do anything
#
print dataf[field].value_counts()

#
# Clean up
#
dataf = dataf.dropna(axis=0)
dataf = dataf.dropna(axis=1)

unwanted_values=["None", "1847"]

if unwanted_values is not None:
    for value in unwanted_values:
        dataf = dataf[dataf[field] != value]

print ("After cleaning up")
print dataf[field].value_counts()

all_fields.remove(field)

print all_fields

X = dataf[all_fields]
y = dataf[field]
#
# Transform
#
label_encoder = {}
for col_name, col in X.iteritems():
    if col.dtype.name == "object":
        #
        # For multi selection, col is a list. Use
        # json to load it and check if it is a list
        #
        is_list = MultiIdBinarizer.is_multi_selection(col)

        if is_list:
            #
            # Multi select is 2 dimensional
            #
            le = MultiIdBinarizer()
            le.fit(col, col_name)
            X = le.transform(X)
        else:
            le = LabelEncoder()
            le.fit(col)
            X[col_name] = le.transform(X[col_name])
        label_encoder[col_name] = le
    elif col.dtype.name == "float64":
        #
        #   Normalize it
        # http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html
        # Note that labelencoder can be used to normalize as well
        # labelencoder is good except SVM.
        #
        # le = LabelEncoder()
        #
        # Our own
        #
        # le = ResNormalizationEncoder()

        le = LabelEncoder()

        le.fit(col)
        X[col_name] = le.transform(X[col_name])
        label_encoder[col_name] = le

#
#   Need to split first
#
X_train, X_test, y_train, y_test = \
            train_test_split(X.values, y.values,
                             test_size=0.5,
                             random_state=0,
                             stratify=y)


X_tmp = pds.DataFrame(data=X_train)
y_tmp = pds.DataFrame(data=y_train)

data_training = pds.concat([X_tmp, y_tmp],
                           axis=1)

counts = data_training.iloc[:, -1].value_counts()
print("Training dataframe: {}".format(counts))

#
# The following code only works for two values in counts!!!
# Also we assume at this point the first one is the majority
#
count_list = []
for itr in counts.iteritems():
    count = [itr[0], itr[1]]
    count_list.append(count)


data_major = data_training[data_training.iloc[:, -1] == count_list[0][0]]
data_minor = data_training[data_training.iloc[:, -1] == count_list[1][0]]

row_count = data_major.shape[0]
minor_count = data_minor.shape[0]
print(str(row_count))

#
#   Compute how many times we can do this
#
fold = row_count/minor_count/5
print("We need to do {} times".format(fold))

svm1 = SVC(kernel="rbf", class_weight="balanced")
svm1.fit(X_tmp, y_tmp)
y_1 = svm1.predict(X_test)
accuracy = accuracy_score(y_true=y_test,
                          y_pred=y_1)

estimators = []
for i in range(0, fold, 1):
    samples_df = data_major.sample(minor_count*5,
                                   replace=False)
    dataf_est = pds.concat([samples_df, data_minor], axis=0)

    X_train_est = dataf_est.iloc[:, :-1]
    y_train_est = dataf_est.iloc[:, -1]

    #
    # Random Forest already use voting. SVM is better.
    #
    svm = SVC(kernel="rbf", class_weight="balanced")
    #svm = SVC(kernel="linear")
    svm.fit(X_train_est, y_train_est)
    estimators.append(svm)

print("Now to predict")

predicts = ny.asarray([clf.predict(X_test) for clf in estimators])

num_test_samples = predicts.shape[1]

print(pds.value_counts(pds.Series(y_test)))

count_dict = {}
correct_dict = {}

#
# Check how each model is doing
#
for i in range(0, fold, 1):
    accuracy = accuracy_score(y_true=y_test,
                              y_pred=predicts[i, :])
    analysis = analyze(y_test, predicts[i, :])
    print("The {}th model has accuracy: {} and {}".format(i, accuracy, analysis))


for i in range(0, num_test_samples, 1):
    pred_i = predicts[:, i]
    value_counts = pds.value_counts(pds.Series(pred_i))

    predict_vote = None
    predict_max = 0
    for itr in value_counts.iteritems():
        if itr[1] > predict_max:
            predict_vote = itr[0]
            predict_max = itr[1]

    if y_test[i] in count_dict:
        count_dict[y_test[i]] = count_dict[y_test[i]] + 1
    else:
        count_dict[y_test[i]] = 1

    if predict_vote == y_test[i]:
        if predict_vote == "752":
            print value_counts

        if predict_vote in correct_dict:
            correct_dict[predict_vote] = correct_dict[predict_vote] + 1
        else:
            correct_dict[predict_vote] =1

print(str(count_dict))
print(str(correct_dict))


