from appium import webdriver
from appium.webdriver.appium_service import AppiumService

# from src.Runner.test_Onboarding import click_id, click_acc
from appium.webdriver.common.appiumby import AppiumBy

appium_service = AppiumService()
AppiumService().start()
print('Start Appium')
desired_caps = {
    'platformName': 'Android',
    'udid': 'PD21BDD464023694',
    'platformVersion': '12',
    'appPackage': 'com.logitech.logue',
    'appActivity': 'com.logitech.logue.activity.SplashActivity',
    'noReset': 'true'
}
# # dict (
# #     platform = 'Android'
# #     uuid = 'PD21BDD464023694'
# #     platform = 'Android'
# #     pla
# # )
#
#
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
# yield driver
# driver.quit()
appium_service.stop()


# driver_info = None
# appium_service = None


# def setup_function():
#     global appium_service
#     appium_service = AppiumService()
#     appium_service.start()
#
#     desired_caps = {"platformName": "Android",
#                     "appium:udid": "PD21BDD464023694",
#                     "appium:platformVersion": "12", 'appPackage': 'com.logitech.logue',
#                     'appActivity': 'com.logitech.logue.activity.SplashActivity'}
#
#     global driver_info
#     driver_info = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#     driver_info.implicitly_wait(10)
#     yield driver_info
#     driver_info.quit()
#     appium_service.stop()


# def click_id(element_id=None):
#     driver.implicitly_wait(5)
#     driver.find_element(AppiumBy.ID, element_id).click()
#
#
# def click_acc(access_id=None):
#     driver.implicitly_wait(5)
#     driver.find_element(AppiumBy.ACCESSIBILITY_ID, access_id).click()


def click_id(element_id=None):
    driver.implicitly_wait(5)
    driver.find_element(AppiumBy.ID, element_id).click()


def click_acc(access_id=None):
    driver.implicitly_wait(5)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, access_id).click()


def click_text(class_name=None):
    driver.implicitly_wait(5)
    driver.find_element_by_name(AppiumBy.TEXT, class_name).click()


def enter_text(enter_text_1=None, info_dt=None):
    driver.implicitly_wait(5)
    driver.findElement(AppiumBy.ID, enter_text_1.sendKeys(info_dt))


def test_sup_me():
    # click_id('com.logitech.logue:id/getStarted')
    # click_id('com.logitech.logue:id/btnContinue')
    # # driver.implicitly_wait(5)
    # click_id('com.logitech.logue:id/textview_skip')
    # # driver.implicitly_wait(5)
    # click_id('com.logitech.logue:id/btnDecline')
    # # driver.implicitly_wait(5)
    # click_id('com.logitech.logue:id/progressText')
    # driver.implicitly_wait(5)
    click_acc('Navigate up')
    # driver.implicitly_wait(5)
    click_id('com.logitech.logue:id/rename')
    # driver.implicitly_wait(5)
    click_id('com.logitech.logue:id/surpriseButton')
    # driver.implicitly_wait(5)
    click_id('com.logitech.logue:id/saveButton')
    # driver.implicitly_wait(5)
    click_acc('Navigate up')
    # driver.implicitly_wait(5)
    # driver.implicitly_wait(5)
    # driver.find_element(AppiumBy.ID, 'com.logitech.logue:id/getStarted').click()
    # driver.implicitly_wait(5)
    # driver.find_element(AppiumBy.ID, 'com.logitech.logue:id/btnContinue').click()
    # driver.implicitly_wait(5)
    # driver.find_element(AppiumBy.ID, 'com.logitech.logue:id/textview_skip').click()
    # driver.implicitly_wait(5)
    # driver.find_element(AppiumBy.ID, 'com.logitech.logue:id/btnDecline').click()
    # driver.implicitly_wait(5)
    # driver.find_element(AppiumBy.ID, 'com.logitech.logue:id/progressText').click()
    # driver.implicitly_wait(5)
    # driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Navigate up').click()
    # driver.implicitly_wait(5)
    # driver.find_element(AppiumBy.ID, 'com.logitech.logue:id/rename').click()
    # driver.implicitly_wait(10)
    # driver.find_element(AppiumBy.ID, 'com.logitech.logue:id/surpriseButton').click()
    # driver.implicitly_wasit(10)
    # driver.find_element(AppiumBy.ID, 'com.logitech.logue:id/saveButton').click()
    # driver.implicitly_wait(5)
    # driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Navigate up').click()
