from appium import webdriver
def init_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    # desired_caps['deviceName'] = '192.168.73.102:24'
    # desired_caps['deviceName'] = '192.168.238.101:24'
    desired_caps['deviceName'] = '192.168.73.102:5555'
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
