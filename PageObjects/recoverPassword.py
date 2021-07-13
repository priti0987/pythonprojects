class RecoverPassword:
    radioButton_mobileNumber_xpath = "//input[@value='MOBILE']"
    radioButton_emailID_xpath = "//input[@value='EMAIL']"
    button_continue_xpath = "//button[@type='submit']"
    title_recoverPasswordMN_xpath = "//span[@title='Нууц үг сэргээх']"
    title_recoverPasswordEN_xpath = "//span[@title='Recover password']"

    def __init__(self,driver):
        self.driver = driver

    def selectMobileNumber(self):
        self.driver.find_element_by_xpath(self.radioButton_mobileNumber_xpath).click()

    def selectEmailID(self):
        self.driver.find_element_by_xpath(self.radioButton_emailID_xpath).click()

    def clickOnContinue(self):
        self.driver.find_element_by_xpath(self.button_continue_xpath).click()


