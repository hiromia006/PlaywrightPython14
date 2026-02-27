from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.tutorialspoint.com/selenium/practice/browser-windows.php")

    # Wait for new tab to open after click
    with context.expect_page() as new_page_info:
        page.click("button[title='New Tab']")   # clicks a link that opens new tab

    new_tab = new_page_info.value
    new_tab.wait_for_load_state()
    sleep(3)
    print("New Tab URL  :", new_tab.url)
    print("New Tab Title:", new_tab.title())

    browser.close()