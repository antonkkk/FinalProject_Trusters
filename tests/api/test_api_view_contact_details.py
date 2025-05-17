import pytest
from helper.utils import send_request


# Test positive: get contact details by id
@pytest.mark.contact_details
@pytest.mark.smoke
@pytest.mark.acceptance
def test_api_01_view_contact_details(
        read_config, read_user_creds, read_contact_temp):
    # Authorization
    URL = f'{read_config["URL"]}/users/login'
    response = send_request(
        "POST", URL, json=read_user_creds)
    token = response.json()["token"]

    # Add contact
    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    response = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])
    contact_id = response.json()["_id"]

    # Get Contact by id
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    response = send_request("GET", URL, headers=headers)
    assert response.json()["_id"] == contact_id


# Test negative: get unknown contact details by id
@pytest.mark.contact_details
@pytest.mark.regression
@pytest.mark.acceptance
def test_api_02_view_unknown_contact_details(
        read_config, read_user_creds, read_contact_temp):
    # Authorization
    URL = f'{read_config["URL"]}/users/login'
    response = send_request(
        "POST", URL, json=read_user_creds)
    token = response.json()["token"]

    # Add contact
    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    response = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])
    contact_id = response.json()["_id"]
    # Delete Contact
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    send_request("DELETE", URL, headers=headers)

    # Try to get deleted Contact
    response = send_request("GET", URL, headers=headers, assert_status=False)
    assert response.status_code == 404, (
       f"Status code is not '404', response: {response.text}")
