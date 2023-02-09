import pytest
import os
import json

# collect and return the general configurations, like url's, rapidapi's host, key, etc
@pytest.fixture(scope="session")
def get_main_cfgs():
    cfg_path = os.path.join(os.curdir, "cfg", "input_configurations.json")
    with open(cfg_path) as f_cfg:
        cfg_content_json = json.load(f_cfg)
    return cfg_content_json


# collect and return the all test cases
@pytest.fixture(scope="session")
def get_test_cases():
    tests_file_path = os.path.join(os.curdir, "cfg", "test_cases.json")
    with open(tests_file_path) as f_get_tests:
        all_tests_json = json.load(f_get_tests)
    return all_tests_json