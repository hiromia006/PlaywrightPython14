from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as rohan:
    browser = rohan.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.click("//button[text()='Click for JS Alert']")
    sleep(2)
    alert = page.wait_for_event("dialog")
    print(alert.message)
    sleep(2)
    alert.accept()
    page.click("//button[text()='Click for JS Confirm']")
    sleep(2)
    alert = page.wait_for_event("dialog")
    print(alert.message)
    alert.dismiss()
    page.click("//button[text()='Click for JS Prompt']")
    alert = page.wait_for_event("dialog")
    print(alert.message)
    alert.accept("Rohan Sharma")