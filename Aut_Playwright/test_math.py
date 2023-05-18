import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

global wait 
global driver 
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
   def test_sqrt():
      num = 25
      driver.get('https://www.browserstack.com/live')
      sign_link = wait.until(EC.presence_of_element_located(
      (By.LINK_TEXT, 'Sign in')
      ))
      sign_link.click()
      assert math.sqrt(num) == 5

   def testSquare():
      num = 7
      assert 7*7 == 49

   def tesequality():
      assert 10 == 11

finally:
    driver.quit()