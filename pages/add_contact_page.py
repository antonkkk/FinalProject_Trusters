from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddContactPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def submit(self):
        self.driver.find_element(By.ID, "submit").click()

    def cancel(self):
        self.driver.find_element(By.ID, "cancel").click()

    def cancel_creation(self):
        # Просто вызывает метод cancel, чтобы сохранить читаемость
        self.cancel()
