import requests
from helper.send_request import send_request


#  Test positive: delete contact by id
def test_api_01_delete_contact(read_config, read_user_creds, read_contact_temp):
    URL = f'{read_config["URL"]}/users/login'
    response = send_request("POST", URL, json=read_user_creds)
    token = response.json()["token"]  # Используем .json() для извлечения токена

    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    response = send_request("POST", URL, headers=headers, json=read_contact_temp[0])
    contact_id = response.json()["_id"]  # Используем .json() для получения ID контакта

    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    response = requests.delete(URL, headers=headers)  # Delete Contact
    assert response.status_code == 200, f"Status code is not '200', response: {response.text}"

    response = requests.get(URL, headers=headers)  # Try Get deleted Contact
    assert response.status_code == 404, f"Status code is not '404', response: {response.text}"


#  Test negative: delete unknown contact by id
def test_api_02_delete_unknown_contact(read_config, read_user_creds, read_contact_temp):
    URL = f'{read_config["URL"]}/users/login'
    response = send_request("POST", URL, json=read_user_creds)
    token = response.json()["token"]  # Используем .json() для извлечения токена

    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    response = send_request("POST", URL, headers=headers, json=read_contact_temp[0])
    contact_id = response.json()["_id"]  # Используем .json() для получения ID контакта

    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    response = requests.delete(URL, headers=headers)  # Delete Contact
    response = requests.delete(URL, headers=headers)  # Delete unknown Contact
    assert response.status_code == 404, f"Status code is not '404', response: {response.text}"
