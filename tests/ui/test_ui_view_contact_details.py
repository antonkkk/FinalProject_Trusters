import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.contact_details_page import ContactDetailsPage
from pages.contact_list_page import ContactListPage
from pages.login_page import LoginPage
from test_data.user_creds import UserCreds


@pytest.mark.contact_details
@pytest.mark.smoke
@pytest.mark.acceptance
# Test positive: open Contact Details page for target contact
def test_ui_01_view_contact_details(browser):
    # Authorization
    login_page = LoginPage(browser)
    login_page.open()
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    # Open Contact List page, select any contact item, remember firstname and lastname
    contact_list_page = ContactListPage(browser)
    contact_list_page.open()

    contact_item = contact_list_page.select_any_contact()
    full_name_cell = contact_item.find_element(By.XPATH, "./td[2]")
    full_name = full_name_cell.text.split()
    contact_firstname = full_name[0]
    contact_lastname = full_name[1]
    contact_item.click()

    # Open Contact Details page, check the page header
    contact_details_page = ContactDetailsPage(browser)
    contact_details_page.open()
    header = browser.find_element(By.XPATH, "//h1")
    assert header.text == "Contact Details"

    # Check firstname and lastname are the same as on Contact List page
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.ID, 'firstName')))
    wait.until(EC.visibility_of_element_located((By.ID, 'lastName')))
    firstname_field = browser.find_element(By.ID, 'firstName')
    lastname_field = browser.find_element(By.ID, 'lastName')

    assert firstname_field.text == contact_firstname
    assert lastname_field.text == contact_lastname


@pytest.mark.contact_details
@pytest.mark.acceptance
# Test positive: return to Contact List page from Contact Details page
def test_ui_02_return_to_contact_list_from_contact_details(browser):
    # Authorization
    login_page = LoginPage(browser)
    login_page.open()
    login_page.complete_login(UserCreds.valid_email, UserCreds.valid_password)

    # Open Contact List page, select any contact item
    contact_list_page = ContactListPage(browser)
    contact_list_page.open()
    contact_item = contact_list_page.select_any_contact()
    contact_item.click()

    # Open Contact Details page
    contact_details_page = ContactDetailsPage(browser)
    contact_details_page.open()

    # Click to the Return to Contact List button
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.ID, 'return')))
    return_button = browser.find_element(By.ID, 'return')
    return_button.click()
    header = browser.find_element(By.XPATH, "//h1")
    assert header.text == "Contact List"
