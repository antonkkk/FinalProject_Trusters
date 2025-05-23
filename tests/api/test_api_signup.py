import pytest
import allure
from helper.utils import send_request
from helper.utils import generate_random_email


@allure.feature("Signup functionality")
@pytest.mark.sign_up
@pytest.mark.smoke
def test_successful_signup(read_config, read_signup_temp):
    url = f'{read_config["URL"]}/users'
    email = generate_random_email()

    payload = read_signup_temp.copy()
    payload["email"] = email

    response = send_request("POST", url, json=payload)

    assert response.status_code == 201, \
        f"Expected status code 201, but got {response.status_code}"
    assert "token" in response.json()


@allure.feature("Signup functionality")
@pytest.mark.sign_up
def test_negative_signup_with_existing_email(read_config, read_user_creds, read_signup_temp):
    url = f'{read_config["URL"]}/users'

    payload = read_signup_temp.copy()
    payload["email"] = read_user_creds["email"]
    payload["password"] = read_user_creds["password"]

    response = send_request("POST", url, json=payload, assert_status=False)

    assert response.status_code == 400, \
        f"Expected status code 400, but got {response.status_code}"
    assert "message" in response.json()
    assert response.json()["message"] == "Email address is already in use"
