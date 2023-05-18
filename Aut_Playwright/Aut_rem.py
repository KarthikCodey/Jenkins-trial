from playwright.sync_api import sync_playwright
import time

def main():
    with sync_playwright() as playwright:
        browser_type = playwright.chromium
        #browser_type.connect(wsEndpoint)
        #remote_websocket_endpoint = 'ws://192.168.1.104:4444/playwright/chromium'
        #browser = browser_type.connect_over_cdp(
        #    endpoint=remote_websocket_endpoint,
        #)
        browser = playwright.chromium.connect_over_cdp('ws://localhost:4444/playwright/chromium')

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

        context.close()
        browser.close()

if __name__ == '__main__':
    main()
