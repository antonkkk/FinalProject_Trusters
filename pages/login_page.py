from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "submit")
    ERROR_MESSAGE = (By.ID, "error")
    LOGOUT_BUTTON = (By.ID, "logout")

    def fill_email(self, value):
        self.get_element(self.EMAIL_INPUT).send_keys(value)

    def fill_password(self, value):
        self.get_element(self.PASSWORD_INPUT).send_keys(value)

    def click_submit(self):
        self.get_element(self.SUBMIT_BUTTON).click()

    def complete_login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_submit()

    def should_be_login_page(self):
        assert self.get_element(self.EMAIL_INPUT).is_displayed(), "Email input not visible"
        assert self.get_element(self.SUBMIT_BUTTON).is_enabled(), "Submit button not enabled"
