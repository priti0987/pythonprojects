class foreignCustomerPassword:
    text_username_id = "customerAuthForm_registrationNumber"
    text_passportNumber_id = "customerAuthForm_registrationNumber"
    button_continue_xpath = "//button[@type='submit']"

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element_by(self.text_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by(self.text_passportNumber_id).send_keys(password)

    def clickOnContinue(self):
        self.driver.find_element_by(self.button_continue_xpath).click()