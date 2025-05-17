import pytest
from pages.signup_page import SignupPage
from test_data.env import Env
from test_data.user_creds import UserCreds


@pytest.mark.sign_up
def test_successful_signup(browser):
    signup_page = SignupPage(browser)
    signup_page.open(Env.URL_signup)
    signup_page.fill_signup_form(
        first_name=UserCreds.valid_name,
        last_name=UserCreds.valid_lastname,
        password=UserCreds.valid_password
    )
    signup_page.click_submit()

    assert not signup_page.is_error_message_present("Email address is already in use"), \
        "Unexpected error: Email already in use"
    signup_page.should_be_logged_in()

@pytest.mark.sign_up
def test_signup_existing_email(browser):
    signup_page = SignupPage(browser)
    signup_page.open(Env.URL_signup)

    signup_page.fill_signup_form(
        first_name=UserCreds.valid_name,
        last_name=UserCreds.valid_lastname,
        password=UserCreds.valid_password,
        email=UserCreds.valid_email
    )
    signup_page.click_submit()

    assert signup_page.is_error_message_present("Email address is already in use"), \
        "Expected error message not shown for existing email"

@pytest.mark.sign_up
def test_signup_missing_fields(browser):
    signup_page = SignupPage(browser)
    signup_page.open(Env.URL_signup)

    signup_page.click_submit()

    assert signup_page.is_error_message_present("User validation failed: firstName: "
                                                "Path `firstName` is required., "
                                                "lastName: Path `lastName` is required., "
                                                "email: Email is invalid, "
                                                "password: Path `password` is required."), \
        "Expected error for missing fields not displayed"

@pytest.mark.sign_up
def test_signup_invalid_email_format(browser):
    signup_page = SignupPage(browser)
    signup_page.open(Env.URL_signup)

    signup_page.fill_signup_form(
        first_name=UserCreds.valid_name,
        last_name=UserCreds.valid_lastname,
        password=UserCreds.valid_password,
        email=UserCreds.invalid_email
    )
    signup_page.click_submit()

    assert signup_page.is_error_message_present("User validation failed: email: Email is invalid"), \
        "Expected error for invalid email format not displayed"