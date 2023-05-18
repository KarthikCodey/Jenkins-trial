from playwright.sync_api import sync_playwright
import asyncio
import time

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
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

        
        browser.close()


if __name__ == '__main__':
    main()
