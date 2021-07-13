from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    link_language_xpath = "//img[@src='/images/svg/signin/lang-mn.svg']"
    text_username_id = "username"
    text_password_id = "password"
    button_login_xpath = "//button[@type='submit']"
    link_forgotPassword_xpath = "//a[@href='/auth/forgotpassword/step/1']"
    text_domain_xpath = "//input[@type='text']"
    button_domain_xpath = "//span[text()='Хадгалах']"

    def __init__(self,driver):
        self.driver = driver

    def setDomain(self,domain):

        self.driver.find_element_by_xpath(self.text_domain_xpath).clear()
        self.driver.find_element_by_xpath(self.text_domain_xpath).send_keys(domain)

    def clickOnDomainButton(self):
        self.driver.find_element_by_xpath(self.button_domain_xpath).click()

    def setLanguage(self):
        self.driver.find_element_by_xpath(self.link_language_xpath).click()

    def setUserName(self, username):
        self.driver.find_element_by_id(self.text_username_id).send_keys(username)

    def setpassword(self, PASSWORD):
        self.driver.find_element_by_id(self.text_password_id).send_keys(PASSWORD)

    def clickOnLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickOnForgotPassword(self):
        self.driver.find_element_by_xpath(self.link_forgotPassword_xpath).click()

    def elementForgotPassword(self):
        self.driver.find_element_by_xpath(self.link_forgotPassword_xpath)







