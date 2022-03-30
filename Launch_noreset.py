from appium import webdriver
from appium.webdriver.appium_service import AppiumService


# desired_cap = {
#     "platformName": "Android",
#     "appium:udid": "PD21BDD464023694",
#     "appium:platformVersion": "12",
#     "appium:appPackage": "com.logitech.logue",
#     "appium:appActivity": "com.logitech.logue.activity.SplashActivity"
# }
#
#
# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

desired_cap_reset = {
  "platformName": "Android",
  "appium:udid": "PD21BDD464023694",
  "appium:platformVersion": "12",
  "appium:appPackage": "com.logitech.logue",
  "appium:appActivity": "com.logitech.logue.activity.SplashActivity",
  "appium:noReset": "true"
}


driver_no_reset = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap_reset)

# def setup_function():
#     appium_service = AppiumService()
#     appium_service.start()
#
#     desired_caps = {"platformName": "Android",
#                     "appium:udid": "PD21BDD464023694",
#                     "appium:platformVersion": "12", 'appPackage': 'com.logitech.logue',
#                     'appActivity': 'com.logitech.logue.activity.SplashActivity'}
#
#     driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#     appium_service.stop()


