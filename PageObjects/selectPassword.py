from selenium.webdriver.common.by import By
class SelectPwd:
    title_selectPasswordType_className = "ant-page-header-heading-title"
    radioButton_loginPassword_xpath = "//input[@value='SPWD']"
    radioButton_transaction_xpath = "//input[@value='TPWD']"
    button_continue_xpath = "//button[@type='submit']"
    link_backArrow_xpath = "//span[@class='anticon anticon-arrow-left']"
    button_back_xpath = "//button[@class='ant-btn ant-btn-lg ant-btn-block']"
    message_selectWarning_xpath = "//div[@role='alert']"



    def __init__(self,driver):
        self.driver = driver

    def selectLoginPassword(self):
        self.driver.find_element_by_xpath(self.radioButton_loginPassword_xpath).click()

    def selectTransactionPassword(self):
        self.driver.find_element_by_xpath(self.radioButton_transaction_xpath).click()

    def clickOnContinue(self):
        self.driver.find_element_by_xpath(self.button_continue_xpath).click()

    def clickOnBackArrow(self):
        self.driver.find_element_by_xpath(self.link_backArrow_xpath).click()

    def clickOnBackButton(self):
        self.driver.find_element_by_class_name(self.button_back_xpath).click()

    def elementLoginPassword(self):
        self.driver.find_element_by_xpath(self.radioButton_loginPassword_xpath)






