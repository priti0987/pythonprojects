import time
import xlrd
from behave import *
from selenium import webdriver
import easygui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import *

class Signup:

    text_username_id = "customerAuthForm_loginUserId"

    Firstdropdown_xpath = "//*[@class='ant-select-selection-search-input'][1]"
    dropdown_reg1_value_xpath = "//*[@title='Б'][1]"
    dropdown_xpath2 = "(//input[@type='search'])[2]"
    dropdown_reg2_value_xpath_of_Д = "//*[@title='Д']"
    dropdown_reg2_value_xpath_Д = "Keys.DOWN + Keys.DOWN +Keys.DOWN +Keys.DOWN +Keys.DOWN +Keys.DOWN + Keys.ENTER"
    reg_number_xpath = "//input[@class='ant-input'][2]"
    reg_number_value = "91101304"
    emailid_xpath = "//input[@id='email']"
    emailid_value = "infura7@gmail.com"
    phone_number_xpath = "//input[@id='phoneNumber']"
    phone_number_value = "88131370"
    continue_button_xpath="//button[@class='ant-btn ant-btn-primary ant-btn-lg ant-btn-block']"

    def __init__(self, driver):
        self.driver = driver

    def selectDropdown1(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath("(//div[@class='ant-select-selector'])[1]")
        action.move_to_element(element).click().perform()
        data = self.driver.find_elements_by_xpath("//div[@class='ant-select-item-option-content']")
        Char1 = "A"
        for regchar1 in data:
            
            elementValue = regchar1.text
            time.sleep(1)
            if elementValue is Char1:
                regchar1.click()
                break

    def selectDropdown2(self):
        action2 = ActionChains(self.driver)
        element2 = self.driver.find_element_by_xpath("(//div[@class='ant-select-selector'])[2]")
        action2.move_to_element(element2).click().perform()
        data2 = self.driver.find_elements_by_xpath("//div[@class='ant-select-item-option-content']")
        Char2 = "Г"
        for regchar2 in data2:
            elementValue2 = regchar2.text
            easygui.msgbox(elementValue2)
            if elementValue2 is Char2:
                easygui.msgbox("inside2if")
                regchar2.click()
                break
        #self.driver.find_elements_by_xpath("(//*[@class='ant-select-selector'])[2]").click()
        #self.driver.find_element_by_xpath("//span[@class='ant-select-selection-item']").send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).sendKeys(Keys.ENTER)

        #value= self.driver.find_element_by_xpath(self.dropdown_reg2_value_xpath_Д)
        #easygui.msgbox("Select Value from dropdown")
        # self.driver.find_element_by_xpath(DropDown_Elements[1]).send_keys("Keys.DOWN +Keys.DOWN + Keys.ENTER")

    def enterReg_number(self):
        self.driver.find_element_by_xpath(self.reg_number_xpath).send_keys(self.reg_number_value)

    def enterEmailid(self):
        self.driver.find_element_by_xpath(self.emailid_xpath).send_keys(self.emailid_value)

    def enterPhone_number(self):
        self.driver.find_element_by_xpath(self.phone_number_xpath).send_keys(self.phone_number_value)

    def clickOn_ContinueButton(self):
        self.driver.find_element_by_xpath(self.continue_button_xpath).click()

