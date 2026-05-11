from datetime import datetime
import time
import os
import shutil

import yaml
import requests

from fn_watsonx_analyst.config.loaders import ModelConfig


def main():
    model_list_path = "../fn_watsonx_analyst/config/model_list.txt"
    output_yaml_path = "../fn_watsonx_analyst/config/models.yaml"

    # Backup the previous models.yaml if it exists
    if os.path.exists(output_yaml_path):
        backup_path = (
            output_yaml_path + "." + str(int(datetime.now().timestamp())) + ".backup"
        )
        shutil.copy(output_yaml_path, backup_path)

    model_configs = []

    # Read the model IDs and costs from the file
    with open(model_list_path, "r", encoding="utf-8") as file:
        model_lines = file.readlines()

    for line in model_lines:
        # ignore comments
        if line[0] == "#":
            continue
        parts = line.strip().split()

        # Ignore blank lines
        if not parts:
            continue

        model_id = parts[0]
        input_cost = float(parts[1]) if len(parts) > 1 else 0.0
        output_cost = float(parts[2]) if len(parts) > 2 else input_cost

        # Query the API for model specifications
        url = \
            f"https://us-south.ml.cloud.ibm.com/ml/v1/foundation_model_specs?version=2024-03-14&filters=modelid_{model_id}"
        response = requests.get(url, timeout=5 * 60)

        body = response.json()

        if not body["resources"]:
            print(f"Failed to fetch details for model {model_id}")
            continue

        model_limits = response.json()["resources"][0]["model_limits"]
        max_sequence_length = model_limits["max_sequence_length"]
        max_output_tokens = model_limits["max_output_tokens"]

        model_config: ModelConfig = {
            "name": model_id,
            "context_length": max_sequence_length,
            "max_output_tokens": max_output_tokens,
            "input_cost": input_cost,
            "output_cost": output_cost,
        }

        model_configs.append(model_config)

        # Sleep for 0.3 seconds between queries
        time.sleep(0.3)

    with open(output_yaml_path, "w", encoding="utf-8") as yaml_file:
        for config in model_configs:
            # dump the dictionary to the yaml file, maintaining the dictionary field order
            yaml.dump([config], yaml_file, default_flow_style=False, sort_keys=False)
            yaml_file.write("\n")

if __name__ == "__main__":
    main()
