from appium import webdriver
# 配置项
des = {
    'platformName': 'Android',
    'platformVersion': '8.1',
    'deviceName': 'Samsun Galaxy Note 2',
    'app': 'D:/newdream/APK/jisuanqi_587.apk',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'udid': '192.168.164.105:5555',
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    # 'neCommandTimeout'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)