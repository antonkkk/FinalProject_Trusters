from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_data.contact_fields_locators import Locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def get_element(self, locator):
        element = WebDriverWait(
            self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_error_text(self):
        error = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        return error.text

    def wait_all_fields_visible(self):
        for key in Locators.locators:
            WebDriverWait(
                self.driver, 15).until(EC.visibility_of_element_located(Locators.locators[key]))

    def fill_contact_form(self, contact):
        self.driver.find_element(*Locators.locators["firstName"]).send_keys(contact["firstName"])
        self.driver.find_element(*Locators.locators["lastName"]).send_keys(contact["lastName"])
        self.driver.find_element(
            *Locators.locators["birthdate"]).send_keys(contact.get("birthdate", ""))
        self.driver.find_element(*Locators.locators["email"]).send_keys(contact.get("email", ""))
        self.driver.find_element(*Locators.locators["phone"]).send_keys(contact.get("phone", ""))
        self.driver.find_element(*Locators.locators["street1"]).send_keys(contact.get("street1", ""))
        self.driver.find_element(*Locators.locators["street2"]).send_keys(contact.get("street2", ""))
        self.driver.find_element(*Locators.locators["city"]).send_keys(contact.get("city", ""))
        self.driver.find_element(
            *Locators.locators["stateProvince"]).send_keys(contact.get("stateProvince", ""))
        self.driver.find_element(
            *Locators.locators["postalCode"]).send_keys(contact.get("postalCode", ""))
        self.driver.find_element(*Locators.locators["country"]).send_keys(contact.get("country", ""))
