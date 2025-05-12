import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.add_contact_page import AddContactPage


@pytest.mark.smoke
def test_verify_phone_number_field_negative(browser):
    page = AddContactPage(browser)

    browser.get("https://thinking-tester-contact-list.herokuapp.com/login")
    browser.find_element(By.ID, "email").send_keys("trusters_test@gmail.com")
    browser.find_element(By.ID, "password").send_keys("1234567")
    browser.find_element(By.ID, "submit").click()

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))

    browser.get("https://thinking-tester-contact-list.herokuapp.com/addContact")
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    contact = {
        "firstName": "John",
        "lastName": "Doe",
        "phone": "invalid_phone",
        "street": "123 Elm St",
        "city": "Metropolis",
        "postalCode": "12345",
        "birthdate": "1990-01-01"
    }
    page.fill_contact_form(contact)
    page.submit()

    error_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text

    assert "Contact validation failed: phone: Phone number is invalid" in error_text


@pytest.mark.regression
def test_input_more_than_max_chars_in_first_last_name(browser):
    page = AddContactPage(browser)

    browser.get("https://thinking-tester-contact-list.herokuapp.com/login")
    browser.find_element(By.ID, "email").send_keys("trusters_test@gmail.com")
    browser.find_element(By.ID, "password").send_keys("1234567")
    browser.find_element(By.ID, "submit").click()

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))

    browser.get("https://thinking-tester-contact-list.herokuapp.com/addContact")
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    contact = {
        "firstName": "A" * 256,
        "lastName": "B" * 256,
        "phone": "1234567890",
        "street": "123 Elm St",
        "city": "Metropolis",
        "postalCode": "12345",
        "birthdate": "1990-01-01"
    }
    page.fill_contact_form(contact)
    page.submit()

    error_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text

    assert "firstName: Path `firstName`" in error_text or "lastName: Path `lastName`" in error_text


@pytest.mark.regression
def test_input_more_than_max_chars_in_phone(browser):
    page = AddContactPage(browser)

    browser.get("https://thinking-tester-contact-list.herokuapp.com/login")
    browser.find_element(By.ID, "email").send_keys("trusters_test@gmail.com")
    browser.find_element(By.ID, "password").send_keys("1234567")
    browser.find_element(By.ID, "submit").click()

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))

    browser.get("https://thinking-tester-contact-list.herokuapp.com/addContact")
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    contact = {
        "firstName": "John",
        "lastName": "Doe",
        "phone": "1" * 256,
        "street": "123 Elm St",
        "city": "Metropolis",
        "postalCode": "12345",
        "birthdate": "1990-01-01"
    }
    page.fill_contact_form(contact)
    page.submit()

    error_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text

    assert "phone" in error_text and "longer than the maximum allowed length" in error_text


@pytest.mark.regression
def test_input_more_than_max_chars_in_postal_code(browser):
    page = AddContactPage(browser)

    browser.get("https://thinking-tester-contact-list.herokuapp.com/login")
    browser.find_element(By.ID, "email").send_keys("trusters_test@gmail.com")
    browser.find_element(By.ID, "password").send_keys("1234567")
    browser.find_element(By.ID, "submit").click()

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))

    browser.get("https://thinking-tester-contact-list.herokuapp.com/addContact")
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    contact = {
        "firstName": "John",
        "lastName": "Doe",
        "phone": "1234567890",
        "street": "123 Elm St",
        "city": "Metropolis",
        "postalCode": "123456789012345",
        "birthdate": "1990-01-01"
    }
    page.fill_contact_form(contact)
    page.submit()

    error_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text

    assert "postalCode" in error_text and "longer than the maximum allowed length" in error_text


@pytest.mark.regression
def test_submit_empty_required_fields(browser):
    page = AddContactPage(browser)

    browser.get("https://thinking-tester-contact-list.herokuapp.com/login")
    browser.find_element(By.ID, "email").send_keys("trusters_test@gmail.com")
    browser.find_element(By.ID, "password").send_keys("1234567")
    browser.find_element(By.ID, "submit").click()

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))

    browser.get("https://thinking-tester-contact-list.herokuapp.com/addContact")
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    contact = {
        "firstName": "",
        "lastName": "",
        "phone": "",
        "street": "",
        "city": "",
        "postalCode": "",
        "birthdate": ""
    }
    page.fill_contact_form(contact)
    page.submit()

    error_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text
    assert "Contact validation failed" in error_text
    assert "firstName: Path `firstName` is required." in error_text
    assert "lastName: Path `lastName` is required." in error_text


@pytest.mark.smoke
def test_cancel_contact_creation_using_cancel_button(browser):
    page = AddContactPage(browser)

    browser.get("https://thinking-tester-contact-list.herokuapp.com/login")
    browser.find_element(By.ID, "email").send_keys("trusters_test@gmail.com")
    browser.find_element(By.ID, "password").send_keys("1234567")
    browser.find_element(By.ID, "submit").click()

    WebDriverWait(browser, 5).until(EC.url_contains("/contactList"))

    browser.get("https://thinking-tester-contact-list.herokuapp.com/addContact")
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "firstName")))

    page.cancel_creation()

    WebDriverWait(browser, 5).until(
        EC.url_contains("/contactList")
    )

    assert browser.current_url == "https://thinking-tester-contact-list.herokuapp.com/contactList"
