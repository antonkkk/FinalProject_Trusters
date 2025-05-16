import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.add_contact_page import AddContactPage
from pages.login_page import LoginPage
from test_data.user_creds import UserCreds
from test_data.contact_template import ContactTemplate
from test_data.env import Env


@pytest.mark.smoke
def test_verify_phone_number_field_negative(browser):
    login_page = LoginPage(browser)
    login_page.open(Env.URL)
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))
    ac_page = AddContactPage(browser)
    ac_page.open(Env.URL_ac)

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    ContactTemplate.contact_add["phone"] = "invalid_phone"

    ac_page.fill_contact_form(ContactTemplate.contact_add)
    ac_page.submit()

    error_text = ac_page.get_error_text()

    assert "Contact validation failed: phone: Phone number is invalid" in error_text


@pytest.mark.regression
def test_input_more_than_max_chars_in_first_last_name(browser):
    login_page = LoginPage(browser)
    login_page.open(Env.URL)
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))
    ac_page = AddContactPage(browser)
    ac_page.open(Env.URL_ac)

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    ContactTemplate.contact_add["firstName"] = "A" * 256
    ContactTemplate.contact_add["lastName"] = "B" * 256

    ac_page.fill_contact_form(ContactTemplate.contact_add)
    ac_page.submit()

    error_text = ac_page.get_error_text()

    assert "firstName: Path `firstName`" in error_text or "lastName: Path `lastName`" in error_text


@pytest.mark.regression
def test_input_more_than_max_chars_in_phone(browser):
    login_page = LoginPage(browser)
    login_page.open(Env.URL)
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))
    ac_page = AddContactPage(browser)
    ac_page.open(Env.URL_ac)

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    ContactTemplate.contact_add["phone"] = "1" * 256

    ac_page.fill_contact_form(ContactTemplate.contact_add)
    ac_page.submit()

    error_text = ac_page.get_error_text()

    assert "phone" in error_text and "longer than the maximum allowed length" in error_text


@pytest.mark.regression
def test_input_more_than_max_chars_in_postal_code(browser):
    login_page = LoginPage(browser)
    login_page.open(Env.URL)
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))
    ac_page = AddContactPage(browser)
    ac_page.open(Env.URL_ac)

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    ContactTemplate.contact_add["postalCode"] = "123456789012345"

    ac_page.fill_contact_form(ContactTemplate.contact_add)
    ac_page.submit()

    error_text = ac_page.get_error_text()

    assert "postalCode" in error_text and "longer than the maximum allowed length" in error_text


@pytest.mark.regression
def test_submit_empty_required_fields(browser):
    login_page = LoginPage(browser)
    login_page.open(Env.URL)
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))
    ac_page = AddContactPage(browser)
    ac_page.open(Env.URL_ac)

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    ContactTemplate.contact_add["firstName"] = ""
    ContactTemplate.contact_add["lastName"] = ""

    ac_page.fill_contact_form(ContactTemplate.contact_add)
    ac_page.submit()

    error_text = ac_page.get_error_text()
    assert "Contact validation failed" in error_text
    assert "firstName: Path `firstName` is required." in error_text
    assert "lastName: Path `lastName` is required." in error_text


@pytest.mark.smoke
def test_cancel_contact_creation_using_cancel_button(browser):
    login_page = LoginPage(browser)
    login_page.open(Env.URL)
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))
    ac_page = AddContactPage(browser)
    ac_page.open(Env.URL_ac)

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    ac_page.cancel_creation()

    WebDriverWait(browser, 5).until(
        EC.url_contains("/contactList")
    )

    assert browser.current_url == "https://thinking-tester-contact-list.herokuapp.com/contactList"
