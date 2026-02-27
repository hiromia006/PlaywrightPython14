from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.tutorialspoint.com/selenium/practice/browser-windows.php")
    with  context.expect_page() as newTabInfo:
        page.click("button[title='New Tab']")

    new_tab= newTabInfo.value
    new_tab.wait_for_load_state()
    print("New Tab Title: ", new_tab.title())
    print("New Tab URL: ", new_tab.url)
    allUrl=new_tab.locator("a").all()
    for url in allUrl:
        print(url.get_attribute("href"))
    sleep(3)

    browser.close()