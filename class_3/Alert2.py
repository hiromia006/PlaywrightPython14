from time import sleep

from playwright.sync_api import sync_playwright, Dialog

def handle_dialog(dialog: Dialog):
    print(f"Type    : {dialog.type}")       # alert | confirm | prompt | beforeunload
    print(f"Message : {dialog.message}")

    if dialog.type == "alert":
        dialog.accept()                     # Just close it

    elif dialog.type == "confirm":
        # dialog.accept()                     # Click OK
        dialog.dismiss()                  # Click Cancel

    elif dialog.type == "prompt":
        dialog.accept("my input text")     # Type and click OK
        print(dialog.message)              # Get default value of prompt
        # dialog.dismiss()                  # Click Cancel

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.on("dialog", handle_dialog)

    page.goto("https://www.tutorialspoint.com/selenium/practice/alerts.php")
    page.click("button[onclick='showAlert()']")

    sleep(3)
    page.click("button[onclick='myDesk()']")

    sleep(3)
    page.click("button[onclick='myPromp()']")

    browser.close()