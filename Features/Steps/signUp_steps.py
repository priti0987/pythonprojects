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
    try:
        signup_page.ClickonLanguageLink()
        login_password_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//a[@href='/auth/signup/step/1']")))
        assert True
        if(context.driver.find_element(By.XPATH,"//a[normalize-space()='Sign Up']").is_displayed):
            context.driver.save_screenshot(".\\Screenshots\\" + "SelectPasswordPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank SignUp Page is in English Language",
                       attachment_type=AttachmentType.PNG)
            myLogger.info("*****Expected Element for sign up page Found in English Language*****")
        elif(context.driver.find_element(By.XPATH,"//a[contains(text(),'Бүртгүүлэх')]").is_displayed):

            context.driver.save_screenshot(".\\Screenshots\\" + "SelectPasswordPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank SignUp Page is in English Language",
                       attachment_type=AttachmentType.PNG)
            myLogger.info("*****Expected Element for sign up page Found in Mongolian Language*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("*****Expected Element for sign up page Not Found in English Language******")


@when(u'Set Valid dropdown Values')
def Validvaluesdropdown(context):
    global signup_page
    signup_page = Signup(context.driver)
    signup_page.MyDropwon()

@when(u'Set Valid Values')
def Validvalues(context):
    global signup_page
    signup_page = Signup(context.driver)
    signup_page.MyDropwon()
    signup_page.enterValidSignUpdata()
    signup_page.clickOn_ContinueButton()
    try:
            time.sleep(8)
            if(WebDriverWait(context.driver, 20).until(EC.presence_of_element_located(
                            (By.XPATH, '//input[@id="otp"]'))).is_displayed()):
                    myLogger.info("The OTP Page is present")

                    context.driver.save_screenshot(".\\Screenshots\\" + "OTP_Page.png")
                    allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank OTP Channel Selection Page Displayed",
                        attachment_type=AttachmentType.PNG)
                    myLogger.info("*****Expected OTP Page is Found*****")
                    context.driver.find_element(By.CLASS_NAME, "ant-page-header-back-button").click()

    except NoSuchElementException:
                    myLogger.info("*****Expected OTP Page is not found")
                    context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectOTPPAGE.png")
                    allure.attach(context.driver.get_screenshot_as_png(),
                    name="Khan Bank OTP Channel Selection Page Not Displayed",
                    attachment_type=AttachmentType.PNG)

@when(u'Set ValidSignUpdata')
def Validvalues(context):
        global signup_page
        signup_page = Signup(context.driver)

        signup_page.enterValidSignUpdata()
        signup_page.clickOn_ContinueButton()
        try:
            time.sleep(8)
            if(WebDriverWait(context.driver, 20).until(EC.presence_of_element_located(
                            (By.XPATH, '//input[@id="otp"]'))).is_displayed()):
                    myLogger.info("The OTP Page is present")
                    easygui.msgbox("page")

                    context.driver.save_screenshot(".\\Screenshots\\" + "OTP_Page.png")
                    allure.attach(context.driver.get_screenshot_as_png(),
                          name="Khan Bank OTP Channel Selection Page Displayed",
                        attachment_type=AttachmentType.PNG)
                    myLogger.info("*****Expected OTP Page is Found*****")

        except NoSuchElementException:
                    myLogger.info("*****Expected OTP Page is not found")
                    context.driver.save_screenshot(".\\Screenshots\\" + "IncorrectOTPPAGE.png")
                    allure.attach(context.driver.get_screenshot_as_png(),
                    name="Khan Bank OTP Channel Selection Page Not Displayed",
                    attachment_type=AttachmentType.PNG)




@when(u'Enter Input fields For signUp')
def EnterFields(context):
    global login_page
    login_page = Login(context.driver)

    global signup_page
    signup_page = Signup(context.driver)

    data_sheet_path = "C:\\KhanBankApp\\TestData\\DataSheet.xlsx"
    rows = Utilities.excelUtils.getRowCount(data_sheet_path, "Datasheet_Signup")

    for r in range(3, rows + 1):
        #signup_page.MyDropwon()
        Reg_number = Utilities.excelUtils.readData(data_sheet_path,"Datasheet_Signup",r ,1)
        Emailid = Utilities.excelUtils.readData(data_sheet_path,"Datasheet_Signup",r,2)
        Phone_number = Utilities.excelUtils.readData(data_sheet_path,"Datasheet_Signup",r,3)
        signup_page.enterReg_number(Reg_number)
        signup_page.enterEmailid(Emailid)
        signup_page.enterPhone_number(Phone_number)
        signup_page.clickOn_ContinueButton()
        time.sleep(8)
        try:
            if(WebDriverWait(context.driver, 20).until(EC.presence_of_element_located(
                                (By.XPATH, "//div[text()='Enter registration number']"))).is_displayed()):
                myLogger.info("Enter registration number")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup", r, 5, "Test passes")

            elif(WebDriverWait(context.driver, 20).until(EC.presence_of_element_located(
                                (By.XPATH, "//button[@id='email']"))).is_displayed()):

                myLogger.info("Invalid Email id")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup", r, 5, "test passes")
            elif (WebDriverWait(context.driver, 30).until(EC.presence_of_element_located(
                    (By.XPATH, "//button[@id='otp']"))).is_displayed()):
                easygui.msgbox("otppage")
                myLogger.info("OTP Page")
                Utilities.excelUtils.writeData(data_sheet_path, "Datasheet_Signup", r, 5, "test passes")

        except:
                easygui.msgbox("exp")
                myLogger.info("*****Popup*****")
                error_popup_close_button = WebDriverWait(context.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@class='kb-button with-bordered']")))
                error_popup_close_button.click()


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
def step_impl_Close(context):
    context.driver.close()
    myLogger.info("Browser is closed")


@when(u'To check All 35 Cyrillic characters')
def CheckAllcharFor_dropdown(context):
    global signup_page
    signup_page = Signup(context.driver)
    signup_page.CheckAllCharatorsfromDropdown()

