from playwright.sync_api import  sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user", timeout=1000) # timeout is the maximum time to wait for the element to be visible before throwing an error. The default value is 30000 milliseconds (30 seconds).
    page.locator("#password").fill("secret_sauce", timeout=1000)
    page.locator("#login-button").click()
    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")
    browser.close()