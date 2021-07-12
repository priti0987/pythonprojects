import time
import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from PageObjects.login import Login
from PageObjects.selectPassword import SelectPwd
from Utilities.constants import Constants
from Utilities.customLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

myLogger = LogGen.logGen()

