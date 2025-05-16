from selenium.webdriver.common.by import By


class Locators:
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
