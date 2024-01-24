class Validator:
    def __init__(self, configuration):
        self.configuration = configuration
        self.validate_configuration()

    def validate_configuration(self):
        if 'expectations' not in self.configuration:
            raise ValueError("Configuration must include expectations.")

    def validate(self, data):
        raise NotImplementedError

class ExpectValuesValidator(Validator):
    def validate(self, data):
        results = []
        for expectation in self.configuration['expectations']:
            details = expectation.get('expect_values')
            if not details:
                continue

            fld_name = details['fld_name']
            expected_values = set(details['values'])
            for record in data:
                if record[fld_name] not in expected_values:
                    results.append(f"Record {data.index(record)}: {fld_name} = {record[fld_name]} is not in {expected_values}")
        return results

class ExpectRangeValidator(Validator):
    def validate(self, data):
        results = []
        for expectation in self.configuration['expectations']:
            details = expectation.get('expect_range')
            if not details:
                continue

            fld_name = details['fld_name']
            range_min = details['range_lower']
            range_max = details['range_upper']
            for record in data:
                value = float(record[fld_name])
                if not (range_min <= value <= range_max):
                    results.append(f"Record {data.index(record)}: {fld_name} = {value} is not in range {range_min}-{range_max}")
        return results