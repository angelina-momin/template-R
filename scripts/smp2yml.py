import json
import yaml
import sys

def main(smp_file):
    # Read JSON file
    with open(smp_file, 'r') as json_file:
        data = json.load(json_file)

    # Convert JSON to YAML
    yaml_data = yaml.dump(data['content'])

    # Write YAML data to file
    with open('./smp.yml', 'w') as yaml_file:
        yaml_file.write(yaml_data)

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Please provide the path to the JSON file as an argument.")
        sys.exit(1)
    smp_file = sys.argv[1]
    main(smp_file)