from appium import webdriver
des ={
  "platformName": "Android",
  "platformVersion": "6.0.1",
  "deviceName": "mumu",
  "browserName": "Chrome",
  "udid": "127.0.0.1:62001",
  "noReset": "True",
  "unicodeKeyboard": "True",
  "resetKeyboard": "True",
  "chromedriverExecuteable":"D:/LEO/appium/chromedriver"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)
driver.get("https://www.qq.com")
# driver.implicitly_wait(10)
driver.find_element_by_link_text('体育').click()
