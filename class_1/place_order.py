from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as rohan:
    browser = rohan.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    sleep(3)

    page.click("#add-to-cart-sauce-labs-backpack")
    page.click("//span[@class='shopping_cart_badge']")
    page.click("//button[@id='checkout']")
    sleep(3)
    page.fill("#first-name", "Rohan")
    page.fill("#last-name", "Sharma")
    page.fill("#postal-code", "123456")
    sleep(3)

    page.click("#continue")
    page.click("#finish")
    page.click("#back-to-products")

    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")
    browser.close()
