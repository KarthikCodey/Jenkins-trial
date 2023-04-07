from appium import webdriver
from appium import webdriver as driver
from os import path
#from appium.options.android import UiAutomator2Options
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import pytest
import urllib3
import warnings
import sys
#import pytest_html
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


@pytest.mark.usefixtures("driver_init_1")
class BasicTest:
    pass
class Test_URL(BasicTest):
        def test_login(self):
            # Log in to the application
            wait = WebDriverWait(self.driver, 10)
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
            wait.until(EC.presence_of_element_located(
                (MobileBy.ID, 'com.android.permissioncontroller:id/permission_deny_button'))).click()
            wait.until(EC.presence_of_element_located(
                (MobileBy.ID, 'org.wikipedia:id/view_announcement_action_negative'))).click()
            # Check if user is logged in
            wait.until(EC.presence_of_element_located(
                (MobileBy.ID, 'org.wikipedia:id/drawer_icon_menu'))).click()
            elll=wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[1]'))).text
            print(elll)
            assert elll == 'John123W'
            self.driver.back()
            self.driver.quit()

        def test_wrong_search(self):
            # Search for wrong text
            wait = WebDriverWait(self.driver, 10)
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
            wait.until(EC.presence_of_element_located(
                (MobileBy.ID, 'com.android.permissioncontroller:id/permission_deny_button'))).click()
            wait.until(EC.presence_of_element_located(
                (MobileBy.ID, 'org.wikipedia:id/view_announcement_action_negative'))).click()
            wait.until(EC.presence_of_element_located(
                (MobileBy.ACCESSIBILITY_ID, 'Search Wikipedia'))).click()
            search = wait.until(EC.presence_of_element_located(
                (MobileBy.ID, 'org.wikipedia:id/search_src_text')))
            search.click()
            search.send_keys('BroSdfkEaaw'+'\n')
            Res=wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView'))).text
            print(Res)
            assert Res == 'No results found'
            self.driver.quit()
            

        def test_correct_search(self):  
            #Search for correct text
            wait = WebDriverWait(self.driver, 10)
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
            wait.until(EC.presence_of_element_located(
                (MobileBy.ID, 'com.android.permissioncontroller:id/permission_deny_button'))).click()
            wait.until(EC.presence_of_element_located(
                (MobileBy.ID, 'org.wikipedia:id/view_announcement_action_negative'))).click()
            print('logged in')
            wait.until(EC.presence_of_element_located(
                (MobileBy.ACCESSIBILITY_ID, 'Search Wikipedia'))).click()
            print('logged in1')
            search = wait.until(EC.presence_of_element_located(
                (MobileBy.ID, 'org.wikipedia:id/search_src_text')))
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
            self.driver.quit()    

