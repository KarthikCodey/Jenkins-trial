import json
import urllib
import subprocess
from playwright.sync_api import sync_playwright
import os
import time
from multiprocessing import Process


def run_test(desired_capabilities):
    with sync_playwright() as playwright:
        clientPlaywrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
        desired_capabilities['client.playwrightVersion'] = clientPlaywrightVersion

        cdpUrl = 'wss://cdp.browserstack.com/playwright?caps=' + urllib.parse.quote(json.dumps(desired_capabilities))
        if desired_capabilities['browser'] == 'chrome':
            browser = playwright.chromium.connect(cdpUrl)
            print('Connected to Chromium')
        elif desired_capabilities['browser'] == 'playwright-firefox':
            browser = playwright.firefox.connect(cdpUrl)
            print('Connected to Firefox')
        elif desired_capabilities['browser'] == 'playwright-webkit':
            browser = playwright.webkit.connect(cdpUrl)
            print('Connected to Webkit')
        else:
            raise Exception('Unsupported browser: ' + desired_capabilities['browser'])

        context = browser.new_context()
        page = context.new_page()

        page.goto('https://www.browserstack.com/live')

        # incorrect email
        login = page.query_selector('[href="/users/sign_in"]')
        login.click()  # Step 1: Login
        page.fill('#user_email_login', 'warne708murali800@gmail.com')
        page.click('#user_submit')
        error_element = page.query_selector('div.error-msg.show span[aria-live="polite"]')
        time.sleep(10)
        pg = page.query_selector('[href="/users/password/new"]')
        assert pg is not None, "Element not found"

        # Correct email
        page.fill('#user_email_login', '')
        page.fill('#user_password', '')  # Clear the input field
        time.sleep(3)
        page.reload()

        page.fill('#user_email_login', 'warne708murali800@gmail.com')  # Step 2: Username
        page.fill('#user_password', 'Shane@800')  # Step 3: Password
        time.sleep(3)

        page.click('#user_submit')  # Step 4: Click Sign In
        print('hi1')
        time.sleep(10)
        dash = page.query_selector('[href="https://live.browserstack.com/dashboard"]')
        assert dash is not None, "Element not found"
        print('hi')
        if dash is not None:
            # following line of code is responsible for marking the status of the test on BrowserStack as 'passed'.
            # You can use this code in your after hook after each test
            mark_test_status("passed", "Landed on correct page", page)
        else:
            mark_test_status("failed", "Didn't land on the correct page", page)

        context.close()
        browser.close()


def mark_test_status(status, reason, page):
    page.evaluate("_ => {}", "browserstack_executor: {\"action\": \"setSessionStatus\", \"arguments\": {\"status\":\""+ status + "\", \"reason\": \"" + reason + "\"}}");


def main():
    desired_caps_list = [
        {
            'browser': 'chrome',
            'browser_version': 'latest',
            'os': 'osx',
            'os_version': 'catalina',
            'name': 'Branded Google Chrome on Catalina',
            'build': 'playwright-python-3',
            'browserstack.username': os.environ.get('BROWSERSTACK_USERNAME'),
            'browserstack.accessKey': os.environ.get('BROWSERSTACK_ACCESS_KEY')
        },
        # Add desired capabilities for other parallel instances here
        {
            'browser': 'playwright-firefox',
            'browser_version': 'latest',
            'os': 'windows',
            'os_version': '10',
            'name': 'Branded firefox on Windows',
            'build': 'playwright-python-3',
            'browserstack.username': os.environ.get('BROWSERSTACK_USERNAME'),
            'browserstack.accessKey': os.environ.get('BROWSERSTACK_ACCESS_KEY')
        },
        {
            'browser': 'playwright-webkit',
            'browser_version': 'latest',
            'os': 'osx',
            'os_version': 'Ventura',
            'name': 'Branded Webkit on Catalina',
            'build': 'playwright-python-3',
            'browserstack.username': os.environ.get('BROWSERSTACK_USERNAME'),
            'browserstack.accessKey': os.environ.get('BROWSERSTACK_ACCESS_KEY')
        }
    ]

    processes = []
    for desired_caps in desired_caps_list:
        process = Process(target=run_test, args=(desired_caps,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == '__main__':
    main()
