import pytest
from utils.constants import *
# import os
#
# path = os.getcwd()
# driver_path = path.replace("\\", "/")+ drivers

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in Browser Name eg. chrome, firefox")


@pytest.fixture(scope='class')
def test_launch_browser(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:/Users/celin/PycharmProjects/Automation_POM_Framework/drivers/chromedriver.exe")

    elif browser == "ff":
        driver = webdriver.Firefox(executable_path="C:/Users/celin/PycharmProjects/Automation_POM_Framework/drivers/geckodriver.exe")
    driver.get(URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver
    yield
    driver.quit()
