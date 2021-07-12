from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
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

    def clickOnForgotPassword(self):

        self.driver.find_element_by_xpath(self.link_forgotPassword_xpath).click()






