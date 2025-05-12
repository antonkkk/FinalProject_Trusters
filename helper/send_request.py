import requests

def send_request(method, url, headers=None, params=None, data=None, json=None, assert_status=True):
    response = requests.request(method, url, headers=headers, params=params, data=data, json=json)

    # Пробуем вызвать .json() только чтобы при ошибке вывести текст в Exception (не возвращаем здесь словарь!)
    try:
        response_data = response.json()
    except ValueError:
        response_data = response.text

    if assert_status and response.status_code not in (200, 201):
        raise Exception(f"Request failed with status code {response.status_code}. Response: {response_data}")

    return response  # <-- именно объект response!
