import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# def pytest_addoption(parser):
#    parser.addoption(
#        "--browsername", action="store", default="chrome"
#    )


@pytest.fixture(scope="class")
def setup(request):
    #   browserName = request.config.getoption("--browsername")
    #   if browserName == "chrome":
    #     driver = webdriver.Chrome(
    #    executable_path="C:\\Users\\Lokesh\\Desktop\\Python\\Lib\\chromedriver_win32\\chromedriver.exe")
    #  elif browserName =="firefox":

    #     driver = webdriver.Edge(
    #        executable_path="C:\\Users\\Lokesh\\Desktop\\Python\\Lib\\msedgedriver.exe")

    driver = webdriver.Chrome(
        executable_path="C:\\Users\\Lokesh\\Desktop\\Python\\Lib\\chromedriver_win32\\chromedriver.exe")
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()
    #    driver.find_element(By)
    request.cls.driver = driver
    yield
    # driver.close()
