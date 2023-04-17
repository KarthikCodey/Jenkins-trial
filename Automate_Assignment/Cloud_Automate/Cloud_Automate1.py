from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

#options = webdriver.ChromeOptions()

#chrome_options.add_argument("--headless")

# Set the path to your Chromedriver executable
#chromedriver_path = "/Users/karthik/Downloads"

# Set the system property
#chrome_options.add_argument(f"--webdriver.chrome.driver={chromedriver_path}")
username=os.environ.get('BROWSERSTACK_USERNAME')
key=os.environ.get('BROWSERSTACK_ACCESS_KEY')
# Replace <REMOTE_DRIVER_IP> and <REMOTE_DRIVER_PORT> with the IP address and port number of your remote Selenium driver
#remote_driver_url = "http://192.168.29.153:4444/wd/hub"
url = 'https://' +username+':'+ key + '@hub-cloud.browserstack.com/wd/hub'
#driver = webdriver.Remote(remote_driver_url, desired_capabilities=webdriver.DesiredCapabilities.CHROME)

# set the system property for ChromeDriver
chrome_driver_path = "/Users/karthik/Downloads/chromedriver"
webdriver.firefox.driver = chrome_driver_path
chrome_options = webdriver.FirefoxOptions()

# launch the Chrome browser
#driver = webdriver.Chrome()
# set browser options as required
driver = webdriver.Remote(url, options=chrome_options)


try:
    wait = WebDriverWait(driver, 20)
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
    #time.sleep(3)
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
    #WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    #    (By.LINK_TEXT, 'Live')))

    print('Correct Scenario')

finally:
    driver.quit()
