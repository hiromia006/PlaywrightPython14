from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.tutorialspoint.com/selenium/practice/alerts.php")

    # page.on("dialog", lambda dialog: dialog.accept())
    # page.click("button[onclick='showAlert()']")

    def handle_dialog(dialog):
        print(f"Dialog Type: {dialog.type}")
        print(f"Dialog Message: {dialog.message}")
        dialog.dismiss()

    page.on("dialog", handle_dialog)
    page.click("//button[@onclick='myDesk()']")

    page.close()