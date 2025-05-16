from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ContactListPage(BasePage):
    all_contact_items = (By.CLASS_NAME, "contactTableBodyRow")

    def __init__(self, driver):
        super().__init__(driver)

    def select_any_contact(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(self.all_contact_items)
        )
        all_items = self.driver.find_elements(*self.all_contact_items)
        return random.choice(all_items)
