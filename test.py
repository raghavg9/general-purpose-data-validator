import pytest
from validator import ExpectValuesValidator, ExpectRangeValidator

@pytest.fixture
def values_validator_data():
    return [{'WARRANTY_DURATION': 'A'}, {'WARRANTY_DURATION': 'C'}]

@pytest.fixture
def values_validator_config():
    return {'expectations': [{'expectation_code': 'FIRST_EXP_CODE', 'expect_values': {'fld_name': 'WARRANTY_DURATION', 'values': ['A', 'B', 'C']}}]}

@pytest.fixture
def range_validator_data():
    return [{'AMOUNT': '5'}, {'AMOUNT': '19'}]

@pytest.fixture
def range_validator_config():
    return {'expectations': [{'expectation_code': 'SECOND_EXP_CODE', 'expect_range': {'fld_name': 'AMOUNT', 'range_lower': 1, 'range_upper': 10}}]}

# def test_expect_values_validator(values_validator_data, values_validator_config):
#     validator = ExpectValuesValidator(values_validator_config)
#     results = validator.validate(values_validator_data)
#     assert "WARRANTY_DURATION = C is not in" in results[0]
#     assert "'A'" in results[0]
#     assert "'B'" in results[0]
#     assert "'C'" in results[0]

# def test_expect_range_validator(range_validator_data, range_validator_config):
#     validator = ExpectRangeValidator(range_validator_config)
#     results = validator.validate(range_validator_data)
#     expected_results = ["Record 1: AMOUNT = 19.0 is not in range 1-10"]
#     assert results == expected_results

def test_expect_values_validator(values_validator_data, values_validator_config):
    validator = ExpectValuesValidator(values_validator_config)
    results = validator.validate(values_validator_data)
    expected_message = "WARRANTY_DURATION = D is not in"
    assert any(expected_message in result for result in results)
    for val in ['A', 'B', 'C']:
        assert any(f"'{val}'" in result for result in results)

def test_expect_range_validator(range_validator_data, range_validator_config):
    validator = ExpectRangeValidator(range_validator_config)
    results = validator.validate(range_validator_data)
    expected_message = "Record 1: AMOUNT = 19.0 is not in range 1-10"
    assert expected_message in results



# def test_expect_values_validator(values_validator_data, values_validator_config):
#     # Change one of the values to 'D', which is not in the list ['A', 'B', 'C']
#     values_validator_data = [{'WARRANTY_DURATION': 'A'}, {'WARRANTY_DURATION': 'D'}]

#     validator = ExpectValuesValidator(values_validator_config)
#     results = validator.validate(values_validator_data)

#     # Check for an error message for 'WARRANTY_DURATION = D'
#     expected_message = "WARRANTY_DURATION = D is not in {'A', 'B', 'C'}"
#     assert any(expected_message in result for result in results)
