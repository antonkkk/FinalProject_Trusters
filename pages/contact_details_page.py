from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from test_data.contact_fields_locators import Locators


class ContactDetailsPage(BasePage):
    delete_button = (By.ID, 'delete')
    edit_button = (By.ID, 'edit-contact')
    return_button = (By.ID, 'return')
    firstname_field = (By.ID, 'firstName')
    lastname_field = (By.ID, 'lastName')
    header = (By.XPATH, "//h1[text()='Contact Details']")

    def __init__(self, driver):
        super().__init__(driver)

    # Check new values on Contact Details page after update on Edit Contact page
    def check_values(self, contact):
        flag = True
        for key in Locators.locators:
            new_field = self.driver.find_element(*Locators.locators[key])
            if new_field.text != contact[key]:
                flag = False
                break
        return flag
