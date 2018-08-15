# 导入单元测试框架
import unittest, time, os
# 导入自动化测试工具selenium
import selenium
from appium import webdriver


class Mytest(unittest.TestCase):
    def setUp(self):
        print('selenium version =', selenium.__version__)
        desired_caps = {}
        # 平台
        desired_caps['platformName'] = 'Android'
        # android版本
        desired_caps['platformVersion'] = '4.4.2'
        # 连接的设备名
        desired_caps['deviceName'] = '127.0.0.1:62001'
        # 包名
        desired_caps['appPackage'] = 'com.ztgame.fir.gseal'
        # Activity名
        desired_caps['appActivity'] = 'org.cocos2dx.lua.SplashActivity'

        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test1(self):
        print("1212")


if __name__ == '__main__':
    unittest.main()
