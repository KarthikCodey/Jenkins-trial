from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
#chrome_options.set_capability("browserVersion", "67")
#chrome_options.set_capability("platformName", "Windows XP")
driver = webdriver.Remote(
    command_executor='http://192.168.29.153:4444/wd/hub',
    options=chrome_options
)
driver.get("http://www.google.com")
driver.quit()  