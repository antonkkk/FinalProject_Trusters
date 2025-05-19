import pytest
import allure
from pages.login_page import LoginPage
from test_data.env import Env
from test_data.user_creds import UserCreds
from helper.utils import generate_random_email


@allure.feature("Login functionality")
@pytest.mark.login
@pytest.mark.smoke
@pytest.mark.acceptance
@pytest.mark.regression
def test_successful_login(browser):
    login_page = LoginPage(browser)
    login_page.open(Env.URL_login)
    login_page.should_be_login_page()

    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    login_page.should_be_logged_in()


@allure.feature("Login functionality")
@pytest.mark.login
@pytest.mark.acceptance
@pytest.mark.regression
def test_login_invalid_password(browser):
    login_page = LoginPage(browser)
    login_page.open(Env.URL_login)
    login_page.should_be_login_page()

    login_page.complete_login(UserCreds.valid_email, UserCreds.invalid_password)

    login_page.should_be_login_page()
    error_text = login_page.get_error_text()
    assert "Incorrect username or password" in error_text, \
        "Expected error message for invalid password was not shown"


@allure.feature("Login functionality")
@pytest.mark.login
@pytest.mark.acceptance
@pytest.mark.regression
def test_login_invalid_email(browser):
    login_page = LoginPage(browser)
    login_page.open(Env.URL_login)
    login_page.should_be_login_page()

    unregistered_email = generate_random_email()

    login_page.complete_login(unregistered_email, UserCreds.valid_password)

    login_page.should_be_login_page()
    error_text = login_page.get_error_text()
    assert "Incorrect username or password" in error_text, \
        "Expected error message for invalid email was not shown"


@allure.feature("Login functionality")
@pytest.mark.login
@pytest.mark.regression
def test_login_empty_credentials(browser):
    login_page = LoginPage(browser)
    login_page.open(Env.URL_login)
    login_page.should_be_login_page()

    login_page.complete_login(UserCreds.empty_email, UserCreds.empty_password)

    login_page.should_be_login_page()
    error_text = login_page.get_error_text()
    assert "Incorrect username or password" in error_text, \
        "Expected error message for empty credentials was not shown"


@allure.feature("Login functionality")
@pytest.mark.login
@pytest.mark.regression
def test_login_with_empty_password(browser):
    login_page = LoginPage(browser)
    login_page.open(Env.URL_login)
    login_page.should_be_login_page()

    login_page.complete_login(UserCreds.valid_email, UserCreds.empty_password)

    login_page.should_be_login_page()
    error_text = login_page.get_error_text()
    assert "Incorrect username or password" in error_text, \
        "Expected error message for empty password was not shown"


@allure.feature("Login functionality")
@pytest.mark.login
@pytest.mark.regression
def test_login_with_empty_email(browser):
    login_page = LoginPage(browser)
    login_page.open(Env.URL_login)
    login_page.should_be_login_page()

    login_page.complete_login(UserCreds.empty_email, UserCreds.valid_password)

    login_page.should_be_login_page()
    error_text = login_page.get_error_text()
    assert "Incorrect username or password" in error_text, \
        "Expected error message for empty email was not shown"


@allure.feature("Logout functionality")
@pytest.mark.logout
@pytest.mark.smoke
@pytest.mark.acceptance
@pytest.mark.regression
def test_successful_logout(browser):
    login_page = LoginPage(browser)
    login_page.open(Env.URL_login)
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)
    login_page.should_be_logged_in()

    login_page.click_logout()

    login_page.should_be_login_page()
