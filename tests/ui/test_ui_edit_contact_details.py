import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.contact_details_page import ContactDetailsPage
from pages.contact_list_page import ContactListPage
from pages.edit_contact_details_page import EditContactPage
from pages.login_page import LoginPage
from test_data.user_creds import UserCreds
from test_data.contact_template import ContactTemp


@pytest.mark.contact_details
@pytest.mark.smoke
@pytest.mark.acceptance
# Test positive: Open Edit Contact page
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
# Test positive: Submit changes on Edit Contact page
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

    # Clear and fill all Edit Contact page fields
    edit_contact_page.wait_all_fields_visible()
    edit_contact_page.clear_form()

    edit_contact_page.fill_edit_contact_form(ContactTemp.contact_edit)
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
    assert contact_details_page.check_values(ContactTemp.contact_edit)


@pytest.mark.contact_details
@pytest.mark.regression
@pytest.mark.acceptance
# Test positive: Cancel changes on Edit Contact page
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

    # Clear and fill all Edit Contact page fields
    edit_contact_page.wait_all_fields_visible()
    edit_contact_page.clear_form()

    edit_contact_page.fill_edit_contact_form(ContactTemp.contact_cancel)
    edit_contact_page.click_cancel_button()

    # Open Contact Details page
    contact_details_page = ContactDetailsPage(browser)
    contact_details_page.open()

    # Check new values are not applied on Contact Details page
    contact_details_page.wait_all_fields_visible()
    assert not contact_details_page.check_values(ContactTemp.contact_cancel)


@pytest.mark.contact_details
@pytest.mark.smoke
@pytest.mark.acceptance
# Test negative: Submit Edit Contact form with empty required fields
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

    # Make empty required fields on Edit Contact page
    edit_contact_page.wait_all_fields_visible()
    edit_contact_page.clear_form()
    edit_contact_page.click_submit_button()

    # Check error message appears on Edit Contact page
    error_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text
    assert "Validation failed" in error_text
    assert "firstName: Path `firstName` is required." in error_text, "Firstname validation failed"
    assert "lastName: Path `lastName` is required." in error_text, "Lastname validation failed"


@pytest.mark.contact_details
@pytest.mark.regression
@pytest.mark.acceptance
# Test negative: Submit Edit Contact form with invalid format Phone, Date of Birth, Email, Postal Code
def test_ui_05_submit_edit_contact_with_invalid_format_values(browser):
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

    # Clear and fill all Edit Contact page fields
    edit_contact_page.wait_all_fields_visible()
    edit_contact_page.clear_form()

    ContactTemp.contact_edit["postalCode"] = "postalcode"
    ContactTemp.contact_edit["phone"] = "8-029-3665544"
    ContactTemp.contact_edit["email"] = "email@"
    ContactTemp.contact_edit["birthdate"] = "20-12-2000"

    edit_contact_page.fill_edit_contact_form(ContactTemp.contact_edit)
    edit_contact_page.click_submit_button()

    # Check error message appears on Edit Contact page
    error_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text
    assert "Validation failed" in error_text
    assert "postalCode: Postal code is invalid" in error_text, "Postal Code validation failed"
    assert "phone: Phone number is invalid" in error_text, "Phone validation failed"
    assert "email: Email is invalid" in error_text, "Email validation failed"
    assert "birthdate: Birthdate is invalid" in error_text, "Date of Birth validation failed"


@pytest.mark.contact_details
@pytest.mark.acceptance
# Test negative: Submit required fields with over max length values
def test_ui_06_submit_edit_required_fields_with_over_len_values(browser):
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

    # Clear and fill all Edit Contact page fields
    edit_contact_page.wait_all_fields_visible()
    edit_contact_page.clear_form()

    ContactTemp.contact_edit["firstName"] = "FirstNamemorethan20sy"
    ContactTemp.contact_edit["lastName"] = "LastNamemorethan20sym"

    edit_contact_page.fill_edit_contact_form(ContactTemp.contact_edit)
    edit_contact_page.click_submit_button()

    # Check error message appears on Edit Contact page
    error_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text
    assert "Validation failed" in error_text
    assert "lastName: Path `lastName`" in error_text, "Lastname field validation failed"
    assert "firstName: Path `firstName`" in error_text, "Firstname field validation failed"
    assert "is longer than the maximum allowed length (20)" in error_text


@pytest.mark.contact_details
@pytest.mark.acceptance
# Test negative: Submit optional fields with over max length values
def test_ui_07_submit_edit_optional_fields_with_over_len_values(browser):
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

    # Clear and fill all Edit Contact page fields
    edit_contact_page.wait_all_fields_visible()
    edit_contact_page.clear_form()

    ContactTemp.contact_edit["postalCode"] = "12345678901"
    ContactTemp.contact_edit["phone"] = "1234567890123456"
    ContactTemp.contact_edit["city"] = "MyLongCityMyLongCity MyLongCityMyLongCity"

    edit_contact_page.fill_edit_contact_form(ContactTemp.contact_edit)
    edit_contact_page.click_submit_button()

    # Check error message appears on Edit Contact page
    error_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text
    assert "Validation failed" in error_text
    assert (f"postalCode: Path `postalCode` (`{ContactTemp.contact_edit["postalCode"]}`) is longer"
            f" than the maximum allowed length (10)") in error_text, "Postal Code validation failed"
    assert (f"city: Path `city` (`{ContactTemp.contact_edit["city"]}`) is longer"
            f" than the maximum allowed length (40)") in error_text, "City validation failed"
    assert (f"phone: Path `phone` (`{ContactTemp.contact_edit["phone"]}`) is longer"
            f" than the maximum allowed length (15)") in error_text, "Phone validation failed"
