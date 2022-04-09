from selenium.webdriver.common.by import By


class checkoutb:
    def __init__(self, driver):
        self.driver = driver

    checkout = (By.XPATH, "//h4[@class='card-title']/a")

    def check(self):
        return self.driver.find_elements(*checkoutb.checkout)
