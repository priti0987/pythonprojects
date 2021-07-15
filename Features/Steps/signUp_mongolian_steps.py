
import time
import allure
import easygui
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.login import Login
from PageObjects.selectPassword import SelectPwd
from PageObjects.signUpPage import Signup
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from Utilities.constants import Constants
from Utilities.customLogger import LogGen
from behave import *
from selenium import webdriver
import easygui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from easygui import *

myLogger = LogGen.logGen()

@when('Open SignUpPage')
def Signup1(context):
    global login_page
    login_page = Login(context.driver)
    time.sleep(2)


    try:
        login_page.clickOnSignupLink()
        login_password_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//input[@id='email']")))
        assert True
        context.driver.save_screenshot(".\\Screenshots\\" + "SelectPasswordPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank SignUp Page",
                      attachment_type=AttachmentType.PNG)
        myLogger.info("*****Expected Element for sign up page Found*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Expected Element for sign up page Not Found******")

@when(u'Add data in signup page')
def step_impl(context):
    global signup_page
    signup_page = Signup(context.driver)

    signup_page.selectDropdown1()

    signup_page.selectDropdown2()
    signup_page.enterReg_number()
    signup_page.enterEmailid()
    signup_page.enterPhone_number()

@then(u'Click on Continue button')
def step_impl(context):
    global signup_page
    signup_page = Signup(context.driver)
    signup_page.clickOn_ContinueButton()
#context.driver.find_element_by_xpath("(//input[@type='search'])[1]").click()
     #context.driver.find_element_by_xpath("//div[@class='ant-select-item-option-content'][text()='A']").click()
     #context.driver.find_element_by_xpath("(//input[@type='search'])[2]").click()
     #context.driver.find_element_by_xpath("(//input[@type='search'])[2]").send_keys(Keys.DOWN + Keys.DOWN+ Keys.DOWN + Keys.ENTER)
     #context.driver.find_element_by_xpath("//input[@class='ant-input'][2]").send_keys("9898654")
     #context.driver.find_element_by_xpath("//input[@id='email']").send_keys("Priti@domain.com")
     #context.driver.find_element_by_xpath("//input[@id='phoneNumber']").send_keys("100")



