# Import the 'modules' that are required for execution to run Selenium tests in parallel with Python
import pytest
from selenium import webdriver
import urllib3
import warnings
import os

username=os.environ.get('BROWSERSTACK_USERNAME')
key=os.environ.get('BROWSERSTACK_ACCESS_KEY')

ch_cap = {
	'bstack:options' : {
		"os" : "Windows",
		"osVersion" : "11",
		"browserVersion" : "latest",
        "projectName" : "Auto Parallel",
		"buildName" : "Ch 1",
		"local" : "false",
		"seleniumVersion" : "3.5.2",
	},
	"browserName" : "Edge",
}

ch1_cap = {
	'bstack:options' : {
		"os" : "OS X",
		"osVersion" : "Monterey",
		"browserVersion" : "latest",
        "projectName" : "Auto Parallel",
		"buildName" : "Ch 2",
		"local" : "false",
		"seleniumVersion" : "3.14.0",
	},
	"browserName" : "Chrome",
}

saf_cap = {
	'bstack:options' : {
		"os" : "OS X",
		"osVersion" : "Monterey",
		"browserVersion" : "15.0",
        "projectName" : "Auto Parallel",
		"buildName" : "Saf 1",
		"local" : "false",
		"seleniumVersion" : "3.14.0",
	},
	"browserName" : "Safari",
}

saf1_cap = {
	'bstack:options' : {
		"os" : "OS X",
		"osVersion" : "Big Sur",
		"browserVersion" : "14.0",
		"projectName" : "Auto Parallel",
		"buildName" : "Saf 2",
		"local" : "false",
		"seleniumVersion" : "3.14.0",
	},
	"browserName" : "Safari",
}

fire_cap = {
	'bstack:options' : {
		"os" : "OS X",
		"osVersion" : "Monterey",
		"browserVersion" : "latest",
        "projectName" : "Auto Parallel",
		"buildName" : "Fire 1",
		"local" : "false",
		"seleniumVersion" : "3.10.0",
	},
	"browserName" : "Firefox",
}

fire1_cap = {
	'bstack:options' : {
		"os" : "Windows",
		"osVersion" : "11",
		"browserVersion" : "latest",
		"projectName" : "Auto Parallel",
		"buildName" : "Fire 2",
		"local" : "false",
		"seleniumVersion" : "3.10.0",
	},
	"browserName" : "Firefox",
}


ie_cap = {
	'bstack:options' : {
		"os" : "Windows",
		"osVersion" : "8.1",
		"browserVersion" : "11.0",
        "projectName" : "Auto Parallel",
		"buildName" : "IE 1",
		"local" : "false",
		"seleniumVersion" : "3.5.2",
	},
	"browserName" : "IE",
}

ie1_cap = {
	'bstack:options' : {
		"os" : "Windows",
		"osVersion" : "10",
		"browserVersion" : "11.0",
		"projectName" : "Auto Parallel",
		"buildName" : "IE 2",
		"local" : "false",
		"seleniumVersion" : "3.5.2",
	},
	"browserName" : "IE",
}


edge_cap = {
	'bstack:options' : {
		"os" : "OS X",
		"osVersion" : "Monterey",
		"browserVersion" : "latest",
		"projectName" : "Auto Parallel",
		"buildName" : "Edge 1",
		"local" : "false",
		"seleniumVersion" : "3.5.2",
	},
	"browserName" : "Edge",
}

edge1_cap = {
	'bstack:options' : {
		"os" : "Windows",
		"osVersion" : "11",
		"browserVersion" : "latest",
		"projectName" : "Auto Parallel",
		"buildName" : "Edge 2",
		"local" : "false",
		"seleniumVersion" : "3.5.2",
	},
	"browserName" : "Edge",
}

 

@pytest.fixture(scope="class")
def driver_init_1(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "https://" + username + ":" + key + "@hub.browserstack.com/wd/hub"
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities = ch_cap)
    request.cls.driver = web_driver
    yield
    web_driver.close()

@pytest.fixture(scope="class")
def driver_init_2(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "https://" + username + ":" + key + "@hub.browserstack.com/wd/hub"
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities = ch1_cap)
    request.cls.driver = web_driver
    yield
    web_driver.close()
    
@pytest.fixture(scope="class")
def driver_init_3(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "https://" + username + ":" + key + "@hub.browserstack.com/wd/hub"
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities = saf_cap)
    request.cls.driver = web_driver
    yield
    web_driver.close()
    
@pytest.fixture(scope="class")
def driver_init_4(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "https://" + username + ":" + key + "@hub.browserstack.com/wd/hub"
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities = saf1_cap)
    request.cls.driver = web_driver
    yield
    web_driver.close()
    
@pytest.fixture(scope="class")
def driver_init_5(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "https://" + username + ":" + key + "@hub.browserstack.com/wd/hub"
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities = fire_cap)
    request.cls.driver = web_driver
    yield
    web_driver.close()
    
@pytest.fixture(scope="class")
def driver_init_6(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "https://" + username + ":" + key + "@hub.browserstack.com/wd/hub"
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities = fire1_cap)
    request.cls.driver = web_driver
    yield
    web_driver.close()
    
@pytest.fixture(scope="class")
def driver_init_7(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "https://" + username + ":" + key + "@hub.browserstack.com/wd/hub"
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities = ie_cap)
    request.cls.driver = web_driver
    yield
    web_driver.close()
    
@pytest.fixture(scope="class")
def driver_init_8(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "https://" + username + ":" + key + "@hub.browserstack.com/wd/hub"
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities = ie1_cap)
    request.cls.driver = web_driver
    yield
    web_driver.close()
    
@pytest.fixture(scope="class")
def driver_init_9(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "https://" + username + ":" + key + "@hub.browserstack.com/wd/hub"
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities = edge_cap)
    request.cls.driver = web_driver
    yield
    web_driver.close()
    
@pytest.fixture(scope="class")
def driver_init_91(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "https://" + username + ":" + key + "@hub.browserstack.com/wd/hub"
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities = edge1_cap)
    request.cls.driver = web_driver
    yield
    web_driver.close()

