class SetPassword:
    text_newPWD_id = "customerAuthForm_password"
    text_reenterPWD_id = "customerAuthForm_reTypePassword"
    button_proceed_xpath = "//span[text()='Proceed']"

    def __init__(self,driver):
        self.driver = driver

    def setNewPassword(self,newPassword):
        self.driver.find_element_by_id(self.text_newPWD_id).send_keys(newPassword)

    def reenterPassword(self,newPassword):
        self.driver.find_element_by_id(self.text_reenterPWD_id).send_keys(newPassword)

    def clickOnProceed(self):
        self.driver.find_element_by_xpath(self.button_proceed_xpath).click()
