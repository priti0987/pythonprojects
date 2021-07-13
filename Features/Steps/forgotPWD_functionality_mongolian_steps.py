import time

import allure
from allure_commons.types import AttachmentType
from behave import *
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from PageObjects.recoverPassword import RecoverPassword
from Utilities.constants import Constants
from Utilities.customLogger import LogGen

myLogger = LogGen.logGen()

@when(u'I enter username and registration number')
def step_impl(context):
    global mongolian_customer_page
    mongolian_customer_page = MongolianCustomerPassword(context.driver)
    #mongolian_customer_page.setUsername("infura_7")
    #mongolian_customer_page.setRegNumber("61082018")
    #time.sleep(2)
    mongolian_customer_page.clickOnRegDrpDwn1()


@when(u'I click on Continue button')
def step_impl(context):
    global mongolian_customer_page
    mongolian_customer_page = MongolianCustomerPassword(context.driver)
    mongolian_customer_page.clickOnContinue()


@then(u'I should be displayed with the OTP channel selection page')
def step_impl(context):
    global recover_password_page
    recover_password_page = RecoverPassword(context.driver)
    try:
        title_recover_password = context.driver.find_element_by_xpath("//span[@title='Нууц үг сэргээх']").text
        if title_recover_password == "Нууц үг сэргээх":
            assert True
            context.driver.save_screenshot(".\\Screenshots\\" + "RecoverPasswordTitleMatches.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Recover Password Title Matches",
                  attachment_type=AttachmentType.PNG)
            myLogger.info("*****Recover Password title matches*****")
        else:
            assert False
            context.driver.save_screenshot(".\\Screenshots\\" + "RecoverPasswordTitleDoesNotMatch.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Khan Bank Recover Password Title does not match",
                          attachment_type=AttachmentType.PNG)
            myLogger.info("*****Recover Password title does not match*****")

    except Exception as e:
        myLogger.exception(e)
        context.driver.close()
        myLogger.info("Unable to validate the OTP channel selection page")











