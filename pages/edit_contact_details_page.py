from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_data.env import Env


class EditContactPage:
    locators = {
        "firstname": (By.ID, "firstName"),
        "lastname": (By.ID, "lastName"),
        "birthdate": (By.ID, "birthdate"),
        "email": (By.ID, "email"),
        "phone": (By.ID, "phone"),
        "street1": (By.ID, "street1"),
        "street2": (By.ID, "street2"),
        "city": (By.ID, "city"),
        "stateProvince": (By.ID, "stateProvince"),
        "postalCode": (By.ID, "postalCode"),
        "country": (By.ID, "country")
    }

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(Env.URL_edit_contact)

    def wait_all_fields_visible(self):
        for key in self.locators:
            WebDriverWait(
                self.driver, 10).until(EC.visibility_of_element_located(self.locators[key]))

    # Clear all fields on Edit Contact page
    def clear_form(self):
        for key in self.locators:
            upd_field = self.driver.find_element(*self.locators[key])
            upd_field.clear()

    def fill_edit_contact_form(self, contact):
        self.driver.find_element(*self.locators["firstname"]).send_keys(contact["firstName"])
        self.driver.find_element(*self.locators["lastname"]).send_keys(contact["lastName"])
        self.driver.find_element(
            *self.locators["birthdate"]).send_keys(contact.get("birthdate", ""))
        self.driver.find_element(*self.locators["email"]).send_keys(contact.get("email", ""))
        self.driver.find_element(*self.locators["phone"]).send_keys(contact.get("phone", ""))
        self.driver.find_element(*self.locators["street1"]).send_keys(contact.get("street1", ""))
        self.driver.find_element(*self.locators["street2"]).send_keys(contact.get("street2", ""))
        self.driver.find_element(*self.locators["city"]).send_keys(contact.get("city", ""))
        self.driver.find_element(
            *self.locators["stateProvince"]).send_keys(contact.get("stateProvince", ""))
        self.driver.find_element(
            *self.locators["postalCode"]).send_keys(contact.get("postalCode", ""))
        self.driver.find_element(*self.locators["country"]).send_keys(contact.get("country", ""))

    def click_submit_button(self):
        self.driver.find_element(By.ID, "submit").click()

    def click_cancel_button(self):
        self.driver.find_element(By.ID, "cancel").click()
