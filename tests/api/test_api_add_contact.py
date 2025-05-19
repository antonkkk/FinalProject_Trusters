import pytest
import allure
from helper.utils import send_request


@allure.feature("Add contact functionality")
@pytest.mark.add_contact
@pytest.mark.smoke
@pytest.mark.acceptance
def test_add_contact_with_all_valid_fields(read_config, read_user_creds):
    login_url = f'{read_config["URL"]}/users/login'
    response = send_request("POST", login_url, json=read_user_creds)
    token = response.json()["token"]

    url = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    contact = {
        "firstName": "John",
        "lastName": "Doe",
        "phone": "1234567890",
        "street": "123 Elm St",
        "city": "Metropolis",
        "postalCode": "12345",
        "birthdate": "1990-01-01"
    }
    response = send_request("POST", url, headers=headers, json=contact)
    assert response.status_code in (200, 201), f"Failed to add contact: {response.text}"


@allure.feature("Add contact functionality")
@pytest.mark.add_contact
@pytest.mark.regression
def test_submit_with_invalid_email_format(read_config, read_user_creds):
    login_url = f'{read_config["URL"]}/users/login'
    response = send_request("POST", login_url, json=read_user_creds)
    token = response.json()["token"]

    url = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    contact = {
        "firstName": "John",
        "lastName": "Doe",
        "phone": "1234567890",
        "email": "invalid_email",
        "street": "123 Elm St"
    }
    response = send_request("POST", url, headers=headers, json=contact, assert_status=False)
    assert response.status_code == 400
    assert "email" in response.json()["errors"]


@allure.feature("Add contact functionality")
@pytest.mark.add_contact
@pytest.mark.regression
def test_verify_invalid_birthdate_format(read_config, read_user_creds):
    login_url = f'{read_config["URL"]}/users/login'
    response = send_request("POST", login_url, json=read_user_creds)
    token = response.json()["token"]

    url = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    contact = {
        "firstName": "John",
        "lastName": "Doe",
        "birthdate": "invalid_date"
    }
    response = send_request("POST", url, headers=headers, json=contact, assert_status=False)
    assert response.status_code == 400
    assert "birthdate" in response.json()["errors"]


@allure.feature("Add contact functionality")
@pytest.mark.add_contact
@pytest.mark.acceptance
@pytest.mark.regression
def test_add_contact_with_only_required_fields(read_config, read_user_creds):
    login_url = f'{read_config["URL"]}/users/login'
    response = send_request("POST", login_url, json=read_user_creds)
    token = response.json()["token"]

    url = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    contact = {
        "firstName": "John",
        "lastName": "Doe"
    }
    response = send_request("POST", url, headers=headers, json=contact)
    assert response.status_code in (200, 201), f"Failed to add contact: {response.text}"
