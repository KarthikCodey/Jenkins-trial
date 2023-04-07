from appium import webdriver
from os import path
#from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import os

options = ({
    "app":"bs://6a9816144584f6a2e71213e587044bd4903147c4",#wikipedia
    "platformVersion" : "9.0",
    "deviceName" : "Google Pixel 3",
    # Set other BrowserStack capabilities
    'bstack:options' : {
        "projectName" : "First Python project",
        "buildName" : "browserstack-build-1",
        "sessionName" : "BStack first_test",
        # Set your access credentials
        "userName" : os.environ["BROWSERSTACK_USERNAME"],
        "accessKey" : os.environ["BROWSERSTACK_ACCESS_KEY"]
    }
})
# Initialize the remote Webdriver using BrowserStack remote URL
# and options defined above
driver = webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub", desired_capabilities= options)


try:
    #Log in to the application
    wait = WebDriverWait(driver, 10)
    time.sleep(5)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button'))).click()
    wait.until(EC.presence_of_element_located(
        (MobileBy.ID, 'org.wikipedia:id/drawer_icon_menu'))).click()
    wait.until(EC.presence_of_element_located(
        (MobileBy.ID, 'org.wikipedia:id/main_drawer_login_button'))).click()
    wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText'))).send_keys('John123W')
    wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText'))).send_keys('Wick456J')
    wait.until(EC.presence_of_element_located(
        (MobileBy.ID, 'org.wikipedia:id/login_button'))).click()
    #Check if user is logged in
    wait.until(EC.presence_of_element_located(
        (MobileBy.ID, 'org.wikipedia:id/drawer_icon_menu'))).click()
    elll=wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[1]'))).text
    print(elll)
    assert elll == 'John123W'
    driver.back()
    #Search for wrong text
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Search Wikipedia'))).click()
    search = wait.until(EC.presence_of_element_located(
        (MobileBy.CLASS_NAME, 'android.widget.EditText')))
    search.click()
    search.send_keys('BroSdfkEaaw'+'\n')
    Res=wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView'))).text
    print(Res)
    assert Res == 'No results found'
    #Search for correct text
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Clear query'))).click()
    search.click()
    search.send_keys('BrowserStack'+'\n')
    Res1=wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.view.ViewGroup[1]/android.widget.TextView[2]')))
    print(Res1.text)
    assert Res1.text == 'Software company based in India'
    Res1.click()
    Res2=wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[5]/android.view.View/android.widget.TextView[1]'))).text
    print(Res2)
    assert Res2 == 'The subscription-based service was founded by Ritesh Arora and Nakul Aggarwal in 2011'
    
finally:
    driver.quit()


