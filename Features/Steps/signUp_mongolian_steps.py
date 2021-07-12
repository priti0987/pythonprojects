import time
import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from PageObjects.login import Login
from PageObjects.selectPassword import SelectPwd
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from Utilities.constants import Constants
from Utilities.customLogger import LogGen

myLogger = LogGen.logGen()
@when('Open SignUpPage')
def Signup1(context):
    context.driver.find_element_by_xpath("//a[@href='/auth/signup/step/1']").click()
@when(u'Add data in signup page')
def step_impl(context):
    context.driver.find_element_by_xpath("(//input[@type='search'])[1]").click()
    time.sleep(1)
    context.driver.find_element_by_xpath("//div[@class='ant-select-item-option-content'][text()='A']").click()
    context.driver.find_element_by_xpath("(//input[@type='search'])[2]").click()
    time.sleep(2)
    # button = context.driver.find_element_by_xpath("//div[@class='ant-select-item ant-select-item-option'][@title='Д']").click()
    context.driver.implicitly_wait(5)
    context.driver.find_element_by_xpath("(//input[@type='search'])[2]").send_keys(
        Keys.DOWN + Keys.DOWN + Keys.DOWN + Keys.ENTER)
    # ActionChains(context.driver).move_to_element(button).click(button)
    context.driver.find_element_by_xpath("//input[@class='ant-input'][2]").send_keys("9898654")
    context.driver.find_element_by_xpath("//input[@id='email']").send_keys("Priti@domain.com")
    context.driver.find_element_by_xpath("//input[@id='phoneNumber']").send_keys("100")
    # easygui.msgbox("close?")
