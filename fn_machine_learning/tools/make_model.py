from ToolCommand import ToolCommand
import sys
import csv
import fn_machine_learning.lib.resilient_utils as resilient_utils
import resilient.co3base as resilient
import os

HELP_STR = """
python get_incidents -p PASSWORD"""

arg_str = "hf:m:p:"
arg_list = ["help", "csv", "model", "percentage"]


class SampleCmd(ToolCommand):

    def do_command(self):
        model_name = self.opts_dict["model"]
        csv_file = os.path.abspath(self.opts_dict["csv"])
        print("Using csv file: " + csv_file)
        percentage = self.opts_dict["percentage"]

        model = resilient_utils.get_model(model_name)

        fields = []
        with open(csv_file, "r") as infile:
            reader = csv.DictReader(infile)
            fields = list(reader.fieldnames)

        if len(fields) > 2:
            field_idx = 0
            for field in fields:
                print("{}: {}".format(str(field_idx), field))
                field_idx = field_idx + 1

        predict_idx_str = raw_input("Predict Field:")
        features_str = raw_input("Features: ")

        predict = fields[int(predict_idx_str)].strip()
        features = []
        selected = features_str.split(',')
        for select in selected:
            idx = int(select)
            tmp = fields[idx].strip()
            features.append(tmp)

        print("Using features: [{}] to predict {}".format(str(features), predict))

        if model:
            model.build(csv_file=csv_file,
                       features=features,
                       prediction=predict,
                       test_prediction=float(percentage))
            print("Done. Accuracy is {}".format(str(model.accuracy)))



if __name__ == "__main__":
	sample_cmd = SampleCmd(HELP_STR)
	sample_cmd.run_command(sys.argv[1:], arg_str, arg_list)
