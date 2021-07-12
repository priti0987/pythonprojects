class MongolianCustomerPassword:
    title_forgotPassword_xpath = "//span[@title='Forgot Password']"
    text_username_id = "customerAuthForm_loginUserId"
    dropdown_reg1_xpath = "//input[@type='search'])[1]"
    dropdown_reg2_xpath = "//input[@type='search'])[2]"

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element_by_id(self.text_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.text_passportNumber_id).send_keys(password)

    def clickOnContinue(self):
        self.driver.find_element_by_xpath(self.button_continue_xpath).click()


