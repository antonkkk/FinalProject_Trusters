from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    email = (By.ID, "email")
    password = (By.ID, "password")
    submit_button = (By.ID, "submit")

    def __init__(self, driver):
        super().__init__(driver)

    def complete_login(self, email, password):
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.submit_button).click()
