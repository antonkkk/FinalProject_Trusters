import json
import pytest


@pytest.fixture()
def read_config():
    with open('test_data/config.json', encoding='utf-8') as f:
        return json.load(f)


@pytest.fixture()
def read_user_creds():
    with open('test_data/user_creds.json', encoding='utf-8') as f:
        return json.load(f)


@pytest.fixture()
def read_contact_temp():
    with open('test_data/add_contact_template.json', encoding='utf-8') as f:
        return json.load(f)
