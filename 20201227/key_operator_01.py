from appium import webdriver
# 配置项
des = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "XIAO MI 6",
  "automationName": "UiAutomator1",
  "appPackage": "com.android.contacts",
  "appActivity": ".activities.PeopleActivity",
  "udid": "127.0.0.1:62026",
  "noReset": "True",
  "unicodeKeyboard": "True",
  "resetKeyboard": "True"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)

# element = driver.find_element_by_xpath('//android.widget.TextView[ends-with(@text,"leo")]')

# print(element)

# 拖拽元素
# driver.flick()

size = driver.get_window_size()

