import pytest
from helper.utils import send_request


# Test positive: update all contact details fields
@pytest.mark.edit_contact
@pytest.mark.smoke
@pytest.mark.acceptance
def test_api_01_update_cd(read_config, read_user_creds, read_contact_temp):
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
    response = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])
    contact_id = response.json()["_id"]

    # Update Contact details
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    response = send_request(
        "PUT", URL, headers=headers, json=read_contact_temp[1])

    # Check Contact values from response
    response_data = response.json()
    assert response_data["firstName"] == read_contact_temp[1]["firstName"]
    assert response_data["lastName"] == read_contact_temp[1]["lastName"]
    assert response_data["birthdate"] == read_contact_temp[1]["birthdate"]
    assert response_data["email"] == read_contact_temp[1]["email"]
    assert response_data["phone"] == read_contact_temp[1]["phone"]
    assert response_data["street1"] == read_contact_temp[1]["street1"]
    assert response_data["street2"] == read_contact_temp[1]["street2"]
    assert response_data["city"] == read_contact_temp[1]["city"]
    assert response_data["stateProvince"] == read_contact_temp[1]["stateProvince"]
    assert response_data["postalCode"] == read_contact_temp[1]["postalCode"]
    assert response_data["country"] == read_contact_temp[1]["country"]


# Test positive: partial update contact details fields
@pytest.mark.edit_contact
@pytest.mark.acceptance
@pytest.mark.regression
def test_api_02_partial_update_cd(read_config, read_user_creds, read_contact_temp):
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
    response = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])
    contact_id = response.json()["_id"]

    # Partial Update Contact details
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    response = send_request(
        "PATCH", URL, headers=headers, json=read_contact_temp[2])

    # Check Contact values from response
    response_data = response.json()
    assert response_data["firstName"] == read_contact_temp[2]["firstName"]
    assert response_data["lastName"] == read_contact_temp[2]["lastName"]
    assert response_data["email"] == read_contact_temp[0]["email"]
    assert response_data["phone"] == read_contact_temp[0]["phone"]


#  Test negative: update contact details with empty required fields
@pytest.mark.edit_contact
@pytest.mark.smoke
@pytest.mark.acceptance
def test_api_03_update_cd_with_empty_req_fields(
        read_config, read_user_creds, read_contact_temp):
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
    response = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])
    contact_id = response.json()["_id"]

    # Update Contact details
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["firstName"] = ""
    read_contact_temp[0]["lastName"] = ""
    response = send_request(
        "PUT", URL, headers=headers, json=read_contact_temp[0], assert_status=False)
    assert response.status_code == 400, (
        f"Status code is not '400', response: {response.text}")


#  Test negative: update contact details with invalid Postal Code format
@pytest.mark.edit_contact
@pytest.mark.acceptance
@pytest.mark.regression
def test_api_04_update_cd_with_invalid_postal_code(
        read_config, read_user_creds, read_contact_temp):
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
    response = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])
    contact_id = response.json()["_id"]

    # Update Contact details
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["postalCode"] = "postcode"
    response = send_request(
        "PUT", URL, headers=headers, json=read_contact_temp[0], assert_status=False)
    assert response.status_code == 400, (
        f"Status code is not '400', response: {response.text}")


#  Test negative: update contact details with invalid Date of Birth format
@pytest.mark.edit_contact
@pytest.mark.acceptance
@pytest.mark.regression
def test_api_05_update_cd_with_invalid_birth_date(
        read_config, read_user_creds, read_contact_temp):
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
    response = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])
    contact_id = response.json()["_id"]

    # Update Contact details
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["birthdate"] = "20-12-2000"
    response = send_request(
        "PUT", URL, headers=headers, json=read_contact_temp[0], assert_status=False)
    assert response.status_code == 400, (
        f"Status code is not '400', response: {response.text}")


#  Test negative: update contact details with invalid Phone format
@pytest.mark.edit_contact
@pytest.mark.acceptance
@pytest.mark.regression
def test_api_06_update_cd_with_invalid_phone(
        read_config, read_user_creds, read_contact_temp):
    # Authorization
    URL = f'{read_config["URL"]}/users/login'
    response = send_request("POST", URL, json=read_user_creds)
    token = response.json()["token"]

    # Add Contact
    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    response = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])
    contact_id = response.json()["_id"]

    # Update Contact details
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["phone"] = "8-029-3665544"
    response = send_request(
        "PUT", URL, headers=headers, json=read_contact_temp[0], assert_status=False)
    assert response.status_code == 400, (
        f"Status code is not '400', response: {response.text}")


#  Test negative: update contact details with invalid Email format
@pytest.mark.edit_contact
@pytest.mark.acceptance
@pytest.mark.regression
def test_api_07_update_cd_with_invalid_email(
        read_config, read_user_creds, read_contact_temp):
    # Authorization
    URL = f'{read_config["URL"]}/users/login'
    response = send_request("POST", URL, json=read_user_creds)
    token = response.json()["token"]

    # Add Contact
    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    response = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])
    contact_id = response.json()["_id"]

    # Update Contact details
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["email"] = "email@"
    response = send_request(
        "PUT", URL, headers=headers, json=read_contact_temp[0], assert_status=False)
    assert response.status_code == 400, (
        f"Status code is not '400', response: {response.text}")


#  Test negative: update contact details with required fields >20 symbols max length
@pytest.mark.edit_contact
@pytest.mark.acceptance
@pytest.mark.regression
def test_api_08_update_cd_with_over_len_req_fields(
        read_config, read_user_creds, read_contact_temp):
    # Authorization
    URL = f'{read_config["URL"]}/users/login'
    response = send_request("POST", URL, json=read_user_creds)
    token = response.json()["token"]

    # Add Contact
    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    response = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])
    contact_id = response.json()["_id"]

    # Update Contact Firstname
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["firstName"] = "FirstNamemorethan20sy"
    response = send_request(
        "PUT", URL, headers=headers, json=read_contact_temp[0], assert_status=False)
    assert response.status_code == 400, (
        f"Status code is not '400', response: {response.text}")

    # Update Contact Lastname
    read_contact_temp[0]["firstName"] = "Emily"
    read_contact_temp[0]["lastName"] = "LastNamemorethan20sym"
    response = send_request(
        "PUT", URL, headers=headers, json=read_contact_temp[0], assert_status=False)
    assert response.status_code == 400, (
        f"Status code is not '400', response: {response.text}")


#  Test negative: update contact details with Postal Code >10 symbols max length
@pytest.mark.edit_contact
@pytest.mark.acceptance
def test_api_09_update_cd_with_over_len_post_code(
        read_config, read_user_creds, read_contact_temp):
    # Authorization
    URL = f'{read_config["URL"]}/users/login'
    response = send_request("POST", URL, json=read_user_creds)
    token = response.json()["token"]

    # Add Contact
    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    response = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])
    contact_id = response.json()["_id"]

    # Update Contact details
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["postalCode"] = "12345678901"
    response = send_request(
        "PUT", URL, headers=headers, json=read_contact_temp[0], assert_status=False)
    assert response.status_code == 400, (
        f"Status code is not '400', response: {response.text}")


#  Test negative: update contact details with Phone >15 symbols max length
@pytest.mark.edit_contact
@pytest.mark.acceptance
def test_api_10_update_cd_with_over_len_phone(
        read_config, read_user_creds, read_contact_temp):
    # Authorization
    URL = f'{read_config["URL"]}/users/login'
    response = send_request("POST", URL, json=read_user_creds)
    token = response.json()["token"]

    # Add Contact
    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    response = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])
    contact_id = response.json()["_id"]

    # Update Contact details
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["phone"] = "1234567890123456"
    response = send_request(
        "PUT", URL, headers=headers, json=read_contact_temp[0], assert_status=False)
    assert response.status_code == 400, (
        f"Status code is not '400', response: {response.text}")


#  Test negative: update contact details with optional fields >40 symbols max length
@pytest.mark.edit_contact
@pytest.mark.acceptance
def test_api_11_update_cd_with_over_len_opt_fields(
        read_config, read_user_creds, read_contact_temp):
    # Authorization
    URL = f'{read_config["URL"]}/users/login'
    response = send_request("POST", URL, json=read_user_creds)
    token = response.json()["token"]

    # Add Contact
    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    response = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])
    contact_id = response.json()["_id"]

    # Update Contact details optional field City
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    read_contact_temp[0]["city"] = "MyLongCityMyLongCity MyLongCityMyLongCity"
    response = send_request(
        "PUT", URL, headers=headers, json=read_contact_temp[0], assert_status=False)
    assert response.status_code == 400, (
        f"Status code is not '400', response: {response.text}")

    # Update Contact details optional field Street Address 1
    read_contact_temp[0]["city"] = "Oldtown"
    read_contact_temp[0]["street1"] = "MyLongStreetAddress MyLongStreetAddress M"
    response = send_request(
        "PUT", URL, headers=headers, json=read_contact_temp[0], assert_status=False)
    assert response.status_code == 400, (
        f"Status code is not '400', response: {response.text}")
