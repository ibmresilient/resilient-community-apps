from ToolCommand import ToolCommand
import sys
import pandas as pds

HELP_STR = """
python check_imbalance -f csv_file_with_samples -p prediction_field"""

arg_str = "hf:p:"
arg_list = ["help", "csvfile", "prediction"]


class CheckImbalance(ToolCommand):
    """
    This command takes a csv file and a prediction field
    And it will check whether the samples are imbalanced
    """
    def __init__(self, help_str):
        #
        # No need to talk to a server
        #
        ToolCommand.__init__(self,
                             help_string=help_str,
                             server_tool=False)

    def do_command(self):
        filename = self.opts_dict.get("csvfile", None)
        predict = self.opts_dict.get("prediction", None)
        if filename and predict:
            dataf = pds.read_csv(filename,
                                 sep=',',
                                 # usecols=["name", "id", "description", "hostname", "incident_type_ids", "confirmed", "negative_pr_likely", "nist_attack_vectors", predict],
                                 # usecols=[predict, "id", "confirmed", "exposure_type_id"],
                                 dtype={predict: object},
                                 skipinitialspace=True,
                                 quotechar='"',
                                 error_bad_lines=True)
            print(dataf[predict].value_counts())
        else:
            print("Error with inputs: {}".format(str(self.opts_dict)))

if __name__ == "__main__":
    cmd = CheckImbalance(HELP_STR)
    cmd.run_command(sys.argv[1:], arg_str, arg_list)