from playwright.sync_api import sync_playwright

with sync_playwright() as naima:
    browser = naima.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    print(page.title())

    browser.close()