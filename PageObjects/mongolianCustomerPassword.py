import time
from selenium.webdriver.common.keys import Keys

class MongolianCustomerPassword:
    title_forgotPassword_xpath = "//span[@title='Forgot Password']"
    text_username_id = "customerAuthForm_loginUserId"
    dropdown_reg1_xpath = "//input[@type='search'])[1]"
    dropdown_reg2_xpath = "//input[@type='search'])[2]"
    text_regNumber_xpath = "//input[@class='ant-input'][2]"
    button_continue_xpath = "//button[@type='submit']"
    option_reg1_xpath = "//div[@class='ant-select-item-option-content'][text()='A']"

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element_by_id(self.text_username_id).send_keys(username)

    def clickOnRegDrpDwn1(self):
        self.driver.find_element_by_xpath(self.dropdown_reg1_xpath).click()

    def setRegDrpDwn1(self):
        self.driver.find_element_by_xpath(self.option_reg1_xpath).click()

    def clickOnRegDrpDwn2(self):
        self.driver.find_element_by_xpath(self.dropdown_reg2_xpath).click()

    def setRegDrpDwn2(self):
        self.driver.find_element_by_xpath(self.dropdown_reg2_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.dropdown_reg2_xpath).send_keys(Keys.DOWN + Keys.DOWN + Keys.ENTER)

    def setRegNum(self,regNum):
        self.driver.find_element_by_xpath(self.text_regNumber_xpath).send_keys(regNum)

    def clickOnContinue(self):
        self.driver.find_element_by_xpath(self.button_continue_xpath).click()


