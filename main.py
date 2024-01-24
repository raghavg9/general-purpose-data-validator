import yaml
from validator import ExpectValuesValidator, ExpectRangeValidator

def load_yaml_configuration(configuration_file):
    with open(configuration_file, 'r') as file:
        return yaml.safe_load(file)

def validate_data(configuration_file, data):
    config = load_yaml_configuration(configuration_file)
    results = []

    for expectation in config['suite']['expectations']:
        if 'expect_values' in expectation:
            validator = ExpectValuesValidator({'expectations': [expectation]})
            results.extend(validator.validate(data))
        elif 'expect_range' in expectation:
            validator = ExpectRangeValidator({'expectations': [expectation]})
            results.extend(validator.validate(data))

    return results

if __name__ == "__main__":
    print("HELLO! Validation starting:)")
    configuration_file = 'config.yml'
    # Replace this with your actual data to be validated
    data = [{'WARRANTY_DURATION': 'A', 'AMOUNT': '5'}, {'WARRANTY_DURATION': 'D', 'AMOUNT': '19'}]
    validation_results = validate_data(configuration_file, data)
    for result in validation_results:
        print(result)
