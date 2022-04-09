import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions

from PageObject.checkout import checkoutb
from PageObject.shop import Homepage
from Utility.baseClass import base


class TestDemo(base):

    def test_browser(self, setup):
        log = self.test_logDemo()
        log.info(self.driver.title)
        print(self.driver.title)
        home = Homepage(self.driver)
        #home.shopButton().click()
        listshops=home.shopButton()
        #listshops = checkoutb(self.driver)
        time.sleep(2)
        listshop = listshops.check()
        # listshop = self.driver.find_elements(by=By.XPATH, value="//h4[@class='card-title']/a")
        for item in listshop:
            if item.text == "Nokia Edge":
                item.find_element(by=By.XPATH, value="parent :: h4/parent :: div/parent::div/div[2]/button").click()
        self.driver.find_element(by=By.CSS_SELECTOR, value=".nav-link.btn.btn-primary").click()

        self.driver.find_element(by=By.CSS_SELECTOR, value=".btn.btn-success").click()

        # to check on checkbox button
        # self.driver.find_element(by=By.CSS_SELECTOR, value=".btn-danger").click()
        time.sleep(5)

        self.driver.find_element(by=By.ID, value="country").send_keys("Ind")
        # need to pass only paramter
        self.waitingForElement("suggestions")

        citys = self.driver.find_elements(by=By.XPATH, value="//div[@class='suggestions']/ul")
        for city in citys:
            if city.text == "India":
                city.click()
