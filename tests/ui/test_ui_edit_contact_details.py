import pytest
import allure
from selenium.webdriver.common.by import By
from pages.contact_details_page import ContactDetailsPage
from pages.contact_list_page import ContactListPage
from pages.edit_contact_details_page import EditContactPage
from pages.login_page import LoginPage
from test_data.user_creds import UserCreds
from test_data.contact_template import ContactTemplate
from test_data.env import Env


# Test positive: Open Edit Contact page
@allure.feature("Edit functionality")
@pytest.mark.edit_contact
@pytest.mark.smoke
@pytest.mark.acceptance
def test_ui_01_open_edit_contact_details(browser):
    # Authorization
    login_page = LoginPage(browser)
    login_page.open(Env.URL)
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    # Open Contact List page, select any contact item
    cl_page = ContactListPage(browser)
    cl_page.open(Env.URL_cl)
    contact_item = cl_page.select_any_contact()
    contact_item.click()

    # Open Contact Details page, click Edit Contact button
    cd_page = ContactDetailsPage(browser)
    cd_page.open(Env.URL_cd)
    edit_contact_button = cd_page.get_element(cd_page.edit_button)
    edit_contact_button.click()

    # Check Edit Contact page
    header = browser.find_element(By.XPATH, "//h1")
    assert header.text == "Edit Contact"


# Test positive: Submit changes on Edit Contact page
@allure.feature("Edit functionality")
@pytest.mark.edit_contact
@pytest.mark.smoke
@pytest.mark.acceptance
@pytest.mark.regression
def test_ui_02_submit_edit_contact_changes(browser):
    # Authorization
    login_page = LoginPage(browser)
    login_page.open(Env.URL)
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    # Open Contact List page, select any contact item
    cl_page = ContactListPage(browser)
    cl_page.open(Env.URL_cl)
    contact_item = cl_page.select_any_contact()
    contact_item.click()

    # Open Contact Details page, click Edit Contact button
    cd_page = ContactDetailsPage(browser)
    cd_page.open(Env.URL_cd)
    edit_contact_button = cd_page.get_element(cd_page.edit_button)
    edit_contact_button.click()

    # Open Edit Contact page
    ec_page = EditContactPage(browser)
    ec_page.open(Env.URL_ec)
    browser.implicitly_wait(10)

    # Clear and fill all Edit Contact page fields
    ec_page.wait_all_fields_visible()
    ec_page.wait_required_fields_not_empty()
    ec_page.clear_form()

    ec_page.fill_contact_form(ContactTemplate.contact_edit)
    ec_page.click_submit_button()

    # Open Contact Details page
    cd_page = ContactDetailsPage(browser)
    cd_page.open(Env.URL_cd)
    header = cd_page.get_element(cd_page.header)
    assert header.text == "Contact Details"

    # Check new values on Contact Details page
    cd_page.wait_all_cd_fields_not_empty()
    assert cd_page.check_values(ContactTemplate.contact_edit)


# Test positive: Cancel changes on Edit Contact page
@allure.feature("Edit functionality")
@pytest.mark.edit_contact
@pytest.mark.regression
@pytest.mark.acceptance
def test_ui_03_cancel_edit_contact_changes(browser):
    # Authorization
    login_page = LoginPage(browser)
    login_page.open(Env.URL)
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    # Open Contact List page, select any contact item
    cl_page = ContactListPage(browser)
    cl_page.open(Env.URL_cl)
    contact_item = cl_page.select_any_contact()
    contact_item.click()

    # Open Contact Details page, click Edit Contact button
    cd_page = ContactDetailsPage(browser)
    cd_page.open(Env.URL_cd)
    edit_contact_button = cd_page.get_element(cd_page.edit_button)
    edit_contact_button.click()

    # Open Edit Contact page
    ec_page = EditContactPage(browser)
    ec_page.open(Env.URL_ec)
    browser.implicitly_wait(10)

    # Clear and fill Edit Contact page required fields
    ec_page.wait_all_fields_visible()
    ec_page.clear_required_fields()

    ec_page.fill_required_fields(ContactTemplate.contact_cancel)
    ec_page.click_cancel_button()

    # Open Contact Details page
    cd_page = ContactDetailsPage(browser)
    cd_page.open(Env.URL_cd)

    # Check new values are not applied on Contact Details page
    cd_page.wait_required_fields_not_empty()
    assert not cd_page.check_required_fields(ContactTemplate.contact_cancel)


# Test negative: Submit Edit Contact form with empty required fields
@allure.feature("Edit functionality")
@pytest.mark.edit_contact
@pytest.mark.smoke
@pytest.mark.acceptance
@pytest.mark.regression
def test_ui_04_submit_edit_contact_with_empty_req_fields(browser):
    # Authorization
    login_page = LoginPage(browser)
    login_page.open(Env.URL)
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    # Open Contact List page, select any contact item
    cl_page = ContactListPage(browser)
    cl_page.open(Env.URL_cl)
    contact_item = cl_page.select_any_contact()
    contact_item.click()

    # Open Contact Details page, click Edit Contact button
    cd_page = ContactDetailsPage(browser)
    cd_page.open(Env.URL_cd)
    edit_contact_button = cd_page.get_element(cd_page.edit_button)
    edit_contact_button.click()

    # Open Edit Contact page
    ec_page = EditContactPage(browser)
    ec_page.open(Env.URL_ec)

    # Make empty required fields on Edit Contact page
    ec_page.wait_required_fields_not_empty()
    ec_page.clear_required_fields()
    ec_page.click_submit_button()

    # Check error message appears on Edit Contact page
    error_text = ec_page.get_error_text()
    assert "Validation failed" in error_text
    assert "firstName: Path `firstName` is required." in error_text, "Firstname validation failed"
    assert "lastName: Path `lastName` is required." in error_text, "Lastname validation failed"


# Test negative: Submit Edit Contact form with invalid format Phone, Birth Date, Email, Postal Code
@allure.feature("Edit functionality")
@pytest.mark.edit_contact
@pytest.mark.regression
@pytest.mark.acceptance
def test_ui_05_submit_edit_contact_with_invalid_format_values(browser):
    # Authorization
    login_page = LoginPage(browser)
    login_page.open(Env.URL)
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    # Open Contact List page, select any contact item
    cl_page = ContactListPage(browser)
    cl_page.open(Env.URL_cl)
    contact_item = cl_page.select_any_contact()
    contact_item.click()

    # Open Contact Details page, click Edit Contact button
    cd_page = ContactDetailsPage(browser)
    cd_page.open(Env.URL_cd)
    edit_contact_button = cd_page.get_element(cd_page.edit_button)
    edit_contact_button.click()

    # Open Edit Contact page
    ec_page = EditContactPage(browser)
    ec_page.open(Env.URL_ec)
    browser.implicitly_wait(10)

    # Clear and fill all Edit Contact page fields
    ec_page.wait_all_fields_visible()
    ec_page.wait_required_fields_not_empty()
    ec_page.clear_form()

    ContactTemplate.contact_edit["postalCode"] = "postalcode"
    ContactTemplate.contact_edit["phone"] = "8-029-3665544"
    ContactTemplate.contact_edit["email"] = "email@"
    ContactTemplate.contact_edit["birthdate"] = "20-12-2000"

    ec_page.fill_contact_form(ContactTemplate.contact_edit)
    ec_page.click_submit_button()

    # Check error message appears on Edit Contact page
    error_text = ec_page.get_error_text()
    assert "Validation failed" in error_text
    assert "postalCode: Postal code is invalid" in error_text, "Postal Code validation failed"
    assert "phone: Phone number is invalid" in error_text, "Phone validation failed"
    assert "email: Email is invalid" in error_text, "Email validation failed"
    assert "birthdate: Birthdate is invalid" in error_text, "Date of Birth validation failed"


# Test negative: Submit required fields with over max length values
@allure.feature("Edit functionality")
@pytest.mark.edit_contact
@pytest.mark.acceptance
@pytest.mark.regression
def test_ui_06_submit_edit_required_fields_with_over_len_values(browser):
    # Authorization
    login_page = LoginPage(browser)
    login_page.open(Env.URL)
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    # Open Contact List page, select any contact item
    cl_page = ContactListPage(browser)
    cl_page.open(Env.URL_cl)
    contact_item = cl_page.select_any_contact()
    contact_item.click()

    # Open Contact Details page, click Edit Contact button
    cd_page = ContactDetailsPage(browser)
    cd_page.open(Env.URL_cd)
    edit_contact_button = cd_page.get_element(cd_page.edit_button)
    edit_contact_button.click()

    # Open Edit Contact page
    ec_page = EditContactPage(browser)
    ec_page.open(Env.URL_ec)
    browser.implicitly_wait(10)

    # Clear and fill all Edit Contact page fields
    ec_page.wait_all_fields_visible()
    ec_page.wait_required_fields_not_empty()
    ec_page.clear_form()

    ContactTemplate.contact_edit["firstName"] = "FirstNamemorethan20sy"
    ContactTemplate.contact_edit["lastName"] = "LastNamemorethan20sym"

    ec_page.fill_contact_form(ContactTemplate.contact_edit)
    ec_page.click_submit_button()

    # Check error message appears on Edit Contact page
    error_text = ec_page.get_error_text()
    assert "Validation failed" in error_text
    assert "lastName: Path `lastName`" in error_text, "Lastname field validation failed"
    assert "firstName: Path `firstName`" in error_text, "Firstname field validation failed"
    assert "is longer than the maximum allowed length (20)" in error_text


# Test negative: Submit optional fields with over max length values
@allure.feature("Edit functionality")
@pytest.mark.edit_contact
@pytest.mark.regression
def test_ui_07_submit_edit_optional_fields_with_over_len_values(browser):
    # Authorization
    login_page = LoginPage(browser)
    login_page.open(Env.URL)
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    # Open Contact List page, select any contact item
    cl_page = ContactListPage(browser)
    cl_page.open(Env.URL_cl)
    contact_item = cl_page.select_any_contact()
    contact_item.click()

    # Open Contact Details page, click Edit Contact button
    cd_page = ContactDetailsPage(browser)
    cd_page.open(Env.URL_cd)
    edit_contact_button = cd_page.get_element(cd_page.edit_button)
    edit_contact_button.click()

    # Open Edit Contact page
    ec_page = EditContactPage(browser)
    ec_page.open(Env.URL_ec)
    browser.implicitly_wait(10)

    # Clear and fill all Edit Contact page fields
    ec_page.wait_all_fields_visible()
    ec_page.wait_required_fields_not_empty()
    ec_page.clear_form()

    ContactTemplate.contact_edit["postalCode"] = "12345678901"
    ContactTemplate.contact_edit["phone"] = "1234567890123456"
    ContactTemplate.contact_edit["city"] = "MyLongCityMyLongCity MyLongCityMyLongCity"

    ec_page.fill_contact_form(ContactTemplate.contact_edit)
    ec_page.click_submit_button()

    # Check error message appears on Edit Contact page
    error_text = ec_page.get_error_text()
    assert "Validation failed" in error_text
    assert (f'postalCode: Path `postalCode` (`{ContactTemplate.contact_edit["postalCode"]}`) is'
            f' longer than the maximum allowed length (10)') in error_text, \
        "Postal Code validation failed"
    assert (f'city: Path `city` (`{ContactTemplate.contact_edit["city"]}`) is longer'
            f' than the maximum allowed length (40)') in error_text, "City validation failed"
    assert (f'phone: Path `phone` (`{ContactTemplate.contact_edit["phone"]}`) is longer'
            f' than the maximum allowed length (15)') in error_text, "Phone validation failed"
