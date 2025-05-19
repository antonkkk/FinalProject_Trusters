import pytest
import allure
from helper.utils import send_request


# Test positive: delete contact by id
@allure.feature("Delete functionality")
@pytest.mark.delete_contact
@pytest.mark.smoke
@pytest.mark.acceptance
@pytest.mark.regression
def test_api_01_delete_contact(read_config, read_user_creds, read_contact_temp):
    # Authorization
    URL = f'{read_config["URL"]}/users/login'
    response = send_request("POST", URL, json=read_user_creds)
    token = response.json()["token"]

    # Add contact
    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    response = send_request("POST", URL, headers=headers, json=read_contact_temp[0])
    contact_id = response.json()["_id"]

    # Delete contact
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    send_request("DELETE", URL, headers=headers)

    # Try Get deleted Contact
    response = send_request("GET", URL, headers=headers, assert_status=False)
    assert response.status_code == 404, f"Status code is not '404', response: {response.text}"


# Test negative: delete unknown contact by id
@allure.feature("Delete functionality")
@pytest.mark.delete_contact
@pytest.mark.regression
def test_api_02_delete_unknown_contact(read_config, read_user_creds, read_contact_temp):
    # Authorization
    URL = f'{read_config["URL"]}/users/login'
    response = send_request("POST", URL, json=read_user_creds)
    token = response.json()["token"]

    # Add contact
    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    response = send_request("POST", URL, headers=headers, json=read_contact_temp[0])
    contact_id = response.json()["_id"]

    # Delete contact
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    send_request("DELETE", URL, headers=headers)

    # Delete unknown contact
    response = send_request("DELETE", URL, headers=headers, assert_status=False)
    assert response.status_code == 404, f"Status code is not '404', response: {response.text}"
