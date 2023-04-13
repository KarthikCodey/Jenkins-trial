import pytest
import sys
#import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

 
@pytest.mark.usefixtures("driver_init_6")
class BasicTest:
    pass
class Test_URL(BasicTest):
    def test_open_url(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.browserstack.com/live")
        self.driver.maximize_window()
        sign_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Sign in')
        ))
        sign_link.click()
        username = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#user_email_login')
        ))
        #assert username == ' '
        print(self.driver.title)
        self.driver.quit()

#Incorrect Email        
    def test_invalid_email(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.browserstack.com/live")
        self.driver.maximize_window()
        sign_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Sign in')
        ))
        sign_link.click()
        username = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#user_email_login')
        ))
        username.send_keys('warne708murali800gmail.com')

        password = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#user_password')
        ))
        password.send_keys('Shane@800')
        self.driver.find_element(By.CSS_SELECTOR, '#user_submit').click()
        time.sleep(3)
        username.clear()
        password.clear()
        print('Incorrect Email Scenario')
        self.driver.quit()

#Incorrect Password        
    def test_invalid_password(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.browserstack.com/live")
        self.driver.maximize_window()
        sign_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Sign in')
        ))
        sign_link.click()
        username = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#user_email_login')
        ))
        username.send_keys('warne708murali800@gmail.com')

        password = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#user_password')
        ))
        password.send_keys('Shane$800')
        self.driver.find_element(By.CSS_SELECTOR, '#user_submit').click()
        time.sleep(3)
        username.clear()
        password.clear()
        print('Incorrect Password Scenario')
        self.driver.quit()


#Unregistered Email        
    def test_unregistered(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.browserstack.com/live")
        self.driver.maximize_window()
        sign_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Sign in')
        ))
        sign_link.click()
        username = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#user_email_login')
        ))
        username.send_keys('warne708murali800@hmail.c')
        password = self.driver.find_element(By.CSS_SELECTOR, '#user_password')
        password.click()
        time.sleep(3)
        lusername = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#user_full_name')
        ))
        time.sleep(3)

        choices = self.driver.find_element(By.CSS_SELECTOR,"a.sign-in-link")
        choices.click()
        #time.sleep(15)
        username = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#user_email_login')
        ))    
        #assert username == ' '
        print('Unregistered Mail Scenario')
        self.driver.quit()


#Correct Scenario
    def test_correct(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.browserstack.com/live")
        self.driver.maximize_window()
        sign_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Sign in')
        ))
        sign_link.click()
        username = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#user_email_login')
        ))
        username.send_keys('warne708murali800@gmail.com')
        password = wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '#user_password')
                ))
        password.send_keys('Shane@800')
        self.driver.find_element(By.CSS_SELECTOR, '#user_submit').click()
        time.sleep(5)
        check=wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, 'Live')))
        #time.sleep(10)
        print('Correct Scenario')
        self.driver.quit()
