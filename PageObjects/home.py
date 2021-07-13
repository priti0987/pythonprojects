from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Homepage:
    link_logOut_xpath = "//li[@class='lo']//i[@class='icon-powerLine']"
    popup_yes_xpath="//button[normalize-space()='Yes']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnLogOut(self):
        self.driver.find_element_by_xpath(self.link_logOut_xpath).click()
        self.driver.find_element_by_xpath(self.popup_yes_xpath).click()
