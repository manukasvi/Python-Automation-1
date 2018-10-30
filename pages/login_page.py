from selenium import webdriver
from selenium.webdriver.common.by import By
from base.orange_selenium_driver import SeleniumDriver
import os
from selenium.webdriver.support.select import Select
import time

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _login_link = "Login"
    _user_name_field = "txtUsername"
    _password_field = "txtPassword"
    _login_button = "btnLogin"

    def enterEmail(self, email):
        self.sendKeys(email, self._user_name_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def dropDownSelect(self):
        timeZoneElement = self.driver.find_element(By.XPATH, "//select[@name='timezone']")
        sel = Select(timeZoneElement)
        sel.select_by_visible_text("(GMT+05:30) Chennai, Kolkata, Mumbai, New Delhi")
        time.sleep(5)

    def clickLoginButton(self):
        self.elementClick(self._login_button)

    def login(self, email, password):
        #self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        #self.dropDownSelect()
        self.clickLoginButton()








