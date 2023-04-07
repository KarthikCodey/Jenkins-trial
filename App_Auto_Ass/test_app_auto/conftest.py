# Import the 'modules' that are required for execution to run Selenium tests in parallel with Python
import pytest
from selenium import webdriver
import urllib3
import warnings
import os
#from appium.options.android import UiAutomator2Options
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import appium


username=os.environ.get('BROWSERSTACK_USERNAME')
key=os.environ.get('BROWSERSTACK_ACCESS_KEY')

Pixel1_options = ({
    "app":"bs://6a9816144584f6a2e71213e587044bd4903147c4",#wikipedia
    "os_version" : "13.0",
    "device" : "Google Pixel 7 Pro",
    # Set other BrowserStack capabilities
    'bstack:options' : {
        "projectName" : "App Auto Parallel",
        "buildName" : "Pix1",
        "sessionName" : "Run1",
        # Set your access credentials
        "userName" : os.environ["BROWSERSTACK_USERNAME"],
        "accessKey" : os.environ["BROWSERSTACK_ACCESS_KEY"]
    }
})

Pixel2_options = ({
    "app":"bs://6a9816144584f6a2e71213e587044bd4903147c4",#wikipedia
    "os_version" : "12.0",
    "device" : "Google Pixel 6 Pro",
    # Set other BrowserStack capabilities
    'bstack:options' : {
        "projectName" : "App Auto Parallel",
        "buildName" : "Pix2",
        "sessionName" : "Run1",
        # Set your access credentials
        "userName" : os.environ["BROWSERSTACK_USERNAME"],
        "accessKey" : os.environ["BROWSERSTACK_ACCESS_KEY"]
    }
})

OneP1_options = ({
    "app":"bs://6a9816144584f6a2e71213e587044bd4903147c4",#wikipedia
    "os_version" : "11.0",
    "device" : "OnePlus 9",
    # Set other BrowserStack capabilities
    'bstack:options' : {
        "projectName" : "App Auto Parallel",
        "buildName" : "OneP1",
        "sessionName" : "Run1",
        # Set your access credentials
        "userName" : os.environ["BROWSERSTACK_USERNAME"],
        "accessKey" : os.environ["BROWSERSTACK_ACCESS_KEY"]
    }
})

OneP2_options = ({
    "app":"bs://6a9816144584f6a2e71213e587044bd4903147c4",#wikipedia
    "os_version" : "10.0",
    "device" : "OnePlus 8",
    # Set other BrowserStack capabilities
    'bstack:options' : {
        "projectName" : "App Auto Parallel",
        "buildName" : "OneP2",
        "sessionName" : "Run1",
        # Set your access credentials
        "userName" : os.environ["BROWSERSTACK_USERNAME"],
        "accessKey" : os.environ["BROWSERSTACK_ACCESS_KEY"]
    }
})

Samsung1_options = ({
    "app":"bs://6a9816144584f6a2e71213e587044bd4903147c4",#wikipedia
    "os_version" : "12.0",
    "device" : "Samsung Galaxy Tab S8",
    # Set other BrowserStack capabilities
    'bstack:options' : {
        "projectName" : "App Auto Parallel",
        "buildName" : "Sam1",
        "sessionName" : "Run1",
        # Set your access credentials
        "userName" : os.environ["BROWSERSTACK_USERNAME"],
        "accessKey" : os.environ["BROWSERSTACK_ACCESS_KEY"]
    }
})

Samsung2_options = ({
    "app":"bs://6a9816144584f6a2e71213e587044bd4903147c4",#wikipedia
    "platformVersion" : "11.0",
    "deviceName" : "Samsung Galaxy Tab S7",
    # Set other BrowserStack capabilities
    'bstack:options' : {
        "projectName" : "App Auto Parallel",
        "buildName" : "Sam2",
        "sessionName" : "Run1",
        # Set your access credentials
        "userName" : os.environ["BROWSERSTACK_USERNAME"],
        "accessKey" : os.environ["BROWSERSTACK_ACCESS_KEY"]
    }
})


@pytest.fixture(scope="class")
def driver_init_1(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "http://hub.browserstack.com/wd/hub"
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities= Pixel1_options)
    request.cls.driver = web_driver
    yield
    web_driver.quit()

@pytest.fixture(scope="class")
def driver_init_2(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "http://hub.browserstack.com/wd/hub"
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities= Pixel2_options)
    request.cls.driver = web_driver
    yield
    web_driver.quit()

@pytest.fixture(scope="class")
def driver_init_3(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "http://hub.browserstack.com/wd/hub"
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities= OneP1_options)
    request.cls.driver = web_driver
    yield
    web_driver.quit()

@pytest.fixture(scope="class")
def driver_init_4(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "http://hub.browserstack.com/wd/hub"
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities= OneP2_options)
    request.cls.driver = web_driver
    yield
    web_driver.quit()

@pytest.fixture(scope="class")
def driver_init_5(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "http://hub.browserstack.com/wd/hub"
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities= Samsung1_options)
    request.cls.driver = web_driver
    yield
    web_driver.quit()

@pytest.fixture(scope="class")
def driver_init_6(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "http://hub.browserstack.com/wd/hub"
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities= Samsung2_options)
    request.cls.driver = web_driver
    yield
    web_driver.quit()
