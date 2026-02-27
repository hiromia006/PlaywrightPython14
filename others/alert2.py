from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.tutorialspoint.com/selenium/practice/alerts.php")

    def handle_dialog(dialog):
        print("Type    :", dialog.type)
        print("Message :", dialog.message)
        dialog.accept()

    page.on("dialog", handle_dialog)
    page.click("button[onclick='showAlert()']")

    page.close()
