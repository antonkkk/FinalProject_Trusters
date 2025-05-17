from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_data.user_creds import UserCreds
from helper.utils import generate_random_email
from pages.base_page import BasePage


class SignupPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "submit")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_MESSAGE = (By.ID, "error")
    LOGOUT_BUTTON = (By.ID, "logout")

    def should_be_signup_page(self):
        assert self.get_element(self.FIRST_NAME_INPUT).is_displayed(), "First name input not visible"
        assert self.get_element(self.SUBMIT_BUTTON).is_enabled(), "Submit button not enabled"

    def fill_first_name(self, value):
        self.get_element(self.FIRST_NAME_INPUT).send_keys(value)

    def fill_last_name(self, value):
        self.get_element(self.LAST_NAME_INPUT).send_keys(value)

    def fill_email(self, value):
        self.get_element(self.EMAIL_INPUT).send_keys(value)

    def fill_password(self, value):
        self.get_element(self.PASSWORD_INPUT).send_keys(value)

    def fill_signup_form(self, first_name, last_name, password, email=None):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        if email is None:
            email = generate_random_email()
        self.fill_email(email)
        self.fill_password(password)
        return email

    def click_submit(self):
        self.get_element(self.SUBMIT_BUTTON).click()

    def click_cancel(self):
        self.get_element(self.CANCEL_BUTTON).click()

    def is_error_message_present(self, message_text="Email address is already in use"):
        try:
            error_element = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located((By.ID, "error"))
            )
            return message_text in error_element.text
        except:
            return False
