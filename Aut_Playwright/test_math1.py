from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

def pytest_namespace():
    driver = webdriver.Chrome()
    name = 2

def test_OpenBE(self):
    print(self.name)
    wait = WebDriverWait(pytest.driver, 10)
    pytest.driver.get('https://www.browserstack.com/live')
    sign_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Sign in')
    ))
    sign_link.click()

#def tes_navigateToSubmit():
        #browser.get('urlremoved.com')
        #time.sleep(10)
        #browser.find_element_by_id('button').click()

#def tes_Submission():
        #browser.get('urlremoved.com')
        #browser.find_element_by_id('Name').send_keys("Name here")
        #browser.find_element_by_id("ID").send_keys("123456")
        #browser.find_element_by_id("email").send_keys("email@email.com")