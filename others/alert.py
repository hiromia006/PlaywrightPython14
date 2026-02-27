from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.tutorialspoint.com/selenium/practice/alerts.php")

    # ✅ Register BEFORE the click
    page.on("dialog", lambda dialog: dialog.accept())
    page.click("button[onclick='showAlert()']")

    page.close()
