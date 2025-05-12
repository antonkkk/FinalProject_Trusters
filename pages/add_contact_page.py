from selenium.webdriver.common.by import By


class AddContactPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact_form(self, contact):
        self.driver.find_element(By.ID, "firstName").send_keys(contact["firstName"])
        self.driver.find_element(By.ID, "lastName").send_keys(contact["lastName"])
        self.driver.find_element(By.ID, "birthdate").send_keys(contact.get("birthdate", ""))
        self.driver.find_element(By.ID, "email").send_keys(contact.get("email", ""))
        self.driver.find_element(By.ID, "phone").send_keys(contact.get("phone", ""))
        self.driver.find_element(By.ID, "street1").send_keys(contact.get("street1", ""))
        self.driver.find_element(By.ID, "street2").send_keys(contact.get("street2", ""))
        self.driver.find_element(By.ID, "city").send_keys(contact.get("city", ""))
        self.driver.find_element(By.ID, "stateProvince").send_keys(contact.get("stateProvince", ""))
        self.driver.find_element(By.ID, "postalCode").send_keys(contact.get("postalCode", ""))
        self.driver.find_element(By.ID, "country").send_keys(contact.get("country", ""))

    def submit(self):
        self.driver.find_element(By.ID, "submit").click()

    def cancel(self):
        self.driver.find_element(By.ID, "cancel").click()

    def cancel_creation(self):
        # Просто вызывает метод cancel, чтобы сохранить читаемость
        self.cancel()

    def get_error_message(self):
        return self.driver.find_element(By.CLASS_NAME, "error-message").text
