
from playwright.async_api import async_playwright
import asyncio
import time

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.browserstack.com/live')

        #incorrect email
        login = await page.query_selector('[href="/users/sign_in"]')
        await login.click() #Step 1: Login
        await page.fill('#user_email_login','warne708murali800@gmail.com')
        await page.click('#user_submit')
        error_element = await page.query_selector('div.error-msg.show span[aria-live="polite"]')
        time.sleep(10)
        pg = await page.query_selector('[href="/users/password/new"]')
        assert pg is not None, "Element not found"
        print(page.title)
        
        #Correct email
        await page.fill('#user_email_login', '')
        await page.fill('#user_password', '')  # Clear the input field
        time.sleep(3)
        await page.reload()

        await page.fill('#user_email_login','warne708murali800@gmail.com')#Step 2: Username
        await page.fill('#user_password','Shane@800')#Step 3: Password
        time.sleep(3)

        await page.click('#user_submit')  # Step 4: Click Sign In
        print('hi1')
        time.sleep(10)
        dash = await page.query_selector('[href="https://live.browserstack.com/dashboard"]')
        assert dash is not None, "Element not found"
        print(page.title)
        await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
