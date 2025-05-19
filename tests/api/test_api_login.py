import pytest
import allure
from helper.utils import send_request


@allure.feature("Login functionality")
@pytest.mark.smoke
@pytest.mark.login
def test_successful_login(read_config, read_user_creds):
    url = f'{read_config["URL"]}/users/login'

    payload = {
        "email": read_user_creds["email"],
        "password": read_user_creds["password"]
    }

    response = send_request("POST", url, json=payload)

    assert response.status_code == 200, \
        f"Expected status code 200, but got {response.status_code}"
    assert "token" in response.json()


@allure.feature("Login functionality")
@pytest.mark.login
def test_negative_login_with_invalid_password(read_config, read_user_creds):
    url = f'{read_config["URL"]}/users/login'

    payload = {
        "email": read_user_creds["email"],
        "password": "wrongpassword"
    }

    response = send_request("POST", url, json=payload, assert_status=False)

    assert response.status_code == 401, \
        f"Expected status code 401, but got {response.status_code}"
    assert response.text.strip() == "", \
        f"Expected empty response body, got: {response.text}"


@allure.feature("Login functionality")
@pytest.mark.login
def test_negative_login_with_invalid_email(read_config):
    url = f'{read_config["URL"]}/users/login'

    payload = {
        "email": "nonexistent@example.com",
        "password": "somepassword"
    }

    response = send_request("POST", url, json=payload, assert_status=False)

    assert response.status_code == 401, \
        f"Expected status code 401, but got {response.status_code}"
    assert response.text.strip() == "", \
        f"Expected empty response body, got: {response.text}"


@allure.feature("Login functionality")
@pytest.mark.login
def test_negative_login_with_empty_password(read_config, read_user_creds):
    url = f'{read_config["URL"]}/users/login'

    payload = {
        "email": read_user_creds["email"],
        "password": ""
    }

    response = send_request("POST", url, json=payload, assert_status=False)

    assert response.status_code == 401, \
        f"Expected status code 401, but got {response.status_code}"
    assert response.text.strip() == "", \
        f"Expected empty response body, got: {response.text}"


@allure.feature("Login functionality")
@pytest.mark.login
def test_negative_login_with_empty_email(read_config):
    url = f'{read_config["URL"]}/users/login'

    payload = {
        "email": "",
        "password": "somepassword"
    }

    response = send_request("POST", url, json=payload, assert_status=False)

    assert response.status_code == 401, \
        f"Expected status code 401, but got {response.status_code}"
    assert response.text.strip() == "", \
        f"Expected empty response body, got: {response.text}"
