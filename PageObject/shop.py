from selenium.webdriver.common.by import By

from PageObject.checkout import checkoutb


class Homepage:

    def __init__(self, driver):
        self.driver =driver

    shop = (By.LINK_TEXT, "Shop")

    def shopButton(self):
        self.driver.find_element(*Homepage.shop).click()
        checkouts=checkoutb(self.driver)
        return checkouts


