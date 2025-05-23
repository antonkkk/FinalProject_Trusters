from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from test_data.contact_fields_locators import Locators


class EditContactPage(BasePage):
    submit_button = (By.ID, 'submit')
    cancel_button = (By.ID, 'cancel')

    def __init__(self, driver):
        super().__init__(driver)

    # Clear all fields on Edit Contact page
    def clear_form(self):
        for key in Locators.locators:
            upd_field = self.driver.find_element(*Locators.locators[key])
            upd_field.clear()

    def clear_required_fields(self):
        firstname = self.driver.find_element(*Locators.locators["firstName"])
        firstname.clear()
        lastname = self.driver.find_element(*Locators.locators["lastName"])
        lastname.clear()

    def fill_required_fields(self, contact):
        self.driver.find_element(*Locators.locators["firstName"]).send_keys(contact["firstName"])
        self.driver.find_element(*Locators.locators["lastName"]).send_keys(contact["lastName"])

    def click_submit_button(self):
        self.driver.find_element(*self.submit_button).click()

    def click_cancel_button(self):
        self.driver.find_element(*self.cancel_button).click()
