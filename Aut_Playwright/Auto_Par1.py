from playwright.sync_api import sync_playwright
import threading
import time

def run_browser(browser_type):
    with sync_playwright() as p:
        browser = None
        if browser_type == "chromium":
            browser = p.chromium.launch(headless=False)
        elif browser_type == "firefox":
            browser = p.firefox.launch(headless=False)
        elif browser_type == "webkit":
            browser = p.webkit.launch(headless=False)

        page = browser.new_page()
        page.goto('https://www.browserstack.com/live')


        login = page.query_selector('[href="/users/sign_in"]')
        login.click() #Step 1: Login

        page.fill('#user_email_login','warne708murali800@gmail.com')#Step 2: Username
        page.fill('#user_password','Shane@800')#Step 3: Password
        time.sleep(3)

        button = page.locator('#user_submit')#Step 4: Click Sign me In
        button.click()
        print(browser_type)

        time.sleep(10)

        browser.close()

if __name__ == '__main__':
    threads = []
    for browser_type in ["chromium", "firefox", "webkit"]:
        t = threading.Thread(target=run_browser, args=(browser_type,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
