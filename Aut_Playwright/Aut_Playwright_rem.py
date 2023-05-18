import subprocess
from playwright.sync_api import sync_playwright
import time


def main():
    with sync_playwright() as playwright:
        clientPlaywrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
        #desired_cap1['client.playwrightVersion'] = clientPlaywrightVersion

        cdpUrl = 'wss://localhost:4444/playwright/chromium'
        browser = playwright.chromium.connect(cdpUrl)

        #browser_type = playwright.chromium
        #remote_websocket_endpoint = 'ws://192.168.1.104:4444/playwright/chromium'
        #browser = playwright.launch_remote(
        #    browser_url=remote_websocket_endpoint,
        #)
        #browser = browser_type.connect(
        #    ws_endpoint='ws://192.168.1.104:4444/playwright/chromium'
        #)
        context = browser.new_context()
        #page = context.new_page()
    #with sync_playwright() as playwright:
    #    browser_type = playwright.chromium
    #    browser = browser_type.connect_over_cdp(
    #        endpoint='http://localhost:4444/wd/hub',
    #        browser_url='http://localhost:4444/webdriver/chrome'
    #    )
    #    context = browser.new_context()

    #    page = context.new_page()
        page = browser.new_page()
        page.goto('https://www.browserstack.com/live')

        #incorrect email
        login = page.query_selector('[href="/users/sign_in"]')
        login.click() #Step 1: Login
        page.fill('#user_email_login','warne708murali800@gmail.com')
        page.click('#user_submit')
        error_element = page.query_selector('div.error-msg.show span[aria-live="polite"]')
        time.sleep(10)
        pg = page.query_selector('[href="/users/password/new"]')
        assert pg is not None, "Element not found"
        
        #Correct email
        page.fill('#user_email_login', '')
        page.fill('#user_password', '')  # Clear the input field
        time.sleep(3)
        page.reload()

        page.fill('#user_email_login','warne708murali800@gmail.com')#Step 2: Username
        page.fill('#user_password','Shane@800')#Step 3: Password
        time.sleep(3)

        page.click('#user_submit')  # Step 4: Click Sign In
        print('hi1')
        time.sleep(10)
        dash = page.query_selector('[href="https://live.browserstack.com/dashboard"]')
        assert dash is not None, "Element not found"
        print('hi')
        if dash is not None:
        # following line of code is responsible for marking the status of the test on BrowserStack as 'passed'. You can use this code in your after hook after each test
            mark_test_status("passed", "Landed on correct page", page)
        else:
            mark_test_status("failed", "Didn't land on the correct page", page)


        context.close()
        browser.close()

def mark_test_status(status, reason, page):
  page.evaluate("_ => {}", "browserstack_executor: {\"action\": \"setSessionStatus\", \"arguments\": {\"status\":\""+ status + "\", \"reason\": \"" + reason + "\"}}");
    

if __name__ == '__main__':
    main()
