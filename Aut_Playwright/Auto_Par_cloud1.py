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
        browser = playwright[desired_capabilities['browser']].connect(cdpUrl)

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
            'browser': 'chromium',
            'browser_version': 'latest',
            'os': 'osx',
            'os_version': 'catalina',
            'name': 'Chromium on Catalina',
            'build': 'playwright-python-2',
            'browserstack.username': 'karthik533',
            'browserstack.accessKey': 'xKaXkaGAnzjFNKmzkqmY'
        },
        {
            'browser': 'firefox',
            'browser_version': 'latest',
            'os': 'windows',
            'os_version': '10',
            'name': 'Firefox on Windows',
            'build': 'playwright-python-2',
            'browserstack.username': 'karthik533',
            'browserstack.accessKey': 'xKaXkaGAnzjFNKmzkqmY'
        },
        {
            'browser': 'webkit',
            'browser_version': 'latest',
            'os': 'windows',
            'os_version': '10',
            'name': 'WebKit on Windows',
            'build': 'playwright-python-2',
            'browserstack.username': 'karthik533',
            'browserstack.accessKey': 'xKaXkaGAnzjFNKmzkqmY'
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
