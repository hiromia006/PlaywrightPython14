from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) # headless=False means that the browser will be visible when the script is run. If headless=True, the browser will run in the background without a user interface.
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user") # CSS Selector
    page.fill("//input[@id='password']", "secret_sauce") # XPath Selector
    sleep(3)
    page.click("#login-button")
    sleep(3)
    browser.close()