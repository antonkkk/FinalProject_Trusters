from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddContactPage(BasePage):
    FIRST_NAME = (By.ID, "firstName")
    EMAIL = (By.ID, "email")
    SUBMIT_BUTTON = (By.ID, "submit")
    CONTACT_ROWS = (By.CSS_SELECTOR, "tr.contactTableBodyRow")

    def __init__(self, driver):
        super().__init__(driver)

    def submit(self):
        self.driver.find_element(By.ID, "submit").click()

    def cancel(self):
        self.driver.find_element(By.ID, "cancel").click()

    def cancel_creation(self):
        # Просто вызывает метод cancel, чтобы сохранить читаемость
        self.cancel()

    def get_contacts_emails(self):
        emails = []
        rows = self.driver.find_elements(*self.CONTACT_ROWS)
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 3:
                email = cells[3].text.strip()
                if email:
                    emails.append(email)
        return emails

    def fill_first_name(self, first_name):
        elem = self.get_element(self.FIRST_NAME)
        elem.clear()
        elem.send_keys(first_name)

    def fill_email(self, email):
        elem = self.get_element(self.EMAIL)
        elem.clear()
        elem.send_keys(email)
