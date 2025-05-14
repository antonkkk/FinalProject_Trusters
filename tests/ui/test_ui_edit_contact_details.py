import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.contact_details_page import ContactDetailsPage
from pages.contact_list_page import ContactListPage
from pages.edit_contact_details_page import EditContactPage
from pages.login_page import LoginPage
from test_data.user_creds import UserCreds


@pytest.mark.contact_details
@pytest.mark.smoke
@pytest.mark.acceptance
# Test positive: open Edit Contact page
def test_ui_01_open_edit_contact_details(browser):
    # Authorization
    login_page = LoginPage(browser)
    login_page.open()
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    # Open Contact List page, select any contact item
    contact_list_page = ContactListPage(browser)
    contact_list_page.open()
    contact_item = contact_list_page.select_any_contact()
    contact_item.click()

    # Open Contact Details page, click Edit Contact button
    contact_details_page = ContactDetailsPage(browser)
    contact_details_page.open()
    edit_contact_button = WebDriverWait(
        browser, 10).until(EC.visibility_of_element_located((By.ID, 'edit-contact')))
    edit_contact_button.click()

    # Check Edit Contact page
    header = browser.find_element(By.XPATH, "//h1")
    assert header.text == "Edit Contact"


@pytest.mark.contact_details
@pytest.mark.smoke
@pytest.mark.acceptance
# Test positive: submit changes on Edit Contact page
def test_ui_02_submit_edit_contact_changes(browser):
    # Authorization
    login_page = LoginPage(browser)
    login_page.open()
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    # Open Contact List page, select any contact item
    contact_list_page = ContactListPage(browser)
    contact_list_page.open()
    contact_item = contact_list_page.select_any_contact()
    contact_item.click()

    # Open Contact Details page, click Edit Contact button
    contact_details_page = ContactDetailsPage(browser)
    contact_details_page.open()
    edit_contact_button = WebDriverWait(
        browser, 10).until(EC.visibility_of_element_located((By.ID, 'edit-contact')))
    edit_contact_button.click()

    # Open Edit Contact page
    edit_contact_page = EditContactPage(browser)
    edit_contact_page.open()

    contact = {
        "firstName": "1testName",
        "lastName": "2testName",
        "birthdate": "1955-05-05",
        "email": "test_new@email.com",
        "phone": "8997777777",
        "street1": "1testStreet",
        "street2": "2testStreet",
        "city": "testCity",
        "stateProvince": "testProvince",
        "postalCode": "00005",
        "country": "testCountry"
    }

    # Clear and fill all Edit Contact page fields
    edit_contact_page.wait_all_fields_visible()
    edit_contact_page.clear_form()

    edit_contact_page.fill_edit_contact_form(contact)
    edit_contact_page.click_submit_button()

    # Open Contact Details page
    contact_details_page = ContactDetailsPage(browser)
    contact_details_page.open()
    header = WebDriverWait(
        browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='Contact Details']")))
    assert header.text == "Contact Details"

    # Check new values on Contact Details page
    contact_details_page.wait_all_fields_visible()
    assert contact_details_page.check_values(contact)


@pytest.mark.contact_details
@pytest.mark.regression
@pytest.mark.acceptance
# Test negative: cancel changes on Edit Contact page
def test_ui_03_cancel_edit_contact_changes(browser):
    # Authorization
    login_page = LoginPage(browser)
    login_page.open()
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    # Open Contact List page, select any contact item
    contact_list_page = ContactListPage(browser)
    contact_list_page.open()
    contact_item = contact_list_page.select_any_contact()
    contact_item.click()

    # Open Contact Details page, click Edit Contact button
    contact_details_page = ContactDetailsPage(browser)
    contact_details_page.open()
    edit_contact_button = WebDriverWait(
        browser, 10).until(EC.visibility_of_element_located((By.ID, 'edit-contact')))
    edit_contact_button.click()

    # Open Edit Contact page
    edit_contact_page = EditContactPage(browser)
    edit_contact_page.open()

    contact = {
        "firstName": "cancelName",
        "lastName": "cancelName",
        "birthdate": "1000-05-05",
        "email": "test_cancel@email.com",
        "phone": "800000000",
        "street1": "1cancelStreet",
        "street2": "2cancelStreet",
        "city": "cancelCity",
        "stateProvince": "cancelProvince",
        "postalCode": "09990",
        "country": "cancelCountry"
    }

    # Clear and fill all Edit Contact page fields
    edit_contact_page.wait_all_fields_visible()
    edit_contact_page.clear_form()

    edit_contact_page.fill_edit_contact_form(contact)
    edit_contact_page.click_cancel_button()

    # Open Contact Details page
    contact_details_page = ContactDetailsPage(browser)
    contact_details_page.open()

    # Check new values are not applied on Contact Details page
    contact_details_page.wait_all_fields_visible()
    assert not contact_details_page.check_values(contact)


@pytest.mark.contact_details
@pytest.mark.smoke
@pytest.mark.acceptance
# Test positive: open Edit Contact page
def test_ui_04_submit_edit_contact_with_empty_req_fields(browser):
    # Authorization
    login_page = LoginPage(browser)
    login_page.open()
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    # Open Contact List page, select any contact item
    contact_list_page = ContactListPage(browser)
    contact_list_page.open()
    contact_item = contact_list_page.select_any_contact()
    contact_item.click()

    # Open Contact Details page, click Edit Contact button
    contact_details_page = ContactDetailsPage(browser)
    contact_details_page.open()
    edit_contact_button = WebDriverWait(
        browser, 10).until(EC.visibility_of_element_located((By.ID, 'edit-contact')))
    edit_contact_button.click()

    # Open Edit Contact page
    edit_contact_page = EditContactPage(browser)
    edit_contact_page.open()

    # Fill empty required fields on Edit Contact page
    edit_contact_page.wait_all_fields_visible()
    edit_contact_page.clear_form()
    edit_contact_page.click_submit_button()

    error_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text
    assert "Validation failed" in error_text
    assert "firstName: Path `firstName` is required." in error_text
    assert "lastName: Path `lastName` is required." in error_text
