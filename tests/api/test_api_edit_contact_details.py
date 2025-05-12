import requests
from helper.send_request import send_request


#  Test positive: update all contact details fields
def test_api_01_update_cd(read_config, read_user_creds, read_contact_temp):
    URL = f'{read_config["URL"]}/users/login'
    token = send_request("POST", URL, json=read_user_creds)["token"]  # Authorization, get token

    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    contact_id = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])["_id"]  # Add Contact

    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    response = send_request(
        "PUT", URL, headers=headers, json=read_contact_temp[1])  # Update Contact details

    assert response["firstName"] == read_contact_temp[1]["firstName"]
    assert response["lastName"] == read_contact_temp[1]["lastName"]
    assert response["birthdate"] == read_contact_temp[1]["birthdate"]
    assert response["email"] == read_contact_temp[1]["email"]
    assert response["phone"] == read_contact_temp[1]["phone"]
    assert response["street1"] == read_contact_temp[1]["street1"]
    assert response["street2"] == read_contact_temp[1]["street2"]
    assert response["city"] == read_contact_temp[1]["city"]
    assert response["stateProvince"] == read_contact_temp[1]["stateProvince"]
    assert response["postalCode"] == read_contact_temp[1]["postalCode"]
    assert response["country"] == read_contact_temp[1]["country"]


#  Test positive: partial update contact details fields
def test_api_02_partial_update_cd(read_config, read_user_creds, read_contact_temp):
    URL = f'{read_config["URL"]}/users/login'
    token = send_request("POST", URL, json=read_user_creds)["token"]  # Authorization, get token

    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    contact_id = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])["_id"]  # Add Contact

    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    response = send_request(
        "PATCH", URL, headers=headers, json=read_contact_temp[2])  # Partial Update Contact details

    assert response["firstName"] == read_contact_temp[2]["firstName"]
    assert response["lastName"] == read_contact_temp[2]["lastName"]
    assert response["birthdate"] == read_contact_temp[0]["birthdate"]
    assert response["email"] == read_contact_temp[0]["email"]
    assert response["phone"] == read_contact_temp[0]["phone"]
    assert response["street1"] == read_contact_temp[0]["street1"]
    assert response["street2"] == read_contact_temp[0]["street2"]
    assert response["city"] == read_contact_temp[0]["city"]
    assert response["stateProvince"] == read_contact_temp[0]["stateProvince"]
    assert response["postalCode"] == read_contact_temp[0]["postalCode"]
    assert response["country"] == read_contact_temp[0]["country"]


#  Test negative: update contact details with empty required fields
def test_api_03_update_cd_with_empty_req_fields(read_config, read_user_creds, read_contact_temp):
    URL = f'{read_config["URL"]}/users/login'
    token = send_request("POST", URL, json=read_user_creds)["token"]  # Authorization, get token

    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    contact_id = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])["_id"]  # Add Contact

    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["firstName"] = ""
    read_contact_temp[0]["lastName"] = ""
    response = requests.put(
        URL, headers=headers, json=read_contact_temp[0])  # Update Contact details
    assert response.status_code == 400, f"Status code is not '400', response: {response.text}"


#  Test negative: update contact details with invalid Postal Code format
def test_api_04_update_cd_with_ivalid_postal_code(read_config, read_user_creds, read_contact_temp):
    URL = f'{read_config["URL"]}/users/login'
    token = send_request("POST", URL, json=read_user_creds)["token"]  # Authorization, get token

    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    contact_id = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])["_id"]  # Add Contact

    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["postalCode"] = "postcode"
    response = requests.put(
        URL, headers=headers, json=read_contact_temp[0])  # Update Contact details
    assert response.status_code == 400, f"Status code is not '400', response: {response.text}"


#  Test negative: update contact details with invalid Date of Birth format
def test_api_05_update_cd_with_ivalid_birth_date(read_config, read_user_creds, read_contact_temp):
    URL = f'{read_config["URL"]}/users/login'
    token = send_request("POST", URL, json=read_user_creds)["token"]  # Authorization, get token

    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    contact_id = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])["_id"]  # Add Contact

    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["birthdate"] = "20-12-2000"
    response = requests.put(
        URL, headers=headers, json=read_contact_temp[0])  # Update Contact details
    assert response.status_code == 400, f"Status code is not '400', response: {response.text}"


#  Test negative: update contact details with invalid Phone format
def test_api_06_update_cd_with_ivalid_phone(read_config, read_user_creds, read_contact_temp):
    URL = f'{read_config["URL"]}/users/login'
    token = send_request("POST", URL, json=read_user_creds)["token"]  # Authorization, get token

    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    contact_id = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])["_id"]  # Add Contact

    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["phone"] = "8-029-3665544"
    response = requests.put(
        URL, headers=headers, json=read_contact_temp[0])  # Update Contact details
    assert response.status_code == 400, f"Status code is not '400', response: {response.text}"


#  Test negative: update contact details with invalid Email format
def test_api_07_update_cd_with_ivalid_email(read_config, read_user_creds, read_contact_temp):
    URL = f'{read_config["URL"]}/users/login'
    token = send_request("POST", URL, json=read_user_creds)["token"]  # Authorization, get token

    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    contact_id = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])["_id"]  # Add Contact

    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["email"] = "email@"
    response = requests.put(
        URL, headers=headers, json=read_contact_temp[0])  # Update Contact details
    assert response.status_code == 400, f"Status code is not '400', response: {response.text}"


#  Test negative: update contact details with required fields >20 symbols max length
def test_api_08_update_cd_with_over_len_req_fields(read_config, read_user_creds, read_contact_temp):
    URL = f'{read_config["URL"]}/users/login'
    token = send_request("POST", URL, json=read_user_creds)["token"]  # Authorization, get token

    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    contact_id = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])["_id"]  # Add Contact

    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["firstName"] = "FirstNamemorethan20sy"
    response = requests.put(
        URL, headers=headers, json=read_contact_temp[0])  # Update Contact details
    assert response.status_code == 400, f"Status code is not '400', response: {response.text}"

    read_contact_temp[0]["firstName"] = "Emily"
    read_contact_temp[0]["lastName"] = "LastNamemorethan20sym"

    response = requests.put(
        URL, headers=headers, json=read_contact_temp[0])  # Update Contact details
    assert response.status_code == 400, f"Status code is not '400', response: {response.text}"


#  Test negative: update contact details with Postal Code >10 symbols max length
def test_api_09_update_cd_with_over_len_post_code(read_config, read_user_creds, read_contact_temp):
    URL = f'{read_config["URL"]}/users/login'
    token = send_request("POST", URL, json=read_user_creds)["token"]  # Authorization, get token

    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    contact_id = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])["_id"]  # Add Contact

    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["postalCode"] = "12345678901"
    response = requests.put(
        URL, headers=headers, json=read_contact_temp[0])  # Update Contact details
    assert response.status_code == 400, f"Status code is not '400', response: {response.text}"


#  Test negative: update contact details with Phone >15 symbols max length
def test_api_10_update_cd_with_over_len_phone(read_config, read_user_creds, read_contact_temp):
    URL = f'{read_config["URL"]}/users/login'
    token = send_request("POST", URL, json=read_user_creds)["token"]  # Authorization, get token

    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    contact_id = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])["_id"]  # Add Contact

    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["phone"] = "1234567890123456"
    response = requests.put(
        URL, headers=headers, json=read_contact_temp[0])  # Update Contact details
    assert response.status_code == 400, f"Status code is not '400', response: {response.text}"


#  Test negative: update contact details with optional fields >40 symbols max length
def test_api_11_update_cd_with_over_len_opt_fields(read_config, read_user_creds, read_contact_temp):
    URL = f'{read_config["URL"]}/users/login'
    token = send_request("POST", URL, json=read_user_creds)["token"]  # Authorization, get token

    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    contact_id = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])["_id"]  # Add Contact

    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["city"] = "MyLongCityMyLongCity MyLongCityMyLongCity"
    response = requests.put(
        URL, headers=headers, json=read_contact_temp[0])  # Update Contact details
    assert response.status_code == 400, f"Status code is not '400', response: {response.text}"

    read_contact_temp[0]["city"] = "Oldtown"
    read_contact_temp[0]["street1"] = "MyLongStreetAddress MyLongStreetAddress M"

    response = requests.put(
        URL, headers=headers, json=read_contact_temp[0])  # Update Contact details
    assert response.status_code == 400, f"Status code is not '400', response: {response.text}"
