import pytest
import json


@pytest.fixture()
def read_config():
    with open('test_data/config.json') as f:
        return json.load(f)


@pytest.fixture()
def read_user_creds():
    with open('test_data/user_creds.json') as f:
        return json.load(f)


@pytest.fixture()
def read_add_temp():
    with open('test_data/add_contact_template.json') as f:
        return json.load(f)
