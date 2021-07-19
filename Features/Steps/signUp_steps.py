import time
import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.login import Login
from PageObjects.selectPassword import SelectPwd
from PageObjects.signUpPage import Signup
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from Utilities.constants import Constants
from Utilities.customLogger import LogGen
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
myLogger = LogGen.logGen()
from webdriver_manager.firefox import GeckoDriverManager
import easygui
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import *
from selenium.webdriver.common.by import By
from PageObjects.login import Login
from PageObjects.selectPassword import SelectPwd
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from Utilities.constants import Constants
from Utilities.customLogger import LogGen
from selenium.webdriver.firefox.options import Options
import Utilities.excelUtils
from selenium.common.exceptions import *

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
    option1 = Options()
    option1.add_argument("--disable-notifications")

    context.driver = webdriver.Firefox()
    myLogger.info("*****Driver Initialized*****")
    #easygui.msgbox("loginFirefox")
    global login_page
    login_page = Login(context.driver)

    try:
        context.driver.get(Constants.RETAIL_URL)
        time.sleep(2)
        context.driver.maximize_window()
        #easygui.msgbox("Firefox")


        login_page.clearDomain()
        login_page.setRetailDomain()
        login_page.clickOnDomainButton()
        #login_page.refreshPage()
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


@when('Open SignUpPage')
def Signup1(context):
    global login_page
    login_page = Login(context.driver)
    time.sleep(2)


    try:
        login_page.clickOnSignupLink()
        login_password_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//input[@id='email']")))
        assert True
        context.driver.save_screenshot(".\\Screenshots\\" + "SelectPasswordPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank SignUp Page",
                      attachment_type=AttachmentType.PNG)
        myLogger.info("*****Expected Element for sign up page Found*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Expected Element for sign up page Not Found******")


@when('Click On Language Link')
def Clicklanguage(context):
    global signup_page
    signup_page = Signup(context.driver)
    #easygui.msgbox("Execution related popup?")
    time.sleep(1)


    try:
        signup_page.ClickonLanguageLink()
        login_password_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//img[@src='/images/svg/signin/lang-mn.svg']")))
        assert True
        context.driver.save_screenshot(".\\Screenshots\\" + "SelectPasswordPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank SignUp Page is in English Language",
                      attachment_type=AttachmentType.PNG)
        myLogger.info("*****Expected Element for sign up page Found in English Language*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Expected Element for sign up page Not Found in English Language******")



@when(u'Set Valid Drop Down Values')
def step_impl(context):
    global signup_page
    signup_page = Signup(context.driver)
    signup_page.MyDropwon()



@when(u'Enter Input fields For signUp')
def AAAstep_impl(context):
    global signup_page
    signup_page = Signup(context.driver)

    data_sheet_path = "C:\\KhanBankApp\\TestData\\DataSheet.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Datasheet_Signup")


    Reg_number = Utilities.excelUtils.readData(data_sheet_path,"Datasheet_Signup",3 ,1)

    signup_page.enterReg_number(Reg_number)
    signup_page.enterEmailid()
    signup_page.enterPhone_number()
    signup_page.clickOn_ContinueButton()
    try:
        time.sleep(3)
        if (context.driver.find_element(By.XPATH,"//input[@id='otp']").is_displayed()):
        # email_radio_button = context.driver.find_element(By.XPATH, "//input[@value='EMAIL']")
            myLogger.info("The OTP Page is present")

            Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup", 3, 5, "Test Passed")
            context.driver.save_screenshot(".\\Screenshots\\" + "CorrectForeignDataForSPWD.png")
            allure.attach(context.driver.get_screenshot_as_png(),
                      name="Khan Bank OTP Channel Selection Page Displayed",
                      attachment_type=AttachmentType.PNG)
            myLogger.info("*****Expected Element Email Radio Button is Found*****")
            context.driver.find_element(By.CLASS_NAME, "ant-page-header-back-button").click()

    except NoSuchElementException:
        myLogger.info("*****Expected OTP Page is not found")
        Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup", 3, 5, "Test Failed")
    context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectForeignDataForSPWD.png")
    allure.attach(context.driver.get_screenshot_as_png(),
                  name="Khan Bank OTP Channel Selection Page Not Displayed",
                  attachment_type=AttachmentType.PNG)
    # time.sleep(2)

@then(u'Click on Continue button')
def continuebuttn(context):

    global signup_page
    signup_page = Signup(context.driver)
    signup_page.clickOn_ContinueButton()
    #Verify Message
    try:

        login_password_element = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='otp']")))
        assert True
        context.driver.save_screenshot(".\\Screenshots\\" + "SelectPasswordPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Signup OTP Page",
                      attachment_type=AttachmentType.PNG)
        myLogger.info("*****Expected Element for signUp OTP page Found*****")

    except Exception as e:
        myLogger.exception(e)
        myLogger.info("*****Expected Element for sign up OTP page Not Found******")




    #context.driver.find_element_by_xpath("(//input[@type='search'])[1]").click()
     #context.driver.find_element_by_xpath("//div[@class='ant-select-item-option-content'][text()='A']").click()
     #context.driver.find_element_by_xpath("(//input[@type='search'])[2]").click()
     #context.driver.find_element_by_xpath("(//input[@type='search'])[2]").send_keys(Keys.DOWN + Keys.DOWN+ Keys.DOWN + Keys.ENTER)
     #context.driver.find_element_by_xpath("//input[@class='ant-input'][2]").send_keys("9898654")
     #context.driver.find_element_by_xpath("//input[@id='email']").send_keys("Priti@domain.com")
     #context.driver.find_element_by_xpath("//input[@id='phoneNumber']").send_keys("100")




@then(u'I close the browser')
def step_impl(context):
    context.driver.close()
    myLogger.info("Browser is closed")


@when(u'To check All 35 Cyrillic characters')
def CheckAllcharFor_dropdown(context):
    global signup_page
    signup_page = Signup(context.driver)
    signup_page.CheckAllCharatorsfromDropdown()

