import requests
from helper.send_request import send_request


def test_api_01_get_contact_details(read_config, read_user_creds, read_add_temp):
    URL = f'{read_config["URL"]}/users/login'
    token = send_request("POST", URL, json=read_user_creds)["token"]  # Authorization, get token
    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    contact_id = send_request("POST", URL, headers=headers, json=read_add_temp)["_id"]  # Add cont
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    response = send_request("GET", URL, headers=headers) # Check Get Contact details
    assert response
