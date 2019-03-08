import time
import os
import pytest
from selenium import webdriver
from Pages.loginpage import LoginPage
from Pages.homepage import HomePage
from utils.constants import *

@pytest.mark.usefixtures("test_launch_browser")
class TestLogin:
    def test_login(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_user_name()
        lp.enter_password()
        lp.click_on_login_btn()

    def test_logout(self):
        driver = self.driver
        time.sleep(30)
        # driver.find_element_by_xpath("//*[text()='Logout']").click()
        hp = HomePage(driver)
        hp.click_on_logout()
