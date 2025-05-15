import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.add_contact_page import AddContactPage
from pages.login_page import LoginPage
from test_data.user_creds import UserCreds
from test_data.contact_template import ContactTemp


@pytest.mark.smoke
def test_verify_phone_number_field_negative(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))
    page = AddContactPage(browser)
    page.open()

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    ContactTemp.contact_add["phone"] = "invalid_phone"

    page.fill_contact_form(ContactTemp.contact_add)
    page.submit()

    error_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text

    assert "Contact validation failed: phone: Phone number is invalid" in error_text


@pytest.mark.regression
def test_input_more_than_max_chars_in_first_last_name(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))
    page = AddContactPage(browser)
    page.open()

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    ContactTemp.contact_add["firstName"] = "A" * 256
    ContactTemp.contact_add["lastName"] = "B" * 256

    page.fill_contact_form(ContactTemp.contact_add)
    page.submit()

    error_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text

    assert "firstName: Path `firstName`" in error_text or "lastName: Path `lastName`" in error_text


@pytest.mark.regression
def test_input_more_than_max_chars_in_phone(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))
    page = AddContactPage(browser)
    page.open()

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    ContactTemp.contact_add["phone"] = "1" * 256

    page.fill_contact_form(ContactTemp.contact_add)
    page.submit()

    error_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text

    assert "phone" in error_text and "longer than the maximum allowed length" in error_text


@pytest.mark.regression
def test_input_more_than_max_chars_in_postal_code(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))
    page = AddContactPage(browser)
    page.open()

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    ContactTemp.contact_add["postalCode"] = "123456789012345"

    page.fill_contact_form(ContactTemp.contact_add)
    page.submit()

    error_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text

    assert "postalCode" in error_text and "longer than the maximum allowed length" in error_text


@pytest.mark.regression
def test_submit_empty_required_fields(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))
    page = AddContactPage(browser)
    page.open()

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    ContactTemp.contact_add["firstName"] = ""
    ContactTemp.contact_add["lastName"] = ""

    page.fill_contact_form(ContactTemp.contact_add)
    page.submit()

    error_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text
    assert "Contact validation failed" in error_text
    assert "firstName: Path `firstName` is required." in error_text
    assert "lastName: Path `lastName` is required." in error_text


@pytest.mark.smoke
def test_cancel_contact_creation_using_cancel_button(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))
    page = AddContactPage(browser)
    page.open()

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    page.cancel_creation()

    WebDriverWait(browser, 5).until(
        EC.url_contains("/contactList")
    )

    assert browser.current_url == "https://thinking-tester-contact-list.herokuapp.com/contactList"
