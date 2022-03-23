from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

desired_cap = {
    "platformName": "Android",
    "appium:udid": "PD21BDD464023694",
    "appium:platformVersion": "12",
    "appium:appPackage": "com.logitech.logue",
    "appium:appActivity": "com.logitech.logue.activity.SplashActivity"
}

desired_cap_1 = {
    "platformName": "Android",
    "appium:udid": "PD21BDD464023694",
    "appium:platformVersion": "12",
    "appium:appPackage": "com.jaybirdsport.audio",
    "appium:appActivity": "com.jaybirdsport.audio.ui.EntryActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

driver.implicitly_wait(5)
driver.find_element(AppiumBy.ID, 'com.logitech.logue:id/getStarted').click()
driver.implicitly_wait(5)
driver.find_element(AppiumBy.ID, 'com.logitech.logue:id/btnContinue').click()
driver.implicitly_wait(5)
driver.find_element(AppiumBy.ID, 'com.logitech.logue:id/textview_skip').click()
driver.implicitly_wait(5)
driver.find_element(AppiumBy.ID, 'com.logitech.logue:id/btnDecline').click()
driver.implicitly_wait(5)
driver.find_element(AppiumBy.ID, 'com.logitech.logue:id/progressText').click()
driver.implicitly_wait(5)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Navigate up').click()
driver.implicitly_wait(5)
driver.find_element(AppiumBy.ID, 'com.logitech.logue:id/rename').click()
driver.implicitly_wait(10)
driver.find_element(AppiumBy.ID, 'com.logitech.logue:id/surpriseButton').click()
driver.implicitly_wait(5)
driver.find_element(AppiumBy.ID, 'com.logitech.logue:id/saveButton').click()
driver.implicitly_wait(5)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Navigate up').click()
