import time

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By

desired_cap = {
    "platformName": "Android",
    "appium:udid": "PD21BDD464023694",
    "appium:platformVersion": "12",
    "appium:appPackage": "com.logitech.logue",
    "appium:appActivity": "com.logitech.logue.activity.SplashActivity"
}

# appium_service = AppiumService()
# appium_service.start()
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

time.sleep(15)
driver.find_element(By.NAME, 'GET STARTED').click()
time.sleep(15)
driver.find_element(By.NAME, 'CONTINUE').click()

# appium_service.stop()
