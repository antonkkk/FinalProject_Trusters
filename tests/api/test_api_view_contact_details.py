import requests
from helper.send_request import send_request


# Test positive: get contact details by id
def test_api_01_view_contact_details(
        read_config, read_user_creds, read_contact_temp):
    # Авторизация
    URL = f'{read_config["URL"]}/users/login'
    response = send_request(
        "POST", URL, json=read_user_creds)  # Исправлено: вызов send_request
    token = response.json()["token"]  # Исправлено: теперь используем .json()

    # Добавление контакта
    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    response = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])  # send_request
    contact_id = response.json()["_id"]  # Исправлено: теперь используем .json()

    # Получение контакта по id
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    response = send_request("GET", URL, headers=headers)  # send_request
    assert response.json()["_id"] == contact_id  # Исправлено: используем .json()


# Test negative: get unknown contact details by id
def test_api_02_view_unknown_contact_details(
        read_config, read_user_creds, read_contact_temp):
    # Авторизация
    URL = f'{read_config["URL"]}/users/login'
    response = send_request(
        "POST", URL, json=read_user_creds)  # Исправлено: вызов send_request
    token = response.json()["token"]  # Исправлено: теперь используем .json()

    # Добавление контакта
    URL = f'{read_config["URL"]}/contacts'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}'
    }
    response = send_request(
        "POST", URL, headers=headers, json=read_contact_temp[0])  # send_request
    contact_id = response.json()["_id"]  # Исправлено: теперь используем .json()

    # Удаление контакта
    URL = f'{read_config["URL"]}/contacts/{contact_id}'
    requests.delete(URL, headers=headers)  # Стандартный requests для DELETE

    # Попытка получить удалённый контакт
    response = requests.get(URL, headers=headers)  # Стандартный requests для GET
    assert response.status_code == 404, (
        f"Status code is not '404', response: {response.text}")
