import pytest
import random
import string
from helper.send_request import send_request


def generate_random_email():
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"autotest_{random_part}@example.com"


@pytest.mark.sign_up
def test_successful_signup(read_config):
    url = f'{read_config["URL"]}/users'
    email = generate_random_email()
    password = "Test1234"

    payload = {
        "firstName": "Auto",
        "lastName": "Test",
        "email": email,
        "password": password
    }

    response = send_request("POST", url, json=payload)

    assert response.status_code == 201, \
        f"Expected status code 201, but got {response.status_code}"
    assert "token" in response.json()


@pytest.mark.sign_up
def test_negative_signup_with_existing_email(read_config, read_user_creds):
    url = f'{read_config["URL"]}/users'

    payload = {
        "firstName": "Test",
        "lastName": "User",
        "email": read_user_creds["email"],
        "password": read_user_creds["password"]
    }

    response = send_request("POST", url, json=payload, assert_status=False)

    assert response.status_code == 400, \
        f"Expected status code 400, but got {response.status_code}"
    assert "message" in response.json()
    assert response.json()["message"] == "Email address is already in use"
