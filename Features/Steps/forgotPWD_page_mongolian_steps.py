import time
import easygui
import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import *
from selenium.webdriver.common.by import By
from PageObjects.login import Login
from PageObjects.selectPassword import SelectPwd
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from Utilities.constants import Constants
from Utilities.customLogger import LogGen

myLogger = LogGen.logGen()

@given(u'I launch the Khan Bank Retail application in Ie')
def step_impl(context):
    context.driver = webdriver.Ie()
    myLogger.info("*****Driver Initialized*****")
    global login_page
    login_page = Login(context.driver)
    try:

        context.driver.get(Constants.RETAIL_URL)
        context.driver.maximize_window()
        login_page.clearDomain()
        login_page.setRetailDomain()
        login_page.clickOnDomainButton()
        time.sleep(2)
        if context.driver.title == Constants.RETAIL_HOMEPAGE_TITLE:
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Retail LoginPage Displayed ",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Homepage title matches****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Retail LoginPage Not Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Homepage title does not match*****")
    except:
        #myLogger.exception("Error occured during execution: %s", e.message)
        myLogger.info("*****Unable to launch the application")

@given(u'I launch the Khan Bank Corporate application in Firefox')
def step_impl(context):
    context.driver = webdriver.Firefox()
    myLogger.info("*****Driver Initialized*****")
    global login_page
    login_page = Login(context.driver)
    try:

        context.driver.get(Constants.RETAIL_URL)
        context.driver.maximize_window()
        login_page.clearDomain()
        login_page.setRetailDomain()
        login_page.clickOnDomainButton()
        time.sleep(2)
        if context.driver.title == Constants.CORPORATE_HOMEPAGE_TITLE:
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank CORPORATE LoginPage Displayed ",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Homepage title matches****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank CORPORATE LoginPage Not Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Homepage title does not match*****")
    except:
        #myLogger.exception("Error occured during execution: %s", e.message)
        myLogger.info("*****Unable to launch the application")




@given(u'I launch the Khan Bank Retail application in Firefox')
def Firefox(context):
    context.driver = webdriver.Firefox()
    myLogger.info("*****Driver Initialized*****")
    #easygui.msgbox("loginFirefox")
    global login_page
    login_page = Login(context.driver)

    try:
        context.driver.get(Constants.RETAIL_URL)
        context.driver.maximize_window()
        #easygui.msgbox("Firefox")
        login_page.clearDomain()
        login_page.setRetailDomain()
        login_page.clickOnDomainButton()
        #easygui.msgbox("loginFirefoxDomain")

        if context.driver.title == Constants.RETAIL_HOMEPAGE_TITLE:
            assert True
            context.driver.save_screenshot(".\\Screenshots\\"+"LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank LoginPage",attachment_type = AttachmentType.PNG)
            myLogger.info("*****Homepage title matches*****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank LoginPage",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Homepage title does not match*****")
    except:
        #myLogger.exception("Error occured during execution: %s", e.message)
        myLogger.info("*****Unable to launch the application")


@given(u'I launch the Khan Bank application')
def step_impl(context):
    context.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    myLogger.info("*****Driver Initialized*****")
    global login_page
    login_page = Login(context.driver)
    try:

        context.driver.get(Constants.BASE_URL)
        context.driver.maximize_window()
        login_page.setDomain()
        login_page.clickOnDomainButton()

        if context.driver.title == Constants.HOMEPAGE_TITLE:
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank LoginPage Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Homepage title matches****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "LoginPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank LoginPage Not Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Homepage title does not match*****")
    except:
        #myLogger.exception("Error occured during execution: %s", e.message)
        myLogger.info("*****Unable to launch the application")


@when(u'I click on Forgot Password link')
def step_impl(context):
    global login_page
    login_page = Login(context.driver)
    global select_password_page
    select_password_page = SelectPwd(context.driver)

    try:
        login_page.clickOnForgotPassword()
        login_password_element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"//input[@value='SPWD']")))
        assert True
        context.driver.save_screenshot(".\\Screenshots\\" + "SelectPasswordPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Select Password Page",
                      attachment_type=AttachmentType.PNG)
        myLogger.info("*****Expected Element Login Password Radio Button Found*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Expected Element Login Password Radio Button Not Found******")


@when(u'I select the login password to be reset')
def step_impl(context):
    global select_password_page
    select_password_page = SelectPwd(context.driver)
    select_password_page.selectLoginPassword()
    select_password_page.clickOnContinue()

@then(u'I select the transaction password to be reset')
def step_impl(context):
    global select_password_page
    select_password_page = SelectPwd(context.driver)
    select_password_page.selectTransactionPassword()
    select_password_page.clickOnContinue()

@when(u'I select the transaction password to be reset')
def step_impl(context):
    global select_password_page
    select_password_page = SelectPwd(context.driver)
    select_password_page.selectTransactionPassword()
    select_password_page.clickOnContinue()


@then(u'I should be displayed with the Forgot password page for Mongolian Customer')
def step_impl(context):
    global mongolian_customer_password_page
    mongolian_customer_password_page = MongolianCustomerPassword(context.driver)
    try:
        username_element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID,"customerAuthForm_loginUserId")))
        assert True
        context.driver.save_screenshot(".\\Screenshots\\" + "ForgotPWDPageMongolian.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Forgot Password Page for Mongolian Customers Displayed",
                          attachment_type=AttachmentType.PNG)
        myLogger.info("*****Expected Element Username Text field Found*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Expected Element Username Text field Not Found******")


@then(u'I click on Continue button without selecting a password')
def step_impl(context):
    global select_password_page
    select_password_page = SelectPwd(context.driver)
    select_password_page.clickOnContinue()
    time.sleep(3)

@then(u'Warning message should be displayed')
def step_impl(context):
    global select_password_page
    select_password_page = SelectPwd(context.driver)

    try:
        warning_select_password_msg = context.driver.find_element_by_xpath("//div[@role='alert']").text
        if warning_select_password_msg == "Нууц үгийн төрөл сонгоно уу":
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "SelectPWDTypeWarning.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Select Password Type Warning Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("Warning message - Select Password Type is displayed")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "NoSelectPWDTypeWarning.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Select Password Type Warning Not Displayed",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("Warning message - Select Password Type is not displayed")
    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("Unable to test the negative test - Without selecting a password type ")


@then(u'I close the browser')
def step_impl(context):
    context.driver.close()
    myLogger.info("Browser is closed")

