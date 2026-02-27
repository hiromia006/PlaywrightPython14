from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    # Tab 1
    page1 = context.new_page()
    page1.goto("https://www.google.com")
    print("Tab 1:", page1.title())

    # Tab 2
    page2 = context.new_page()
    page2.goto("https://www.youtube.com")
    print("Tab 2:", page2.title())

    # Switch back to Tab 1
    page1.bring_to_front()
    print("Switched to Tab 1:", page1.title())

    browser.close()