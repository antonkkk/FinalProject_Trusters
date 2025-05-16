import pytest
from selenium.webdriver.common.by import By
from pages.contact_details_page import ContactDetailsPage
from pages.contact_list_page import ContactListPage
from pages.login_page import LoginPage
from test_data.user_creds import UserCreds
from test_data.env import Env


@pytest.mark.contact_details
@pytest.mark.smoke
@pytest.mark.acceptance
# Test positive: open Contact Details page for target contact
def test_ui_01_view_contact_details(browser):
    # Authorization
    login_page = LoginPage(browser)
    login_page.open(Env.URL)
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    # Open Contact List page, select any contact item, remember firstname and lastname
    cl_page = ContactListPage(browser)
    cl_page.open(Env.URL_cl)

    contact_item = cl_page.select_any_contact()
    full_name_cell = contact_item.find_element(By.XPATH, "./td[2]")
    full_name = full_name_cell.text.split()
    contact_firstname = full_name[0]
    contact_lastname = full_name[1]
    contact_item.click()

    # Open Contact Details page, check the page header
    cd_page = ContactDetailsPage(browser)
    cd_page.open(Env.URL_cd)
    header = browser.find_element(By.XPATH, "//h1")
    assert header.text == "Contact Details"

    # Check firstname and lastname are the same as on Contact List page
    firstname_field = cd_page.get_element(cd_page.firstname_field)
    lastname_field = cd_page.get_element(cd_page.lastname_field)

    assert firstname_field.text == contact_firstname
    assert lastname_field.text == contact_lastname


@pytest.mark.contact_details
@pytest.mark.acceptance
# Test positive: return to Contact List page from Contact Details page
def test_ui_02_return_to_contact_list_from_contact_details(browser):
    # Authorization
    login_page = LoginPage(browser)
    login_page.open(Env.URL)
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    # Open Contact List page, select any contact item
    cl_page = ContactListPage(browser)
    cl_page.open(Env.URL_cl)
    contact_item = cl_page.select_any_contact()
    contact_item.click()

    # Open Contact Details page
    cd_page = ContactDetailsPage(browser)
    cd_page.open(Env.URL_cd)

    # Click to the Return to Contact List button
    return_button = cd_page.get_element(cd_page.return_button)
    return_button.click()
    header = browser.find_element(By.XPATH, "//h1")
    assert header.text == "Contact List"


@pytest.mark.contact_details
@pytest.mark.acceptance
# Test positive: Check the Delete button presence on the Contact Details page
def test_ui_03_delete_button_is_on_contact_details(browser):
    # Authorization
    login_page = LoginPage(browser)
    login_page.open(Env.URL)
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    # Open Contact List page, select any contact item
    cl_page = ContactListPage(browser)
    cl_page.open(Env.URL_cl)
    contact_item = cl_page.select_any_contact()
    contact_item.click()

    # Open Contact Details page, check the Delete button presence
    cd_page = ContactDetailsPage(browser)
    cd_page.open(Env.URL_cd)

    delete_button = cd_page.get_element(ContactDetailsPage.delete_button)
    assert delete_button
