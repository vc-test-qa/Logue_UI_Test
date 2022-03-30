from appium.webdriver.common.appiumby import AppiumBy
from Launch import driver


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


def test_onboard():
    # setup_function()
    click_id('com.logitech.logue:id/getStarted')

    click_id('com.logitech.logue:id/btnContinue')
    # driver.implicitly_wait(5)
    click_id('com.logitech.logue:id/textview_skip')
    # driver.implicitly_wait(5)
    click_id('com.logitech.logue:id/btnDecline')
    # driver.implicitly_wait(5)
    click_id('com.logitech.logue:id/progressText')
