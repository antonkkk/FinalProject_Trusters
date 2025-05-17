import pytest
from pages.signup_page import SignupPage
from test_data.env import Env
from test_data.user_creds import UserCreds


@pytest.mark.sign_up
def test_successful_signup(browser):
    signup_page = SignupPage(browser)
    signup_page.open(Env.URL_signup)
    signup_page.fill_signup_form(
        first_name=UserCreds.signup_valid_name,
        last_name=UserCreds.signup_valid_lastname,
        password=UserCreds.signup_valid_pass
    )
    signup_page.click_submit()

    assert not signup_page.is_error_message_present(), "Unexpected error: Email already in use"
    signup_page.should_be_logged_in()
