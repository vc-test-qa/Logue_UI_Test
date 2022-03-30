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

# desired_cap_reset = {
#   "platformName": "Android",
#   "appium:udid": "PD21BDD464023694",
#   "appium:platformVersion": "12",
#   "appium:appPackage": "com.logitech.logue",
#   "appium:appActivity": "com.logitech.logue.activity.SplashActivity",
#   "appium:noReset": "true"
# }
#
#
# driver_no_reset = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap_reset)

# driver = None
# appium_service = None


# global appium_service
# global driver


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
print('Stop Appium')
# def setup_function():
#     global appium_service
#     global driver
#     appium_service = AppiumService()
#     appium_service.start()
#
#     desired_caps = {}
#     desired_caps['platformName']: 'Android'
#     desired_caps['udid']: 'PD21BDD464023694'
#     desired_caps['platformVersion']: '12'
#     desired_caps['appPackage']: 'com.logitech.logue'
#     desired_caps['appActivity']: 'com.logitech.logue.activity.SplashActivity'
#
#     driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#     driver.implicitly_wait(10)
#
#
# def teardown_function():
#     # yield driver
#     driver.quit()
#     appium_service.stop()
