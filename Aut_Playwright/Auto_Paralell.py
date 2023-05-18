from playwright.sync_api import Playwright, sync_playwright
import time

def run_test(browser_type: str) -> None:
    with sync_playwright() as p:
        browser: Playwright = getattr(p, browser_type).launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.browserstack.com/live')

        login = page.query_selector('[href="/users/sign_in"]')
        login.click() #Step 1: Login

        page.fill('#user_email_login','warne708murali800@gmail.com')#Step 2: Username
        page.fill('#user_password','Shane@800')#Step 3: Password
        time.sleep(3)

        button = page.locator('#user_submit')#Step 4: Click Sign me In
        button.click()

        time.sleep(10)
        print(browser)

        browser.close()

def main() -> None:
    browsers = ['chromium', 'firefox', 'webkit']

    for browser in browsers:
        run_test(browser)

if __name__ == '__main__':
    main()
