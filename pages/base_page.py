from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from test_data.contact_fields_locators import Locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    LOGOUT_BUTTON = (By.ID, "logout")

    def open(self, url):
        self.driver.get(url)

    def should_be_logged_in(self):
        self.get_element((By.ID, "logout")), \
            "Logout button not found — user is likely not logged in"

    def get_element(self, locator):
        return WebDriverWait(
            self.driver, 10).until(EC.visibility_of_element_located(locator))

    def get_error_text(self):
        try:
            error_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "error"))
            )
            # In case error value attribute is non-empty, return text
            return error_element.text.strip()
        # In case error value attribute is empty, return empty string
        except TimeoutException:
            return ""

    def wait_all_fields_visible(self):
        for key in Locators.locators:
            WebDriverWait(
                self.driver, 15).until(EC.visibility_of_element_located(Locators.locators[key]))

    def wait_all_cd_fields_not_empty(self):
        for key in Locators.locators:
            try:
                element = WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_element_located(Locators.locators[key])
                )
                WebDriverWait(self.driver, 10).until(
                    lambda driver: element.get_attribute('value') != ''
                )
            except TimeoutException:
                return False
        return True

    def wait_required_fields_not_empty(self):
        required = [Locators.locators["firstName"], Locators.locators["lastName"]]
        for locator in required:
            try:
                element = WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_element_located(locator)
                )
                WebDriverWait(self.driver, 10).until(
                    lambda driver: element.get_attribute('value') != ''
                )
            except TimeoutException:
                return False
        return True

    def fill_contact_form(self, contact):
        self.driver.find_element(*Locators.locators["firstName"]).send_keys(contact["firstName"])
        self.driver.find_element(*Locators.locators["lastName"]).send_keys(contact["lastName"])
        self.driver.find_element(
            *Locators.locators["birthdate"]).send_keys(contact.get("birthdate", ""))
        self.driver.find_element(*Locators.locators["email"]).send_keys(contact.get("email", ""))
        self.driver.find_element(*Locators.locators["phone"]).send_keys(contact.get("phone", ""))
        self.driver.find_element(
            *Locators.locators["street1"]).send_keys(contact.get("street1", ""))
        self.driver.find_element(
            *Locators.locators["street2"]).send_keys(contact.get("street2", ""))
        self.driver.find_element(*Locators.locators["city"]).send_keys(contact.get("city", ""))
        self.driver.find_element(
            *Locators.locators["stateProvince"]).send_keys(contact.get("stateProvince", ""))
        self.driver.find_element(
            *Locators.locators["postalCode"]).send_keys(contact.get("postalCode", ""))
        self.driver.find_element(
            *Locators.locators["country"]).send_keys(contact.get("country", ""))

    def click_logout(self):
        self.get_element(self.LOGOUT_BUTTON).click()
        self.get_element((By.ID, "signup"))
