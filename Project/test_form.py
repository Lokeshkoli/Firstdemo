import time
from select import select

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObject.formPage import form
from Utility.baseClass import base
# Page object design is implemented in design
# how to handle driver object in page object class is present
# we need to use contructor for given driver variable the lifr
# we need to use self with variable and method to call
# we need to pass class driver variable to page objetc class, so that driver life can be continue
# data can be used using data provider or by parametr or by test data class
# data need to create in same class if not use by all the method
# conftest is used for all the common method like browser invoke
# fixture can help us to call it on all the class
#base class have useable methodwhich can be use whenever required like wait, and dropdown
#log can use to see when test is getting fail, to see what are step we are flollowing
# report can be generate using command
#Screenshot on test failure can be attached


from testdata.homePage import Homepagevalue


class TestdemoForm(base):

    def test_fillUpForm(self,getdata4):
        log = self.test_logDemo()
        log.info(self.driver.title)
        getformData= form(self.driver)
        getformData.formName().send_keys(getdata4["First Name"])
        getformData.emailName().send_keys(getdata4["Mail"])
        #getformData.passwordName().send_keys("Lokesh")

        dropdown = self.driver.find_element(by=By.ID, value="exampleFormControlSelect1")
        self.selectVosibleText(dropdown,getdata4["Gender"])

       # self.driver.refresh()
       # time.sleep(5)

    @pytest.fixture(params=[("Lokesh","Lokesh@gmail.com","Female"),("Lokesh2","Lokesh@gmail.com","Female")])
    def getData(self, request):
        return request.param

    @pytest.fixture()
    def getData2(self):
        return "Lokesh", "Lokesh@gmail.com", "Female"

    @pytest.fixture(params=[{"FirstName" : "Lokesh","Email" : "Lokesh@gmail.com","Gender" : "Female"}])
    def getData3(self, request):
        return request.param

    @pytest.fixture(params=Homepagevalue.getdataexcel("Testcase2"))
    def getdata4(self,request):
        return request.param



