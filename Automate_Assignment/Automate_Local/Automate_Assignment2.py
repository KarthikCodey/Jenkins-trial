from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://www.browserstack.com/live')
    sign_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Sign in')
    ))
    sign_link.click()
    
    #Incorrect Email
    username = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#user_email_login')
    ))
    username.send_keys('warne708murali800gmail.com')
    
    password = driver.find_element(By.CSS_SELECTOR, '#user_password')
    password.send_keys('Shane@800')
    
    
    driver.find_element(By.CSS_SELECTOR, '#user_submit').click()

    
    time.sleep(3)
    username.clear()
    password.clear()
    print('Incorrect Email Scenario')

    #Incorrect Password
    username = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#user_email_login')
    ))
    username.send_keys('warne708murali800@gmail.com')
    
    password = driver.find_element(By.CSS_SELECTOR, '#user_password')
    password.send_keys('Shane$800')
    
    
    driver.find_element(By.CSS_SELECTOR, '#user_submit').click()
    
    time.sleep(3)
    username.clear()
    password.clear()
    print('Incorrect Password Scenario')

    #Unregistered Email
    username = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#user_email_login')
    ))
    username.send_keys('warne708murali800@hmail.com')
    password = driver.find_element(By.CSS_SELECTOR, '#user_password')
    password.click()
    time.sleep(3)
    lusername = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#user_full_name')
    ))
    time.sleep(3)

    choices = driver.find_element(By.CSS_SELECTOR,"a.sign-in-link")
    choices.click()
    
    time.sleep(3)
    print('Unregistered Mail Scenario')
    
    #Correct Scenario
    username = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#user_email_login')
    ))
    username.send_keys('warne708murali800@gmail.com')
    
    password = driver.find_element(By.CSS_SELECTOR, '#user_password')
    password.send_keys('Shane@800')
    
    driver.find_element(By.CSS_SELECTOR, '#user_submit').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.LINK_TEXT, 'Live')))

    #time.sleep(10)
    print('Correct Scenario')

finally:
    driver.quit()
