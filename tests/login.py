from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from base.orange_selenium_driver import SeleniumDriver
from pages.login_page import LoginPage
import time
import unittest

class TestLoginOrange(unittest.TestCase):

    def test(self):
        driverLocation = "C:\\Users\\mkasvi\\Selenium_tutorial\\Libs\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseURL = "https://opensource-demo.orangehrmlive.com/"
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)

        LPP = LoginPage(driver)
        LPP.login("Admin","admin123")

        loginIcon = driver.find_element(By.XPATH,"//a[@id='welcome']")
        if loginIcon is not None:
            print("Login Successful")
        else:
            print("login unsuccessful")

TLO = TestLoginOrange()
TLO.test()
