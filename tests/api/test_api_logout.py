import pytest
import allure
from helper.utils import send_request


@allure.feature("Logout functionality")
@pytest.mark.smoke
@pytest.mark.logout
def test_successful_logout(read_config, auth_token):
    logout_url = f'{read_config["URL"]}/users/logout'
    headers = {"Authorization": f"Bearer {auth_token}"}

    response = send_request("POST", logout_url, headers=headers)
    assert response.status_code == 200, \
        f"Expected logout status 200, got {response.status_code}"
