import fn_machine_learning.lib.resilient_utils as resilient_utils
from fn_machine_learning.lib.ml_model_common import MlModelCommon
import os
import csv


model_name = "Logistic Regression"
csv_file = csv_file = os.path.abspath("data/bank.csv")
percentage = 0.5

model = resilient_utils.get_model(model_name)

with open(csv_file, "r") as infile:
    reader = csv.DictReader(infile)
    fields = list(reader.fieldnames)

if len(fields) > 2:
    field_idx = 0
    for field in fields:
        print("{}: {}".format(str(field_idx), field))
        field_idx = field_idx + 1
#
# gdpr_harm_risk has all NaN
#
#features=["id","plan_status","workspace", "gdpr_harm_risk", "confirmed"]
#
# This one can predict for incident
#
#features=["id","plan_status","workspace", "confirmed", "severity_code", "resolution_id"]
#predict="crimestatus_id"

features=["age","job","marital", "education", "balance", "default", "loan", "campaign", "poutcome"]
predict="y"

if model:
    # bank.csv uses this
    model.separator=';'
    model.build(csv_file=csv_file,
                features=features,
                prediction=predict,
                test_prediction=float(percentage))
    print("Done. Accuracy is {}".format(str(model.accuracy)))

    #
    # Save the model
    #
    model.save_to_file()

    saved_model = MlModelCommon.load_from_file()

    print("Loaded back")

    #
    # Create a dict for data
    #
    di = {
        "age": 28,
        "job": "services",
        "marital": "married",
        "education":"secondary",
        "default": "no",
        "balance":5678,
        "loan": "no",
        "campaign":1,
        "poutcome": "failure",
        "others": 12345
    }

    ret = saved_model.predict_result(di)

    print(str(ret))



