import json
import pytest
from selenium import webdriver
from helper.send_request import send_request


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()  # Или другой браузер
    yield driver
    driver.quit()


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


@pytest.fixture()
def read_signup_temp():
    with open('test_data/signup.json', encoding='utf-8') as f:
        return json.load(f)


@pytest.fixture(scope="function")
def auth_token():
    with open('test_data/config.json', encoding='utf-8') as cfg_file:
        config = json.load(cfg_file)
    with open('test_data/user_creds.json', encoding='utf-8') as creds_file:
        creds = json.load(creds_file)

    login_url = f'{config["URL"]}/users/login'
    payload = {
        "email": creds["email"],
        "password": creds["password"]
    }

    response = send_request("POST", login_url, json=payload)
    assert response.status_code == 200, \
        f"Login failed with status code {response.status_code}"

    token = response.json().get("token")
    assert token, "Login response did not contain token"
    return token
