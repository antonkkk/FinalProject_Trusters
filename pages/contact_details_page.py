from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_data.env import Env


class ContactDetailsPage:
    delete_button = (By.ID, 'delete')
    locators = {
        "firstName": (By.ID, "firstName"),
        "lastName": (By.ID, "lastName"),
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
        self.driver.get(Env.URL_contact_details)

    def click_edit_button(self):
        self.driver.find_element(By.ID, "edit-contact").click()

    def check_element(self, locator):
        element = WebDriverWait(
            self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def click_return_to_contact_list_button(self):
        self.driver.find_element(By.ID, "return").click()

    def wait_all_fields_visible(self):
        for key in self.locators:
            WebDriverWait(
                self.driver, 10).until(EC.visibility_of_element_located(self.locators[key]))

    # Check new values on Contact Details page after update on Edit Contact page
    def check_values(self, contact):
        flag = True
        for key in self.locators:
            new_field = self.driver.find_element(*self.locators[key])
            if new_field.text != contact[key]:
                flag = False
                break
        return flag
