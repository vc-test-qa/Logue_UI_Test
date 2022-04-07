from appium import webdriver


class Driver:
    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '12'
        desired_caps['uuid'] = '0B231JEC207105'
        desired_caps['appPackage'] = 'com.logitech.logue'
        desired_caps['appActivity'] = 'com.logitech.logue.activity.SplashActivity'

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver
