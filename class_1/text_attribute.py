from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as rohan:
    browser = rohan.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")

    attribute_value = page.locator("#login-button").get_attribute("value")
    print(attribute_value)
    class_value = page.locator("#login-button").get_attribute("class")
    print(class_value)
    page.click("#login-button")
    sleep(3)

    txt = page.locator("a[id='item_4_title_link'] div[class='inventory_item_name ']").text_content()
    print(txt)

    # page.locator("div[class='inventory_item_name ']").click()
    all_locator = page.locator("div[class='inventory_item_name ']").all()

    for locator in all_locator:
        print(locator.text_content())

    page.close()
