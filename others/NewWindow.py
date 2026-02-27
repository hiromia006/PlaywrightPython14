from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    # Window 1
    context1 = browser.new_context()
    page1 = context1.new_page()
    page1.goto("https://www.google.com")
    print("Window 1:", page1.title())

    # Window 2
    context2 = browser.new_context()
    page2 = context2.new_page()
    page2.goto("https://www.youtube.com")
    print("Window 2:", page2.title())

    browser.close()