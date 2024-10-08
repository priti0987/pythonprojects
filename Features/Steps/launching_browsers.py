import time

import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from PageObjects.login import Login
from PageObjects.selectPassword import SelectPwd
from PageObjects.mongolianCustomerPassword import MongolianCustomerPassword
from Utilities.constants import Constants
from Utilities.customLogger import LogGen

myLogger = LogGen.logGen()

@given(u'I initiate the Microsoft Edge Browser')
def initiate_edge(context):
    context.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    myLogger.info("*****Microsoft Driver Initialized*****")


@given(u'I initiate the Google Chrome Browser')
def initiate_chrome(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    myLogger.info("*****Google Chrome Driver Initialized*****")


@given(u'I initiate the Mozilla Firefox Browser')
def initiate_firefox(context):
    context.driver = webdriver.Firefox()
    myLogger.info("*****Mozilla FIrefox Driver Initialized*****")


@given(u'I initiate the IE Browser')
def initiate_ie(context):
    context.driver = webdriver.Ie(IEDriverManager().install())
    myLogger.info("*****IE Driver Initialized*****")



