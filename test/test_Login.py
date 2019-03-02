import time

from selenium import webdriver

def test_launch_browser():
    global driver
    driver = webdriver.Chrome(executable_path="C:/Users/celin/PycharmProjects/Automation_POM_Framework/drivers/chromedriver.exe")

    driver.get("https://demo.actitime.com/login.do")
    driver.maximize_window()
    driver.implicitly_wait(30)

def test_login():
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_name("pwd").send_keys("manager")
    driver.find_element_by_xpath("//div[text()='Login ']").click()


def test_logout():
    time.sleep(5)
    driver.find_element_by_xpath("//*[text()='Logout']").click()

# launch_browser()
# login()
# logout()