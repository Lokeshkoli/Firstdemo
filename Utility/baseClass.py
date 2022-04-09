import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class base:
    def waitingForElement(self, text):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, text)))

    def selectVosibleText(self, locator, value ):
        a = Select(locator)
        a.select_by_visible_text(value)

    def test_logDemo(self):
        logger = logging.getLogger(__name__)
        file = logging.FileHandler("file.log")

        formatone = logging.Formatter(" %(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file.setFormatter(formatone)
        logger.addHandler(file)
        logger.setLevel(logging.DEBUG)
        logger.debug("This is debug statement")
        logger.info("This is info statement")
        logger.warning("This is warning statement")
        logger.error("This is error message")
        logger.critical("This is crtical message")
        return logger

