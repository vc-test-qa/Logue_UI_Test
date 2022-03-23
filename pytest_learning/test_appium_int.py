from appium import webdriver
from appium.webdriver.appium_service import AppiumService

from appium.webdriver.common.appiumby import AppiumBy

from Launch import driver

driver_info = None
appium_service = None


def setup_function():
    global appium_service
    appium_service = AppiumService()
    appium_service.start()

    desired_caps = {"platformName": "Android",
                    "appium:udid": "PD21BDD464023694",
                    "appium:platformVersion": "12", 'appPackage': 'com.logitech.logue',
                    'appActivity': 'com.logitech.logue.activity.SplashActivity'}

    global driver_info
    driver_info = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver_info.implicitly_wait(10)
    yield driver
    driver.quit()
    driver_info.quit()
    appium_service.stop()


def click(element_id, waiting_time=5):
    driver_info.implicitly_wait(waiting_time)
    driver_info.find_element(AppiumBy.ID, element_id).click()


def test_onboard():
    driver_info.implicitly_wait(5)
    driver_info.find_element(AppiumBy.ID, 'com.logitech.logue:id/getStarted').click()
    driver_info.implicitly_wait(5)
    driver_info.find_element(AppiumBy.ID, 'com.logitech.logue:id/btnContinue').click()
    driver_info.implicitly_wait(5)
    driver_info.find_element(AppiumBy.ID, 'com.logitech.logue:id/textview_skip').click()
    driver_info.implicitly_wait(5)
    driver_info.find_element(AppiumBy.ID, 'com.logitech.logue:id/btnDecline').click()
    driver_info.implicitly_wait(5)
    driver_info.find_element(AppiumBy.ID, 'com.logitech.logue:id/progressText').click()
    driver_info.implicitly_wait(5)
    driver_info.find_element(AppiumBy.ACCESSIBILITY_ID, 'Navigate up').click()
    driver_info.implicitly_wait(5)
    driver_info.find_element(AppiumBy.ID, 'com.logitech.logue:id/rename').click()
    driver_info.implicitly_wait(10)
    driver_info.find_element(AppiumBy.ID, 'com.logitech.logue:id/surpriseButton').click()
    driver_info.implicitly_wait(10)
    driver_info.find_element(AppiumBy.ID, 'com.logitech.logue:id/saveButton').click()
    driver_info.implicitly_wait(5)
    driver_info.find_element(AppiumBy.ACCESSIBILITY_ID, 'Navigate up').click()
