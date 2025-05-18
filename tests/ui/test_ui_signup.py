import pytest
from pages.signup_page import SignupPage
from test_data.env import Env
from test_data.user_creds import UserCreds


@pytest.mark.sign_up
@pytest.mark.smoke
@pytest.mark.acceptance
@pytest.mark.regression
def test_successful_signup(browser):
    signup_page = SignupPage(browser)
    signup_page.open(Env.URL_signup)
    signup_page.should_be_signup_page()

    signup_page.fill_signup_form(
        first_name=UserCreds.valid_firstname,
        last_name=UserCreds.valid_lastname,
        password=UserCreds.valid_password
    )
    signup_page.click_submit()

    error_text = signup_page.get_error_text()
    assert "Email address is already in use" not in error_text, \
        "Unexpected error: Email already in use"


@pytest.mark.sign_up
@pytest.mark.acceptance
@pytest.mark.regression
def test_signup_existing_email(browser):
    signup_page = SignupPage(browser)
    signup_page.open(Env.URL_signup)
    signup_page.should_be_signup_page()

    signup_page.fill_signup_form(
        first_name=UserCreds.valid_firstname,
        last_name=UserCreds.valid_lastname,
        password=UserCreds.valid_password,
        email=UserCreds.valid_email
    )
    signup_page.click_submit()

    signup_page.should_be_signup_page()
    error_text = signup_page.get_error_text()
    assert "Email address is already in use" in error_text, \
        "Expected error message not shown for existing email"


@pytest.mark.sign_up
@pytest.mark.regression
def test_signup_missing_fields(browser):
    signup_page = SignupPage(browser)
    signup_page.open(Env.URL_signup)
    signup_page.should_be_signup_page()

    signup_page.fill_signup_form(
        first_name=UserCreds.valid_firstname,
        last_name="",
        email=UserCreds.empty_email,
        password=UserCreds.empty_password
    )

    signup_page.click_submit()

    signup_page.should_be_signup_page()
    error_text = signup_page.get_error_text()
    assert "lastName: Path `lastName` is required" in error_text, \
        "The error does not highlight missing Last Name"
    assert "password: Path `password` is required" in error_text, \
        "The error does not highlight missing password"
    assert "email: Email is invalid" in error_text, \
        "The error does not highlight missing email"


@pytest.mark.sign_up
@pytest.mark.regression
def test_signup_invalid_email_format(browser):
    signup_page = SignupPage(browser)
    signup_page.open(Env.URL_signup)
    signup_page.should_be_signup_page()

    signup_page.fill_signup_form(
        first_name=UserCreds.valid_firstname,
        last_name=UserCreds.valid_lastname,
        password=UserCreds.valid_password,
        email=UserCreds.invalid_format_email
    )
    signup_page.click_submit()

    signup_page.should_be_signup_page()
    error_text = signup_page.get_error_text()
    assert "User validation failed: email: Email is invalid" in error_text, \
        "Expected error for invalid email format not displayed"
