from selenium.webdriver.common.by import By


class form:
    def __init__(self, driver):
        self.driver = driver

    name1 = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.NAME, "password")

    def formName(self):
        return self.driver.find_element(*form.name1)

    def emailName(self):
        return self.driver.find_element(*form.email)

    def passwordName(self):
        return self.driver.find_element(*form.password)
